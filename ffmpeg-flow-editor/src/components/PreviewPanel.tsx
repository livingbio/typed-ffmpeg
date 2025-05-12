import { Paper, Typography, Box } from '@mui/material';
import { Node, Edge } from 'reactflow';
import { NodeData } from '../types/node';
import { generateFFmpegCommand } from '../utils/generateFFmpegCommand';
import { NodeMappingManager } from '../utils/nodeMapping';
import { useEffect, useState } from 'react';

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
  nodes: Node<NodeData>[];
  edges: Edge[];
  nodeMappingManager: NodeMappingManager;
}

export default function PreviewPanel({ nodes, edges, nodeMappingManager }: PreviewPanelProps) {
  const [pythonCode, setPythonCode] = useState<string>('');
  const [error, setError] = useState<string | undefined>(undefined);
  const [isLoading, setIsLoading] = useState<boolean>(false);

  useEffect(() => {
    const updatePythonCode = async () => {
      try {
        setIsLoading(true);
        const { python, error } = await generateFFmpegCommand(nodeMappingManager);
        setPythonCode(python);
        setError(error);
      } catch (e) {
        console.error('Error updating Python code:', e);
        setError(e instanceof Error ? e.message : String(e));
      } finally {
        setIsLoading(false);
      }
    };

    updatePythonCode();
  }, [nodes, edges, nodeMappingManager]);

  return (
    <Paper
      elevation={0}
      sx={{
        p: 2,
        backgroundColor: '#f5f5f5',
        borderRadius: 1,
        fontFamily: 'monospace',
        fontSize: '0.875rem',
        whiteSpace: 'pre-wrap',
        overflow: 'auto',
        maxHeight: '300px',
      }}
    >
      {isLoading ? (
        <Typography variant="body2">Loading FFmpeg command...</Typography>
      ) : error ? (
        <Box>
          <Typography variant="body2" color="error" fontWeight="bold" gutterBottom>
            Error generating FFmpeg command:
          </Typography>
          <Typography variant="body2" color="error" component="pre">
            {error}
          </Typography>
        </Box>
      ) : (
        <Typography variant="body2" component="pre">
          {pythonCode || '# No valid FFmpeg command generated'}
        </Typography>
      )}
    </Paper>
  );
}
