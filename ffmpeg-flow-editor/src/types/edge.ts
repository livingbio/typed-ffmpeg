export type EdgeType = 'av' | 'audio' | 'video' | 'global' | 'input' | 'output';

export const EDGE_COLORS = {
  av: '#9c27b0', // Purple
  audio: '#2196f3', // Blue
  video: '#f44336', // Red
  global: '#000000', // Black
  input: '#000000', // Black
  output: '#000000', // Blacks
} as const;

export interface EdgeData {
  type: EdgeType;
  sourceIndex?: number | null;
  targetIndex?: number | null;
}
