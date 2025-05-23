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
  ReactFlowProvider,
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
import {
  VideoStream,
  AudioStream,
  AVStream,
  Stream,
  FilterableStream,
  OutputStream,
  StreamType,
} from '../types/dag';
import { NodeData } from '../types/node';

const nodeTypes = {
  filter: FilterNode,
  global: GlobalNode,
  input_: InputNode,
  output_: OutputNode,
} as const;

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

// Helper to generate random filename
function generateRandomFilename(type: 'input' | 'output'): string {
  const randomId = Math.random().toString(36).substring(2, 8);
  return `${type}-${randomId}.mp4`;
}

// Helper function to create a node
const createNode = async (
  filterType: string,
  parameters: Record<string, string> | undefined,
  position: { x: number; y: number } | undefined,
  nodeMappingManager: NodeMappingManager,
  filter?: (typeof predefinedFilters)[0]
): Promise<Node<NodeData>> => {
  const defaultPosition = {
    x: Math.random() * 500 + 200,
    y: Math.random() * 300 + 100,
  };
  let type: 'global' | 'input' | 'output' | 'filter';
  let filename: string | undefined;
  let name: string;
  let nodeType_: 'global' | 'input_' | 'output_' | 'filter';

  if (filterType == 'global') {
    type = 'global';
    name = 'global';
    nodeType_ = 'global';
  } else if (filterType == 'input') {
    type = 'input';
    name = 'input';
    nodeType_ = 'input_';
    filename = parameters?.filename || generateRandomFilename('input');
  } else if (filterType == 'output') {
    type = 'output';
    name = 'output';
    nodeType_ = 'output_';
    filename = parameters?.filename || generateRandomFilename('output');
  } else {
    type = 'filter';
    name = filterType;
    nodeType_ = 'filter';
  }

  const nodeId = await nodeMappingManager.addNode({
    type,
    name,
    filename,
    inputs: [],
    filter,
    kwargs: parameters || {},
  });
  const nodeData = nodeMappingManager.getNodeData(nodeId);

  return {
    id: nodeId,
    type: nodeType_,
    position: position || defaultPosition,
    data: nodeData,
  };
};

// Helper function to create an edge
const createEdge = (
  source: string,
  target: string,
  sourceHandle: string | null,
  targetHandle: string | null,
  nodeMappingManager: NodeMappingManager
): Edge<EdgeData> => {
  if (!sourceHandle || !targetHandle) {
    throw new Error('Source or target handle not found');
  }

  const sourceIndex = parseInt(sourceHandle.split('-')[1] || '0');
  const targetIndex = parseInt(targetHandle.split('-')[1] || '0');

  const edgeId = nodeMappingManager.addEdge(source, target, sourceIndex, targetIndex);

  // Get the stream from the edge mapping
  const stream = nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId);
  if (!stream) {
    throw new Error('Stream not found in mapping');
  }

  // Determine edge type using helper function
  const edgeType = getEdgeTypeFromStream(stream);

  return {
    id: edgeId,
    source,
    target,
    sourceHandle,
    targetHandle,
    style: { stroke: EDGE_COLORS[edgeType] },
    data: { type: edgeType, sourceIndex, targetIndex },
    type: 'smoothstep',
    animated: false,
  };
};

function FFmpegFlowEditorInner() {
  const [nodeMappingManager] = useState(() => new NodeMappingManager());
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [reactFlowInstance, setReactFlowInstance] = useState<ReactFlowInstance | null>(null);

  // Initialize nodes
  useEffect(() => {
    // Create React Flow nodes
    const initializeNodes = async () => {
      const initialNodes = [
        await createNode('input', {}, { x: 100, y: 300 }, nodeMappingManager),
        await createNode('output', {}, { x: 1600, y: 300 }, nodeMappingManager),
        await createNode('global', {}, { x: 2000, y: 300 }, nodeMappingManager),
      ];

      setNodes(initialNodes);

      // Create initial edge between output and global nodes
      const outputNode = initialNodes[1]; // output node
      const globalNode = initialNodes[2]; // global node
      const initialEdge = createEdge(
        outputNode.id,
        globalNode.id,
        'output-0',
        'input-0',
        nodeMappingManager
      );

      setEdges([initialEdge]);
    };

    initializeNodes();
  }, [nodeMappingManager, setNodes, setEdges]);

  // Add event listener for node data update
  useEffect(() => {
    const handleNodeDataUpdate = async (event: Event) => {
      const customEvent = event as CustomEvent;
      const { id, data } = customEvent.detail;
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id);
      if (node) {
        await nodeMappingManager.updateNode(id, {
          kwargs: data.parameters,
          filename: data.filename,
        });
        // Get updated node data with new handles
        const updatedNodeData = nodeMappingManager.getNodeData(id);

        // Update node state
        setNodes((nds) =>
          nds.map((node) => {
            if (node.id === id) {
              return {
                ...node,
                data: {
                  ...node.data,
                  ...data,
                  handles: updatedNodeData.handles,
                },
              };
            }
            return node;
          })
        );
      } else {
        throw new Error(`Node ${id} not found`);
      }
    };

    window.addEventListener('updateNodeData', handleNodeDataUpdate);
    return () => {
      window.removeEventListener('updateNodeData', handleNodeDataUpdate);
    };
  }, [setNodes, nodeMappingManager]);

  const isValidConnection = useCallback(
    (connection: Connection): boolean => {
      // Rule 1: Can't connect to input nodes
      const targetNode = nodes.find((node) => node.id === connection.target) as
        | Node<NodeData>
        | undefined;
      const sourceNode = nodes.find((node) => node.id === connection.source) as
        | Node<NodeData>
        | undefined;
      const sourceIndex = parseInt(connection.sourceHandle?.split('-')[1] || '0');
      const targetIndex = parseInt(connection.targetHandle?.split('-')[1] || '0');

      switch (sourceNode?.data.nodeType) {
        case 'global':
          return false;
        case 'input':
          return true;
        case 'output':
          return targetNode?.data.nodeType === 'global';
        case 'filter':
          // if there is already an edge connected to the source node, return false
          return true;
      }

      switch (targetNode?.data.nodeType) {
        case 'global':
          return sourceNode?.data.nodeType === 'output';
        case 'input':
          return false;
        case 'output':
          return true;
        case 'filter':
          return (
            sourceNode?.data.handles.outputs[sourceIndex].type ===
            targetNode?.data.handles.inputs[targetIndex].type
          );
      }

      return false;
    },
    [nodes]
  );

  const onConnect = useCallback(
    (params: Connection) => {
      if (isValidConnection(params) && params.source && params.target) {
        const newEdge = createEdge(
          params.source,
          params.target,
          params.sourceHandle,
          params.targetHandle,
          nodeMappingManager
        );

        setEdges((eds) => addEdge(newEdge, eds));
      }
    },
    [isValidConnection, setEdges, nodeMappingManager]
  );

  const onAddNode = useCallback(
    async (
      filterType: string,
      parameters?: Record<string, string>,
      position?: { x: number; y: number }
    ) => {
      const newNode = await createNode(filterType, parameters, position, nodeMappingManager);
      setNodes((nds) => [...nds, newNode]);
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

  const onNodesDelete = useCallback(
    (nodesToDelete: Node[]) => {
      nodesToDelete.forEach((node) => {
        // Remove node from mapping
        nodeMappingManager.removeNode(node.id);
      });
    },
    [nodeMappingManager]
  );

  const onEdgesDelete = useCallback(
    (edgesToDelete: Edge[]) => {
      edgesToDelete.forEach((edge) => {
        // Remove edge from mapping
        nodeMappingManager.removeEdge(edge.id);
      });
    },
    [nodeMappingManager]
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
        onNodesDelete={onNodesDelete}
        onEdgesDelete={onEdgesDelete}
        isValidConnection={isValidConnection}
        nodeTypes={nodeTypes}
        onInit={setReactFlowInstance}
        onDragOver={onDragOver}
        onDrop={onDrop}
        defaultViewport={{ x: 0, y: 0, zoom: 0.75 }}
        fitView={false}
        minZoom={0.1}
        maxZoom={2}
        style={{
          width: '100%',
          height: '100%',
          background: '#f5f5f5',
        }}
      >
        <Background />
        <Controls />
      </ReactFlow>
      <Sidebar onAddFilter={onAddNode} nodeMappingManager={nodeMappingManager} />
    </Box>
  );
}

export default function FFmpegFlowEditor() {
  return (
    <ReactFlowProvider>
      <FFmpegFlowEditorInner />
    </ReactFlowProvider>
  );
}
