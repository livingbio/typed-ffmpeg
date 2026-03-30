/**
 * Factory functions for creating FFmpeg filter nodes.
 *
 * In TypeScript, formula typings are pre-evaluated at codegen time,
 * so FFMpegFilterDef always has static arrays (no eval).
 */

import { StreamType, type FFMpegFilterDef } from "../common/schema.js";
import { ignoreDefault } from "../utils/frozenRecord.js";
import { FilterableStream } from "./baseStreams.js";
import { FilterNode } from "./nodes.js";

/**
 * Create a FilterNode from an FFmpeg filter definition.
 *
 * @param filterDef - The FFmpeg filter definition
 * @param inputs - The input streams
 * @param kwargs - Filter parameters
 * @returns A configured FilterNode
 */
export function filterNodeFactory(
  filterDef: FFMpegFilterDef,
  inputs: readonly FilterableStream[],
  kwargs: Record<string, unknown> = {},
): FilterNode {
  const inputTypings = filterDef.typingsInput.map((k) =>
    k === "video" ? StreamType.Video : StreamType.Audio,
  );

  const outputTypings = filterDef.typingsOutput.map((k) =>
    k === "video" ? StreamType.Video : StreamType.Audio,
  );

  return new FilterNode(
    filterDef.name,
    inputs,
    ignoreDefault(kwargs),
    inputTypings,
    outputTypings,
  );
}
