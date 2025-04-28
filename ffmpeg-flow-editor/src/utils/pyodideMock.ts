import { spawn } from 'child_process';

// Mock implementation of Pyodide that executes Python code locally
export class PyodideMock {
  private pythonPath: string;

  constructor(pythonPath: string = 'python3') {
    this.pythonPath = pythonPath;
  }

  async runPythonAsync(code: string): Promise<string> {
    return new Promise((resolve, reject) => {
      const pythonProcess = spawn(this.pythonPath, ['-c', code]);

      let stdout = '';
      let stderr = '';

      pythonProcess.stdout.on('data', (data: Buffer) => {
        stdout += data.toString();
      });

      pythonProcess.stderr.on('data', (data: Buffer) => {
        stderr += data.toString();
      });

      pythonProcess.on('close', (code: number) => {
        if (code === 0) {
          resolve(stdout);
        } else {
          reject(new Error(`Python process exited with code ${code}: ${stderr}`));
        }
      });

      pythonProcess.on('error', (err: Error) => {
        reject(new Error(`Failed to start Python process: ${err.message}`));
      });
    });
  }

  async loadPackage(_packageName: string): Promise<void> {
    // In the mock implementation, we don't need to do anything for package loading
    // since we're using the local Python environment
    return Promise.resolve();
  }
}

// Mock implementation of loadPyodide function
export async function loadPyodideMock(_options: { indexURL: string }): Promise<PyodideMock> {
  return new PyodideMock();
}
