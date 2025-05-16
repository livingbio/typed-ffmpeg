/**
 * Represents the type of edge (connection) between nodes in the filter graph
 * Determines what type of data flows through the connection:
 * - av: Combined audio/video stream
 * - audio: Audio-only stream
 * - video: Video-only stream
 * - global: Global configuration flow
 * - input: Input file connection
 * - output: Output file connection
 */
export type EdgeType = 'av' | 'audio' | 'video' | 'global' | 'input' | 'output';

/**
 * Color mapping for different edge types
 * Used for visual differentiation in the flow editor
 */
export const EDGE_COLORS = {
  av: '#9c27b0', // Purple
  audio: '#2196f3', // Blue
  video: '#f44336', // Red
  global: '#000000', // Black
  input: '#000000', // Black
  output: '#000000', // Black
} as const;

/**
 * Data associated with an edge in the filter graph
 * Contains information about the connection type and endpoint indices
 */
export interface EdgeData {
  /** The type of data flowing through this edge */
  type: EdgeType;
  /** Index of the output handle on the source node (if applicable) */
  sourceIndex?: number | null;
  /** Index of the input handle on the target node (if applicable) */
  targetIndex?: number | null;
}
