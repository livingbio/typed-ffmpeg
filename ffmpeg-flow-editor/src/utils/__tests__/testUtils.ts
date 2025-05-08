import path from "node:path";
import { loadPyodide } from "pyodide";

// Create a singleton instance of Pyodide
let pyodide: Awaited<ReturnType<typeof loadPyodide>> | null = null;

/**
 * Get or initialize the Pyodide instance for testing
 * @returns Promise resolving to the Pyodide instance
 */
export async function getTestPyodide() {
  if (!pyodide) {
    // Get the path to the pyodide files in node_modules
    const pyodidePath = path.resolve(process.cwd(), "node_modules", "pyodide");

    pyodide = await loadPyodide({
      indexURL: pyodidePath,
    });
    await pyodide.loadPackage("micropip");
    await pyodide.runPythonAsync(`
      import micropip
      await micropip.install('typed-ffmpeg')
    `);
  }
  return pyodide;
}

/**
 * Setup the global window mock with Pyodide for testing
 */
export function setupPyodideMock() {
  // Reset the Pyodide instance
  pyodide = null;

  // Setup window mock with the actual Pyodide
  global.window = {
    loadPyodide: getTestPyodide,
  } as unknown as Window & typeof globalThis;
}

export default {
  getTestPyodide,
  setupPyodideMock,
};
