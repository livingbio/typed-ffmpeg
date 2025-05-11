import { Paper, Typography } from '@mui/material';
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

  useEffect(() => {
    const updatePythonCode = async () => {
      const { python } = await generateFFmpegCommand(nodeMappingManager);
      setPythonCode(python);
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
      <Typography variant="body2" component="pre">
        {pythonCode || '# No valid FFmpeg command generated'}
      </Typography>
    </Paper>
  );
}
