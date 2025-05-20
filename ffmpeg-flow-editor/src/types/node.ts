import { EdgeType } from './edge';

export type NodeType = 'input' | 'filter' | 'output' | 'global';

export interface NodeData {
  label: string;
  nodeType: NodeType;
  filterName?: string;
  filename?: string;
  parameters?: Record<string, string>;
  handles: {
    inputs: { id: string; type: EdgeType }[];
    outputs: { id: string; type: EdgeType }[];
  };
}
