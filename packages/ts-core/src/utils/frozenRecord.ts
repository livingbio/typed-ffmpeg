/**
 * Utilities for working with immutable records, replacing Python's FrozenDict.
 */

import { Default, isDefault } from "./types.js";

/** The value types allowed in FFmpeg node kwargs. */
export type KwargsValue = string | number | boolean;

/** An immutable record of kwargs values. */
export type FrozenKwargs = Readonly<Record<string, KwargsValue>>;

/**
 * Merge multiple record objects into a single frozen record.
 * Null/undefined maps are skipped. Null/undefined values within maps are excluded.
 */
export function merge(
  ...maps: (Record<string, unknown> | null | undefined)[]
): FrozenKwargs {
  const result: Record<string, KwargsValue> = {};
  for (const m of maps) {
    if (m == null) continue;
    for (const [k, v] of Object.entries(m)) {
      if (v != null && !isDefault(v)) {
        result[k] = v as KwargsValue;
      }
    }
  }
  return Object.freeze(result);
}

/**
 * Filter out Default values from a record, keeping only explicitly set values.
 */
export function ignoreDefault(
  kwargs: Record<string, unknown>,
): FrozenKwargs {
  const result: Record<string, KwargsValue> = {};
  for (const [k, v] of Object.entries(kwargs)) {
    if (!isDefault(v) && v != null) {
      result[k] = v as KwargsValue;
    }
  }
  return Object.freeze(result);
}
