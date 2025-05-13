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
} from '../types/dag';
import { dumps } from './serialize';

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

  constructor() {
    // Initialize the global node
    this.globalNode = new GlobalNode([], {});
    this.globalNodeId = this.generateNodeId(this.globalNode);
    this.nodeMapping.nodeMap.set(this.globalNodeId, this.globalNode);
    this.nodeMapping.reverseMap.set(this.globalNode, this.globalNodeId);
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

  // Add a node to the mapping
  addNodeToMapping(params: {
    type: 'filter' | 'input' | 'output' | 'global';
    name?: string;
    filename?: string;
    inputs?: (FilterableStream | null | OutputStream)[];
    input_typings?: StreamType[];
    output_typings?: StreamType[];
    kwargs?: Record<string, string | number | boolean>;
  }): string {
    // Special handling for GlobalNode
    if (params.type === 'global') {
      // Update the existing GlobalNode's properties
      if (params.inputs) {
        this.globalNode.inputs = params.inputs as OutputStream[];
      }
      if (params.kwargs) {
        this.globalNode.kwargs = { ...this.globalNode.kwargs, ...params.kwargs };
      }
      return this.globalNodeId;
    }

    let node: FilterNode | InputNode | OutputNode;

    switch (params.type) {
      case 'filter':
        if (!params.name || !params.input_typings || !params.output_typings) {
          throw new Error('FilterNode requires name, input_typings, and output_typings');
        }
        node = new FilterNode(
          params.name,
          (params.inputs as (FilterableStream | null)[]) || [],
          params.input_typings,
          params.output_typings,
          params.kwargs
        );
        break;

      case 'input':
        if (!params.filename) {
          throw new Error('InputNode requires filename');
        }
        node = new InputNode(params.filename, [], params.kwargs);
        break;

      case 'output':
        if (!params.filename) {
          throw new Error('OutputNode requires filename');
        }
        node = new OutputNode(
          params.filename,
          (params.inputs as (FilterableStream | null)[]) || [],
          params.kwargs
        );
        break;

      default:
        throw new Error('Invalid node type');
    }

    const nodeId = this.generateNodeId(node);
    this.nodeMapping.nodeMap.set(nodeId, node);
    this.nodeMapping.reverseMap.set(node, nodeId);
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
      const streamType = sourceNode.output_typings[sourceIndex];
      switch (streamType.value) {
        case 'video':
          stream = new VideoStream(sourceNode, sourceIndex);
          break;
        case 'audio':
          stream = new AudioStream(sourceNode, sourceIndex);
          break;
        default:
          throw new Error('Invalid stream type');
      }
    } else if (sourceNode instanceof InputNode) {
      stream = new AVStream(sourceNode, null);
    } else if (sourceNode instanceof OutputNode) {
      stream = new OutputStream(sourceNode, null);
    } else if (sourceNode instanceof GlobalNode) {
      stream = new GlobalStream(sourceNode, null);
    } else {
      throw new Error('Unsupported source node type');
    }

    // Update target node's inputs array
    if (targetNode instanceof FilterNode) {
      // Set the input at the specified index
      if (stream instanceof GlobalStream || stream instanceof OutputStream) {
        throw new Error('Stream type mismatch');
      }

      if (
        (targetNode.input_typings[targetIndex].value == 'video' && stream instanceof AudioStream) ||
        (targetNode.input_typings[targetIndex].value == 'audio' && stream instanceof VideoStream)
      ) {
        throw new Error('Stream type mismatch');
      }
      targetNode.inputs[targetIndex] = stream;
    } else if (targetNode instanceof OutputNode) {
      // Ensure inputs array is long enough
      while (targetNode.inputs.length <= targetIndex) {
        targetNode.inputs.push(null);
      }
      // Set the input at the specified index
      if (!(stream instanceof FilterableStream)) {
        throw new Error('Stream is not a FilterableStream');
      }
      targetNode.inputs[targetIndex] = stream;
    } else if (targetNode instanceof GlobalNode) {
      // Ensure inputs array is long enough
      while (targetNode.inputs.length <= targetIndex) {
        targetNode.inputs.push(null);
      }
      // Set the input at the specified index
      if (!(stream instanceof OutputStream)) {
        throw new Error('Stream type mismatch');
      }
      targetNode.inputs[targetIndex] = stream as OutputStream;
    } else {
      throw new Error('Target node type does not support inputs');
    }

    const edgeId = this.generateEdgeId(sourceNodeId, targetNodeId, sourceIndex, targetIndex);
    this.edgeMapping.edgeMap.set(edgeId, stream);
    this.edgeMapping.reverseMap.set(stream, edgeId);
    this.edgeMapping.targetMap.set(stream, { nodeId: targetNodeId, index: targetIndex });

    return edgeId;
  }

  // Remove an edge from the mapping
  removeEdgeFromMapping(edgeId: string): void {
    // Remove the edge from the mapping
    const stream = this.edgeMapping.edgeMap.get(edgeId);
    if (!stream) {
      throw new Error('Edge not found in mapping');
    }

    // remove the edge from target's input
    const targetNode = this.edgeMapping.targetMap.get(stream)?.nodeId;
    if (!targetNode) {
      throw new Error('Target node not found in mapping');
    }
    const targetNodeInstance = this.nodeMapping.nodeMap.get(targetNode);
    if (!targetNodeInstance) {
      throw new Error('Target node not found in mapping');
    }
    targetNodeInstance.inputs[this.edgeMapping.targetMap.get(stream)?.index ?? 0] = null;
    this.edgeMapping.targetMap.delete(stream);
    this.edgeMapping.edgeMap.delete(edgeId);
  }

  // Get current mapping state
  getNodeMapping(): NodeMapping {
    return this.nodeMapping;
  }

  // Get current edge mapping state
  getEdgeMapping(): EdgeMapping {
    return this.edgeMapping;
  }

  // Update a node's properties
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
      throw new Error('Node not found in mapping');
    }

    if (node instanceof FilterNode) {
      // Update input_typings and reinitialize inputs array if needed
      if (updates.input_typings) {
        node.input_typings = updates.input_typings;
        // Reinitialize inputs array with null values
        node.inputs = new Array(node.input_typings.length).fill(null);
      }
      // Update output_typings
      if (updates.output_typings) {
        node.output_typings = updates.output_typings;
      }
      // Update kwargs
      if (updates.kwargs) {
        node.kwargs = { ...node.kwargs, ...updates.kwargs };
      }
    } else if (node instanceof InputNode || node instanceof OutputNode) {
      // Update filename
      if (updates.filename) {
        node.filename = updates.filename;
      }
      // Update kwargs
      if (updates.kwargs) {
        node.kwargs = { ...node.kwargs, ...updates.kwargs };
      }
    } else if (node instanceof GlobalNode) {
      // Update kwargs
      if (updates.kwargs) {
        node.kwargs = { ...node.kwargs, ...updates.kwargs };
      }
    }
  }

  // Recursively add nodes and their connected streams to the mapping
  recursiveAddToMapping(
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
    // If the item is a stream, get its source node and process that
    if (
      item instanceof FilterableStream ||
      item instanceof VideoStream ||
      item instanceof AudioStream ||
      item instanceof AVStream ||
      item instanceof OutputStream ||
      item instanceof GlobalStream
    ) {
      return this.recursiveAddToMapping(item.node);
    }

    // If the item is a node, add it to the mapping
    let params: {
      type: 'filter' | 'input' | 'output' | 'global';
      name?: string;
      filename?: string;
      inputs?: (FilterableStream | null | OutputStream)[];
      input_typings?: StreamType[];
      output_typings?: StreamType[];
      kwargs?: Record<string, string | number | boolean>;
    };

    if (item instanceof FilterNode) {
      params = {
        type: 'filter',
        name: item.name,
        inputs: item.inputs,
        input_typings: item.input_typings,
        output_typings: item.output_typings,
        kwargs: item.kwargs,
      };
    } else if (item instanceof InputNode) {
      params = {
        type: 'input',
        filename: item.filename,
        kwargs: item.kwargs,
      };
    } else if (item instanceof OutputNode) {
      params = {
        type: 'output',
        filename: item.filename,
        inputs: item.inputs,
        kwargs: item.kwargs,
      };
    } else if (item instanceof GlobalNode) {
      params = {
        type: 'global',
        inputs: item.inputs,
        kwargs: item.kwargs,
      };
    } else {
      throw new Error('Unsupported node type');
    }

    const nodeId = this.addNodeToMapping(params);

    // If it's a FilterNode or OutputNode, process its inputs recursively
    if (item instanceof FilterNode || item instanceof OutputNode) {
      item.inputs.forEach((inputStream, index) => {
        if (inputStream) {
          // Recursively process the input stream
          const sourceNodeId = this.recursiveAddToMapping(inputStream.node);

          // Add the edge to the mapping
          this.addEdgeToMapping(sourceNodeId, nodeId, inputStream.index ?? 0, index);
        }
      });
    }

    return nodeId;
  }

  // Convert the global node to JSON
  toJson(): string {
    return dumps(this.globalNode);
  }
}
