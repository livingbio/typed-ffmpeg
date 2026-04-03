/**
 * Context management for FFmpeg filter graph traversal.
 */

import { FilterNode, InputNode } from "../dag/nodes.js";
import { Node, Stream } from "../dag/schema.js";

/** Remove duplicates from an array while preserving order. */
function removeDuplicates<T>(seq: T[]): T[] {
  const seen = new Set<T>();
  const result: T[] = [];
  for (const x of seq) {
    if (!seen.has(x)) {
      result.push(x);
      seen.add(x);
    }
  }
  return result;
}

/** Recursively collect all nodes and streams upstream from a node. */
function collect(node: Node): { nodes: Node[]; streams: Stream[] } {
  const nodes: Node[] = [node];
  const streams: Stream[] = [...node.inputs];

  for (const stream of node.inputs) {
    const sub = collect(stream.node);
    nodes.push(...sub.nodes);
    streams.push(...sub.streams);
  }

  return { nodes, streams };
}

/**
 * Context for analyzing an FFmpeg filter graph DAG.
 */
export class DAGContext {
  readonly node: Node;
  readonly nodes: readonly Node[];
  readonly streams: readonly Stream[];

  private _allNodes: Node[] | undefined;
  private _allStreams: Stream[] | undefined;
  private _outgoingNodes: Map<Stream, [Node, number][]> | undefined;
  private _outgoingStreams: Map<Node, Stream[]> | undefined;
  private _nodeIds: Map<Node, number> | undefined;
  private _nodeLabels: Map<Node, string> | undefined;

  constructor(node: Node, nodes: readonly Node[], streams: readonly Stream[]) {
    this.node = node;
    this.nodes = nodes;
    this.streams = streams;
  }

  /** Build a DAGContext from a root node. */
  static build(node: Node): DAGContext {
    const { nodes, streams } = collect(node);
    return new DAGContext(
      node,
      removeDuplicates(nodes),
      removeDuplicates(streams),
    );
  }

  /** All nodes sorted by processing order (upstream first). */
  get allNodes(): Node[] {
    if (!this._allNodes) {
      this._allNodes = [...this.nodes].sort(
        (a, b) => a.upstreamNodes.size - b.upstreamNodes.size,
      );
    }
    return this._allNodes;
  }

  /** All streams sorted by processing order. */
  get allStreams(): Stream[] {
    if (!this._allStreams) {
      this._allStreams = [...this.streams].sort((a, b) => {
        const depDiff = a.node.upstreamNodes.size - b.node.upstreamNodes.size;
        if (depDiff !== 0) return depDiff;
        return (a.index ?? 0) - (b.index ?? 0);
      });
    }
    return this._allStreams;
  }

  /** Map of streams to the (node, inputIndex) pairs that consume them. */
  get outgoingNodes(): Map<Stream, [Node, number][]> {
    if (!this._outgoingNodes) {
      const map = new Map<Stream, [Node, number][]>();
      for (const node of this.nodes) {
        for (let idx = 0; idx < node.inputs.length; idx++) {
          const stream = node.inputs[idx];
          if (!map.has(stream)) map.set(stream, []);
          map.get(stream)!.push([node, idx]);
        }
      }
      this._outgoingNodes = map;
    }
    return this._outgoingNodes;
  }

  /** Map of nodes to the streams that originate from them. */
  get outgoingStreams(): Map<Node, Stream[]> {
    if (!this._outgoingStreams) {
      const map = new Map<Node, Stream[]>();
      for (const stream of this.streams) {
        if (!map.has(stream.node)) map.set(stream.node, []);
        map.get(stream.node)!.push(stream);
      }
      this._outgoingStreams = map;
    }
    return this._outgoingStreams;
  }

  /** Map of nodes to their unique integer IDs (per type). */
  get nodeIds(): Map<Node, number> {
    if (!this._nodeIds) {
      const index: Map<Function, number> = new Map();
      const ids = new Map<Node, number>();
      const sorted = [...this.nodes].sort((a, b) => a.maxDepth - b.maxDepth);
      for (const node of sorted) {
        const cls = node.constructor;
        const id = index.get(cls) ?? 0;
        ids.set(node, id);
        index.set(cls, id + 1);
      }
      this._nodeIds = ids;
    }
    return this._nodeIds;
  }

  /** Map of nodes to their string labels for FFmpeg filter graphs. */
  get nodeLabels(): Map<Node, string> {
    if (!this._nodeLabels) {
      let inputIdx = 0;
      let filterIdx = 0;
      const labels = new Map<Node, string>();
      const sorted = [...this.nodes].sort((a, b) => a.maxDepth - b.maxDepth);
      for (const node of sorted) {
        if (node instanceof InputNode) {
          labels.set(node, String(inputIdx++));
        } else if (node instanceof FilterNode) {
          labels.set(node, `s${filterIdx++}`);
        } else {
          labels.set(node, "out");
        }
      }
      this._nodeLabels = labels;
    }
    return this._nodeLabels;
  }

  /** Get all (node, inputIndex) pairs that consume a stream. */
  getOutgoingNodes(stream: Stream): [Node, number][] {
    return this.outgoingNodes.get(stream) ?? [];
  }

  /** Get the label for a node. */
  getNodeLabel(node: Node): string {
    return this.nodeLabels.get(node) ?? "out";
  }

  /** Get all streams that originate from a node. */
  getOutgoingStreams(node: Node): Stream[] {
    return this.outgoingStreams.get(node) ?? [];
  }
}
