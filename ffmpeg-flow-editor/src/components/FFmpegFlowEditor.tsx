import { useState, useCallback, useEffect } from 'react';
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
import { Box } from '@mui/material';
import FilterNode from './FilterNode';
import Sidebar from './Sidebar';
import { predefinedFilters } from '../types/ffmpeg';

const nodeTypes = {
  filter: FilterNode,
};

const initialNodes: Node[] = [
  {
    id: 'input',
    type: 'filter',
    position: { x: 100, y: 100 },
    data: {
      label: 'Input',
      filterType: 'input',
      filterString: '[0:v]',
    },
  },
  {
    id: 'output',
    type: 'filter',
    position: { x: 800, y: 100 },
    data: {
      label: 'Output',
      filterType: 'output',
      filterString: '[outv]',
    },
  },
];

const initialEdges: Edge[] = [];

export default function FFmpegFlowEditor() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  // Add event listener for node data updates
  useEffect(() => {
    const handleNodeDataUpdate = (event: CustomEvent) => {
      const { id, data } = event.detail;
      setNodes((nds) =>
        nds.map((node) => {
          if (node.id === id) {
            return {
              ...node,
              data: {
                ...node.data,
                ...data,
              },
            };
          }
          return node;
        })
      );
    };

    window.addEventListener('updateNodeData', handleNodeDataUpdate as EventListener);
    return () => {
      window.removeEventListener('updateNodeData', handleNodeDataUpdate as EventListener);
    };
  }, [setNodes]);

  const onConnect = useCallback(
    (params: Connection) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  const onAddFilter = useCallback(
    (filterType: string, parameters?: Record<string, string>) => {
      const filter = predefinedFilters.find(f => f.name === filterType);
      if (!filter) return;

      const newNode: Node = {
        id: `${filterType}-${Date.now()}`,
        type: 'filter',
        position: {
          x: Math.random() * 500 + 200,
          y: Math.random() * 300 + 100,
        },
        data: {
          label: filter.label,
          filterType: 'filter',
          filterName: filter.name,
          parameters: parameters || {},
        },
      };

      setNodes((nds) => [...nds, newNode]);
    },
    [setNodes]
  );

  return (
    <Box sx={{
      position: 'fixed',
      width: '100vw',
      height: '100vh',
      top: 0,
      left: 0,
      overflow: 'hidden'
    }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        fitView
        style={{
          width: '100%',
          height: '100%',
          background: '#f5f5f5'
        }}
      >
        <Background />
        <Controls />
      </ReactFlow>
      <Sidebar nodes={nodes} edges={edges} onAddFilter={onAddFilter} />
    </Box>
  );
}
