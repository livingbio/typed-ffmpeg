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
import { validateConnection } from '../utils/connectionValidation';

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
      parameters: {},
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
      parameters: {},
    },
  },
];

const initialEdges: Edge[] = [];

export default function FFmpegFlowEditor() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const [reactFlowInstance, setReactFlowInstance] = useState<ReactFlowInstance | null>(null);

  // Add event listener for node data update
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

  // Use the imported validation function
  const isValidConnection = (connection: Connection): boolean => {
    return validateConnection(connection, nodes, edges);
  };

  const onConnect = useCallback(
    (params: Connection) => {
      if (isValidConnection(params) && params.source && params.target) {
        const sourceNode = nodes.find((node) => node.id === params.source);

        // Determine the edge type
        let edgeType: EdgeType = 'av';
        if (sourceNode?.data.filterType === 'filter' && params.sourceHandle) {
          interface HandleInfo {
            id: string;
            type: EdgeType;
          }

          // Debug log the handles and source handle
          console.log('Finding handle type:', {
            sourceHandle: params.sourceHandle,
            allOutputs: sourceNode.data.handles.outputs,
            filterName: sourceNode.data.filterName,
          });

          const handle = (sourceNode.data.handles.outputs as HandleInfo[]).find(
            (h) => h.id === params.sourceHandle
          );
          console.log('Found handle:', handle);

          if (handle) {
            edgeType = handle.type;
            console.log('Setting edge type from handle:', {
              filterName: sourceNode.data.filterName,
              edgeType,
              handle,
            });
          } else {
            console.error('Could not find handle:', {
              sourceHandle: params.sourceHandle,
              availableHandles: sourceNode.data.handles.outputs,
            });
          }
        } else if (sourceNode?.data.filterType === 'input') {
          // Rule 1: Input nodes mark edges as "av"
          edgeType = 'av';
          console.log('Setting edge type from input node');
        }

        console.log('Final edge type:', {
          type: edgeType,
          color: EDGE_COLORS[edgeType],
          isValid: !!EDGE_COLORS[edgeType],
        });

        if (!EDGE_COLORS[edgeType]) {
          console.error('Invalid edge type:', edgeType);
          throw new Error(`Invalid edge type: ${edgeType}`);
        }

        const newEdge: Edge<EdgeData> = {
          ...params,
          id: `edge-${params.source}-${params.sourceHandle}-${params.target}-${params.targetHandle}`,
          style: { stroke: EDGE_COLORS[edgeType] },
          data: { type: edgeType },
          source: params.source,
          target: params.target,
          type: 'smoothstep',
          animated: false,
        };

        console.log('Creating new edge:', {
          newEdge,
          color: EDGE_COLORS[edgeType],
          style: newEdge.style,
        });
        setEdges((eds) => addEdge(newEdge, eds));
      }
    },
    [isValidConnection, setEdges, nodes, edges]
  );

  const onAddFilter = useCallback(
    (
      filterType: string,
      parameters?: Record<string, string>,
      position?: { x: number; y: number }
    ) => {
      const nodeId = `${filterType}-${Date.now()}`;

      // Handle input and output nodes
      if (filterType === 'input' || filterType === 'output') {
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
            parameters: {},
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

      // Debug log for filter type determination
      console.log('Creating filter node:', {
        filterType,
        inputTypes: filter.stream_typings_input.map((t) => t.type.value),
        outputTypes: filter.stream_typings_output.map((t) => t.type.value),
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
              console.log('Input handle type:', { index, typeValue, type });
              return {
                id: `input-${index}`,
                type,
              };
            }),
            outputs: filter.stream_typings_output.map((ioType, index) => {
              const typeValue = ioType.type.value.toLowerCase();
              const type: EdgeType =
                typeValue === 'audio' ? 'audio' : typeValue === 'video' ? 'video' : 'av';
              console.log('Output handle type:', { index, typeValue, type });
              return {
                id: `output-${index}`,
                type,
              };
            }),
          },
        },
      };

      setNodes((nds) => [...nds, newNode]);
    },
    [setNodes]
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

  const handleImportFlow = useCallback(
    (newNodes: Node[], newEdges: Edge[]) => {
      setNodes(newNodes);
      setEdges(newEdges);
    },
    [setNodes, setEdges]
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
      <Sidebar
        nodes={nodes}
        edges={edges}
        onAddFilter={onAddFilter}
        onImportFlow={handleImportFlow}
      />
    </Box>
  );
}
