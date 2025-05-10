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
import GlobalNode from './GlobalNode';
import InputNode from './InputNode';
import OutputNode from './OutputNode';

import Sidebar from './Sidebar';
import { predefinedFilters } from '../types/ffmpeg';
import { EdgeType, EDGE_COLORS, EdgeData } from '../types/edge';
import { NodeMappingManager } from '../utils/nodeMapping';
import { VideoStream, AudioStream, AVStream, Stream } from '../types/dag';

const nodeTypes = {
  ffmpeg_filter: FilterNode,
  global: GlobalNode,
  input: InputNode,
  output: OutputNode,
};

// Helper function to determine edge type from stream
const getEdgeTypeFromStream = (stream: Stream): EdgeType => {
  if (stream instanceof VideoStream) {
    return 'video';
  } else if (stream instanceof AudioStream) {
    return 'audio';
  } else if (stream instanceof AVStream) {
    return 'av';
  }
  return 'av'; // Default fallback
};

// Helper function to create a node
const createNode = (
  nodeId: string,
  nodeType: string,
  parameters: Record<string, string> | undefined,
  position: { x: number; y: number } | undefined,
  filter?: typeof predefinedFilters[0]
): Node => {
  const defaultPosition = {
    x: Math.random() * 500 + 200,
    y: Math.random() * 300 + 100,
  };

  let handles: { inputs: { id: string; type: string }[]; outputs: { id: string; type: string }[] };

  switch (nodeType) {
    case 'global':
      handles = {
        inputs: [{id: 'input-0', type: 'av'}],
        outputs: [],
      };
      break;
    case 'input':
      handles = {
        inputs: [],
        outputs: [{id: 'output-0', type: 'av'}],
      };
      break;
    case 'output':
      handles = {
        inputs: [{id: 'input-0', type: 'av'}],
        outputs: [{id: 'output-0', type: 'av'}],
      };
      break;
    case 'ffmpeg_filter':
      if (!filter) {
        throw new Error(`Filter ${nodeType} not found`);
      }
      handles = {
        inputs: filter.stream_typings_input.map((ioType, index) => {
          const typeValue = ioType.type.value;
          if (typeValue === 'audio' || typeValue === 'video') {
            return {
              id: `input-${index}`,
              type: typeValue,
            };
          }
          throw new Error(`Invalid stream type: ${typeValue}`);
        }),
        outputs: filter.stream_typings_output.map((ioType, index) => {
          const typeValue = ioType.type.value;
          if (typeValue === 'audio' || typeValue === 'video') {
            return {
              id: `output-${index}`,
              type: typeValue,
            };
          }
          throw new Error(`Invalid stream type: ${typeValue}`);
        }),
      };
      break;
    default:
      throw new Error(`Invalid node type: ${nodeType}`);
  }

  return {
    id: nodeId,
    type: nodeType,
    position: position || defaultPosition,
    data: {
      label: nodeType,
      filterType: nodeType,
      filterName: nodeType === 'filter' ? filter?.name : undefined,
      parameters: parameters || {},
      handles,
    },
  }
};

export default function FFmpegFlowEditor() {
  const [nodeMappingManager] = useState(() => new NodeMappingManager());
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [reactFlowInstance, setReactFlowInstance] = useState<ReactFlowInstance | null>(null);

  // Initialize nodes
  useEffect(() => {
    // Add input node
    const inputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
      inputs: [],
      kwargs: {},
    });

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
      kwargs: {},
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
      kwargs: {},
    });

    // Create React Flow nodes
    const initialNodes = [
      createNode(inputNodeId, 'input', {}, { x: 100, y: 300 }),
      createNode(outputNodeId, 'output', {}, { x: 450, y: 300 }),
      createNode(globalNodeId, 'global', {}, { x: 800, y: 300 }),
    ];

    setNodes(initialNodes);
  }, [nodeMappingManager, setNodes]);

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
      else {
        throw new Error(`Node ${id} not found`);
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
      if (sourceNode?.data.filterType === 'global') {
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

          // Get the stream from the edge mapping
          const stream = nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId);
          if (!stream) {
            throw new Error('Stream not found in mapping');
          }

          // Determine edge type using helper function
          const edgeType = getEdgeTypeFromStream(stream);

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
    [isValidConnection, setEdges, nodeMappingManager]
  );

  const onAddNode = useCallback(
    (
      nodeType: string,
      parameters?: Record<string, string>,
      position?: { x: number; y: number }
    ) => {
      try {
        let nodeId: string;

        // Handle input and output nodes
        if (nodeType === 'input' || nodeType === 'output') {
          nodeId = nodeMappingManager.addNodeToMapping({
            type: nodeType,
            filename: nodeType === 'input' ? 'input.mp4' : 'output.mp4',
            inputs: [],
            kwargs: parameters,
          });
        } else {
          // Handle regular filter nodes
          const filter = predefinedFilters.find((f) => f.name === nodeType);
          if (!filter) {
            throw new Error(`Filter ${nodeType} not found`);
          }

          nodeId = nodeMappingManager.addNodeToMapping({
            type: 'ffmpeg_filter',
            name: filter.name,
            input_typings: filter.stream_typings_input.map((t) => t.type),
            output_typings: filter.stream_typings_output.map((t) => t.type),
            kwargs: parameters,
          });
        }

        const newNode = createNode(
          nodeId,
          nodeType,
          parameters,
          position,
          predefinedFilters.find((f) => f.name === nodeType)
        );

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
        onAddNode(type, undefined, position);
      }
    },
    [reactFlowInstance, onAddNode]
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
      <Sidebar nodes={nodes} edges={edges} onAddFilter={onAddNode} />
    </Box>
  );
}
