import filtersConfig from '../config/filters.json';
import { StreamType } from './dag';

/**
 * Represents an FFmpeg filter with its capabilities, options, and input/output types
 * This interface matches the structure of filters in the filters.json config
 */
export interface FFmpegFilter {
  __class__: 'FFMpegFilter';
  id: string | null;
  /** The name of the filter, used in FFmpeg commands */
  name: string;
  /** Human-readable description of the filter's purpose */
  description: string;
  /** Reference URL or identifier */
  ref: string;
  /** Whether the filter supports slice-based multithreading */
  is_support_slice_threading: boolean;
  /** Whether the filter supports timeline editing */
  is_support_timeline: boolean;
  /** Whether the filter supports frame synchronization */
  is_support_framesync: boolean;
  /** Whether the filter can be controlled via commands during execution */
  is_support_command: boolean;
  /** Whether the filter acts as a sink (endpoint) */
  is_filter_sink: boolean;
  /** Whether the filter acts as a source (starting point) */
  is_filter_source: boolean;
  /** Whether the filter can have a variable number of inputs */
  is_dynamic_input: boolean;
  /** Whether the filter can have a variable number of outputs */
  is_dynamic_output: boolean;
  /** Input stream types this filter accepts */
  stream_typings_input: FFMpegIOType[];
  /** Output stream types this filter produces */
  stream_typings_output: FFMpegIOType[];
  /** Input formula typing (if applicable) */
  formula_typings_input: string | null;
  /** Output formula typing (if applicable) */
  formula_typings_output: string | null;
  /** Pre-processing requirements */
  pre: unknown[];
  /** Available options for this filter */
  options: FFmpegFilterOption[];
}

/**
 * Represents an input/output type for an FFmpeg filter
 * Describes whether the stream is audio, video, or another type
 */
export interface FFMpegIOType {
  __class__: 'FFMpegIOType';
  /** Name/identifier for this IO type */
  name: string;
  /** The stream type (audio, video, etc.) */
  type: StreamType;
}

/**
 * Represents a configurable option for an FFmpeg filter
 * Contains type information, constraints, default values, and available choices
 */
export interface FFmpegFilterOption {
  __class__: 'FFMpegFilterOption';
  /** The name of the option used in FFmpeg command */
  name: string;
  /** Alternative names for the same option */
  alias: string[];
  /** Human-readable description of the option */
  description: string;
  /** Type information for the option */
  type: {
    __class__: 'FFMpegFilterOptionType';
    value: string;
  };
  /** Minimum allowed value (for numeric types) */
  min: string | null;
  /** Maximum allowed value (for numeric types) */
  max: string | null;
  /** Default value if not specified */
  default: string | number | boolean | null;
  /** Whether the option must be specified */
  required: boolean;
  /** Predefined choices for enumerated option types */
  choices: FFmpegFilterOptionChoice[];
  /** Additional flags for the option */
  flags: string;
}

/**
 * Represents a predefined choice for an FFmpeg filter option
 * Used for options that accept enumerated values
 */
export interface FFmpegFilterOptionChoice {
  __class__: 'FFMpegFilterOptionChoice';
  /** The name of the choice */
  name: string;
  /** Human-readable help text for this choice */
  help: string;
  /** The actual value to use in the FFmpeg command */
  value: string;
  /** Additional flags for this choice */
  flags: string;
}

/**
 * Represents a complete FFmpeg command with inputs, outputs, filters, and options
 */
export interface FFmpegCommand {
  /** Input file or stream descriptor */
  input: string;
  /** Output file or stream descriptor */
  output: string;
  /** Filter chain specification */
  filters: string;
  /** Additional command-line options */
  options: string[];
}

/**
 * Predefined filters loaded from the configuration file
 * Contains the complete list of available FFmpeg filters
 */
export const predefinedFilters: FFmpegFilter[] = filtersConfig.filters as FFmpegFilter[];
