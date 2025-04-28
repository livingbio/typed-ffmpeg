import { Box, Typography, Button } from '@mui/material';
import { Node, Edge } from 'reactflow';
import { useState, useEffect } from 'react';
import { generateFFmpegCommand } from '../utils/generateFFmpegCommand';

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
