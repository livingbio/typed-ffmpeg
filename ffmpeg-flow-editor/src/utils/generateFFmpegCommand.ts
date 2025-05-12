import { NodeMappingManager } from './nodeMapping';
import { runPython } from './pyodide';
import * as fs from 'fs';
import * as path from 'path';

export async function generateFFmpegCommand(
  nodeMappingManager: NodeMappingManager
): Promise<{ python: string }> {
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
    console.error('pythonCode', pythonCode);
    // Execute the Python code using the runPython utility
    const result = await runPython(pythonCode);
    return { python: result };
  } catch (error) {
    console.error('Error generating FFmpeg command:', error);

    // Write the Python code to a file for debugging
    const debugDir = path.join(process.cwd(), 'debug');
    if (!fs.existsSync(debugDir)) {
      fs.mkdirSync(debugDir);
    }

    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const debugFile = path.join(debugDir, `ffmpeg_debug_${timestamp}.py`);

    fs.writeFileSync(debugFile, pythonCode);
    console.error(`Debug Python code written to: ${debugFile}`);

    return {
      python: `# Error: ${error instanceof Error ? error.message : String(error)}\n# Debug file: ${debugFile}`,
    };
  }
}
