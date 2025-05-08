export type EdgeType = "av" | "audio" | "video";

export const EDGE_COLORS = {
  av: "#9c27b0", // Purple
  audio: "#2196f3", // Blue
  video: "#f44336", // Red
} as const;

export interface EdgeData {
  type: EdgeType;
}
