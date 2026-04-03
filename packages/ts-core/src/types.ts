/**
 * FFmpeg option type aliases for TypeScript.
 *
 * These types mirror the Python types in ffmpeg_core/types.py,
 * defining the acceptable value types for various FFmpeg options.
 */

import type { Default } from "./utils/types.js";

export type FFBoolean = boolean | "true" | "false" | "1" | "0" | Default | null;

export type FFDuration = string | number | Default | null;

export type FFColor = string | Default | null;

export type FFFlags = string | Default | null;

export type FFDictionary = string | Default | null;

export type FFPixFmt = string | Default | null;

export type FFInt = string | number | Default | null;

export type FFInt64 = string | number | Default | null;

export type FFDouble = string | number | Default | null;

export type FFFloat = string | number | Default | null;

export type FFString = string | number | Default | null;

export type FFVideoRate = string | number | Default | null;

export type FFImageSize = string | Default | null;

export type FFRational = string | Default | null;

export type FFSampleFmt = string | Default | null;

export type FFBinary = string | Default | null;

export type FFFunc = string | number | Default | null;

export type FFTime = string | number | Default | null;

export type FFChannelLayout = string | Default | null;

export type FFUnsigned = string | number | Default | null;
