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

  private isTestMode = false;
  private testIdCounter = 0;
  private nodeIdCounter = 0;

  // Helper function to generate unique ID for a node
  private generateNodeId(node: FilterNode | InputNode | OutputNode | GlobalNode): string {
    if (this.isTestMode) {
      const id = this.testIdCounter++;
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
    if (this.isTestMode) {
      return `edge-${sourceId}-${sourceIndex}-${targetId}-${targetIndex}`;
    }
    return `edge-${sourceId}-${sourceIndex}-${targetId}-${targetIndex}`;
  }

  // Enable test mode for deterministic IDs
  enableTestMode() {
    this.isTestMode = true;
    this.testIdCounter = 0;
  }

  // Disable test mode
  disableTestMode() {
    this.isTestMode = false;
  }

  // Add a node to the mapping
  addNodeToMapping(dagNode: FilterNode | InputNode | OutputNode | GlobalNode): string {
    const nodeId = this.generateNodeId(dagNode);

    this.nodeMapping.nodeMap.set(nodeId, dagNode);
    this.nodeMapping.reverseMap.set(dagNode, nodeId);
    return nodeId;
  }

  // Remove a node from the mapping
  removeNodeFromMapping(nodeId: string) {
    const dagNode = this.nodeMapping.nodeMap.get(nodeId);
    if (dagNode) {
      this.nodeMapping.reverseMap.delete(dagNode);
    }
    this.nodeMapping.nodeMap.delete(nodeId);
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
    let stream: Stream;
    if (sourceNode instanceof FilterNode) {
      const streamType = sourceNode.output_typings[sourceIndex];
      switch (streamType.value) {
        case 'video':
          stream = new VideoStream(sourceNode, sourceIndex);
          break;
        case 'audio':
          stream = new AudioStream(sourceNode, sourceIndex);
          break;
        case 'av':
          stream = new AVStream(sourceNode, sourceIndex);
          break;
        default:
          stream = new FilterableStream(sourceNode, sourceIndex);
      }
    } else if (sourceNode instanceof InputNode) {
      stream = new AVStream(sourceNode, sourceIndex);
    } else if (sourceNode instanceof OutputNode) {
      stream = new OutputStream(sourceNode, sourceIndex);
    } else if (sourceNode instanceof GlobalNode) {
      stream = new GlobalStream(sourceNode, sourceIndex);
    } else {
      throw new Error('Unsupported source node type');
    }

    // Update target node's inputs array
    if (targetNode instanceof FilterNode) {
      // Set the input at the specified index
      if (
        stream instanceof VideoStream &&
        targetNode.input_typings[targetIndex].value === 'audio'
      ) {
        throw new Error('Video stream cannot be connected to audio input');
      }
      if (
        stream instanceof AudioStream &&
        targetNode.input_typings[targetIndex].value === 'video'
      ) {
        throw new Error('Audio stream cannot be connected to video input');
      }
      if (!(stream instanceof FilterableStream)) {
        throw new Error('Stream is not a FilterableStream');
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
  removeEdgeFromMapping(edgeId: string) {
    const stream = this.edgeMapping.edgeMap.get(edgeId);
    if (stream) {
      const targetInfo = this.edgeMapping.targetMap.get(stream);
      if (!targetInfo) {
        throw new Error('Target information not found in mapping');
      }

      const targetNode = this.nodeMapping.nodeMap.get(targetInfo.nodeId);
      if (!targetNode) {
        throw new Error('Target node not found in mapping');
      }

      targetNode.inputs[targetInfo.index] = null;
      this.edgeMapping.reverseMap.delete(stream);
      this.edgeMapping.edgeMap.delete(edgeId);
      this.edgeMapping.targetMap.delete(stream);
    } else {
      throw new Error('Stream not found in mapping');
    }
  }

  // Get current mapping state
  getNodeMapping(): NodeMapping {
    return this.nodeMapping;
  }

  // Get current edge mapping state
  getEdgeMapping(): EdgeMapping {
    return this.edgeMapping;
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
    if (this.isTestMode) {
      this.testIdCounter = 0;
    }
    this.nodeIdCounter = 0;
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
    const nodeId = this.addNodeToMapping(item);

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
}

// Create a singleton instance
export const nodeMappingManager = new NodeMappingManager();
