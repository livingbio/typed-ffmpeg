import { EdgeType } from './edge';
import { FilterNode, InputNode, OutputNode, GlobalNode } from './dag';

export interface BaseNodeData {
  label: string;
  filterString: string;
  parameters: Record<string, string>;
}

export interface InputNodeData extends BaseNodeData {
  filterType: 'input';
  filename: string;
  handles: {
    inputs: [];
    outputs: [{ id: string; type: EdgeType }];
  };
}

export interface OutputNodeData extends BaseNodeData {
  filterType: 'output';
  filename: string;
  handles: {
    inputs: { id: string; type: EdgeType }[];
    outputs: [];
  };
}

export interface FilterNodeData extends BaseNodeData {
  filterType: 'filter';
  filterName: string;
  handles: {
    inputs: { id: string; type: EdgeType }[];
    outputs: { id: string; type: EdgeType }[];
  };
}

export interface GlobalNodeData extends BaseNodeData {
  filterType: 'global';
  handles: {
    inputs: { id: string; type: EdgeType }[];
    outputs: [];
  };
}

export type NodeData = InputNodeData | OutputNodeData | FilterNodeData | GlobalNodeData;

export interface NodeMapping {
  // Maps ReactFlow node ID to DAG node
  nodeMap: Map<string, FilterNode | InputNode | OutputNode | GlobalNode>;
  // Maps DAG node to ReactFlow node ID (for reverse lookup)
  reverseMap: Map<FilterNode | InputNode | OutputNode | GlobalNode, string>;
} 