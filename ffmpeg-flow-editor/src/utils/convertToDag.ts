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
      nodeMap.set(node.id, new OutputNode('output.mp4', []));
    } else if (node.data.filterType === 'filter') {
      const filter = predefinedFilters.find((f) => f.name === node.data.filterName);
      if (filter) {
        nodeMap.set(
          node.id,
          new FilterNode(
            node.data.filterName,
            [],
            [new StreamType('video')],
            [new StreamType('video')],
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

    if (sourceNode && targetNode) {
      if (targetNode instanceof OutputNode) {
        const stream =
          edge.data.type === 'video'
            ? new VideoStream(sourceNode as FilterNode | InputNode)
            : new AudioStream(sourceNode as FilterNode | InputNode);
        targetNode.inputs = [...targetNode.inputs, stream];
      } else if (targetNode instanceof FilterNode) {
        const stream =
          edge.data.type === 'video'
            ? new VideoStream(sourceNode as FilterNode | InputNode)
            : new AudioStream(sourceNode as FilterNode | InputNode);
        targetNode.inputs = [...targetNode.inputs, stream];
      }
    }
  });

  // If there are no nodes, return null
  if (nodes.length === 0) {
    return null;
  }

  // Create a GlobalNode with all output nodes
  const outputNodes = nodes
    .filter((node) => node.data.filterType === 'output')
    .map((node) => nodeMap.get(node.id))
    .filter((node): node is OutputNode => node instanceof OutputNode);

  if (outputNodes.length === 0) {
    return null;
  }

  return new GlobalNode(outputNodes.map((node) => new OutputStream(node)));
}
