import { FFMpegFilter } from '@/types/ffmpeg';
import {
  FilterNode,
  InputNode,
  OutputNode,
  GlobalNode,
  FilterableStream,
  Stream,
  VideoStream,
  AudioStream,
  AVStream,
  OutputStream,
  GlobalStream,
  StreamType,
  StreamTypeEnum,
} from '../types/dag';
import { dumps } from './serialize';
import { EventEmitter } from 'events';
import { evaluateFormula } from './formulaEvaluator';
import { FFmpegFilter, FFMpegIOType, predefinedFilters } from '../types/ffmpeg';

export interface NodeMapping {
  // Maps ReactFlow node ID to DAG node
  nodeMap: Map<string, FilterNode | InputNode | OutputNode | GlobalNode>;
  // Maps DAG node to ReactFlow node ID (for reverse lookup)
  reverseMap: Map<FilterNode | InputNode | OutputNode | GlobalNode, string>;
}

export interface EdgeMapping {
  // Maps ReactFlow edge ID to Stream
  edgeMap: Map<string, Stream>;
  // Maps Stream to ReactFlow edge ID (for reverse lookup)
  reverseMap: Map<Stream, string>;
  // Maps Stream to target node ID and index
  targetMap: Map<Stream, { nodeId: string; index: number }>;
}

// Define update event types - simplify to just UPDATE
export const NODE_MAPPING_EVENTS = {
  UPDATE: 'update',
} as const;

export type NodeMappingEventType = (typeof NODE_MAPPING_EVENTS)[keyof typeof NODE_MAPPING_EVENTS];

/**
 * NodeMappingManager manages the mapping between the ReactFlow graph and the DAG model
 * It provides methods to add/remove nodes and edges, and to convert the mapping to a JSON string
 * It emits an update event when the mapping changes
 */
export class NodeMappingManager {
  private nodeMapping: NodeMapping = {
    nodeMap: new Map(),
    reverseMap: new Map(),
  };

  private edgeMapping: EdgeMapping = {
    edgeMap: new Map(),
    reverseMap: new Map(),
    targetMap: new Map(),
  };

  private nodeIdCounter = 0;
  private globalNode: GlobalNode;
  private globalNodeId: string;
  private eventEmitter = new EventEmitter();

  constructor() {
    // Initialize the global node
    this.globalNode = new GlobalNode([], {});
    this.globalNodeId = this.generateNodeId(this.globalNode);
    this.nodeMapping.nodeMap.set(this.globalNodeId, this.globalNode);
    this.nodeMapping.reverseMap.set(this.globalNode, this.globalNodeId);
  }

  // Event handling methods
  /**
   * Subscribe to mapping update events
   * @param eventType The event type to listen for (always 'update')
   * @param listener The callback function to be called when the event is emitted
   * @returns A function to unsubscribe the listener
   */
  public on(eventType: NodeMappingEventType, listener: () => void): () => void {
    this.eventEmitter.on(eventType, listener);
    return () => {
      this.eventEmitter.off(eventType, listener);
    };
  }

  /**
   * Emit an update event
   */
  private emitUpdate(): void {
    this.eventEmitter.emit(NODE_MAPPING_EVENTS.UPDATE);
  }

  // Helper function to generate unique ID for a node
  private generateNodeId(node: FilterNode | InputNode | OutputNode | GlobalNode): string {
    const id = this.nodeIdCounter++;
    if (node instanceof InputNode) {
      return `input-${id}`;
    } else if (node instanceof OutputNode) {
      return `output-${id}`;
    } else if (node instanceof FilterNode) {
      return `filter-${node.name}-${id}`;
    } else if (node instanceof GlobalNode) {
      return `global-${id}`;
    }
    return `node-${id}`;
  }

  // Helper function to generate unique ID for an edge
  private generateEdgeId(
    sourceId: string,
    targetId: string,
    sourceIndex: number,
    targetIndex: number
  ): string {
    return `edge-${sourceId}-${sourceIndex}-${targetId}-${targetIndex}`;
  }

  // Helper function to ensure node inputs are initialized
  private ensureNodeInputs(node: FilterNode | OutputNode | GlobalNode, count: number): void {
    if (!node.inputs) {
      node.inputs = [];
    }

    // Extend the array if needed
    while (node.inputs.length < count) {
      node.inputs.push(null);
    }
  }
  private async evaluateIOtypings(
    filter: FFMpegFilter,
    kwargs: Record<string, string | number | boolean>
  ): Promise<{ input_typings: StreamTypeEnum[]; output_typings: StreamTypeEnum[] }> {
    // merge parameters with kwargs
    // extract default value from filter.options and convert to a Dict
    let parameters: Record<string, string | number | boolean> = {};
    filter.options.map((option) => {
      parameters[option.name] = option.default;
    });

    // merge parameters with kwargs
    parameters = { ...parameters, ...kwargs };
    let input_typings: StreamTypeEnum[] = [];
    if (!filter.formula_typings_input) {
      input_typings = filter.stream_typings_input.map((t) => t.type.value);
    } else {
      input_typings = await evaluateFormula(filter.formula_typings_input, parameters);
    }
    let output_typings: StreamTypeEnum[] = [];
    if (!filter.formula_typings_output) {
      output_typings = filter.stream_typings_output.map((t) => t.type.value);
    } else {
      output_typings = await evaluateFormula(filter.formula_typings_output, parameters);
    }
    return {
      input_typings,
      output_typings,
    };
  }
  // Add a node to the mapping
  async addNodeToMapping(params: {
    type: 'filter' | 'input' | 'output' | 'global';
    name?: string;
    filename?: string;
    inputs?: (FilterableStream | null | OutputStream)[];
    input_typings?: StreamType[];
    output_typings?: StreamType[];
    kwargs?: Record<string, string | number | boolean>;
  }): Promise<string> {
    // Special handling for GlobalNode
    if (params.type === 'global') {
      // Update the existing GlobalNode's properties
      if (params.inputs) {
        this.globalNode.inputs = params.inputs as unknown as OutputStream[];
      } else {
        // Ensure the global node has empty inputs array
        this.globalNode.inputs = [];
      }

      if (params.kwargs) {
        this.globalNode.kwargs = { ...this.globalNode.kwargs, ...params.kwargs };
      }
      this.emitUpdate();
      return this.globalNodeId;
    }

    let node: FilterNode | InputNode | OutputNode;
    let filterInputs: (FilterableStream | null)[] | undefined;
    let outputInputs: (FilterableStream | null)[] | undefined;
    let inputFilename: string;
    let outputFilename: string;
    let filter: FFMpegFilter | undefined;

    switch (params.type) {
      case 'filter': {
        if (!params.name) {
          throw new Error('FilterNode requires name, input_typings, and output_typings');
        }
        filter = predefinedFilters.find((f) => f.name === params.name);
        if (!filter) {
          throw new Error(`Filter ${params.name} not found`);
        }
        const { input_typings, output_typings } = await this.evaluateIOtypings(
          filter,
          params.kwargs || {}
        );

        // Initialize with proper input array length based on input_typings
        filterInputs = params.inputs || Array(input_typings.length).fill(null);

        node = new FilterNode(
          params.name,
          filterInputs as (FilterableStream | null)[],
          input_typings,
          output_typings,
          params.kwargs
        );
        break;
      }

      case 'input':
        // Generate random filename if not provided
        if (!params.filename) {
          throw new Error('InputNode requires filename');
        }
        inputFilename = params.filename;
        node = new InputNode(inputFilename, [], params.kwargs);
        break;

      case 'output':
        // Generate random filename if not provided
        if (!params.filename) {
          throw new Error('OutputNode requires filename');
        }
        outputFilename = params.filename;
        // Initialize with a single null input if none provided
        outputInputs = params.inputs ? (params.inputs as (FilterableStream | null)[]) : [null];

        node = new OutputNode(outputFilename, outputInputs, params.kwargs);
        break;

      default:
        throw new Error('Invalid node type');
    }

    const nodeId = this.generateNodeId(node);
    this.nodeMapping.nodeMap.set(nodeId, node);
    this.nodeMapping.reverseMap.set(node, nodeId);
    this.emitUpdate();
    return nodeId;
  }

  // Remove a node from the mapping
  removeNodeFromMapping(nodeId: string): void {
    const node = this.nodeMapping.nodeMap.get(nodeId);
    if (!node) {
      throw new Error(`Node ${nodeId} not found in mapping`);
    }

    // Find all edges connected to this node (both as source and target)
    const edgesToRemove: string[] = [];
    for (const [edgeId, stream] of this.edgeMapping.edgeMap) {
      const targetInfo = this.edgeMapping.targetMap.get(stream);
      const sourceNode = stream.node;
      const sourceNodeId = this.nodeMapping.reverseMap.get(
        sourceNode as FilterNode | InputNode | OutputNode | GlobalNode
      );

      if ((targetInfo && targetInfo.nodeId === nodeId) || sourceNodeId === nodeId) {
        edgesToRemove.push(edgeId);
      }
    }

    // Remove all connected edges
    for (const edgeId of edgesToRemove) {
      const stream = this.edgeMapping.edgeMap.get(edgeId);
      if (stream) {
        const targetInfo = this.edgeMapping.targetMap.get(stream);
        if (targetInfo) {
          const targetNode = this.nodeMapping.nodeMap.get(targetInfo.nodeId);
          if (targetNode && targetNode.inputs) {
            targetNode.inputs[targetInfo.index] = null;
          }
        }
        this.edgeMapping.edgeMap.delete(edgeId);
        this.edgeMapping.targetMap.delete(stream);
        this.edgeMapping.reverseMap.delete(stream);
      }
    }

    // Remove the node
    this.nodeMapping.nodeMap.delete(nodeId);
    this.nodeMapping.reverseMap.delete(node);
    this.emitUpdate();
  }

  // Get the global node ID
  getGlobalNodeId(): string {
    return this.globalNodeId;
  }

  // Get the global node instance
  getGlobalNode(): GlobalNode {
    return this.globalNode;
  }

  // Reset mapping state
  resetNodeMapping() {
    this.nodeMapping = {
      nodeMap: new Map(),
      reverseMap: new Map(),
    };
    this.edgeMapping = {
      edgeMap: new Map(),
      reverseMap: new Map(),
      targetMap: new Map(),
    };
    this.nodeIdCounter = 0;

    // Create a new global node
    this.globalNode = new GlobalNode([], {});
    this.globalNodeId = this.generateNodeId(this.globalNode);
    this.nodeMapping.nodeMap.set(this.globalNodeId, this.globalNode);
    this.nodeMapping.reverseMap.set(this.globalNode, this.globalNodeId);
    this.emitUpdate();
  }

  // Add an edge to the mapping
  addEdgeToMapping(
    sourceNodeId: string,
    targetNodeId: string,
    sourceIndex: number,
    targetIndex: number
  ): string {
    const sourceNode = this.nodeMapping.nodeMap.get(sourceNodeId);
    const targetNode = this.nodeMapping.nodeMap.get(targetNodeId);

    if (!sourceNode || !targetNode) {
      throw new Error('Source or target node not found in mapping');
    }

    // Create the appropriate stream type based on source node type
    let stream: VideoStream | AudioStream | AVStream | OutputStream | GlobalStream;

    if (sourceNode instanceof FilterNode) {
      // Check if the sourceIndex is valid
      if (sourceIndex >= sourceNode.output_typings.length) {
        throw new Error(
          `Source node ${sourceNodeId} does not have an output at index ${sourceIndex}`
        );
      }

      const streamType = sourceNode.output_typings[sourceIndex];
      switch (streamType.value) {
        case 'video':
          stream = new VideoStream(sourceNode, sourceIndex);
          break;
        case 'audio':
          stream = new AudioStream(sourceNode, sourceIndex);
          break;
        default:
          throw new Error(`Invalid stream type: ${streamType.value}`);
      }
    } else if (sourceNode instanceof InputNode) {
      stream = new AVStream(sourceNode, null);
    } else if (sourceNode instanceof OutputNode) {
      stream = new OutputStream(sourceNode, targetIndex);
    } else if (sourceNode instanceof GlobalNode) {
      stream = new GlobalStream(sourceNode);
    } else {
      throw new Error('Invalid source node type');
    }

    // Ensure the target node has enough input slots
    if (
      targetNode instanceof FilterNode ||
      targetNode instanceof OutputNode ||
      targetNode instanceof GlobalNode
    ) {
      this.ensureNodeInputs(targetNode, targetIndex + 1);
    } else {
      throw new Error(`Cannot add input to node of type ${targetNode.constructor.name}`);
    }

    // Check stream type compatibility for FilterNode targets
    if (targetNode instanceof FilterNode) {
      // Check if the targetIndex is valid
      if (targetIndex >= targetNode.input_typings.length) {
        throw new Error(
          `Target node ${targetNodeId} does not have an input at index ${targetIndex}`
        );
      }

      const expectedType = targetNode.input_typings[targetIndex]?.value;
      let actualType: string | undefined;

      if (stream instanceof VideoStream) {
        actualType = 'video';
      } else if (stream instanceof AudioStream) {
        actualType = 'audio';
      }

      if (expectedType && actualType && expectedType !== actualType) {
        throw new Error(`Stream type mismatch: expected ${expectedType}, got ${actualType}`);
      }
    }

    // Set input on target node
    if (targetNode.inputs && targetIndex < targetNode.inputs.length) {
      targetNode.inputs[targetIndex] = stream as FilterableStream;
    } else {
      throw new Error(`Target node ${targetNodeId} does not have an input at index ${targetIndex}`);
    }

    // Create edge ID and add to mapping
    const edgeId = this.generateEdgeId(sourceNodeId, targetNodeId, sourceIndex, targetIndex);
    this.edgeMapping.edgeMap.set(edgeId, stream);
    this.edgeMapping.reverseMap.set(stream, edgeId);
    this.edgeMapping.targetMap.set(stream, { nodeId: targetNodeId, index: targetIndex });
    this.emitUpdate();
    return edgeId;
  }

  // Remove an edge from the mapping
  removeEdgeFromMapping(edgeId: string): void {
    const stream = this.edgeMapping.edgeMap.get(edgeId);
    if (!stream) {
      throw new Error(`Edge ${edgeId} not found in mapping`);
    }

    // Remove the stream from the target node's inputs
    const targetInfo = this.edgeMapping.targetMap.get(stream);
    if (targetInfo) {
      const targetNode = this.nodeMapping.nodeMap.get(targetInfo.nodeId);
      if (targetNode && targetNode.inputs) {
        targetNode.inputs[targetInfo.index] = null;
      }
    }

    // Remove from mapping
    this.edgeMapping.edgeMap.delete(edgeId);
    this.edgeMapping.targetMap.delete(stream);
    this.edgeMapping.reverseMap.delete(stream);
    this.emitUpdate();
  }

  // Get the node mapping
  getNodeMapping(): NodeMapping {
    return this.nodeMapping;
  }

  // Get the edge mapping
  getEdgeMapping(): EdgeMapping {
    return this.edgeMapping;
  }

  // Update a node in the mapping
  updateNode(
    nodeId: string,
    updates: {
      input_typings?: StreamType[];
      output_typings?: StreamType[];
      kwargs?: Record<string, string | number | boolean>;
      filename?: string;
    }
  ): void {
    const node = this.nodeMapping.nodeMap.get(nodeId);
    if (!node) {
      throw new Error(`Node ${nodeId} not found in mapping`);
    }

    if (updates.input_typings && node instanceof FilterNode) {
      node.input_typings = updates.input_typings;
      // Ensure inputs array matches the length of input_typings
      this.ensureNodeInputs(node, updates.input_typings.length);
    }

    if (updates.output_typings && node instanceof FilterNode) {
      node.output_typings = updates.output_typings;
    }

    if (updates.kwargs) {
      node.kwargs = { ...node.kwargs, ...updates.kwargs };
    }

    if (updates.filename) {
      if (node instanceof InputNode || node instanceof OutputNode) {
        node.filename = updates.filename;
      } else {
        throw new Error(`Cannot update filename on node type ${node.constructor.name}`);
      }
    }
    this.emitUpdate();
  }

  /**
   * Update multiple nodes at once
   * @param updates Map of nodeId to update object
   */
  updateMultipleNodes(
    updates: Map<
      string,
      {
        input_typings?: StreamType[];
        output_typings?: StreamType[];
        kwargs?: Record<string, string | number | boolean>;
        filename?: string;
      }
    >
  ): void {
    if (updates.size === 0) return;

    let anyUpdates = false;

    for (const [nodeId, updateData] of updates) {
      try {
        const node = this.nodeMapping.nodeMap.get(nodeId);
        if (!node) {
          console.error(`Node ${nodeId} not found in mapping`);
          continue;
        }

        // Apply updates without emitting events
        if (updateData.input_typings && node instanceof FilterNode) {
          node.input_typings = updateData.input_typings;
          this.ensureNodeInputs(node, updateData.input_typings.length);
          anyUpdates = true;
        }

        if (updateData.output_typings && node instanceof FilterNode) {
          node.output_typings = updateData.output_typings;
          anyUpdates = true;
        }

        if (updateData.kwargs) {
          node.kwargs = { ...node.kwargs, ...updateData.kwargs };
          anyUpdates = true;
        }

        if (updateData.filename) {
          if (node instanceof InputNode || node instanceof OutputNode) {
            node.filename = updateData.filename;
            anyUpdates = true;
          }
        }
      } catch (error) {
        console.error(`Error updating node ${nodeId}:`, error);
      }
    }

    // Emit a single update event if any updates were made
    if (anyUpdates) {
      this.emitUpdate();
    }
  }

  // Recursively add a node and all connected nodes/streams to the mapping
  async recursiveAddToMapping(
    item:
      | FilterNode
      | InputNode
      | OutputNode
      | GlobalNode
      | FilterableStream
      | VideoStream
      | AudioStream
      | AVStream
      | OutputStream
      | GlobalStream
  ): string {
    // Suppress events during the recursive operation
    // We'll emit a single event at the end
    const emitUpdate = this.emitUpdate;
    this.emitUpdate = () => {}; // No-op

    let result: string;

    try {
      // If it's a node, add it to the mapping
      if (
        item instanceof FilterNode ||
        item instanceof InputNode ||
        item instanceof OutputNode ||
        item instanceof GlobalNode
      ) {
        // Check if node is already in the mapping
        const existingNodeId = this.nodeMapping.reverseMap.get(item);
        if (existingNodeId) {
          result = existingNodeId;
        } else {
          // Add node to mapping
          let nodeId: string;
          if (item instanceof FilterNode) {
            nodeId = await this.addNodeToMapping({
              type: 'filter',
              name: item.name,
              inputs: item.inputs,
              input_typings: item.input_typings,
              output_typings: item.output_typings,
              kwargs: item.kwargs,
            });
          } else if (item instanceof InputNode) {
            nodeId = await this.addNodeToMapping({
              type: 'input',
              filename: item.filename,
              kwargs: item.kwargs,
            });
          } else if (item instanceof OutputNode) {
            nodeId = await this.addNodeToMapping({
              type: 'output',
              filename: item.filename,
              inputs: item.inputs,
              kwargs: item.kwargs,
            });
          } else if (item instanceof GlobalNode) {
            // For GlobalNode, we update the existing one
            if (item.inputs && item.inputs.length > 0) {
              this.globalNode.inputs = item.inputs;
            }
            if (item.kwargs) {
              this.globalNode.kwargs = { ...this.globalNode.kwargs, ...item.kwargs };
            }
            nodeId = this.globalNodeId;
          } else {
            throw new Error('Invalid node type');
          }

          // Recursively add all input streams to the mapping
          if (item.inputs) {
            for (let i = 0; i < item.inputs.length; i++) {
              const input = item.inputs[i];
              if (input) {
                // Recursively add the input stream's node
                const sourceNodeId = this.recursiveAddToMapping(input.node);
                // Add the edge - using the stream's index property
                const sourceIndex = input.index !== null ? input.index : 0;
                this.addEdgeToMapping(sourceNodeId, nodeId, sourceIndex, i);
              }
            }
          }

          result = nodeId;
        }
      }
      // If it's a stream, recursively add its node and return the node ID
      else if (
        item instanceof VideoStream ||
        item instanceof AudioStream ||
        item instanceof AVStream ||
        item instanceof OutputStream ||
        item instanceof GlobalStream
      ) {
        result = this.recursiveAddToMapping(item.node);
      } else {
        throw new Error('Invalid item type');
      }
    } finally {
      // Restore the original emitUpdate function
      this.emitUpdate = emitUpdate;
      // Emit a single update event at the end
      this.emitUpdate();
    }

    return result;
  }

  // Convert the mapping to a JSON string
  toJson(): string {
    // If we have a global node, use that as the entry point
    return dumps(this.globalNode);
  }
}
