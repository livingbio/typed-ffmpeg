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

  const isValidConnection = (connection: Connection): boolean => {
    const sourceNode = nodes.find((n) => n.id === connection.source);
    const targetNode = nodes.find((n) => n.id === connection.target);

    if (!sourceNode || !targetNode || !connection.sourceHandle || !connection.targetHandle) {
      console.error('Invalid connection: missing node or handle', {
        connection,
        sourceNode,
        targetNode,
      });
      return false;
    }

    // Get the source and target handle types
    const sourceHandle = connection.sourceHandle;
    const targetHandle = connection.targetHandle;

    // Rule 1: Input nodes can have multiple outgoing edges marked as "av"
    if (sourceNode.data.filterType === 'input') {
      console.log('Input node connection allowed');
      return true;
    }

    // Rule 4: Output nodes can accept all types and multiple connections
    if (targetNode.data.filterType === 'output') {
      console.log('Output node connection allowed');
      return true;
    }

    // Rule 2: FilterNode input handles can only connect to one edge
    if (targetNode.data.filterType === 'filter') {
      const targetHasConnection = edges.some(
        (edge) => edge.target === connection.target && edge.targetHandle === connection.targetHandle
      );
      if (targetHasConnection) {
        console.error('Target handle already has a connection');
        return false;
      }
    }

    // Get the types from the data-type attribute
    const sourceHandleElement = document.querySelector(`[data-handle-id="${sourceHandle}"]`);
    const targetHandleElement = document.querySelector(`[data-handle-id="${targetHandle}"]`);

    if (!sourceHandleElement || !targetHandleElement) {
      console.error('Could not find handle elements', { sourceHandle, targetHandle });
      return false;
    }

    const sourceType = sourceHandleElement.getAttribute('data-type') as EdgeType;
    const targetType = targetHandleElement.getAttribute('data-type') as EdgeType;

    console.log('Connection types:', { sourceType, targetType, sourceHandle, targetHandle });

    // Rule 3: FilterNode output handles mark the edge type
    // Rule 2: FilterNode input handles must match the type or accept 'av'
    if (sourceNode.data.filterType === 'filter' && targetNode.data.filterType === 'filter') {
      // If source is 'av', it can connect to anything
      if (sourceType === 'av') {
        console.log('Source is AV, connection allowed');
        return true;
      }
      // If target is 'av', it can accept anything
      if (targetType === 'av') {
        console.log('Target is AV, connection allowed');
        return true;
      }
      // Otherwise, types must match exactly
      const isValid = sourceType === targetType;
      console.log('Filter to filter connection:', { isValid, sourceType, targetType });
      return isValid;
    }

    console.error('Invalid connection type');
    return false;
  };

  const onConnect = useCallback(
    (params: Connection) => {
      console.log('Connection attempt:', params);

      if (isValidConnection(params) && params.source && params.target) {
        const sourceNode = nodes.find((node) => node.id === params.source);
        console.log('Source node:', sourceNode);

        // Determine the edge type
        let edgeType: EdgeType = 'av';
        if (sourceNode?.data.filterType === 'filter' && params.sourceHandle) {
          // Get the filter definition
          const filter = predefinedFilters.find((f) => f.name === sourceNode.data.filterName);
          if (filter) {
            // Get the output type from the filter definition
            const outputIndex = parseInt(params.sourceHandle.split('-')[1] || '0');
            const outputType = filter.stream_typings_output[outputIndex];
            if (outputType) {
              const typeValue = outputType.type.value.toLowerCase();
              if (typeValue === 'audio') {
                edgeType = 'audio';
              } else if (typeValue === 'video') {
                edgeType = 'video';
              }
            }
          }
          console.log('Setting edge type from filter:', {
            filterName: sourceNode.data.filterName,
            outputType: filter?.stream_typings_output,
            edgeType,
          });
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
      // Handle input and output nodes
      if (filterType === 'input' || filterType === 'output') {
        const newNode: Node = {
          id: `${filterType}-${Date.now()}`,
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
          },
        };
        setNodes((nds) => [...nds, newNode]);
        return;
      }

      // Handle regular filter nodes
      const filter = predefinedFilters.find((f) => f.name === filterType);
      if (!filter) return;

      const newNode: Node = {
        id: `${filterType}-${Date.now()}`,
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
