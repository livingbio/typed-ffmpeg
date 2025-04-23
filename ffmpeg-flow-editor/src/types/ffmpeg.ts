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

export const predefinedFilters: FFmpegFilter[] = [
  {
    name: 'scale',
    label: 'Scale',
    description: 'Scale the input video to a new size',
    parameters: [
      {
        name: 'width',
        type: 'number',
        required: true,
        description: 'Output width',
        validation: { min: 1 },
      },
      {
        name: 'height',
        type: 'number',
        required: true,
        description: 'Output height',
        validation: { min: 1 },
      },
    ],
  },
  {
    name: 'crop',
    label: 'Crop',
    description: 'Crop the input video',
    parameters: [
      {
        name: 'width',
        type: 'number',
        required: true,
        description: 'Crop width',
        validation: { min: 1 },
      },
      {
        name: 'height',
        type: 'number',
        required: true,
        description: 'Crop height',
        validation: { min: 1 },
      },
      {
        name: 'x',
        type: 'number',
        required: true,
        description: 'X position',
        validation: { min: 0 },
      },
      {
        name: 'y',
        type: 'number',
        required: true,
        description: 'Y position',
        validation: { min: 0 },
      },
    ],
  },
  {
    name: 'overlay',
    label: 'Overlay',
    description: 'Overlay one video on top of another',
    parameters: [
      {
        name: 'x',
        type: 'number',
        required: true,
        description: 'X position',
      },
      {
        name: 'y',
        type: 'number',
        required: true,
        description: 'Y position',
      },
    ],
  },
  {
    name: 'trim',
    label: 'Trim',
    description: 'Trim the input video',
    parameters: [
      {
        name: 'start',
        type: 'number',
        required: true,
        description: 'Start time in seconds',
        validation: { min: 0 },
      },
      {
        name: 'end',
        type: 'number',
        required: true,
        description: 'End time in seconds',
        validation: { min: 0 },
      },
    ],
  },
  {
    name: 'fade',
    label: 'Fade',
    description: 'Add fade in/out effect',
    parameters: [
      {
        name: 'type',
        type: 'string',
        required: true,
        description: 'Fade type (in/out)',
        default: 'in',
      },
      {
        name: 'duration',
        type: 'number',
        required: true,
        description: 'Fade duration in seconds',
        validation: { min: 0 },
      },
    ],
  },
];
