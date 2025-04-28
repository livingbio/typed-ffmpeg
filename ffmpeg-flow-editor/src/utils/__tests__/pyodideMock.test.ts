import { describe, it, expect, beforeEach } from 'vitest';
import { PyodideMock, loadPyodideMock } from '../pyodideMock';

describe('PyodideMock', () => {
  let pyodide: PyodideMock;

  beforeEach(() => {
    pyodide = new PyodideMock();
  });

  it('should execute simple Python code', async () => {
    const result = await pyodide.runPythonAsync('print("Hello, World!")');
    expect(result.trim()).toBe('Hello, World!');
  });

  it('should handle Python errors', async () => {
    await expect(pyodide.runPythonAsync('raise Exception("Test error")')).rejects.toThrow();
  });

  it('should load packages without error', async () => {
    await expect(pyodide.loadPackage('numpy')).resolves.not.toThrow();
  });

  it('should create instance via loadPyodideMock', async () => {
    const instance = await loadPyodideMock({ indexURL: 'test' });
    expect(instance).toBeInstanceOf(PyodideMock);
  });
});
