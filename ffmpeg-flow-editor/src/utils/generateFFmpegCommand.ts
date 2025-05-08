import { Node, Edge } from 'reactflow';
import { convertToDag } from './convertToDag';
import { dumps } from './serialize';
import { runPython } from './pyodide';

export async function generateFFmpegCommand(nodes: Node[], edges: Edge[]): Promise<{ python: string }> {
  // Convert ReactFlow nodes/edges to DAG
  const dag = convertToDag(nodes, edges);
  
  if (!dag) {
    return {
      python: '',
    };
  }

  // Serialize DAG to JSON
  const jsonStr = dumps(dag);

  // Generate Python code using pyodide
  const pythonCode = await runPython(`
from ffmpeg.common.serialize import loads
from ffmpeg.compile.compile_python import compile

stream = loads('''${jsonStr}''')
python_code = compile(stream)
python_code
  `);

  return {
    python: pythonCode,
  };
}
