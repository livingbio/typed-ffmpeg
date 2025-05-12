import { Paper, Typography, Box, Button, CircularProgress } from '@mui/material';
import { Node, Edge } from 'reactflow';
import { NodeData } from '../types/node';
import { generateFFmpegCommand } from '../utils/generateFFmpegCommand';
import { generateFFmpegCommandSimple } from '../utils/generateFFmpegCommandSimple';
import { NodeMappingManager } from '../utils/nodeMapping';
import { useEffect, useState } from 'react';
import { runPython } from '../utils/pyodideUtils';

interface PreviewPanelProps {
  nodes: Node<NodeData>[];
  edges: Edge[];
  nodeMappingManager: NodeMappingManager;
}

export default function PreviewPanel({ nodes, edges, nodeMappingManager }: PreviewPanelProps) {
  const [pythonCode, setPythonCode] = useState<string>('');
  const [result, setResult] = useState<string>('');
  const [error, setError] = useState<string | undefined>(undefined);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [useSimpleMode, setUseSimpleMode] = useState<boolean>(false);

  useEffect(() => {
    const updatePythonCode = async () => {
      try {
        setIsLoading(true);
        
          // Use the simple version for testing
        const commandResult = await generateFFmpegCommandSimple(nodeMappingManager);

        
        setPythonCode(commandResult.python);
        setError(commandResult.error);
      } catch (e) {
        console.error('Error updating Python code:', e);
        setError(e instanceof Error ? e.message : String(e));
      } finally {
        setIsLoading(false);
      }
    };

    updatePythonCode();
  }, [nodes, edges, nodeMappingManager, useSimpleMode]);

  const handleRunPython = async () => {
    if (!pythonCode) return;

    setIsRunning(true);
    setError(undefined);
    
    try {
      const output = await runPython(pythonCode);
      // Use String() to safely convert any output type to a string
      setResult(String(output));
    } catch (err) {
      const errMessage = err instanceof Error ? err.message : String(err);
      console.error('Python execution error:', err);
      setError(errMessage);
    } finally {
      setIsRunning(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(pythonCode);
  };

  const toggleMode = () => {
    setUseSimpleMode(!useSimpleMode);
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
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <Typography variant="subtitle2">Python Code</Typography>
            <Button 
              variant="outlined" 
              size="small" 
              onClick={toggleMode}
              sx={{ fontSize: '0.7rem' }}
            >
              {useSimpleMode ? 'Using Simple Mode' : 'Using Standard Mode'}
            </Button>
          </Box>
          <Box sx={{ display: 'flex', gap: 1 }}>
            <Button 
              variant="outlined" 
              size="small" 
              onClick={handleRunPython}
              disabled={isLoading || isRunning || !pythonCode}
              startIcon={isRunning ? <CircularProgress size={16} /> : null}
            >
              {isRunning ? 'Running...' : 'Run'}
            </Button>
            <Button 
              variant="outlined" 
              size="small" 
              onClick={handleCopy}
              disabled={!pythonCode}
            >
              Copy
            </Button>
          </Box>
        </Box>
        <Paper
          elevation={0}
          sx={{
            p: 2,
            backgroundColor: '#f5f5f5',
            borderRadius: 1,
            overflow: 'auto',
            maxHeight: '200px',
          }}
        >
          {isLoading ? (
            <Typography variant="body2">Loading FFmpeg command...</Typography>
          ) : error ? (
            <Box>
              <Typography variant="body2" color="error" fontWeight="bold" gutterBottom>
                Error generating FFmpeg command:
              </Typography>
              <Typography variant="body2" color="error" component="pre" sx={{ 
                margin: 0, 
                fontFamily: 'monospace',
                fontSize: '0.875rem',
                whiteSpace: 'pre-wrap',
              }}>
                {error}
              </Typography>
            </Box>
          ) : (
            <pre style={{ 
              margin: 0, 
              padding: 0, 
              fontFamily: 'monospace',
              fontSize: '0.875rem',
              lineHeight: 1.5,
              whiteSpace: 'pre-wrap',
              wordBreak: 'break-word',
            }}>
              {pythonCode || '# No valid FFmpeg command generated'}
            </pre>
          )}
        </Paper>
      </Box>

      {/* Results Section (only shown when there are results) */}
      {(result || isRunning) && (
        <Box>
          <Typography variant="subtitle2" sx={{ mb: 1 }}>
            Result {isRunning && '(Running...)'}
          </Typography>
          <Paper
            elevation={0}
            sx={{
              p: 2,
              backgroundColor: '#f5f5f5',
              borderRadius: 1,
              overflow: 'auto',
              maxHeight: '200px',
            }}
          >
            {isRunning ? (
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <CircularProgress size={20} />
                <Typography variant="body2">Executing Python code...</Typography>
              </Box>
            ) : (
              <pre style={{ 
                margin: 0, 
                padding: 0, 
                fontFamily: 'monospace',
                fontSize: '0.875rem',
                lineHeight: 1.5,
                whiteSpace: 'pre-wrap',
                wordBreak: 'break-word',
              }}>
                {result || 'No result'}
              </pre>
            )}
          </Paper>
        </Box>
      )}
    </Box>
  );
}
