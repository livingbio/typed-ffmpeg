import { FFmpegIOType } from '../types/ffmpeg';
import { PyodideMock } from './pyodideMock';

// Type for the Python result
interface PythonResultType {
  value: string;
}

// Create a singleton instance of PyodideMock
let pyodide: PyodideMock | null = null;

async function getPyodide(): Promise<PyodideMock> {
  if (!pyodide) {
    pyodide = new PyodideMock();
    // Load the required Python packages
    await pyodide.loadPackage('ffmpeg');
  }
  return pyodide;
}

// Helper function to evaluate a formula expression
export async function evaluateFormula(
  formula: string,
  parameters: Record<string, string | number | boolean>
): Promise<FFmpegIOType[]> {
  if (!formula) return [];

  try {
    const pyodide = await getPyodide();

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

result = [str(k) for k in eval_formula("${formula}", ${JSON.stringify(pythonParameters)})]
print(json.dumps(result))
`;

    // Execute the Python code
    const result = await pyodide.runPythonAsync(pythonCode);

    // Parse the JSON result
    const parsedResult = JSON.parse(result) as PythonResultType[];

    // Convert the result to FFmpegIOType[]
    if (Array.isArray(parsedResult)) {
      return parsedResult.map((type) => ({
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
