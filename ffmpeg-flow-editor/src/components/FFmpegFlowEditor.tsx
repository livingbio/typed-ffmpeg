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
import { VideoStream, AudioStream, AVStream, Stream, FilterableStream, OutputStream, StreamType } from '../types/dag';
import { NodeData } from '../types/node';

const nodeTypes = {
  filter: FilterNode,
  global: GlobalNode,
  input: InputNode,
  output: OutputNode,
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

// Helper function to create a node
const createNode = (
  filterType: string,
  parameters: Record<string, string> | undefined,
  position: { x: number; y: number } | undefined,
  nodeMappingManager: NodeMappingManager,
  filter?: typeof predefinedFilters[0]
): Node<NodeData> => {
  const defaultPosition = {
    x: Math.random() * 500 + 200,
    y: Math.random() * 300 + 100,
  };

  let handles: { inputs: { id: string; type: EdgeType }[]; outputs: { id: string; type: EdgeType }[] };
  let label: string;
  let mappingData: {
    type: 'global' | 'input' | 'output' | 'filter';
    name?: string;
    filename?: string;
    inputs: (FilterableStream | null)[] | OutputStream[];
    input_typings?: StreamType[];
    output_typings?: StreamType[];
    kwargs: Record<string, string>;
  };
  let nodeType: string;
  
  if (filterType == 'global') {
    nodeType = 'global';
  } else if (filterType == 'input') {
    nodeType = 'input';
  } else if (filterType == 'output') {
    nodeType = 'output';
  } else {
    nodeType = 'filter';
  }
  switch (nodeType) {
    case 'global':
      label = 'global';
      handles = {
        inputs: [{id: 'input-0', type: "av"}],
        outputs: [],
      };
      mappingData = {
        type: 'global',
        inputs: [],
        kwargs: parameters || {},
      };
      break;
    case 'input':
      label = 'input';
      handles = {
        inputs: [],
        outputs: [{id: 'output-0', type: 'av'}],
      };
      mappingData = {
        type: 'input',
        filename: 'input.mp4',
        inputs: [],
        kwargs: parameters || {},
      };
      break;
    case 'output':
      label = 'output';
      handles = {
        inputs: [{id: 'input-0', type: 'av'}],
        outputs: [{id: 'output-0', type: 'av'}],
      };
      mappingData = {
        type: 'output',
        filename: 'output.mp4',
        inputs: [],
        kwargs: parameters || {},
      };
      break;
    case 'filter':
      if (!filter) {
        throw new Error(`Filter ${nodeType} not found`);
      }
      label = filter.name;
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
      mappingData = {
        type: 'filter',
        name: filter.name,
        input_typings: filter.stream_typings_input.map((t) => t.type),
        output_typings: filter.stream_typings_output.map((t) => t.type),
        inputs: [],
        kwargs: parameters || {},
      };
      break;
    default:
      throw new Error(`Invalid node type: ${nodeType}`);
  }

  const nodeId = nodeMappingManager.addNodeToMapping(mappingData);

  return {
    id: nodeId,
    type: nodeType,
    position: position || defaultPosition,
    data: {
      label: label,
      filterName: filterType,
      nodeType: nodeType,
      parameters: parameters || {},
      handles,
    },
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

  const edgeId = nodeMappingManager.addEdgeToMapping(
    source,
    target,
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

export default function FFmpegFlowEditor() {
  const [nodeMappingManager] = useState(() => new NodeMappingManager());
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [reactFlowInstance, setReactFlowInstance] = useState<ReactFlowInstance | null>(null);

  // Initialize nodes
  useEffect(() => {
    // Create React Flow nodes
    const initialNodes = [
      createNode('input', {}, { x: 100, y: 300 }, nodeMappingManager),
      createNode('output', {}, { x: 1600, y: 300 }, nodeMappingManager),
      createNode('global', {}, { x: 2000, y: 300 }, nodeMappingManager),
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
  }, [nodeMappingManager, setNodes, setEdges]);

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
      const targetNode = nodes.find((node) => node.id === connection.target) as Node<NodeData> | undefined;
      const sourceNode = nodes.find((node) => node.id === connection.source) as Node<NodeData> | undefined;
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
          return sourceNode?.data.handles.outputs[sourceIndex].type === targetNode?.data.handles.inputs[targetIndex].type;
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
    (
      filterType: string,
      parameters?: Record<string, string>,
      position?: { x: number; y: number }
    ) => {
      // filterType can be 'input', 'output', 'global', or a filter name
      try {
        const newNode = createNode(
          filterType,
          parameters,
          position,
          nodeMappingManager,
          predefinedFilters.find((f) => f.name === filterType)
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

  const onNodesDelete = useCallback(
    (nodesToDelete: Node[]) => {
      nodesToDelete.forEach((node) => {
        // Remove node from mapping
        nodeMappingManager.removeNodeFromMapping(node.id);
      });
    },
    [nodeMappingManager]
  );

  const onEdgesDelete = useCallback(
    (edgesToDelete: Edge[]) => {
      edgesToDelete.forEach((edge) => {
        // Remove edge from mapping
        nodeMappingManager.removeEdgeFromMapping(edge.id);
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
      <Sidebar 
        nodes={nodes} 
        edges={edges} 
        onAddFilter={onAddNode} 
        nodeMappingManager={nodeMappingManager}
      />
    </Box>
  );
}
