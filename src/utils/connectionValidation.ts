import { Connection, Node, Edge } from 'reactflow';
import { EdgeType } from '../types/edge';

// Extracted from FFmpegFlowEditor for testing and reuse
export const validateConnection = (
  connection: Connection,
  nodes: Node[],
  edges: Edge[]
): boolean => {
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

  // Get the types from the node data using handle IDs
  interface HandleInfo {
    id: string;
    type: EdgeType;
  }

  const sourceType =
    (sourceNode.data.handles.outputs as HandleInfo[]).find((h) => h.id === sourceHandle)?.type ||
    'av';
  const targetType =
    (targetNode.data.handles.inputs as HandleInfo[]).find((h) => h.id === targetHandle)?.type ||
    'av';

  console.log('Connection types:', {
    sourceType,
    targetType,
    sourceHandle,
    targetHandle,
    sourceNode: sourceNode.data,
    targetNode: targetNode.data,
  });

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
