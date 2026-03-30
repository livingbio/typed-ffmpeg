/**
 * Core schema definitions for FFmpeg filters and options.
 *
 * Ports the Python FFMpegFilter, FFMpegFilterDef, StreamType etc.
 * from ffmpeg_core/common/schema.py
 */

/** Fundamental types of media streams in FFmpeg. */
export enum StreamType {
  Audio = "audio",
  Video = "video",
}

/** Data types for FFmpeg filter options. */
export enum FFMpegFilterOptionType {
  Boolean = "boolean",
  Duration = "duration",
  Color = "color",
  Flags = "flags",
  Dictionary = "dictionary",
  PixFmt = "pix_fmt",
  Int = "int",
  Int64 = "int64",
  Double = "double",
  Float = "float",
  String = "string",
  VideoRate = "video_rate",
  ImageSize = "image_size",
  Rational = "rational",
  SampleFmt = "sample_fmt",
  Binary = "binary",
  ChannelLayout = "channel_layout",
  Unsigned = "unsigned",
}

/** FFmpeg filter categories based on input/output stream types. */
export enum FFMpegFilterType {
  AF = "af",
  ASrc = "asrc",
  ASink = "asink",
  VF = "vf",
  VSrc = "vsrc",
  VSink = "vsink",
  AVSrc = "avsrc",
  AVF = "avf",
  VAF = "vaf",
}

/** A single choice for an FFmpeg filter option. */
export interface FFMpegFilterOptionChoice {
  readonly name: string;
  readonly help: string;
  readonly value: string | number;
  readonly flags?: string | null;
}

/** A configurable option for an FFmpeg filter. */
export interface FFMpegFilterOption {
  readonly name: string;
  readonly alias: readonly string[];
  readonly description: string;
  readonly type: FFMpegFilterOptionType;
  readonly min?: string | null;
  readonly max?: string | null;
  readonly default?: boolean | number | string | null;
  readonly required: boolean;
  readonly choices: readonly FFMpegFilterOptionChoice[];
  readonly flags?: string | null;
}

/** Type info for a filter's input or output stream. */
export interface FFMpegIOType {
  readonly name?: string | null;
  readonly type: StreamType;
}

/**
 * Simplified filter definition used for creating filter nodes.
 * typings_input/typings_output can be either:
 * - A tuple of "video"/"audio" strings (static)
 * - A formula string (dynamic, pre-evaluated at codegen time in TS)
 */
export interface FFMpegFilterDef {
  readonly name: string;
  readonly typingsInput: readonly ("video" | "audio")[];
  readonly typingsOutput: readonly ("video" | "audio")[];
}

/** Comprehensive representation of an FFmpeg filter with all metadata. */
export interface FFMpegFilter {
  readonly id?: string | null;
  readonly name: string;
  readonly description: string;
  readonly ref?: string | null;
  readonly isSupportSliceThreading?: boolean | null;
  readonly isSupportTimeline?: boolean | null;
  readonly isSupportFramesync?: boolean | null;
  readonly isSupportCommand?: boolean | null;
  readonly isFilterSink?: boolean | null;
  readonly isFilterSource?: boolean | null;
  readonly isDynamicInput: boolean;
  readonly isDynamicOutput: boolean;
  readonly streamTypingsInput: readonly FFMpegIOType[];
  readonly streamTypingsOutput: readonly FFMpegIOType[];
  readonly formulaTypingsInput?: string | null;
  readonly formulaTypingsOutput?: string | null;
  readonly pre: readonly (readonly [string, string])[];
  readonly options: readonly FFMpegFilterOption[];
}

/** FFmpeg option flag bits. */
export const FFMpegOptionFlag = {
  OPT_FUNC_ARG: 1 << 0,
  OPT_EXIT: 1 << 1,
  OPT_EXPERT: 1 << 2,
  OPT_VIDEO: 1 << 3,
  OPT_AUDIO: 1 << 4,
  OPT_SUBTITLE: 1 << 5,
  OPT_DATA: 1 << 6,
  OPT_PERFILE: 1 << 7,
  OPT_FLAG_OFFSET: 1 << 8,
  OPT_FLAG_SPEC: 1 << 9,
  OPT_FLAG_PERSTREAM: 1 << 10,
  OPT_INPUT: 1 << 11,
  OPT_OUTPUT: 1 << 12,
  OPT_HAS_ALT: 1 << 13,
  OPT_HAS_CANON: 1 << 14,
} as const;

/** FFmpeg option data types. */
export enum FFMpegOptionType {
  Func = "OPT_TYPE_FUNC",
  Bool = "OPT_TYPE_BOOL",
  String = "OPT_TYPE_STRING",
  Int = "OPT_TYPE_INT",
  Int64 = "OPT_TYPE_INT64",
  Float = "OPT_TYPE_FLOAT",
  Double = "OPT_TYPE_DOUBLE",
  Time = "OPT_TYPE_TIME",
}

/** A command-line option for FFmpeg. */
export interface FFMpegOption {
  readonly name: string;
  readonly type: FFMpegOptionType;
  readonly flags: number;
  readonly help: string;
  readonly argname?: string | null;
  readonly canon?: string | null;
}

/** Check if an option applies to input files. */
export function isInputOption(option: FFMpegOption): boolean {
  return (option.flags & FFMpegOptionFlag.OPT_INPUT) !== 0;
}

/** Check if an option applies to output files. */
export function isOutputOption(option: FFMpegOption): boolean {
  return (option.flags & FFMpegOptionFlag.OPT_OUTPUT) !== 0;
}

/** Check if an option applies globally. */
export function isGlobalOption(option: FFMpegOption): boolean {
  return (
    !isInputOption(option) &&
    !isOutputOption(option) &&
    (option.flags & FFMpegOptionFlag.OPT_EXIT) === 0
  );
}
