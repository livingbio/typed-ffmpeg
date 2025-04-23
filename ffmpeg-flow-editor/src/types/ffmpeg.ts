import filtersConfig from '../config/filters.json';

export interface FFmpegFilter {
  name: string;
  label: string;
  description: string;
  parameters: FilterParameter[];
}

export interface FilterParameter {
  name: string;
  type: 'string' | 'number' | 'boolean';
  required: boolean;
  description: string;
  default?: string | number | boolean;
  validation?: {
    min?: number;
    max?: number;
    pattern?: string;
  };
}

export interface FFmpegCommand {
  input: string;
  output: string;
  filters: string;
  options: string[];
}

export const predefinedFilters: FFmpegFilter[] = filtersConfig.filters;
