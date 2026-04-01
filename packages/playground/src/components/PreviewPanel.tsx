import { Paper, Typography, Box, Button, CircularProgress } from '@mui/material';
import { NodeMappingManager, NODE_MAPPING_EVENTS } from '../utils/nodeMapping';
import { useEffect, useState, useRef } from 'react';
import { generateFFmpegCommand } from '../utils/generateFFmpegCommand';
import CheckIcon from '@mui/icons-material/Check';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';

interface PreviewPanelProps {
  nodeMappingManager: NodeMappingManager;
}

// Debounce time in ms
const DEBOUNCE_TIME = 800;

export default function PreviewPanel({
  nodeMappingManager,
}: PreviewPanelProps) {
  const [ffmpegCmd, setFfmpegCmd] = useState<string>('');
  const [error, setError] = useState<string | undefined>(undefined);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [copied, setCopied] = useState(false);

  // Debounce timer reference
  const debounceTimerRef = useRef<number | null>(null);

  // Update command when the mapping changes
  useEffect(() => {
    const updateCommand = async () => {
      try {
        setIsLoading(true);
        setError(undefined);

        const commandResult = await generateFFmpegCommand(nodeMappingManager);

        if (commandResult.error) {
          setError(commandResult.error);
          setFfmpegCmd('');
        } else {
          setFfmpegCmd(commandResult.result || '');
        }
      } catch (e) {
        console.error('Error updating FFmpeg command:', e);
        setError(e instanceof Error ? e.message : String(e));
        setFfmpegCmd('');
      } finally {
        setIsLoading(false);
      }
    };

    const debouncedUpdate = () => {
      if (debounceTimerRef.current !== null) {
        window.clearTimeout(debounceTimerRef.current);
      }
      debounceTimerRef.current = window.setTimeout(() => {
        updateCommand();
        debounceTimerRef.current = null;
      }, DEBOUNCE_TIME);
    };

    const unsubscribe = nodeMappingManager.on(
      NODE_MAPPING_EVENTS.UPDATE,
      debouncedUpdate,
    );

    // Initial update
    debouncedUpdate();

    return () => {
      unsubscribe();
      if (debounceTimerRef.current !== null) {
        window.clearTimeout(debounceTimerRef.current);
      }
    };
  }, [nodeMappingManager]);

  const handleCopyFFmpeg = () => {
    navigator.clipboard.writeText(ffmpegCmd);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  return (
    <Box>
      {/* FFmpeg Command */}
      <Box sx={{ mb: 3 }}>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            mb: 1,
          }}
        >
          <Typography variant="subtitle2" sx={{ fontSize: '0.75rem' }}>
            FFmpeg Command
          </Typography>
          <Button
            variant="outlined"
            size="small"
            onClick={handleCopyFFmpeg}
            disabled={!ffmpegCmd}
            color={copied ? 'success' : 'primary'}
            startIcon={
              copied ? (
                <CheckIcon sx={{ fontSize: '0.85rem !important' }} />
              ) : (
                <ContentCopyIcon sx={{ fontSize: '0.85rem !important' }} />
              )
            }
            sx={{ fontSize: '0.7rem', py: 0.25, minWidth: 72 }}
          >
            {copied ? 'Copied' : 'Copy'}
          </Button>
        </Box>
        <Paper
          elevation={0}
          sx={{
            p: 1.5,
            backgroundColor: '#1e1e1e',
            borderRadius: 1,
            overflow: 'auto',
            maxHeight: '200px',
          }}
        >
          {isLoading ? (
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <CircularProgress size={14} sx={{ color: '#858585' }} />
              <Typography
                variant="body2"
                sx={{ fontSize: '0.75rem', color: '#858585' }}
              >
                Generating command...
              </Typography>
            </Box>
          ) : error ? (
            <Box>
              <Typography
                variant="body2"
                fontWeight="bold"
                gutterBottom
                sx={{ fontSize: '0.75rem', color: '#f48771' }}
              >
                Error:
              </Typography>
              <Typography
                variant="body2"
                component="pre"
                sx={{
                  margin: 0,
                  fontFamily: 'monospace',
                  fontSize: '0.7rem',
                  whiteSpace: 'pre-wrap',
                  color: '#f48771',
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
                fontSize: '0.7rem',
                lineHeight: 1.6,
                whiteSpace: 'pre-wrap',
                wordBreak: 'break-word',
                color: '#d4d4d4',
              }}
            >
              {ffmpegCmd ||
                '# Connect an input and output to generate a command'}
            </pre>
          )}
        </Paper>
      </Box>
    </Box>
  );
}
