import { EdgeType } from "./edge";

export interface NodeData {
    label: string;
    nodeType: 'input' | 'filter' | 'output' | 'global';
    filterName?: string;
    filename?: string;
    parameters?: Record<string, string>;
    handles: {
        inputs: { id: string; type: EdgeType }[];
        outputs: { id: string; type: EdgeType }[];
    };
  }
  
