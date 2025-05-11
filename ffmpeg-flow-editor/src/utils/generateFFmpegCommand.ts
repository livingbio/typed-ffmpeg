import { NodeMappingManager } from './nodeMapping';
import { runPython } from './pyodide';

export async function generateFFmpegCommand(
  nodeMappingManager: NodeMappingManager
): Promise<{ python: string }> {
  try {
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

    // Execute the Python code using the runPython utility
    const result = await runPython(pythonCode);
    return { python: result };
  } catch (error) {
    console.error('Error generating FFmpeg command:', error);
    return { python: `# Error: ${error instanceof Error ? error.message : String(error)}` };
  }
}
