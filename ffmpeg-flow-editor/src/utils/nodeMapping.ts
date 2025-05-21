import { FFMpegFilter, predefinedFilters } from '../types/ffmpeg';
import {
  Node,
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
import { NodeData } from '@/types/node';

export interface NodeMapping {
  // Maps ReactFlow node ID to DAG node
  nodeMap: Map<string, FilterNode | InputNode | OutputNode | GlobalNode>;
  nodeData: Map<string, NodeData>;
}

export interface EdgeMapping {
  // Maps ReactFlow edge ID to Stream
  edgeMap: Map<string, Stream>;
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
    nodeData: new Map(),
  };

  private edgeMapping: EdgeMapping = {
    edgeMap: new Map(),
    targetMap: new Map(),
  };

  private nodeIdCounter = 0;
  private globalNode: GlobalNode;
  private globalNodeId: string;
  private eventEmitter = new EventEmitter();

  constructor() {
    // Initialize the global node
    this.globalNodeId = this.generateNodeId();
    this.globalNode = new GlobalNode([], {}, this.globalNodeId);
    this._addGlobalNode([], {});
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
  private generateNodeId(): string {
    const id = this.nodeIdCounter++;
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
  // Get the node mapping
  getNodeMapping(): NodeMapping {
    return this.nodeMapping;
  }

  // Get the edge mapping
  getEdgeMapping(): EdgeMapping {
    return this.edgeMapping;
  }
  // Get the global node ID
  getGlobalNodeId(): string {
    return this.globalNodeId;
  }

  // Get the global node instance
  getGlobalNode(): GlobalNode {
    return this.globalNode;
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
  private _addGlobalNode(
    inputs: (OutputStream | null)[],
    kwargs: Record<string, string | number | boolean>
  ): string {
    this.globalNode.inputs = inputs;
    this.globalNode.kwargs = kwargs;
    this.nodeMapping.nodeMap.set(this.globalNodeId, this.globalNode);
    this.nodeMapping.nodeData.set(this.globalNodeId, {
      label: 'global',
      nodeType: 'global',
      handles: {
        inputs: [{ id: 'input-0', type: 'av' }],
        outputs: [{ id: 'output-0', type: 'av' }],
      },
    });
    return this.globalNodeId;
  }

  private _addOutputNode(
    filename: string,
    inputs: (FilterableStream | null)[],
    kwargs: Record<string, string | number | boolean>
  ): string {
    const id = this.generateNodeId();
    const node = new OutputNode(filename, inputs, kwargs, id);
    this.nodeMapping.nodeMap.set(id, node);
    this.nodeMapping.nodeData.set(id, {
      label: 'output',
      nodeType: 'output',
      filename,
      handles: {
        inputs: [{ id: 'input-0', type: 'av' }],
        outputs: [{ id: 'output-0', type: 'av' }],
      },
    });
    return id;
  }

  private _addInputNode(
    filename: string,
    kwargs: Record<string, string | number | boolean>
  ): string {
    const id = this.generateNodeId();
    const node = new InputNode(filename, [], kwargs, id);
    this.nodeMapping.nodeMap.set(id, node);
    this.nodeMapping.nodeData.set(id, {
      label: 'input',
      nodeType: 'input',
      filename,
      handles: {
        inputs: [],
        outputs: [{ id: 'output-0', type: 'av' }],
      },
    });
    return id;
  }

  private _addFilterNode(
    name: string,
    inputs: (FilterableStream | null)[],
    input_typings: StreamType[],
    output_typings: StreamType[],
    kwargs: Record<string, string | number | boolean>
  ): string {
    const id = this.generateNodeId();
    const node = new FilterNode(name, inputs, input_typings, output_typings, kwargs, id);
    this.nodeMapping.nodeMap.set(id, node);
    this.nodeMapping.nodeData.set(id, {
      label: name,
      nodeType: 'filter',
      handles: {
        inputs: input_typings.map((t) => ({ id: `input-${t.value}`, type: t.value })),
        outputs: output_typings.map((t) => ({ id: `output-${t.value}`, type: t.value })),
      },
    });
    return id;
  }

  // Add a node to the mapping
  private async _addNode(params: {
    type: 'filter' | 'input' | 'output' | 'global';
    name?: string;
    filename?: string;
    inputs?: (FilterableStream | null | OutputStream)[];
    filter?: FFMpegFilter;
    kwargs?: Record<string, string | number | boolean>;
  }): Promise<string> {
    // Special handling for GlobalNode
    let nodeId: string;
    switch (params.type) {
      case 'global':
        nodeId = this._addGlobalNode(params.inputs as (OutputStream | null)[], params.kwargs || {});
        break;
      case 'output':
        if (!params.filename) {
          throw new Error('OutputNode requires filename');
        }
        nodeId = this._addOutputNode(
          params.filename,
          params.inputs as (FilterableStream | null)[],
          params.kwargs || {}
        );
        break;
      case 'input':
        if (!params.filename) {
          throw new Error('InputNode requires filename');
        }
        nodeId = this._addInputNode(params.filename, params.kwargs || {});
        break;

      case 'filter': {
        if (!params.name) {
          throw new Error('FilterNode requires name');
        }
        if (!params.filter) {
          params.filter = predefinedFilters.find((f) => f.name === params.name);
        }
        if (!params.filter) {
          throw new Error(`Filter ${params.name} not found`);
        }
        const { input_typings, output_typings } = await this.evaluateIOtypings(
          params.filter,
          params.kwargs || {}
        );
        nodeId = this._addFilterNode(
          params.name,
          params.inputs as (FilterableStream | null)[],
          input_typings.map((t) => new StreamType(t)),
          output_typings.map((t) => new StreamType(t)),
          params.kwargs || {}
        );
        break;
      }
    }
    return nodeId;
  }

  async addNode(params: {
    type: 'filter' | 'input' | 'output' | 'global';
    name?: string;
    filename?: string;
    inputs?: (FilterableStream | null | OutputStream)[];
    filter?: FFMpegFilter;
    kwargs?: Record<string, string | number | boolean>;
  }): Promise<string> {
    const nodeId = await this._addNode(params);
    this.emitUpdate();
    return nodeId;
  }

  // Remove a node from the mapping
  removeNode(nodeId: string): void {
    const node = this.nodeMapping.nodeMap.get(nodeId);
    if (!node) {
      throw new Error(`Node ${nodeId} not found in mapping`);
    }

    // Find all edges connected to this node (both as source and target)
    const edgesToRemove: string[] = [];
    for (const [edgeId, stream] of this.edgeMapping.edgeMap) {
      const targetInfo = this.edgeMapping.targetMap.get(stream);
      const sourceNode = stream.node;
      const sourceNodeId = sourceNode.id;

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
      }
    }

    // Clear the node's id before removing it
    node.id = undefined;

    // Remove the node
    this.nodeMapping.nodeMap.delete(nodeId);
    this.nodeMapping.nodeData.delete(nodeId);
    this.emitUpdate();
  }

  // Reset mapping state
  resetNode() {
    this.nodeMapping = {
      nodeMap: new Map(),
    };
    this.edgeMapping = {
      edgeMap: new Map(),
      targetMap: new Map(),
    };
    this.nodeIdCounter = 0;

    // Create a new global node
    this.globalNodeId = this.generateNodeId();
    this.globalNode = new GlobalNode([], {}, this.globalNodeId);
    this._addGlobalNode([], {});
    this.emitUpdate();
  }

  // Add an edge to the mapping
  private _addEdge(
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
    let stream: Stream;

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
      stream = new OutputStream(sourceNode, sourceIndex);
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

      const expectedType = targetNode.input_typings[targetIndex].value;
      let actualType: string | undefined;

      if (stream instanceof VideoStream) {
        actualType = 'video';
      } else if (stream instanceof AudioStream) {
        actualType = 'audio';
      } else if (stream instanceof AVStream) {
        actualType = 'av';
      } else {
        throw new Error(`Invalid stream type ${stream.constructor.name}`);
      }

      if (expectedType && actualType != 'av' && expectedType !== actualType) {
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
    this.edgeMapping.targetMap.set(stream, { nodeId: targetNodeId, index: targetIndex });
    return edgeId;
  }

  addEdge(
    sourceNodeId: string,
    targetNodeId: string,
    sourceIndex: number,
    targetIndex: number
  ): string {
    const edgeId = this._addEdge(sourceNodeId, targetNodeId, sourceIndex, targetIndex);
    this.emitUpdate();
    return edgeId;
  }

  // Remove an edge from the mapping
  removeEdge(edgeId: string): void {
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
    this.emitUpdate();
  }

  // Update a node in the mapping
  async updateNode(
    nodeId: string,
    updates: {
      kwargs?: Record<string, string | number | boolean>;
      filename?: string;
    }
  ): Promise<void> {
    const node = this.nodeMapping.nodeMap.get(nodeId);
    if (!node) {
      throw new Error(`Node ${nodeId} not found in mapping`);
    }

    if (node instanceof FilterNode) {
      const filter = predefinedFilters.find((f) => f.name === node.name);
      if (!filter) {
        throw new Error(`Filter ${node.name} not found`);
      }
      const { input_typings, output_typings } = await this.evaluateIOtypings(filter, {
        ...node.kwargs,
        ...updates.kwargs,
      });
      node.input_typings = input_typings.map((t) => new StreamType(t));
      node.output_typings = output_typings.map((t) => new StreamType(t));
      this.ensureNodeInputs(node, node.input_typings.length);
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

  // Recursively add a node and all connected nodes/streams to the mapping
  private async _recursiveAddInternal(
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
  ): Promise<string> {
    let result: string;

    // If it's a node, add it to the mapping
    if (
      item instanceof FilterNode ||
      item instanceof InputNode ||
      item instanceof OutputNode ||
      item instanceof GlobalNode
    ) {
      // Check if node is already in the mapping
      if (item.id && this.nodeMapping.nodeMap.has(item.id)) {
        result = item.id;
      } else {
        // Add node to mapping
        let nodeId: string;
        if (item instanceof FilterNode) {
          nodeId = await this._addNode({
            type: 'filter',
            name: item.name,
            inputs: item.inputs,
            kwargs: item.kwargs,
          });
        } else if (item instanceof InputNode) {
          nodeId = await this._addNode({
            type: 'input',
            filename: item.filename,
            kwargs: item.kwargs,
          });
        } else if (item instanceof OutputNode) {
          nodeId = await this._addNode({
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
              const sourceNodeId = await this._recursiveAddInternal(input.node);
              // Add the edge - using the stream's index property
              const sourceIndex = input.index !== null ? input.index : 0;
              this._addEdge(sourceNodeId, nodeId, sourceIndex, i);
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
      result = await this._recursiveAddInternal(item.node);
    } else {
      throw new Error('Invalid item type');
    }

    return result;
  }

  public async recursiveAdd(
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
  ): Promise<string> {
    const result = await this._recursiveAddInternal(item);
    this.emitUpdate();
    return result;
  }

  public getNodeData(nodeId: string): NodeData {
    const node = this.nodeMapping.nodeData.get(nodeId);
    if (!node) {
      throw new Error(`Node ${nodeId} not found in mapping`);
    }
    return node;
  }
  // Convert the mapping to a JSON string
  toJson(): string {
    // If we have a global node, use that as the entry point
    return dumps(this.globalNode);
  }
}
