import { runPython } from './pyodideUtils';
import { dumps } from './serialize';
import { StreamTypeEnum } from '../types/dag';

export async function evaluateFormula(
  formula: string,
  parameters: Record<string, string | number | boolean>
): Promise<
  {
    __class__: 'FFMpegIOType';
    value: StreamTypeEnum;
  }[]
> {
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
      __class__: 'StreamType',
      value: type as StreamTypeEnum,
    }));
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
