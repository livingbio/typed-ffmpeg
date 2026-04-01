import {
  Box,
  Typography,
  Divider,
  TextField,
  InputAdornment,
  Button,
  Tooltip,
  IconButton,
} from '@mui/material';
import { Link as MuiLink } from '@mui/material';
import { predefinedFilters } from '../types/ffmpeg';
import { useState, useMemo } from 'react';
import SearchIcon from '@mui/icons-material/Search';
import InputIcon from '@mui/icons-material/Input';
import OutputIcon from '@mui/icons-material/Output';
import DownloadIcon from '@mui/icons-material/Download';
import GitHubIcon from '@mui/icons-material/GitHub';
import UploadIcon from '@mui/icons-material/Upload';
import AutoGraphIcon from '@mui/icons-material/AutoGraph';
import ContentPasteIcon from '@mui/icons-material/ContentPaste';
import CloseIcon from '@mui/icons-material/Close';

import { NodeMappingManager } from '../utils/nodeMapping';

interface SidebarProps {
  onAddFilter: (
    filterType: string,
    parameters?: Record<string, string>,
    position?: { x: number; y: number },
  ) => void;
  nodeMappingManager: NodeMappingManager;
  onLoadJson: (jsonString: string) => Promise<void>;
  onLayout: () => void;
  onPasteCommand?: (command: string) => void;
  onClose?: () => void;
}

export default function Sidebar({
  onAddFilter,
  nodeMappingManager,
  onLoadJson,
  onLayout,
  onPasteCommand,
  onClose,
}: SidebarProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [ffmpegCommand, setFfmpegCommand] = useState('');

  const filteredFilters = useMemo(() => {
    if (!searchQuery)
      return [...predefinedFilters].sort((a, b) => a.name.localeCompare(b.name));
    const query = searchQuery.toLowerCase();
    return predefinedFilters
      .filter(
        (filter) =>
          filter.name.toLowerCase().includes(query) ||
          filter.description.toLowerCase().includes(query),
      )
      .sort((a, b) => a.name.localeCompare(b.name));
  }, [searchQuery]);

  const handleDragStart = (e: React.DragEvent, filterName: string) => {
    e.dataTransfer.setData('application/reactflow', filterName);
    e.dataTransfer.effectAllowed = 'move';
  };

  const handleExport = () => {
    try {
      const json = nodeMappingManager.toJson();
      const blob = new Blob([json], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'ffmpeg-flow.json';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Error exporting flow:', error);
      alert(
        'Error exporting flow: ' +
          (error instanceof Error ? error.message : String(error)),
      );
    }
  };

  const handleLoadJson = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = async (e) => {
        const jsonString = e.target?.result as string;
        if (jsonString) {
          await onLoadJson(jsonString);
        }
      };
      reader.readAsText(file);
    }
  };

  const handlePasteCommand = () => {
    if (onPasteCommand && ffmpegCommand.trim()) {
      onPasteCommand(ffmpegCommand.trim());
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        height: '100%',
        overflow: 'hidden',
      }}
    >
      {/* Header */}
      <Box
        sx={{
          px: 2,
          py: 1.25,
          borderBottom: 1,
          borderColor: 'divider',
          backgroundColor: '#fafafa',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexShrink: 0,
        }}
      >
        <Typography
          variant="subtitle1"
          fontWeight={600}
          sx={{ fontSize: '0.875rem', letterSpacing: '0.01em' }}
        >
          FFmpeg Flow Editor
        </Typography>
        <Box sx={{ display: 'flex', gap: 0.25, alignItems: 'center' }}>
          <Tooltip title="Auto Layout" arrow>
            <IconButton size="small" onClick={onLayout} color="primary">
              <AutoGraphIcon fontSize="small" />
            </IconButton>
          </Tooltip>
          <Tooltip title="Export Flow" arrow>
            <IconButton size="small" onClick={handleExport} color="primary">
              <DownloadIcon fontSize="small" />
            </IconButton>
          </Tooltip>
          <Tooltip title="Import Flow" arrow>
            <IconButton size="small" component="label" color="primary">
              <UploadIcon fontSize="small" />
              <input type="file" hidden accept=".json" onChange={handleLoadJson} />
            </IconButton>
          </Tooltip>
          {onClose && (
            <Tooltip title="Close Panel" arrow>
              <IconButton size="small" onClick={onClose} sx={{ ml: 0.5 }}>
                <CloseIcon fontSize="small" />
              </IconButton>
            </Tooltip>
          )}
        </Box>
      </Box>

      {/* GitHub Link */}
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          py: 0.75,
          borderBottom: 1,
          borderColor: 'divider',
          backgroundColor: '#f5f5f5',
        }}
      >
        <GitHubIcon sx={{ fontSize: 13, mr: 0.5, color: 'text.secondary' }} />
        <MuiLink
          href="https://github.com/livingbio/typed-ffmpeg"
          target="_blank"
          rel="noopener noreferrer"
          underline="hover"
          sx={{ fontSize: '0.7rem', color: 'text.secondary' }}
        >
          github.com/livingbio/typed-ffmpeg
        </MuiLink>
      </Box>

      {/* Scrollable Content */}
      <Box sx={{ flex: 1, overflowY: 'auto', p: 1.5 }}>
        {/* Command Input Section */}
        <Box sx={{ mb: 2 }}>
          <Typography
            variant="overline"
            sx={{
              fontSize: '0.65rem',
              fontWeight: 700,
              color: 'text.secondary',
              letterSpacing: '0.08em',
            }}
          >
            Parse Command
          </Typography>
          <TextField
            fullWidth
            multiline
            rows={3}
            value={ffmpegCommand}
            onChange={(e) => setFfmpegCommand(e.target.value)}
            placeholder="Paste FFmpeg command here..."
            variant="outlined"
            size="small"
            sx={{ mt: 0.5, mb: 1 }}
          />
          <Button
            variant="contained"
            onClick={handlePasteCommand}
            startIcon={<ContentPasteIcon />}
            fullWidth
            size="small"
            disabled={!ffmpegCommand.trim()}
          >
            Parse Command
          </Button>
        </Box>

        <Divider sx={{ my: 1.5 }} />

        {/* I/O Nodes Section */}
        <Box sx={{ mb: 2 }}>
          <Typography
            variant="overline"
            sx={{
              fontSize: '0.65rem',
              fontWeight: 700,
              color: 'text.secondary',
              letterSpacing: '0.08em',
            }}
          >
            I/O Nodes
          </Typography>
          <Box sx={{ display: 'flex', gap: 1, mt: 0.5 }}>
            <Box
              draggable
              onDragStart={(e) => handleDragStart(e, 'input')}
              onClick={() => onAddFilter('input')}
              sx={{
                p: 1,
                cursor: 'grab',
                border: '1px solid #4caf50',
                borderRadius: 1,
                flex: 1,
                display: 'flex',
                alignItems: 'center',
                gap: 0.5,
                backgroundColor: '#f1f8f1',
                transition: 'background-color 0.15s',
                '&:hover': { backgroundColor: '#e8f5e9' },
                '&:active': { cursor: 'grabbing' },
              }}
            >
              <InputIcon fontSize="small" sx={{ color: '#4caf50' }} />
              <Typography
                variant="body2"
                sx={{ fontSize: '0.75rem' }}
                fontWeight={500}
              >
                Input
              </Typography>
            </Box>
            <Box
              draggable
              onDragStart={(e) => handleDragStart(e, 'output')}
              onClick={() => onAddFilter('output')}
              sx={{
                p: 1,
                cursor: 'grab',
                border: '1px solid #2196f3',
                borderRadius: 1,
                flex: 1,
                display: 'flex',
                alignItems: 'center',
                gap: 0.5,
                backgroundColor: '#f0f6ff',
                transition: 'background-color 0.15s',
                '&:hover': { backgroundColor: '#e3f2fd' },
                '&:active': { cursor: 'grabbing' },
              }}
            >
              <OutputIcon fontSize="small" sx={{ color: '#2196f3' }} />
              <Typography
                variant="body2"
                sx={{ fontSize: '0.75rem' }}
                fontWeight={500}
              >
                Output
              </Typography>
            </Box>
          </Box>
        </Box>

        <Divider sx={{ my: 1.5 }} />

        {/* Filters Section */}
        <Box>
          <Typography
            variant="overline"
            sx={{
              fontSize: '0.65rem',
              fontWeight: 700,
              color: 'text.secondary',
              letterSpacing: '0.08em',
            }}
          >
            Filters ({filteredFilters.length})
          </Typography>
          <TextField
            fullWidth
            size="small"
            placeholder="Search filters..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            sx={{ mt: 0.5, mb: 1 }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon fontSize="small" />
                </InputAdornment>
              ),
            }}
          />
          <Box
            sx={{
              border: '1px solid',
              borderColor: 'divider',
              borderRadius: 1,
              overflow: 'hidden',
            }}
          >
            {filteredFilters.map((filter) => (
              <Box
                key={filter.name}
                draggable
                onDragStart={(e) => handleDragStart(e, filter.name)}
                onClick={() => onAddFilter(filter.name)}
                sx={{
                  px: 1.5,
                  py: 0.75,
                  cursor: 'grab',
                  borderBottom: '1px solid',
                  borderColor: 'divider',
                  '&:last-child': { borderBottom: 'none' },
                  transition: 'background-color 0.15s',
                  '&:hover': { backgroundColor: 'action.hover' },
                  '&:active': { cursor: 'grabbing' },
                }}
              >
                <Typography
                  variant="body2"
                  sx={{
                    fontSize: '0.75rem',
                    fontWeight: 600,
                    fontFamily: 'monospace',
                  }}
                >
                  {filter.name}
                </Typography>
                <Typography
                  variant="caption"
                  sx={{ fontSize: '0.68rem' }}
                  color="text.secondary"
                >
                  {filter.description}
                </Typography>
              </Box>
            ))}
          </Box>
        </Box>
      </Box>
    </Box>
  );
}
