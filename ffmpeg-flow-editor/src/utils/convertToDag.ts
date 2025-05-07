import { Node, Edge } from 'reactflow';
import {
  FilterNode,
  InputNode,
  OutputNode,
  GlobalNode,
  FilterableStream,
  VideoStream,
  AudioStream,
  AVStream,
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
      if (!filter) {
        throw new Error(`Filter ${node.data.filterName} not found`);
      }

      const inputTypings = filter.stream_typings_input.map(
        (t) => new StreamType(t.type.value.toString())
      );
      const outputTypings = filter.stream_typings_output.map(
        (t) => new StreamType(t.type.value.toString())
      );

      nodeMap.set(
        node.id,
        new FilterNode(
          node.data.filterName,
          [], // inputs will be set in second pass
          inputTypings,
          outputTypings,
          filter,
          node.data.parameters || {}
        )
      );
    }
  });

  // Second pass: Connect nodes using edges
  edges.forEach((edge) => {
    const sourceNode = nodeMap.get(edge.source);
    const targetNode = nodeMap.get(edge.target);

    if (!sourceNode || !targetNode) {
      throw new Error('Invalid edge: source or target node not found');
    }

    // Create appropriate stream based on edge type
    let stream: FilterableStream;
    if (edge.data.type === 'video') {
      stream = new VideoStream(sourceNode as FilterNode | InputNode);
    } else if (edge.data.type === 'audio') {
      stream = new AudioStream(sourceNode as FilterNode | InputNode);
    } else {
      stream = new AVStream(sourceNode as FilterNode | InputNode);
    }

    // Add stream to target node's inputs
    if (targetNode instanceof FilterNode || targetNode instanceof OutputNode) {
      targetNode.inputs.push(stream);
    }
  });

  // Create global node if there are output nodes
  const outputNodes = Array.from(nodeMap.values()).filter(
    (node): node is OutputNode => node instanceof OutputNode
  );
  if (outputNodes.length > 0) {
    const outputStreams = outputNodes.map((node) => new OutputStream(node));
    const globalNode = new GlobalNode(outputStreams);
    return globalNode;
  }

  return null;
}
