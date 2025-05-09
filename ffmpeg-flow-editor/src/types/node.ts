import { EdgeType } from './edge';

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
    inputs: [{ id: string; type: EdgeType }];
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

export type NodeData = InputNodeData | OutputNodeData | FilterNodeData; 