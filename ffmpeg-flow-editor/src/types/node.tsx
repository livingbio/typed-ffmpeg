export interface NodeData {
    label: string;
    nodeType: 'input' | 'filter' | 'output' | 'global';
    filterName?: string;
    parameters?: Record<string, string>;
    handles: {
        inputs: { id: string; type: string }[];
        outputs: { id: string; type: string }[];
    };
  }
  
