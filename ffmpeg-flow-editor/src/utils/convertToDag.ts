import { Node, Edge } from 'reactflow';
import {
  FilterNode,
  InputNode,
  OutputNode,
  GlobalNode,
  VideoStream,
  AudioStream,
  OutputStream,
  StreamType,
  FilterableStream,
} from '../types/dag';
import { predefinedFilters } from '../types/ffmpeg';

export function convertToDag(nodes: Node[], edges: Edge[]) {
  // Create a map to store node instances
  const nodeMap = new Map<string, FilterNode | InputNode | OutputNode>();

  // First pass: Create all nodes
  nodes.forEach((node) => {
    if (node.data.filterType === 'input') {
      nodeMap.set(node.id, new InputNode('input.mp4'));
    } else if (node.data.filterType === 'output') {
      // Create output node with empty inputs array
      const inputs: FilterableStream[] = [];
      nodeMap.set(node.id, new OutputNode(node.data.filename || 'output.mp4', inputs));
    } else if (node.data.filterType === 'filter') {
      const filter = predefinedFilters.find((f) => f.name === node.data.filterName);
      if (filter && node.data.handles) {
        // Get input and output types from the node's handles
        const inputTypes = node.data.handles.inputs.map((h: { type: string }) => new StreamType(h.type === 'audio' ? 'audio' : 'video'));
        const outputTypes = node.data.handles.outputs.map((h: { type: string }) => new StreamType(h.type === 'audio' ? 'audio' : 'video'));
        
        nodeMap.set(
          node.id,
          new FilterNode(
            node.data.filterName,
            [],
            inputTypes,
            outputTypes,
            node.data.parameters || {}
          )
        );
      }
    }
  });

  // Second pass: Connect nodes based on edges
  edges.forEach((edge) => {
    const sourceNode = nodeMap.get(edge.source);
    const targetNode = nodeMap.get(edge.target);

    if (sourceNode && targetNode && edge.sourceHandle && edge.targetHandle) {
      // Get the source output index from the edge's sourceHandle
      const sourceOutputMatch = edge.sourceHandle.match(/output-(\d+)/);
      const sourceOutputIndex = sourceOutputMatch ? parseInt(sourceOutputMatch[1], 10) : 0;

      // Get the target input index from the edge's targetHandle
      const targetInputMatch = edge.targetHandle.match(/input-(\d+)/);
      const targetInputIndex = targetInputMatch ? parseInt(targetInputMatch[1], 10) : 0;

      // Only create streams from FilterNode or InputNode
      if (sourceNode instanceof FilterNode || sourceNode instanceof InputNode) {
        const stream =
          edge.data?.type === 'video'
            ? new VideoStream(
                sourceNode,
                sourceNode instanceof FilterNode ? sourceOutputIndex : null
              )
            : new AudioStream(
                sourceNode,
                sourceNode instanceof FilterNode ? sourceOutputIndex : null
              );

        if (targetNode instanceof OutputNode) {
          // Ensure the inputs array is large enough
          while (targetNode.inputs.length <= targetInputIndex) {
            targetNode.inputs.push(undefined as unknown as FilterableStream);
          }
          targetNode.inputs[targetInputIndex] = stream;
        } else if (targetNode instanceof FilterNode) {
          // Ensure the inputs array is large enough
          while (targetNode.inputs.length <= targetInputIndex) {
            targetNode.inputs.push(undefined as unknown as FilterableStream);
          }
          targetNode.inputs[targetInputIndex] = stream;
        }
      }
    }
  });

  if (nodes.length === 0) {
    return null;
  }

  // Create a GlobalNode with all output nodes
  const outputNodes = nodes
    .filter((node) => node.data.filterType === 'output')
    .sort((a, b) => {
      const matchA = a.id.match(/output-(\d+)/);
      const matchB = b.id.match(/output-(\d+)/);
      const idA = matchA ? parseInt(matchA[1], 10) : 0;
      const idB = matchB ? parseInt(matchB[1], 10) : 0;
      return idA - idB;
    })
    .map((node) => {
      const outputNode = nodeMap.get(node.id);
      if (outputNode instanceof OutputNode) {
        return outputNode;
      }
      return null;
    })
    .filter((node): node is OutputNode => node !== null);

  if (outputNodes.length === 0) {
    return null;
  }

  return new GlobalNode(outputNodes.map((node) => new OutputStream(node)));
}
