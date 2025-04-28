import { FFmpegIOType } from '../types/ffmpeg';

// Add type declarations for Pyodide
declare global {
  interface Window {
    loadPyodide: (options: { indexURL: string }) => Promise<{
      runPythonAsync: (code: string) => Promise<string>;
      loadPackage: (packageName: string) => Promise<void>;
    }>;
  }
}

// Create a singleton instance of Pyodide
let pyodide: Awaited<ReturnType<typeof window.loadPyodide>> | null = null;

async function getPyodide(): Promise<Awaited<ReturnType<typeof window.loadPyodide>>> {
  if (!pyodide) {
    pyodide = await window.loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.25.1/full/',
    });
    await pyodide.loadPackage('micropip');
    await pyodide.runPythonAsync(`
      import micropip
      await micropip.install('typed-ffmpeg')
    `);
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

parameters = json.loads('${JSON.stringify(pythonParameters)}')

result = [k.value for k in eval_formula("""${formula}""", **parameters)]
json.dumps(result)
`;

    // Execute the Python code
    const result = await pyodide.runPythonAsync(pythonCode);

    // Parse the JSON result
    const parsedResult = JSON.parse(result) as string[];

    // Convert the result to FFmpegIOType[]
    if (Array.isArray(parsedResult)) {
      return parsedResult.map((type) => ({
        __class__: 'FFMpegIOType',
        name: '',
        type: {
          __class__: 'StreamType',
          value: type,
        },
      }));
    }
    console.error('Invalid result:', result);
    throw new Error('Invalid result', { cause: result });
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
