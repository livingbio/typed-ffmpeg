import React, { useEffect, useState } from 'react';
import { Node, Edge } from 'reactflow';

interface PyScriptFFmpegProps {
  nodes: Node[];
  edges: Edge[];
}

declare global {
  interface Window {
    pyodide: any;
    runFFmpegCommand: (nodes: any[], edges: any[]) => Promise<string>;
  }
}

const PyScriptFFmpeg: React.FC<PyScriptFFmpegProps> = ({ nodes, edges }) => {
  const [command, setCommand] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const initializePyScript = async () => {
      try {
        // Wait for PyScript to be ready
        await new Promise((resolve) => {
          const checkPyScript = () => {
            if (window.pyodide) {
              resolve(true);
            } else {
              setTimeout(checkPyScript, 100);
            }
          };
          checkPyScript();
        });

        // Install typed-ffmpeg
        await window.pyodide.runPythonAsync(`
          import micropip
          await micropip.install('typed-ffmpeg')
        `);

        // Define the FFmpeg command generation function
        window.pyodide.runPython(`
          from typed_ffmpeg import FFmpeg
          from js import document, console

          def run_ffmpeg_command(nodes, edges):
              try:
                  # Find input and output nodes
                  input_node = next((n for n in nodes if n['type'] == 'input'), None)
                  output_node = next((n for n in nodes if n['type'] == 'output'), None)

                  if not input_node or not output_node:
                      return "Error: Input and output nodes are required"

                  # Start building the Python code
                  code_lines = ['import ffmpeg', '']

                  # Add input
                  code_lines.append('ffmpeg.input("input.mp4")')

                  # Add filters in order based on edges
                  filter_nodes = []
                  current_node = input_node

                  while True:
                      # Find the next connected node
                      next_edge = next((e for e in edges if e['source'] == current_node['id']), None)
                      if not next_edge:
                          break

                      next_node = next((n for n in nodes if n['id'] == next_edge['target']), None)
                      if not next_node or next_node['type'] != 'filter':
                          break

                      filter_nodes.append(next_node)
                      current_node = next_node

                  # Add filters to the code
                  for node in filter_nodes:
                      filter_name = node['data']['filter'].split('=')[0]
                      filter_args = node['data']['filter'].split('=')[1] if '=' in node['data']['filter'] else ''

                      # Convert filter arguments to Python kwargs
                      kwargs = {}
                      if filter_args:
                          for arg in filter_args.split(':'):
                              if '=' in arg:
                                  key, value = arg.split('=')
                                  kwargs[key] = value

                      # Add the filter to the code
                      kwargs_str = ', '.join(f'{k}="{v}"' for k, v in kwargs.items())
                      code_lines.append(f'.{filter_name}({kwargs_str})')

                  # Add output
                  code_lines.append('.output(filename="output.mp4", pix_fmt="yuv420p")')

                  # Join the code lines
                  return '\\n'.join(code_lines)

              except Exception as e:
                  console.log(f"Error: {str(e)}")
                  return str(e)

          # Make the function available to JavaScript
          window.runFFmpegCommand = run_ffmpeg_command
        `);
      } catch (err) {
        setError('Failed to initialize PyScript');
        console.error(err);
      }
    };

    initializePyScript();
  }, []);

  const generateCommand = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const result = await window.runFFmpegCommand(nodes, edges);
      setCommand(result);
    } catch (err) {
      setError('Failed to generate FFmpeg command');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-4 border rounded-lg">
      <h2 className="text-xl font-bold mb-4">FFmpeg Python Code Generator</h2>
      <button
        onClick={generateCommand}
        disabled={isLoading}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:bg-gray-400"
      >
        {isLoading ? 'Generating...' : 'Generate Python Code'}
      </button>

      {error && <div className="mt-4 p-2 bg-red-100 text-red-700 rounded">{error}</div>}

      {command && (
        <div className="mt-4">
          <h3 className="font-semibold mb-2">Generated Python Code:</h3>
          <pre className="bg-gray-100 p-2 rounded overflow-x-auto">{command}</pre>
        </div>
      )}
    </div>
  );
};

export default PyScriptFFmpeg;
