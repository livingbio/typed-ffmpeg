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
import { EdgeData } from '../types/edge';

export function convertToDag(nodes: Node[], edges: Edge<EdgeData>[]) {
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

  // Second pass: Create streams and connect nodes
  edges.forEach((edge) => {
    const sourceNode = nodeMap.get(edge.source);
    const targetNode = nodeMap.get(edge.target);

    if (sourceNode && targetNode && edge.data) {
      // Create appropriate stream type based on edge data
      let stream;
      if (edge.data.type === 'video') {
        stream = new VideoStream(sourceNode as FilterNode | InputNode, edge.data.sourceIndex ?? null);
      } else if (edge.data.type === 'audio') {
        stream = new AudioStream(sourceNode as FilterNode | InputNode, edge.data.sourceIndex ?? null);
      } else {
        stream = new VideoStream(sourceNode as FilterNode | InputNode, edge.data.sourceIndex ?? null); // Default to video for 'av' type
      }

      // Add stream to target node's inputs with correct index
      if (targetNode instanceof FilterNode || targetNode instanceof OutputNode) {
        const targetIndex = edge.data.targetIndex ?? 0;
        targetNode.inputs[targetIndex] = stream;
      }
    }
  });

  // Create global node with all output nodes
  const outputNodes = Array.from(nodeMap.values()).filter(
    (node): node is OutputNode => node instanceof OutputNode
  );

  return new GlobalNode(
    outputNodes.map((node) => new OutputStream(node)),
    {}
  );
}
