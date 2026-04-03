/**
 * DAG schema definitions for FFmpeg filter graphs.
 *
 * These are the base Node and Stream types. Concrete implementations
 * (FilterNode, InputNode, etc.) are in nodes.ts.
 */

import type { KwargsValue } from "../utils/frozenRecord.js";
import { isDAG } from "./utils.js";

/** Simple string hash (djb2 variant). */
function hashString(str: string): number {
  let hash = 5381;
  for (let i = 0; i < str.length; i++) {
    hash = ((hash << 5) + hash + str.charCodeAt(i)) | 0;
  }
  return Math.abs(hash);
}

/** Auto-incrementing ID for unique node/stream identification. */
let _nextId = 0;

/**
 * Base class for nodes in the DAG.
 * A Node represents a single operation (filter, input file, output file, etc.).
 */
export abstract class Node {
  readonly kwargs: Readonly<Record<string, KwargsValue>>;
  readonly inputs: readonly Stream[];

  /** Unique ID for this node instance. */
  readonly _id: number;

  private _hex: string | undefined;

  constructor(
    kwargs: Record<string, KwargsValue> = {},
    inputs: readonly Stream[] = [],
  ) {
    this._id = _nextId++;
    this.kwargs = Object.freeze({ ...kwargs });
    this.inputs = Object.freeze([...inputs]);
    this._validateDAG();
  }

  /** Hex hash for labeling. */
  get hex(): string {
    if (this._hex === undefined) {
      // Build a string representation without recursion into full object graph
      const parts: string[] = [
        this.constructor.name,
        JSON.stringify(this.kwargs),
        ...this.inputs.map((s) => `${s.node._id}:${s.index}`),
      ];
      this._hex = hashString(parts.join("|")).toString(16);
    }
    return this._hex;
  }

  /** String representation of this node. */
  repr(): string {
    return this.constructor.name;
  }

  /** Maximum depth from this node to the leaves. */
  get maxDepth(): number {
    let max = 0;
    for (const input of this.inputs) {
      max = Math.max(max, input.node.maxDepth);
    }
    return max + 1;
  }

  /** All upstream nodes (including this one). */
  get upstreamNodes(): Set<Node> {
    const result = new Set<Node>([this]);
    for (const input of this.inputs) {
      for (const node of input.node.upstreamNodes) {
        result.add(node);
      }
    }
    return result;
  }

  private _validateDAG(): void {
    const passed = new Set<Node>();
    const queue: Node[] = [this];
    const graph: Record<string, Set<string>> = {};

    while (queue.length > 0) {
      const node = queue.pop()!;
      if (passed.has(node)) continue;
      passed.add(node);

      graph[node.hex] = new Set(node.inputs.map((s) => s.node.hex));
      for (const s of node.inputs) {
        queue.push(s.node);
      }
    }

    if (!isDAG(graph)) {
      throw new Error("Graph is not a DAG");
    }
  }
}

/**
 * Base class for streams in the DAG.
 * A Stream represents a sequence of data flow connecting nodes.
 */
export abstract class Stream {
  readonly node: Node;
  readonly index: number | null;
  readonly optional: boolean;

  private _hex: string | undefined;

  constructor(node: Node, index: number | null = null, optional: boolean = false) {
    this.node = node;
    this.index = index;
    this.optional = optional;
  }

  /** Hex hash for labeling. */
  get hex(): string {
    if (this._hex === undefined) {
      this._hex = hashString(`${this.node.hex}:${this.index}:${this.optional}`).toString(16);
    }
    return this._hex;
  }
}
