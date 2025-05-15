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
import { FFMpegIOType, predefinedFilters } from '../types/ffmpeg';
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
import { evaluateFormula } from '@/utils/formulaEvaluator';

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

  let handles: {
    inputs: { id: string; type: EdgeType }[];
    outputs: { id: string; type: EdgeType }[];
  };
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
  let filename: string | undefined;

  if (filterType == 'global') {
    nodeType = 'global';
  } else if (filterType == 'input') {
    nodeType = 'input';
  } else if (filterType == 'output') {
    nodeType = 'output';
  } else {
    nodeType = 'filter';
  }

  // Move variable declarations outside of switch
  let inputTypes: FFMpegIOType[] = [];
  let outputTypes: FFMpegIOType[] = [];

  switch (nodeType) {
    case 'global':
      label = 'global';
      handles = {
        inputs: [{ id: 'input-0', type: 'av' }],
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
        outputs: [{ id: 'output-0', type: 'av' }],
      };
      filename = parameters?.filename || generateRandomFilename('input');
      mappingData = {
        type: 'input',
        inputs: [],
        kwargs: parameters || {},
        filename: filename,
      };
      break;
    case 'output':
      label = 'output';
      handles = {
        inputs: [{ id: 'input-0', type: 'av' }],
        outputs: [{ id: 'output-0', type: 'av' }],
      };
      filename = parameters?.filename || generateRandomFilename('output');
      mappingData = {
        type: 'output',
        inputs: [],
        kwargs: parameters || {},
        filename: filename,
      };
      break;
    case 'filter':
      if (!filter) {
        throw new Error(`Filter ${nodeType} not found`);
      }
      label = filter.name;

      // Handle dynamic inputs/outputs using formula evaluation
      inputTypes = await (filter.formula_typings_input
        ? evaluateFormula(filter.formula_typings_input, parameters || {})
        : filter.stream_typings_input);

      outputTypes = await (filter.formula_typings_output
        ? await evaluateFormula(filter.formula_typings_output, parameters || {})
        : filter.stream_typings_output);

      handles = {
        inputs: inputTypes.map((ioType: FFMpegIOType, index: number) => {
          const typeValue = ioType.type.value;
          if (typeValue === 'audio' || typeValue === 'video') {
            return {
              id: `input-${index}`,
              type: typeValue,
            };
          }
          throw new Error(`Invalid stream type: ${typeValue}`);
        }),
        outputs: outputTypes.map((ioType: FFMpegIOType, index: number) => {
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
        input_typings: inputTypes.map((t: FFMpegIOType) => t.type),
        output_typings: outputTypes.map((t: FFMpegIOType) => t.type),
        inputs: [],
        kwargs: parameters || {},
      };
      break;
    default:
      throw new Error(`Invalid node type: ${nodeType}`);
  }

  const nodeId = nodeMappingManager.addNodeToMapping(mappingData);
  // if nodeType is input or output add a `_` to the end of the nodeType
  let nodeType_: string;
  if (nodeType === 'input' || nodeType === 'output') {
    nodeType_ = nodeType + '_';
  } else {
    nodeType_ = nodeType;
  }

  return {
    id: nodeId,
    type: nodeType_,
    position: position || defaultPosition,
    data: {
      label: label,
      filterName: filterType,
      nodeType: nodeType,
      parameters: parameters || {},
      handles,
      filename,
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

  const edgeId = nodeMappingManager.addEdgeToMapping(source, target, sourceIndex, targetIndex);

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
    const initializeNodes = async () => {
      try {
        const inputNode = await createNode('input', {}, { x: 100, y: 300 }, nodeMappingManager);
        const outputNode = await createNode('output', {}, { x: 1600, y: 300 }, nodeMappingManager);
        const globalNode = await createNode('global', {}, { x: 2000, y: 300 }, nodeMappingManager);
        
        const initialNodes = [inputNode, outputNode, globalNode];
        setNodes(initialNodes);

        // Create initial edge between output and global nodes
        const initialEdge = createEdge(
          outputNode.id,
          globalNode.id,
          'output-0',
          'input-0',
          nodeMappingManager
        );

        setEdges([initialEdge]);
      } catch (error) {
        console.error('Failed to initialize nodes:', error);
      }
    };

    initializeNodes();
  }, [nodeMappingManager, setNodes, setEdges]);

  // Add event listener for node data update
  useEffect(() => {
    const handleNodeDataUpdate = (event: CustomEvent) => {
      const { id, data } = event.detail;
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id);
      if (node) {
        nodeMappingManager.updateNode(id, {
          kwargs: data.parameters,
          filename: data.filename,
        });
      } else {
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
      // filterType can be 'input', 'output', 'global', or a filter name
      try {
        const newNode = await createNode(
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
      <Sidebar onAddFilter={onAddNode} nodeMappingManager={nodeMappingManager} />
    </Box>
  );
}
