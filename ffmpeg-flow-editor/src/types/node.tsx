export interface NodeData {
    label: string;
    nodeType: 'input' | 'filter' | 'output' | 'global';
    parameters?: Record<string, string>;
    handles: {
        inputs: { id: string; type: string }[];
        outputs: { id: string; type: string }[];
    };
  }
  
