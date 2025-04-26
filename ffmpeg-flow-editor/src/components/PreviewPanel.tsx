import { Box, Typography, Button } from '@mui/material';
import { Node, Edge } from 'reactflow';
import { useState, useEffect } from 'react';

// Add type declarations for Pyodide
declare global {
  interface Window {
    loadPyodide: (options: { indexURL: string }) => Promise<{
      runPythonAsync: (code: string) => Promise<string>;
      loadPackage: (packageName: string) => Promise<void>;
    }>;
  }
}

interface PreviewPanelProps {
  nodes: Node[];
  edges: Edge[];
}

function generateFFmpegCommand(nodes: Node[], edges: Edge[]): { python: string } {
  // Find all input and output nodes
  const inputNodes = nodes.filter((n) => n.data.filterType === 'input');
  const outputNodes = nodes.filter((n) => n.data.filterType === 'output');

  if (inputNodes.length === 0 || outputNodes.length === 0) {
    return {
      python: '',
    };
  }

  // Generate Python code
  let pythonCode = 'import ffmpeg\n\n';

  // Create input streams
  const inputStreams = inputNodes.map((node, index) => {
    return `input${index} = ffmpeg.input("input${index}.mp4")`;
  });

  pythonCode += inputStreams.join('\n') + '\n\n';

  // Track processed streams by node ID
  const nodeStreams: Record<string, string> = {};

  // Initialize with input streams
  inputNodes.forEach((node, index) => {
    nodeStreams[node.id] = `input${index}`;
  });

  // Build filter chains for each input
  inputNodes.forEach((inputNode) => {
    let currentId = inputNode.id;
    let currentStream = nodeStreams[currentId];

    while (true) {
      const edge = edges.find((e) => e.source === currentId);
      if (!edge) break;

      const nextNode = nodes.find((n) => n.id === edge.target);
      if (!nextNode || nextNode.data.filterType !== 'filter') break;

      if (nextNode.data.filterType === 'filter' && nextNode.data.filterName) {
        const filterName = nextNode.data.filterName;
        const parameters = (nextNode.data.parameters as Record<string, string>) || {};

        // Convert parameters to Python kwargs
        const kwargs = Object.entries(parameters)
          .filter(([, value]) => value !== '')
          .map(([key, value]) => {
            // Handle numeric values without quotes
            if (!isNaN(Number(value))) {
              return `${key}=${value}`;
            }
            // Handle boolean values
            if (value.toLowerCase() === 'true' || value.toLowerCase() === 'false') {
              return `${key}=${value.toLowerCase()}`;
            }
            // Handle string values with quotes
            return `${key}="${value}"`;
          })
          .join(', ');

        // Create a new variable for the processed stream with valid Python identifier
        const nodeId = nextNode.id.replace(/-/g, '_');
        const newStreamName = `stream_${nodeId}`;
        pythonCode += `${newStreamName} = ${currentStream}.${filterName}(${kwargs})\n`;
        nodeStreams[nextNode.id] = newStreamName;
        currentStream = newStreamName;
      }

      currentId = nextNode.id;
    }
  });

  pythonCode += '\n';

  // Create output streams
  outputNodes.forEach((node, index) => {
    // Find all streams that connect to this output
    const connectedStreams = edges
      .filter((edge) => edge.target === node.id)
      .map((edge) => {
        const sourceNode = nodes.find((n) => n.id === edge.source);
        if (!sourceNode) return null;
        return nodeStreams[sourceNode.id];
      })
      .filter((stream): stream is string => stream !== null);

    if (connectedStreams.length > 0) {
      pythonCode += `output${index} = ffmpeg.output(${connectedStreams.join(', ')}, filename="output${index}.mp4")\n`;
    }
    // Skip output nodes with no connected streams
  });

  pythonCode += '\n';

  // Add compile line
  pythonCode += '# Compile the command\n';
  const validOutputs = outputNodes
    .map((node, index) => {
      const hasConnections = edges.some((edge) => edge.target === node.id);
      return hasConnections ? `output${index}` : null;
    })
    .filter((output): output is string => output !== null);

  if (validOutputs.length > 1) {
    pythonCode += `ffmpeg.merge_outputs(${validOutputs.join(', ')}).compile_line()`;
  } else if (validOutputs.length === 1) {
    pythonCode += `${validOutputs[0]}.compile_line()`;
  } else {
    pythonCode += '# No valid outputs to compile';
  }

  return {
    python: pythonCode,
  };
}

export default function PreviewPanel({ nodes, edges }: PreviewPanelProps) {
  const [previewData, setPreviewData] = useState<{
    python: string;
  }>({
    python: '',
  });

  const [pyodide, setPyodide] = useState<Awaited<ReturnType<typeof window.loadPyodide>> | null>(
    null
  );
  const [result, setResult] = useState<string>('');
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    async function loadPyodide() {
      try {
        setIsLoading(true);
        const pyodide = await window.loadPyodide({
          indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.25.1/full/',
        });
        await pyodide.loadPackage('micropip');
        await pyodide.runPythonAsync(`
          import micropip
          await micropip.install('typed-ffmpeg')
        `);
        setPyodide(pyodide);
      } catch (error) {
        console.error('Failed to load Pyodide:', error);
        setResult('Failed to load Python environment');
      } finally {
        setIsLoading(false);
      }
    }
    loadPyodide();
  }, []);

  useEffect(() => {
    const newData = generateFFmpegCommand(nodes, edges);
    setPreviewData(newData);
  }, [nodes, edges]);

  // Add new useEffect to automatically run Python when code changes
  useEffect(() => {
    async function runPython() {
      if (!pyodide || !previewData.python) {
        return;
      }

      try {
        setIsLoading(true);
        const output = await pyodide.runPythonAsync(previewData.python);
        setResult(output.toString());
      } catch (error) {
        console.error('Python execution error:', error);
        setResult(`Error: ${error instanceof Error ? error.message : String(error)}`);
      } finally {
        setIsLoading(false);
      }
    }

    runPython();
  }, [pyodide, previewData.python]);

  const handleCopy = () => {
    navigator.clipboard.writeText(previewData.python);
  };

  return (
    <Box>
      {/* Python Code */}
      <Box sx={{ mb: 3 }}>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            mb: 1,
          }}
        >
          <Typography variant="subtitle2">Python Code</Typography>
          <Button variant="outlined" size="small" onClick={handleCopy}>
            Copy
          </Button>
        </Box>
        <Box
          sx={{
            p: 1.5,
            backgroundColor: '#f5f5f5',
            borderRadius: 1,
          }}
        >
          <pre
            style={{
              margin: 0,
              padding: 0,
              fontFamily: 'monospace',
              fontSize: '0.875rem',
              lineHeight: 1.5,
              whiteSpace: 'pre-wrap',
              wordBreak: 'break-word',
            }}
          >
            {previewData.python}
          </pre>
        </Box>
      </Box>

      {/* Result */}
      <Box>
        <Typography variant="subtitle2" sx={{ mb: 1 }}>
          Result {isLoading && '(Loading...)'}
        </Typography>
        <Box
          sx={{
            p: 1.5,
            backgroundColor: '#f5f5f5',
            borderRadius: 1,
          }}
        >
          <pre
            style={{
              margin: 0,
              padding: 0,
              fontFamily: 'monospace',
              fontSize: '0.875rem',
              lineHeight: 1.5,
              whiteSpace: 'pre-wrap',
              wordBreak: 'break-word',
            }}
          >
            {result || 'No result yet'}
          </pre>
        </Box>
      </Box>
    </Box>
  );
}
