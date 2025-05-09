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

// Module-level state
let nodeMapping: NodeMapping = {
  nodeMap: new Map(),
  reverseMap: new Map(),
};

export interface EdgeMapping {
  // Maps ReactFlow edge ID to Stream
  edgeMap: Map<string, Stream>;
  // Maps Stream to ReactFlow edge ID (for reverse lookup)
  reverseMap: Map<Stream, string>;
  // Maps Stream to target node ID and index
  targetMap: Map<Stream, { nodeId: string; index: number }>;
}

// Module-level state
let edgeMapping: EdgeMapping = {
  edgeMap: new Map(),
  reverseMap: new Map(),
  targetMap: new Map(),
};

// Helper function to generate unique ID for a node, so reactflow can use it
export const generateNodeId = (node: FilterNode | InputNode | OutputNode | GlobalNode): string => {
  const randomSuffix = Math.random().toString(36).substr(2, 9);

  if (node instanceof InputNode) {
    return `input-${randomSuffix}`;
  } else if (node instanceof OutputNode) {
    return `output-${randomSuffix}`;
  } else if (node instanceof FilterNode) {
    return `filter-${node.name}-${randomSuffix}`;
  } else if (node instanceof GlobalNode) {
    return `global-${randomSuffix}`;
  }
  return `node-${randomSuffix}`;
};

// Helper function to generate unique ID for an edge
export const generateEdgeId = (
  sourceId: string,
  targetId: string,
  sourceIndex: number,
  targetIndex: number
): string => {
  return `edge-${sourceId}-${sourceIndex}-${targetId}-${targetIndex}`;
};

// Helper function to add a node to the mapping
export const addNodeToMapping = (
  dagNode: FilterNode | InputNode | OutputNode | GlobalNode
): string => {
  const nodeId = generateNodeId(dagNode);

  if (dagNode instanceof FilterNode) {
    dagNode.inputs = new Array(dagNode.input_typings.length).fill(null);
  }

  nodeMapping.nodeMap.set(nodeId, dagNode);
  nodeMapping.reverseMap.set(dagNode, nodeId);
  return nodeId;
};

// Helper function to remove a node from the mapping
export const removeNodeFromMapping = (nodeId: string) => {
  const dagNode = nodeMapping.nodeMap.get(nodeId);
  if (dagNode) {
    nodeMapping.reverseMap.delete(dagNode);
  }
  nodeMapping.nodeMap.delete(nodeId);
};

// Helper function to add an edge to the mapping
export const addEdgeToMapping = (
  sourceNodeId: string,
  targetNodeId: string,
  sourceIndex: number,
  targetIndex: number
): string => {
  const sourceNode = nodeMapping.nodeMap.get(sourceNodeId);
  const targetNode = nodeMapping.nodeMap.get(targetNodeId);

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
    if (stream instanceof VideoStream && targetNode.input_typings[targetIndex].value === 'audio') {
      throw new Error('Video stream cannot be connected to audio input');
    }
    if (stream instanceof AudioStream && targetNode.input_typings[targetIndex].value === 'video') {
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

  const edgeId = generateEdgeId(sourceNodeId, targetNodeId, sourceIndex, targetIndex);
  edgeMapping.edgeMap.set(edgeId, stream);
  edgeMapping.reverseMap.set(stream, edgeId);
  edgeMapping.targetMap.set(stream, { nodeId: targetNodeId, index: targetIndex });

  return edgeId;
};

// Helper function to remove an edge from the mapping
export const removeEdgeFromMapping = (edgeId: string) => {
  const stream = edgeMapping.edgeMap.get(edgeId);
  if (stream) {
    const targetInfo = edgeMapping.targetMap.get(stream);
    if (!targetInfo) {
      throw new Error('Target information not found in mapping');
    }

    const targetNode = nodeMapping.nodeMap.get(targetInfo.nodeId);
    if (!targetNode) {
      throw new Error('Target node not found in mapping');
    }

    targetNode.inputs[targetInfo.index] = null;
    edgeMapping.reverseMap.delete(stream);
    edgeMapping.edgeMap.delete(edgeId);
    edgeMapping.targetMap.delete(stream);
  } else {
    throw new Error('Stream not found in mapping');
  }
};

// Get current mapping state
export const getNodeMapping = (): NodeMapping => nodeMapping;

// Get current edge mapping state
export const getEdgeMapping = (): EdgeMapping => edgeMapping;

// Reset mapping state
export const resetNodeMapping = () => {
  nodeMapping = {
    nodeMap: new Map(),
    reverseMap: new Map(),
  };
  edgeMapping = {
    edgeMap: new Map(),
    reverseMap: new Map(),
    targetMap: new Map(),
  };
};

// Helper function to update a node's properties
export const updateNode = (
  nodeId: string,
  updates: {
    input_typings?: StreamType[];
    output_typings?: StreamType[];
    kwargs?: Record<string, string | number | boolean>;
    filename?: string;
  }
): void => {
  const node = nodeMapping.nodeMap.get(nodeId);
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
};
