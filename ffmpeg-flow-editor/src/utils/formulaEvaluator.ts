import { FFmpegIOType } from '../types/ffmpeg';
import { runPython } from './pyodideUtils';
import { dumps } from './serialize';

export async function evaluateFormula(
  formula: string,
  parameters: Record<string, string | number | boolean>
): Promise<FFmpegIOType[]> {
  if (!formula) throw new Error('Formula is required');

  // Convert parameters to a format that can be passed to Python
  const pythonParameters = Object.entries(parameters).reduce(
    (acc, [key, value]) => {
      acc[key] = value;
      return acc;
    },
    {} as Record<string, string | number | boolean>
  );

  // Create Python code to evaluate the formula
  const pythonCode = `
from ffmpeg.dag.factory import eval_formula
import json

parameters = json.loads('${dumps(pythonParameters)}')

result = [k.value for k in eval_formula("""${formula}""", **parameters)]
return json.dumps(result)
`;

  // Execute the Python code
  const result = (await runPython(pythonCode)) as string;

  // Parse the JSON result
  const parsedResult = JSON.parse(result) as string[];

  // Convert the result to FFmpegIOType[]
  if (Array.isArray(parsedResult)) {
    return parsedResult.map((type) => ({
      __class__: 'FFMpegIOType',
      name: '',
      type: {
        __class__: 'StreamType',
        value: type as unknown as FFmpegIOType['type']['value'],
      },
    })) as FFmpegIOType[];
  }
  console.error('Invalid result:', result);
  throw new Error('Invalid result', { cause: result });
}

// Helper function to parse string parameters
export function parseStringParameter(value: string): string | number | boolean {
  if (value === '') {
    return '';
  }
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
