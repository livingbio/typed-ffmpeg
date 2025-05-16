import { EdgeType } from './edge';

/**
 * Represents the data associated with a node in the FFmpeg filter graph
 * Contains all the information needed to render and process the node
 */
export interface NodeData {
  /** Display name for the node */
  label: string;
  /** Type of the node which determines its behavior and appearance */
  nodeType: 'input' | 'filter' | 'output' | 'global';
  /** Name of the FFmpeg filter (for filter nodes) */
  filterName?: string;
  /** Filename for input/output nodes */
  filename?: string;
  /** Key-value pairs of parameters for the node */
  parameters?: Record<string, string>;
  /** Connection points for the node */
  handles: {
    /** Input connection points where edges can connect to this node */
    inputs: { id: string; type: EdgeType }[];
    /** Output connection points where edges can originate from this node */
    outputs: { id: string; type: EdgeType }[];
  };
}
