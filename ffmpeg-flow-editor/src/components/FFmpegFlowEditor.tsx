import { useCallback, useEffect, useState } from 'react';
import ReactFlow, {
  Node,
  Edge,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  ReactFlowInstance,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { Box } from '@mui/material';
import FilterNode from './FilterNode';
import Sidebar from './Sidebar';
import { predefinedFilters } from '../types/ffmpeg';
import { EdgeType, EDGE_COLORS, EdgeData } from '../types/edge';
import { NodeMappingManager } from '../utils/nodeMapping';

const nodeTypes = {
  filter: FilterNode,
};

export default function FFmpegFlowEditor() {
  const [nodeMappingManager] = useState(() => new NodeMappingManager());
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [reactFlowInstance, setReactFlowInstance] = useState<ReactFlowInstance | null>(null);

  // Add event listener for node data update
  useEffect(() => {
    const handleNodeDataUpdate = (event: CustomEvent) => {
      const { id, data } = event.detail;
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id);
      if (node) {
        nodeMappingManager.updateNode(id, {
          kwargs: data.parameters,
        });
      }
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
  }, [setNodes, nodeMappingManager]);

  const isValidConnection = useCallback(
    (connection: Connection): boolean => {
      // Rule 1: Can't connect to input nodes
      const targetNode = nodes.find((node) => node.id === connection.target);
      if (targetNode?.data.filterType === 'input') {
        console.log('Invalid connection: Cannot connect to input nodes');
        return false;
      }

      // Rule 2: Can't connect from output nodes
      const sourceNode = nodes.find((node) => node.id === connection.source);
      if (sourceNode?.data.filterType === 'output') {
        console.log('Invalid connection: Cannot connect from output nodes');
        return false;
      }

      return true;
    },
    [nodes]
  );

  const onConnect = useCallback(
    (params: Connection) => {
      if (isValidConnection(params) && params.source && params.target) {
        const sourceIndex = parseInt(params.sourceHandle?.split('-')[1] || '0');
        const targetIndex = parseInt(params.targetHandle?.split('-')[1] || '0');

        try {
          const edgeId = nodeMappingManager.addEdgeToMapping(
            params.source,
            params.target,
            sourceIndex,
            targetIndex
          );

          let edgeType: EdgeType = 'av';

          // Determine edge type from source node
          const sourceNode = nodes.find((node) => node.id === params.source);
          if (sourceNode?.data.filterType === 'filter') {
            const handle = sourceNode.data.handles.outputs.find(
              (h: { id: string; type: EdgeType }) => h.id === params.sourceHandle
            );
            if (handle) {
              edgeType = handle.type;
            }
          } else if (sourceNode?.data.filterType === 'input') {
            edgeType = 'av';
          }

          const newEdge: Edge<EdgeData> = {
            ...params,
            id: edgeId,
            style: { stroke: EDGE_COLORS[edgeType] },
            data: { type: edgeType },
            source: params.source,
            target: params.target,
            type: 'smoothstep',
            animated: false,
          };

          setEdges((eds) => addEdge(newEdge, eds));
        } catch (error) {
          console.error('Failed to add edge:', error);
        }
      }
    },
    [isValidConnection, setEdges, nodes, nodeMappingManager]
  );

  const onAddFilter = useCallback(
    (
      filterType: string,
      parameters?: Record<string, string>,
      position?: { x: number; y: number }
    ) => {
      try {
        let nodeId: string;

        // Handle input and output nodes
        if (filterType === 'input' || filterType === 'output') {
          nodeId = nodeMappingManager.addNodeToMapping({
            type: filterType,
            filename: filterType === 'input' ? 'input.mp4' : 'output.mp4',
            inputs: [],
            kwargs: parameters,
          });

          const newNode: Node = {
            id: nodeId,
            type: 'filter',
            position: position || {
              x: Math.random() * 500 + 200,
              y: Math.random() * 300 + 100,
            },
            data: {
              label: filterType === 'input' ? 'Input' : 'Output',
              filterType: filterType,
              filterString: filterType === 'input' ? '[0:v]' : '[outv]',
              parameters: parameters || {},
              handles: {
                inputs: filterType === 'output' ? [{ id: 'input-0', type: 'av' }] : [],
                outputs: filterType === 'input' ? [{ id: 'output-0', type: 'av' }] : [],
              },
            },
          };
          setNodes((nds) => [...nds, newNode]);
          return;
        }

        // Handle regular filter nodes
        const filter = predefinedFilters.find((f) => f.name === filterType);
        if (!filter) return;

        nodeId = nodeMappingManager.addNodeToMapping({
          type: 'filter',
          name: filter.name,
          input_typings: filter.stream_typings_input.map((t) => t.type),
          output_typings: filter.stream_typings_output.map((t) => t.type),
          kwargs: parameters,
        });

        const newNode: Node = {
          id: nodeId,
          type: 'filter',
          position: position || {
            x: Math.random() * 500 + 200,
            y: Math.random() * 300 + 100,
          },
          data: {
            label: filter.name,
            filterType: 'filter',
            filterName: filter.name,
            parameters: parameters || {},
            handles: {
              inputs: filter.stream_typings_input.map((ioType, index) => {
                const typeValue = ioType.type.value.toLowerCase();
                const type: EdgeType =
                  typeValue === 'audio' ? 'audio' : typeValue === 'video' ? 'video' : 'av';
                return {
                  id: `input-${index}`,
                  type,
                };
              }),
              outputs: filter.stream_typings_output.map((ioType, index) => {
                const typeValue = ioType.type.value.toLowerCase();
                const type: EdgeType =
                  typeValue === 'audio' ? 'audio' : typeValue === 'video' ? 'video' : 'av';
                return {
                  id: `output-${index}`,
                  type,
                };
              }),
            },
          },
        };

        setNodes((nds) => [...nds, newNode]);
      } catch (error) {
        console.error('Failed to add node:', error);
      }
    },
    [setNodes, nodeMappingManager]
  );

  const onDragOver = useCallback((event: React.DragEvent) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  }, []);

  const onDrop = useCallback(
    (event: React.DragEvent) => {
      event.preventDefault();

      const type = event.dataTransfer.getData('application/reactflow');
      if (typeof type === 'undefined' || !type) {
        return;
      }

      // Get the position where the node was dropped
      const position = reactFlowInstance?.screenToFlowPosition({
        x: event.clientX,
        y: event.clientY,
      });

      if (position) {
        onAddFilter(type, undefined, position);
      }
    },
    [reactFlowInstance, onAddFilter]
  );

  return (
    <Box
      sx={{
        position: 'fixed',
        width: '100vw',
        height: '100vh',
        top: 0,
        left: 0,
        overflow: 'hidden',
      }}
    >
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        isValidConnection={isValidConnection}
        nodeTypes={nodeTypes}
        onInit={setReactFlowInstance}
        onDragOver={onDragOver}
        onDrop={onDrop}
        fitView
        style={{
          width: '100%',
          height: '100%',
          background: '#f5f5f5',
        }}
      >
        <Background />
        <Controls />
      </ReactFlow>
      <Sidebar nodes={nodes} edges={edges} onAddFilter={onAddFilter} />
    </Box>
  );
}
