// Add type declarations for Pyodide
declare global {
  interface Window {
    loadPyodide: (options: { indexURL: string }) => Promise<{
      runPythonAsync: (code: string) => Promise<string>;
      loadPackage: (packageName: string | string[]) => Promise<void>;
      runPython: (code: string) => unknown;
    }>;
  }
}

// Create a singleton instance of Pyodide
let pyodide: Awaited<ReturnType<typeof window.loadPyodide>> | null = null;
let initialized = false;

/**
 * Get or initialize the Pyodide instance
 * @param options Optional configuration for Pyodide initialization
 * @returns Promise resolving to the Pyodide instance
 */
export async function getPyodide(options?: {
  indexURL?: string;
}): Promise<Awaited<ReturnType<typeof window.loadPyodide>>> {
  if (!pyodide) {
    try {
      // Load Pyodide itself
      console.log('Loading Pyodide...');
      pyodide = await window.loadPyodide({
        indexURL: options?.indexURL || 'https://cdn.jsdelivr.net/pyodide/v0.25.1/full/',
      });
      console.log('Pyodide loaded successfully.');
    } catch (error) {
      console.error('Error loading Pyodide:', error);
      throw new Error(
        `Failed to load Pyodide: ${error instanceof Error ? error.message : String(error)}`
      );
    }
  }

  // Only initialize once
  if (!initialized) {
    try {
      console.log('Loading packages...');
      // Load micropip package
      await pyodide.loadPackage(['micropip']);
      console.log('Micropip loaded successfully.');

      // Initialize micropip and install typed-ffmpeg
      console.log('Installing typed-ffmpeg...');
      await pyodide.runPythonAsync(`
        import micropip
        await micropip.install('typed-ffmpeg')
      `);
      console.log('typed-ffmpeg installed successfully.');

      initialized = true;
    } catch (error) {
      console.error('Error during Pyodide initialization:', error);
      throw new Error(
        `Failed to initialize Pyodide: ${error instanceof Error ? error.message : String(error)}`
      );
    }
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
  try {
    const pyodide = await getPyodide(options);
    return await pyodide.runPythonAsync(code);
  } catch (error) {
    console.error('Error running Python code:', error);
    throw new Error(
      `Error running Python code: ${error instanceof Error ? error.message : String(error)}`
    );
  }
}

/**
 * Reset the Pyodide instance
 * This is useful for testing or when you need to reinitialize Pyodide
 */
export function resetPyodide(): void {
  pyodide = null;
  initialized = false;
  console.log('Pyodide instance reset');
}

export default {
  getPyodide,
  runPython,
  resetPyodide,
};
