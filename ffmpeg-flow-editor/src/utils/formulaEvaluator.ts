import { FFmpegIOType } from '../types/ffmpeg';

// Helper function to evaluate a formula expression
export function evaluateFormula(
  formula: string,
  parameters: Record<string, string | number | boolean>
): FFmpegIOType[] {
  if (!formula) return [];

  // Create a safe evaluation context with only the parameters we need
  const context = {
    ...parameters,
    StreamType: {
      video: { value: 'video' },
      audio: { value: 'audio' },
      av: { value: 'av' },
    },
    CHANNEL_LAYOUT: {
      mono: 1,
      stereo: 2,
      '2.1': 3,
      '3.0': 3,
      '3.1': 4,
      '4.0': 4,
      quad: 4,
      '5.0': 5,
      '5.1': 6,
      '6.1': 7,
      '7.1': 8,
    },
  };

  try {
    // Create a function that evaluates the formula
    const evalFn = new Function('params', `with(params) { return ${formula}; }`);

    // Evaluate the formula
    const result = evalFn(context);

    // Convert the result to FFmpegIOType[]
    if (Array.isArray(result)) {
      return result.map((type) => ({
        __class__: 'FFMpegIOType',
        name: '',
        type: {
          __class__: 'StreamType',
          value: type.value,
        },
      }));
    }

    return [];
  } catch (error) {
    console.error('Error evaluating formula:', error);
    return [];
  }
}

// Helper function to parse string parameters
export function parseStringParameter(value: string): string | number | boolean {
  if (!isNaN(Number(value))) {
    return Number(value);
  }
  if (value.toLowerCase() === 'true') {
    return true;
  }
  if (value.toLowerCase() === 'false') {
    return false;
  }
  return value;
}
