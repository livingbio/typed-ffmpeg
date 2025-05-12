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
      await micropip.install('typed-ffmpeg')
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
export async function runPython(code: string, options?: { indexURL?: string }): Promise<string> {
  const pyodide = await getPyodide(options);
  return await pyodide.runPythonAsync(code);
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
