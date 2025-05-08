import { Node, Edge } from 'reactflow';
import {
  FilterNode,
  InputNode,
  OutputNode,
  GlobalNode,
  VideoStream,
  AudioStream,
  OutputStream,
} from '../types/dag';
import { predefinedFilters } from '../types/ffmpeg';
import { EdgeType, EdgeData } from '../types/edge';

export function convertFromDag(dag: GlobalNode): { nodes: Node[]; edges: Edge[] } {
  const nodes: Node[] = [];
  const edges: Edge[] = [];
  const nodeMap = new Map<string, string>(); // Maps DAG node to React Flow node ID

  // Helper function to create a unique ID for a node
  const createNodeId = (node: FilterNode | InputNode | OutputNode) => {
    if (nodeMap.has(node.toString())) {
      return nodeMap.get(node.toString())!;
    }
    if (node instanceof InputNode) return 'input-0';
    if (node instanceof OutputNode) {
      const index = nodes.filter(n => n.data.filterType === 'output').length;
      return `output-${index}`;
    }
    // For filter nodes, use a consistent ID format
    return `${node.name}-${nodes.filter(n => n.data.filterName === node.name).length}`;
  };

  // Helper function to get edge type from stream
  const getEdgeType = (stream: VideoStream | AudioStream): EdgeType => {
    if (stream instanceof VideoStream) return 'video';
    if (stream instanceof AudioStream) return 'audio';
    return 'av';
  };

  // First pass: Create all nodes
  const processNode = (node: FilterNode | InputNode | OutputNode) => {
    if (nodeMap.has(node.toString())) return;

    const nodeId = createNodeId(node);
    nodeMap.set(node.toString(), nodeId);

    if (node instanceof InputNode) {
      nodes.push({
        id: nodeId,
        type: 'input',
        position: { x: 100, y: 100 }, // React-specific property
        data: {
          label: 'Input',
          filterType: 'input',
          filterString: '[0:v]',
          parameters: {},
          handles: {
            inputs: [],
            outputs: [{ id: 'output-0', type: 'av' }],
          },
        },
      });
    } else if (node instanceof OutputNode) {
      nodes.push({
        id: nodeId,
        type: 'output',
        position: { x: 800, y: 100 }, // React-specific property
        data: {
          label: 'Output',
          filterType: 'output',
          filterString: '[outv]',
          parameters: {},
          handles: {
            inputs: node.inputs.map((_, i) => ({ id: `input-${i}`, type: 'av' })),
            outputs: [],
          },
          filename: node.filename,
        },
      });
    } else if (node instanceof FilterNode) {
      const filter = predefinedFilters.find((f) => f.name === node.name);
      if (!filter) return;

      nodes.push({
        id: nodeId,
        type: 'filter',
        position: { x: Math.random() * 500 + 200, y: Math.random() * 300 + 100 }, // React-specific property
        data: {
          label: node.name,
          filterType: 'filter',
          filterName: node.name,
          parameters: node.kwargs,
          handles: {
            inputs: node.input_typings.map((type, index) => ({
              id: `input-${index}`,
              type: type.value === 'audio' ? 'audio' : type.value === 'video' ? 'video' : 'av',
            })),
            outputs: node.output_typings.map((type, index) => ({
              id: `output-${index}`,
              type: type.value === 'audio' ? 'audio' : type.value === 'video' ? 'video' : 'av',
            })),
          },
        },
      });
    }

    // Process all input streams recursively
    node.inputs.forEach((input) => {
      if (input instanceof VideoStream || input instanceof AudioStream) {
        processNode(input.node);
      }
    });
  };

  // Process all output nodes from the GlobalNode
  dag.inputs.forEach((outputStream) => {
    if (outputStream instanceof OutputStream) {
      processNode(outputStream.node);
    }
  });

  // Second pass: Create edges
  const createEdges = (node: FilterNode | InputNode | OutputNode) => {
    const sourceId = nodeMap.get(node.toString());
    if (!sourceId) return;

    node.inputs.forEach((input, index) => {
      if (input instanceof VideoStream || input instanceof AudioStream) {
        const targetId = nodeMap.get(input.node.toString());
        if (!targetId) return;

        const edgeType = getEdgeType(input);
        const edge: Edge<EdgeData> = {
          id: `edge-${targetId}-output-${input.index || 0}-${sourceId}-input-${index}`,
          source: targetId,
          target: sourceId,
          sourceHandle: `output-${input.index || 0}`,
          targetHandle: `input-${index}`,
          type: 'smoothstep',
          style: { stroke: edgeType === 'video' ? '#f44336' : edgeType === 'audio' ? '#2196f3' : '#9c27b0' },
          data: { type: edgeType },
        };
        edges.push(edge);
      }
    });
  };

  // Create edges for all nodes
  dag.inputs.forEach((outputStream) => {
    if (outputStream instanceof OutputStream) {
      createEdges(outputStream.node);
    }
  });

  return { nodes, edges };
} 