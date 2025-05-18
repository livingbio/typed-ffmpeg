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
  Node,
} from '../types/dag';
import { dumps } from './serialize';
import { EventEmitter } from 'events';
import { FFmpegFilter, FFMpegIOType, predefinedFilters } from '../types/ffmpeg';
import { evaluateFormula } from './formulaEvaluator';

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
  private nodeMap: Map<string, Node> = new Map();
  private edgeMap: Map<string, Stream> = new Map();

  private nodeIdCounter = 0;
  private globalNode: GlobalNode;
  private globalNodeId: string;
  private eventEmitter = new EventEmitter();

  constructor() {
    // Initialize the global node
    this.globalNode = new GlobalNode([], {});
    this.globalNodeId = this.generateNodeId(this.globalNode);
    this.nodeMap.set(this.globalNodeId, this.globalNode);
  }

  private getNodeId(node: Node): string {
    /*
    This function is used to get the node ID from the node.
    */
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const nodeId = this.nodeMap.entries().find(([_, n]) => n === node)?.[0];
    if (!nodeId) {
      throw new Error('Node not found in mapping');
    }
    return nodeId;
  }

  private getEdgeId(stream: Stream): string {
    /*
    This function is used to get the edge ID from the stream.
    */
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const edgeId = this.edgeMap.entries().find(([_, s]) => s === stream)?.[0];
    if (!edgeId) {
      throw new Error('Edge not found in mapping');
    }
    return edgeId;
  }

  private getEdgesByTarget(target: Node): (Stream | null)[] {
    /*
    This function is used to get the edges by the node input.
    */
    return target.inputs;
  }

  private getEdgesBySource(source: Node): (Stream | null)[] {
    /*
    This function is used to get the edges by the node output.
    */
    if (!(source instanceof FilterNode)) {
      return Array.from(this.edgeMap.values()).filter((s) => s.node === source);
    }

    const output: (Stream | null)[] = Array(source.output_typings.length).fill(null);
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    for (const [_, edge] of this.edgeMap) {
      if (edge.node === source) {
        if (edge.index === null) {
          throw new Error('Edge index is null');
        }
        if (output[edge.index] === null) {
          output[edge.index] = edge;
        } else {
          throw new Error('Multiple edges found for the same output');
        }
      }
    }
    return output;
  }

  private getTargetNodeByEdge(edge: Stream): Node {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const target = this.nodeMap.entries().find(([_, n]) => n.inputs.includes(edge))?.[1];
    if (!target) {
      throw new Error('Target node not found in mapping');
    }
    return target;
  }

  // Get the global node ID
  getGlobalNodeId(): string {
    return this.globalNodeId;
  }

  // Get the global node instance
  getGlobalNode(): GlobalNode {
    return this.globalNode;
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

  private addGlobalNode(
    inputs?: (null | OutputStream)[],
    kwargs?: Record<string, string | number | boolean>
  ): GlobalNode {
    // Update the existing GlobalNode's properties
    if (inputs) {
      this.globalNode.inputs = inputs;
    } else {
      // Ensure the global node has empty inputs array
      this.globalNode.inputs = [];
    }

    if (kwargs) {
      this.globalNode.kwargs = { ...this.globalNode.kwargs, ...kwargs };
    }
    return this.globalNode;
  }

  private addInputNode(
    filename?: string,
    kwargs?: Record<string, string | number | boolean>
  ): InputNode {
    // Generate random filename if not provided
    if (!filename) {
      throw new Error('InputNode requires filename');
    }
    return new InputNode(filename, [], kwargs);
  }

  private addOutputNode(
    filename?: string,
    inputs?: (FilterableStream | null)[],
    kwargs?: Record<string, string | number | boolean>
  ): OutputNode {
    // Generate random filename if not provided
    if (!filename) {
      throw new Error('OutputNode requires filename');
    }
    // Initialize with a single null input if none provided
    const outputInputs = inputs ? inputs : [];

    return new OutputNode(filename, outputInputs, kwargs);
  }

  private async evaluateIOtypings(
    filter: FFmpegFilter,
    kwargs: Record<string, string | number | boolean>
  ): Promise<{ input_typings: StreamType[]; output_typings: StreamType[] }> {
    // merge parameters with kwargs
    // extract default value from filter.options and convert to a Dict
    let parameters: Record<string, string | number | boolean> = {};
    filter.options.map((option) => {
      parameters[option.name] = option.default;
    });

    // merge parameters with kwargs
    parameters = { ...parameters, ...kwargs };
    let input_typings: FFMpegIOType[] = [];
    if (!filter.formula_typings_input) {
      input_typings = filter.stream_typings_input;
    } else {
      input_typings = await evaluateFormula(filter.formula_typings_input, parameters);
    }
    let output_typings: FFMpegIOType[] = [];
    if (!filter.formula_typings_output) {
      output_typings = filter.stream_typings_output;
    } else {
      output_typings = await evaluateFormula(filter.formula_typings_output, parameters);
    }
    return {
      input_typings: input_typings.map((t) => t.type),
      output_typings: output_typings.map((t) => t.type),
    };
  }

  private async addFilterNode(
    name: string,
    inputs?: (null | FilterableStream)[],
    kwargs?: Record<string, string | number | boolean>
  ): Promise<FilterNode> {
    if (!name) {
      throw new Error('FilterNode requires name');
    }
    const filter = predefinedFilters.find((f) => f.name === name);
    if (!filter) {
      throw new Error(`Filter ${name} not found`);
    }

    const { input_typings, output_typings } = await this.evaluateIOtypings(filter, kwargs || {});

    // Initialize with proper input array length based on input_typings
    const filterInputs = inputs || [];

    return new FilterNode(name, filterInputs, input_typings, output_typings, kwargs);
  }

  private async addNode(params: {
    type: 'filter' | 'input' | 'output' | 'global';
    name?: string;
    filename?: string;
    inputs?: (FilterableStream | null | OutputStream)[];
    kwargs?: Record<string, string | number | boolean>;
  }): Promise<string> {
    let node: FilterNode | InputNode | OutputNode | GlobalNode;
    switch (params.type) {
      case 'global':
        if (
          !Array.isArray(params.inputs) ||
          !params.inputs.every((i) => i === null || i instanceof OutputStream)
        ) {
          throw new Error('GlobalNode inputs must be a list of OutputStream or null');
        }
        node = this.addGlobalNode(params.inputs, params.kwargs);
        break;
      case 'input':
        node = this.addInputNode(params.filename, params.kwargs);
        break;
      case 'output':
        // check inputs is a list of FilterableStream or null
        if (
          !Array.isArray(params.inputs) ||
          !params.inputs.every((i) => i === null || i instanceof FilterableStream)
        ) {
          throw new Error('OutputNode inputs must be a list of FilterableStream or null');
        }
        node = this.addOutputNode(params.filename, params.inputs, params.kwargs);
        break;
      case 'filter':
        if (!params.name) {
          throw new Error('FilterNode requires name');
        }
        node = await this.addFilterNode(
          params.name,
          params.inputs as (null | FilterableStream)[],
          params.kwargs
        );
        break;
      default:
        throw new Error('Invalid node type');
    }

    const nodeId = this.generateNodeId(node);
    this.nodeMap.set(nodeId, node);
    return nodeId;
  }
  // Add a node to the mapping
  async addNodeMapping(params: {
    type: 'filter' | 'input' | 'output' | 'global';
    name?: string;
    filename?: string;
    inputs?: (FilterableStream | null | OutputStream)[];
    kwargs?: Record<string, string | number | boolean>;
  }): Promise<string> {
    // Special handling for GlobalNode
    const nodeId = await this.addNode(params);
    this.emitUpdate();
    return nodeId;
  }

  private removeEdge(edgeId: string): void {
    const edge = this.edgeMap.get(edgeId);
    if (!edge) {
      throw new Error(`Edge ${edgeId} not found in mapping`);
    }
    const target = this.getTargetNodeByEdge(edge);
    const targetIndex = target.inputs.findIndex((s) => s === edge);

    target.inputs[targetIndex] = null;
    this.edgeMap.delete(edgeId);
  }

  // Remove a node from the mapping
  removeNodeMapping(nodeId: string): void {
    const node = this.nodeMap.get(nodeId);
    if (!node) {
      throw new Error(`Node ${nodeId} not found in mapping`);
    }

    let edges = this.getEdgesBySource(node);
    for (const edge of edges) {
      if (edge) {
        this.removeEdge(this.getEdgeId(edge));
      }
    }

    edges = this.getEdgesByTarget(node);
    for (const edge of edges) {
      if (edge) {
        this.removeEdge(this.getEdgeId(edge));
      }
    }

    this.nodeMap.delete(nodeId);
    this.emitUpdate();
  }

  // Reset mapping state
  resetNodeMapping() {
    this.nodeMap.clear();
    this.edgeMap.clear();
    this.nodeIdCounter = 0;

    // Create a new global node
    this.globalNode = new GlobalNode([], {});
    this.globalNodeId = this.generateNodeId(this.globalNode);
    this.nodeMap.set(this.globalNodeId, this.globalNode);
    this.emitUpdate();
  }

  private async addEdge(
    sourceNodeId: string,
    targetNodeId: string,
    sourceIndex: number,
    targetIndex: number
  ): Promise<string> {
    const sourceNode = this.nodeMap.get(sourceNodeId);
    const targetNode = this.nodeMap.get(targetNodeId);

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
      stream = new AVStream(sourceNode);
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
    this.edgeMap.set(edgeId, stream);
    return edgeId;
  }
  // Add an edge to the mapping
  async addEdgeMapping(
    sourceNodeId: string,
    targetNodeId: string,
    sourceIndex: number,
    targetIndex: number
  ): Promise<string> {
    const edgeId = await this.addEdge(sourceNodeId, targetNodeId, sourceIndex, targetIndex);
    this.emitUpdate();
    return edgeId;
  }

  // Remove an edge from the mapping
  removeEdgeMapping(edgeId: string): void {
    this.removeEdge(edgeId);
    // Remove from mapping
    this.emitUpdate();
  }

  // Update a node in the mapping
  private async updateNode(
    nodeId: string,
    updates: {
      kwargs?: Record<string, string | number | boolean>;
      filename?: string;
    }
  ): Promise<void> {
    const node = this.nodeMap.get(nodeId);
    if (!node) {
      throw new Error(`Node ${nodeId} not found in mapping`);
    }

    if (node instanceof FilterNode) {
      const filter = predefinedFilters.find((f) => f.name === node.name);
      if (!filter) {
        throw new Error(`Filter ${node.name} not found`);
      }
      const { input_typings, output_typings } = await this.evaluateIOtypings(
        filter,
        updates.kwargs || {}
      );
      if (input_typings.length <= node.input_typings.length) {
        // should remove the extra edges
        for (let i = input_typings.length; i < node.input_typings.length; i++) {
          const stream = node.inputs[i];
          if (stream) {
            this.removeEdge(this.getEdgeId(stream));
          }
        }
        node.inputs = node.inputs.slice(0, input_typings.length);
      } else {
        this.ensureNodeInputs(node, input_typings.length);
      }
      if (output_typings.length <= node.output_typings.length) {
        // should remove the extra edges
        this.getEdgesBySource(node).forEach((stream) => {
          if (stream) {
            if (!stream.index) {
              throw new Error('Edge index is null');
            }
            if (stream.index >= output_typings.length) {
              this.removeEdge(this.getEdgeId(stream));
            }
          }
        });
      }
      node.input_typings = input_typings;
      node.output_typings = output_typings;

      if (updates.kwargs) {
        node.kwargs = updates.kwargs;
      }
      // should remove the inputs that are not in the input_typings
    }

    if (updates.filename) {
      if (node instanceof InputNode || node instanceof OutputNode) {
        node.filename = updates.filename;
      } else {
        throw new Error(`Cannot update filename on node type ${node.constructor.name}`);
      }
    }
  }

  public async updateNodeMapping(
    nodeId: string,
    updates: {
      kwargs?: Record<string, string | number | boolean>;
      filename?: string;
    }
  ): Promise<void> {
    await this.updateNode(nodeId, updates);
    this.emitUpdate();
  }

  private async recursiveCreateNode(
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
    // Suppress events during the recursive operation
    // We'll emit a single event at the end
    let result: string;

    // If it's a node, add it to the mapping
    if (
      item instanceof FilterNode ||
      item instanceof InputNode ||
      item instanceof OutputNode ||
      item instanceof GlobalNode
    ) {
      // Check if node is already in the mapping
      const existingNodeId = this.getNodeId(item);
      if (existingNodeId) {
        result = existingNodeId;
      } else {
        // Add node to mapping
        let nodeId: string;
        if (item instanceof FilterNode) {
          nodeId = await this.addNodeMapping({
            type: 'filter',
            name: item.name,
            inputs: item.inputs,
            kwargs: item.kwargs,
          });
        } else if (item instanceof InputNode) {
          nodeId = await this.addNodeMapping({
            type: 'input',
            filename: item.filename,
            kwargs: item.kwargs,
          });
        } else if (item instanceof OutputNode) {
          nodeId = await this.addNodeMapping({
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
              const sourceNodeId = await this.recursiveCreateMapping(input.node);
              // Add the edge - using the stream's index property
              const sourceIndex = input.index !== null ? input.index : 0;
              this.addEdgeMapping(sourceNodeId, nodeId, sourceIndex, i);
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
      result = await this.recursiveCreateMapping(item.node);
    } else {
      throw new Error('Invalid item type');
    }
    return result;
  }
  // Recursively add a node and all connected nodes/streams to the mapping
  async recursiveCreateMapping(
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
    const result = await this.recursiveCreateNode(item);
    this.emitUpdate();
    return result;
  }

  // Convert the mapping to a JSON string
  toJson(): string {
    // If we have a global node, use that as the entry point
    return dumps(this.globalNode);
  }
}
