import React, { useCallback } from 'react';
import ReactFlow, {
  Node,
  Edge,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
} from 'reactflow';
import 'reactflow/dist/style.css';
import FilterNode from './FilterNode';
import InputNode from './InputNode';
import OutputNode from './OutputNode';
import { NodeData } from '../types/node';

// Define node types
const nodeTypes = {
  filter: FilterNode,
  input: InputNode,
  output: OutputNode,
};

// Initial nodes
const initialNodes: Node<NodeData>[] = [
  {
    id: 'input',
    type: 'input',
    position: { x: 100, y: 100 },
    data: {
      label: 'Input',
      filterType: 'input',
      filterString: '[0:v]',
      parameters: {},
      filename: 'input.mp4',
      handles: {
        inputs: [],
        outputs: [{ id: 'output', type: 'video' }]
      }
    },
  },
  {
    id: 'filter',
    type: 'filter',
    position: { x: 400, y: 100 },
    data: {
      label: 'Scale',
      filterType: 'filter',
      filterName: 'scale',
      filterString: 'scale=1280:720',
      parameters: {
        width: '1280',
        height: '720'
      },
      handles: {
        inputs: [{ id: 'input', type: 'video' }],
        outputs: [{ id: 'output', type: 'video' }]
      }
    },
  },
  {
    id: 'output',
    type: 'output',
    position: { x: 700, y: 100 },
    data: {
      label: 'Output',
      filterType: 'output',
      filterString: '[outv]',
      parameters: {},
      filename: 'output.mp4',
      handles: {
        inputs: [{ id: 'input', type: 'video' }],
        outputs: []
      }
    },
  },
];

// Initial edges
const initialEdges: Edge[] = [
  {
    id: 'input-to-filter',
    source: 'input',
    target: 'filter',
    sourceHandle: 'output',
    targetHandle: 'input',
    type: 'av',
    data: { type: 'video' }
  },
  {
    id: 'filter-to-output',
    source: 'filter',
    target: 'output',
    sourceHandle: 'output',
    targetHandle: 'input',
    type: 'av',
    data: { type: 'video' }
  }
];

const MinimalFlowEditor: React.FC = () => {
  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        fitView
      >
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
};

export default MinimalFlowEditor; 