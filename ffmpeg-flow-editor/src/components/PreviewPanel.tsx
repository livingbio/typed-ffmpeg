import { Paper, Typography, Box, Button, CircularProgress } from '@mui/material';
import { NodeMappingManager, NODE_MAPPING_EVENTS } from '../utils/nodeMapping';
import { useEffect, useState, useRef } from 'react';
import { runPython } from '../utils/pyodideUtils';
import { generateFFmpegCommand } from '../utils/generateFFmpegCommand';

interface PreviewPanelProps {
  nodeMappingManager: NodeMappingManager;
}

// Debounce time in ms - adjust as needed
const DEBOUNCE_TIME = 800;

export default function PreviewPanel({ nodeMappingManager }: PreviewPanelProps) {
  const [pythonCode, setPythonCode] = useState<string>('');
  const [ffmpegCmd, setFfmpegCmd] = useState<string>('');
  const [result, setResult] = useState<string>('');
  const [error, setError] = useState<string | undefined>(undefined);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  
  // Debounce timer reference
  const debounceTimerRef = useRef<number | null>(null);

  // Update code when the mapping changes
  useEffect(() => {
    const updatePythonCode = async () => {
      try {
        setIsLoading(true);

        const commandResult = await generateFFmpegCommand(nodeMappingManager);

        setPythonCode(commandResult.python);
        setFfmpegCmd(commandResult.ffmpeg_cmd || '');
        setError(commandResult.error);
      } catch (e) {
        console.error('Error updating Python code:', e);
        setError(e instanceof Error ? e.message : String(e));
      } finally {
        setIsLoading(false);
      }
    };

    // Debounced update function to prevent frequent updates
    const debouncedUpdate = () => {
      // Clear any existing timer
      if (debounceTimerRef.current !== null) {
        window.clearTimeout(debounceTimerRef.current);
      }
      
      // Set a new timer
      debounceTimerRef.current = window.setTimeout(() => {
        updatePythonCode();
        debounceTimerRef.current = null;
      }, DEBOUNCE_TIME);
    };

    // Subscribe to node mapping update events
    // Now we only need to listen for a single UPDATE event
    const unsubscribe = nodeMappingManager.on(NODE_MAPPING_EVENTS.UPDATE, debouncedUpdate);
    
    // Initial update
    debouncedUpdate();
    
    // Cleanup
    return () => {
      unsubscribe();
      if (debounceTimerRef.current !== null) {
        window.clearTimeout(debounceTimerRef.current);
      }
    };
  }, [nodeMappingManager]);

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

  const handleCopyFFmpeg = () => {
    navigator.clipboard.writeText(ffmpegCmd);
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
            <Button variant="outlined" size="small" onClick={handleCopy} disabled={!pythonCode}>
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
              <Typography
                variant="body2"
                color="error"
                component="pre"
                sx={{
                  margin: 0,
                  fontFamily: 'monospace',
                  fontSize: '0.875rem',
                  whiteSpace: 'pre-wrap',
                }}
              >
                {error}
              </Typography>
            </Box>
          ) : (
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
              {pythonCode || '# No valid FFmpeg command generated'}
            </pre>
          )}
        </Paper>
      </Box>

      {/* FFmpeg Command */}
      {ffmpegCmd && (
        <Box sx={{ mb: 3 }}>
          <Box
            sx={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              mb: 1,
            }}
          >
            <Typography variant="subtitle2">FFmpeg Command</Typography>
            <Button variant="outlined" size="small" onClick={handleCopyFFmpeg}>
              Copy
            </Button>
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
              {ffmpegCmd}
            </pre>
          </Paper>
        </Box>
      )}

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
                {result || 'No result'}
              </pre>
            )}
          </Paper>
        </Box>
      )}
    </Box>
  );
}
