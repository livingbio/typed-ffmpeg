import { EdgeType } from './edge';
import { FFMpegFilter } from './ffmpeg';

export type NodeType = 'input' | 'filter' | 'output' | 'global';

export interface NodeData {
  label: string;
  nodeType: NodeType;
  filterName?: string;
  filename?: string;
  filter?: FFMpegFilter;
  parameters?: Record<string, string | number | boolean>;
  handles: {
    inputs: { id: string; type: EdgeType }[];
    outputs: { id: string; type: EdgeType }[];
  };
}
