import { runPython } from './pyodideUtils';

interface PythonResult {
  result: string;
  error: string | null;
}
export async function parseFFmpegCommandToJson(cmd: string): Promise<PythonResult> {
  const pythonCode = `
from ffmpeg.common.serialize import dumps
from ffmpeg.compile.compile_cli import parse
from ffmpeg.dag.nodes import GlobalStream

# Load the JSON string
cli_str = '''${cmd}'''

try:
    # Load the stream from JSON
    node = parse(cli_str)
    stream = GlobalStream(node=node)

    # Compile to Python code
    result = dumps(stream)
    
    # Return both the Python code and the FFmpeg command
    return {
        'result': result,
        'error': None
    }
except Exception as e:
    print(f"ERROR: {str(e)}")
    return {
        'result': f"# Error: {str(e)}",
        'error': str(e)
    }
  `;
  console.log('Executing FFmpeg command generation...');
  const result = (await runPython(pythonCode)) as PythonResult;
  console.log('Raw result value:', result);

  return result;
}

export async function generateFFmpegCommand(json: string): Promise<PythonResult> {
  // Now run the actual FFmpeg command generation
  const pythonCode = `
from ffmpeg.common.serialize import loads
from ffmpeg.compile.compile_python import compile
from ffmpeg.dag.nodes import GlobalStream

# Load the JSON string
json_str = '''${json}'''

try:
  # Load the stream from JSON
  node = loads(json_str)
  stream = GlobalStream(node=node)

  # Compile to Python code
  result = compile(stream)
  
  # Return both the Python code and the FFmpeg command
  return {
      'result': result,
      'error': None
  }
except Exception as e:
  print(f"ERROR: {str(e)}")
  return {
      'result': f"# Error: {str(e)}",
      'error': str(e)
  }
`;

  console.log('Executing FFmpeg command generation...');
  const result = (await runPython(pythonCode)) as PythonResult;
  console.log('Raw result value:', result);
  return result;
}
