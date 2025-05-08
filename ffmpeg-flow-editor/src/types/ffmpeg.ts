import filtersConfig from '../config/filters.json';
import { StreamType } from './dag';

export interface FFmpegFilter {
  __class__: 'FFMpegFilter';
  id: string | null;
  name: string;
  description: string;
  ref: string;
  is_support_slice_threading: boolean;
  is_support_timeline: boolean;
  is_support_framesync: boolean;
  is_support_command: boolean;
  is_filter_sink: boolean;
  is_filter_source: boolean;
  is_dynamic_input: boolean;
  is_dynamic_output: boolean;
  stream_typings_input: FFMpegIOType[];
  stream_typings_output: FFMpegIOType[];
  formula_typings_input: string | null;
  formula_typings_output: string | null;
  pre: unknown[];
  options: FFmpegFilterOption[];
}

export interface FFMpegIOType {
  __class__: 'FFMpegIOType';
  name: string;
  type: StreamType;
}

export interface FFmpegFilterOption {
  __class__: 'FFMpegFilterOption';
  name: string;
  alias: string[];
  description: string;
  type: {
    __class__: 'FFMpegFilterOptionType';
    value: string;
  };
  min: string | null;
  max: string | null;
  default: string | number | boolean | null;
  required: boolean;
  choices: FFmpegFilterOptionChoice[];
  flags: string;
}

export interface FFmpegFilterOptionChoice {
  __class__: 'FFMpegFilterOptionChoice';
  name: string;
  help: string;
  value: string;
  flags: string;
}

export interface FFmpegCommand {
  input: string;
  output: string;
  filters: string;
  options: string[];
}

// Type assertion to ensure the imported filters match our interface
export const predefinedFilters: FFmpegFilter[] = filtersConfig.filters as FFmpegFilter[];
