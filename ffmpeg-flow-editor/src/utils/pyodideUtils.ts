// Add type declarations for Pyodide
declare global {
  interface Window {
    loadPyodide: (options: { indexURL: string }) => Promise<{
      runPythonAsync: (code: string) => Promise<unknown>;
      loadPackage: (packageName: string) => Promise<void>;
      globals: {
        get: (name: string) => unknown;
        set: (name: string, value: unknown) => void;
      };
      stdout: string;
    }>;
  }
}

// Create a singleton instance of Pyodide
let pyodide: Awaited<ReturnType<typeof window.loadPyodide>> | null = null;

/**
 * Get or initialize the Pyodide instance
 * @param options Optional configuration for Pyodide initialization
 * @returns Promise resolving to the Pyodide instance
 */
export async function getPyodide(options?: {
  indexURL?: string;
}): Promise<Awaited<ReturnType<typeof window.loadPyodide>>> {
  if (!pyodide) {
    console.log('Loading Pyodide...');
    pyodide = await window.loadPyodide({
      indexURL: options?.indexURL || 'https://cdn.jsdelivr.net/pyodide/v0.27.5/full/',
    });
    await pyodide.loadPackage('micropip');

    await pyodide.runPythonAsync(`
      import micropip
      await micropip.install('typed-ffmpeg==3.0.0a0')
    `);
    console.log('typed-ffmpeg installed successfully.');
  }
  return pyodide;
}

/**
 * Run Python code using Pyodide
 * @param code Python code to execute
 * @param options Optional configuration for Pyodide initialization
 * @returns Promise resolving to the result of the Python code execution
 */
export async function runPython(code: string, options?: { indexURL?: string }): Promise<unknown> {
  const pyodide = await getPyodide(options);

  // Wrap the code in a function to capture both stdout and return value
  const wrappedCode = `
import json
def __run_code():
${code
  .split('\n')
  .map((line) => '    ' + line)
  .join('\n')}

__run_code_result = json.dumps(__run_code())
`;

  try {
    // Run the wrapped code
    console.log('Running wrapped code:', wrappedCode);
    await pyodide.runPythonAsync(wrappedCode);

    // Get the result
    let result = pyodide.globals.get('__run_code_result') as string;

    // Get stdout if available (for print statements)
    let stdout = '';
    if ('stdout' in pyodide) {
      stdout = pyodide.stdout;
    }

    console.log('Result:', result);
    // If result is undefined/None but we have stdout, return stdout instead
    if (result === undefined && stdout.trim() !== '') {
      result = stdout.trim();
    }

    return JSON.parse(result);
  } catch (error) {
    console.error(`Error executing Python code: ${wrappedCode}`, error);
    throw error;
  }
}

/**
 * Reset the Pyodide instance
 * This is useful for testing or when you need to reinitialize Pyodide
 */
export function resetPyodide(): void {
  pyodide = null;
}

export default {
  getPyodide,
  runPython,
  resetPyodide,
};
