import { NodeMappingManager } from './nodeMapping';
import { runPython } from './pyodideUtils';

interface PythonResult {
  python: string;
  ffmpeg_cmd: string | null;
}
export async function parseFFmpegCommand(cmd: string): Promise<string> {
  return '';
}

export async function generateFFmpegCommand(
  nodeMappingManager: NodeMappingManager
): Promise<{ python: string; ffmpeg_cmd?: string; error?: string }> {
  const json = nodeMappingManager.toJson();

  // First, let's try a very simple Python code to test if the return value works
  const testCode = `
# This is a simple test to see if return values work
test_value = "This is a test return value"
return test_value
`;

  try {
    console.log('Running test Python code...');
    const testResult = await runPython(testCode);
    console.log('Test result type:', typeof testResult);
    console.log('Test result value:', testResult);

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
        'python': result,
        'ffmpeg_cmd': stream.compile_line()
    }
except Exception as e:
    print(f"ERROR: {str(e)}")
    return {
        'python': f"# Error: {str(e)}",
        'ffmpeg_cmd': None
    }
`;

    console.log('Executing FFmpeg command generation...');
    const result = (await runPython(pythonCode)) as PythonResult;
    console.log('Raw result type:', typeof result);
    console.log('Raw result value:', result);

    // Convert result to string and check if it's empty
    const resultStr = String(result.python);
    console.log('Result as string:', resultStr);

    if (!resultStr || resultStr.trim() === '') {
      console.warn('Generated FFmpeg command is empty');
      return {
        python: '',
        error: 'No command was generated. Ensure there are proper connections between nodes.',
      };
    }

    return {
      python: resultStr,
      ffmpeg_cmd: result.ffmpeg_cmd || undefined,
    };
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    console.error('Error generating FFmpeg command:', error);

    // More detailed error for user
    return {
      python: `# Error: ${errorMessage}`,
      error: `Failed to generate FFmpeg command: ${errorMessage}`,
    };
  }
}
