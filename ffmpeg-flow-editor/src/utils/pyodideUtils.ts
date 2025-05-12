// File: src/utils/pydideUtil.ts

import { loadPyodide as loadPyodideNode, PyodideInterface } from 'pyodide';
import path from 'path';
import { pathToFileURL } from 'url';

let pyodide: PyodideInterface | null = null;

function isNode(): boolean {
  return (
    typeof process !== 'undefined' && process.versions != null && process.versions.node != null
  );
}

export async function loadPyodideWrapper(): Promise<void> {
  if (pyodide) return;

  if (isNode()) {
    const pyodidePath = path.resolve(__dirname, '../../pyodide-dist');
    const indexURL = pathToFileURL(pyodidePath);
    console.log('[Pyodide] Node environment. Using indexURL:', indexURL);

    pyodide = await loadPyodideNode({ indexURL: pyodidePath });
  } else {
    const { loadPyodide: loadPyodideBrowser } = await import(
      'https://cdn.jsdelivr.net/pyodide/v0.27.5/full/pyodide.mjs'
    );
    pyodide = await loadPyodideBrowser();
  }
  await pyodide.loadPackage('micropip');
  await pyodide.runPythonAsync('import micropip; await micropip.install("typed-ffmpeg==3.0.0a0")');
}

export async function runPython(code: string): Promise<any> {
  if (!pyodide) {
    throw new Error('Pyodide is not initialized. Call loadPyodideWrapper() first.');
  }
  return await pyodide.runPythonAsync(code);
}
