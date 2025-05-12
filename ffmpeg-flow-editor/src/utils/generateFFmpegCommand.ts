import { NodeMappingManager } from './nodeMapping';
import { runPython } from './pyodideUtils';

export async function generateFFmpegCommand(
  nodeMappingManager: NodeMappingManager
): Promise<{ python: string; error?: string }> {
  const json = nodeMappingManager.toJson();

  // Python code to load and compile the JSON
  const pythonCode = `
from ffmpeg.common.serialize import loads
from ffmpeg.compile.compile_python import compile
from ffmpeg.dag.nodes import GlobalStream

# Load the JSON string
json_str = '''${json}'''

# Load the stream from JSON
node = loads(json_str)
stream = GlobalStream(node=node)

# Compile to Python code
python_code = compile(stream)
print(python_code)
`;

  try {
    // Execute the Python code using the runPython utility
    console.log('Executing FFmpeg command generation...');
    const result = await runPython(pythonCode);

    // Check if the result is empty or undefined
    if (!result || result.trim() === '') {
      console.warn('Generated FFmpeg command is empty');
      return {
        python: '',
        error: 'No command was generated. Ensure there are proper connections between nodes.',
      };
    }

    return { python: result };
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
