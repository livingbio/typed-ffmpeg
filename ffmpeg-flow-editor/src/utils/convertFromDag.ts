import { Node, Edge } from 'reactflow';
import { FilterNode, InputNode, OutputNode, GlobalNode } from '../types/dag';
import { NodeData, InputNodeData, OutputNodeData, FilterNodeData } from '../types/node';
import { EdgeType } from '../types/edge';

export function convertFromDag(dag: GlobalNode): { nodes: Node<NodeData>[]; edges: Edge[] } {
  const nodes: Node<NodeData>[] = [];
  const edges: Edge[] = [];
  const nodeMap = new Map<string, string>(); // Maps DAG node IDs to ReactFlow node IDs

  // Helper function to create a unique ID for a node
  const createNodeId = (node: FilterNode | InputNode | OutputNode) => {
    if (node instanceof InputNode) {
      return `input-${node.filename}`;
    } else if (node instanceof OutputNode) {
      return `output-${node.filename}`;
    } else if (node instanceof FilterNode) {
      return `filter-${node.name}-${Math.random().toString(36).substr(2, 9)}`;
    }
    return '';
  };

  // Helper function to convert stream type to edge type
  const getEdgeType = (type: string): EdgeType => {
    switch (type) {
      case 'av':
        return 'av';
      case 'audio':
        return 'audio';
      case 'video':
      default:
        return 'video';
    }
  };

  // First pass: Create all nodes
  dag.inputs.forEach((output) => {
    const outputNode = output.node;
    const outputId = createNodeId(outputNode);
    nodeMap.set(outputId, outputId);

    // Create output node
    const outputData: OutputNodeData = {
      label: `Output: ${outputNode.filename}`,
      filename: outputNode.filename,
      filterType: 'output',
      filterString: '',
      parameters: {},
      handles: {
        inputs: [{ type: 'video', id: 'input' }],
        outputs: []
      }
    };

    nodes.push({
      id: outputId,
      type: 'output',
      position: { x: 800, y: nodes.length * 150 },
      data: outputData
    });

    // Process input nodes and filter nodes recursively
    const processNode = (node: FilterNode | InputNode, x: number, y: number) => {
      const nodeId = createNodeId(node);
      if (!nodeMap.has(nodeId)) {
        nodeMap.set(nodeId, nodeId);

        if (node instanceof InputNode) {
          const inputData: InputNodeData = {
            label: `Input: ${node.filename}`,
            filename: node.filename,
            filterType: 'input',
            filterString: '',
            parameters: {},
            handles: {
              inputs: [],
              outputs: [{ type: 'video', id: 'output' }]
            }
          };

          nodes.push({
            id: nodeId,
            type: 'input',
            position: { x, y },
            data: inputData
          });
        } else if (node instanceof FilterNode) {
          const filterData: FilterNodeData = {
            label: node.name,
            filterName: node.name,
            filterType: 'filter',
            filterString: '',
            parameters: Object.fromEntries(
              Object.entries(node.kwargs).map(([k, v]) => [k, String(v)])
            ),
            handles: {
              inputs: node.input_typings.map((type, index) => ({
                type: getEdgeType(type.value),
                id: `input-${index}`
              })),
              outputs: node.output_typings.map((type, index) => ({
                type: getEdgeType(type.value),
                id: `output-${index}`
              }))
            }
          };

          nodes.push({
            id: nodeId,
            type: 'filter',
            position: { x, y },
            data: filterData
          });

          // Process input nodes recursively
          node.inputs.forEach((input, index) => {
            if (input.node instanceof FilterNode || input.node instanceof InputNode) {
              processNode(input.node, x - 200, y + index * 100);
            }
          });
        }
      }
    };

    // Process all input nodes for this output
    outputNode.inputs.forEach((input, index) => {
      if (input.node instanceof FilterNode || input.node instanceof InputNode) {
        processNode(input.node, 600, index * 150);
      }
    });
  });

  // Second pass: Create edges
  nodes.forEach((node) => {
    const dagNode = Array.from(nodeMap.entries()).find(([, id]) => id === node.id)?.[0];
    if (dagNode) {
      const dagNodeInstance = dag.inputs.find(o => createNodeId(o.node) === dagNode)?.node as OutputNode | FilterNode | undefined;
      if (dagNodeInstance) {
        dagNodeInstance.inputs.forEach((input, index) => {
          const sourceId = nodeMap.get(createNodeId(input.node));
          if (sourceId) {
            edges.push({
              id: `${sourceId}-${node.id}`,
              source: sourceId,
              target: node.id,
              sourceHandle: 'output',
              targetHandle: `input-${index}`,
              data: { type: 'video' }
            });
          }
        });
      }
    }
  });

  return { nodes, edges };
} 