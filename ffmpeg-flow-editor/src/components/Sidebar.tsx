import { Box, Paper, Typography, Divider, TextField, InputAdornment, Button } from '@mui/material';
import { predefinedFilters } from '../types/ffmpeg';
import { useState, useMemo } from 'react';
import SearchIcon from '@mui/icons-material/Search';
import InputIcon from '@mui/icons-material/Input';
import OutputIcon from '@mui/icons-material/Output';
import DownloadIcon from '@mui/icons-material/Download';
import GitHubIcon from '@mui/icons-material/GitHub';
import { Link as MuiLink } from '@mui/material';
import UploadIcon from '@mui/icons-material/Upload';
import AutoGraphIcon from '@mui/icons-material/AutoGraph';
import ContentPasteIcon from '@mui/icons-material/ContentPaste';

import { NodeMappingManager } from '../utils/nodeMapping';

interface SidebarProps {
  onAddFilter: (
    filterType: string,
    parameters?: Record<string, string>,
    position?: { x: number; y: number }
  ) => void;
  nodeMappingManager: NodeMappingManager;
  onLoadJson: (jsonString: string) => Promise<void>;
  onLayout: () => void;
  onPasteCommand?: (command: string) => void;
}

export default function Sidebar({
  onAddFilter,
  nodeMappingManager,
  onLoadJson,
  onLayout,
  onPasteCommand,
}: SidebarProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [ffmpegCommand, setFfmpegCommand] = useState('');

  const filteredFilters = useMemo(() => {
    if (!searchQuery) return [...predefinedFilters].sort((a, b) => a.name.localeCompare(b.name));
    const query = searchQuery.toLowerCase();
    return predefinedFilters
      .filter(
        (filter) =>
          filter.name.toLowerCase().includes(query) ||
          filter.description.toLowerCase().includes(query)
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
      alert('Error exporting flow: ' + (error instanceof Error ? error.message : String(error)));
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
    <Paper
      elevation={3}
      sx={{
        position: 'fixed',
        right: 0,
        top: 0,
        height: '100vh',
        width: 350,
        backgroundColor: '#fff',
        zIndex: 1000,
        display: 'flex',
        flexDirection: 'column',
      }}
    >
      <Box
        sx={{
          p: 1.5,
          borderBottom: 1,
          borderColor: 'divider',
          backgroundColor: '#f5f5f5',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <Typography variant="h6" sx={{ fontSize: '0.875rem' }}>
          FFmpeg Flow Editor
        </Typography>
        <Box sx={{ display: 'flex', gap: 0.5 }}>
          <Button
            variant="contained"
            onClick={onLayout}
            sx={{
              mb: 1,
              minWidth: '32px',
              width: '32px',
              height: '32px',
              padding: 0,
            }}
          >
            <AutoGraphIcon fontSize="small" />
          </Button>
          <Button
            variant="contained"
            onClick={handleExport}
            sx={{
              mb: 1,
              minWidth: '32px',
              width: '32px',
              height: '32px',
              padding: 0,
            }}
          >
            <DownloadIcon fontSize="small" />
          </Button>
          <Button
            variant="contained"
            component="label"
            sx={{
              mb: 1,
              minWidth: '32px',
              width: '32px',
              height: '32px',
              padding: 0,
            }}
          >
            <UploadIcon fontSize="small" />
            <input type="file" hidden accept=".json" onChange={handleLoadJson} />
          </Button>
        </Box>
      </Box>

      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          p: 1,
          borderBottom: 1,
          borderColor: 'divider',
          backgroundColor: '#f0f0f0',
        }}
      >
        <GitHubIcon sx={{ fontSize: 16, mr: 0.5 }} />
        <MuiLink
          href="https://github.com/livingbio/typed-ffmpeg"
          target="_blank"
          rel="noopener noreferrer"
          underline="hover"
          sx={{ fontSize: '0.75rem' }}
        >
          github.com/livingbio/typed-ffmpeg
        </MuiLink>
      </Box>

      <Box sx={{ p: 1.5, overflow: 'auto' }}>
        {/* Command Input Section */}
        <Box sx={{ mb: 2 }}>
          <Typography variant="subtitle2" sx={{ fontSize: '0.75rem' }} gutterBottom>
            FFmpeg Command
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
            sx={{ mb: 1 }}
          />
          <Button
            variant="contained"
            onClick={handlePasteCommand}
            startIcon={<ContentPasteIcon />}
            fullWidth
            size="small"
          >
            Parse Command
          </Button>
        </Box>

        <Divider sx={{ my: 1.5 }} />

        {/* I/O Nodes Section */}
        <Box sx={{ mb: 2 }}>
          <Typography variant="subtitle2" gutterBottom>
            I/O Nodes
          </Typography>
          <Box
            sx={{
              display: 'flex',
              gap: 0.5,
              mb: 1.5,
            }}
          >
            <Paper
              elevation={0}
              draggable
              onDragStart={(e) => handleDragStart(e, 'input')}
              onClick={() => onAddFilter('input')}
              sx={{
                p: 1,
                cursor: 'grab',
                border: '1px solid',
                borderColor: 'divider',
                borderRadius: 1,
                flex: 1,
                display: 'flex',
                alignItems: 'center',
                gap: 0.5,
                '&:hover': {
                  backgroundColor: '#f5f5f5',
                },
                '&:active': {
                  cursor: 'grabbing',
                },
              }}
            >
              <InputIcon fontSize="small" />
              <Typography variant="body2" sx={{ fontSize: '0.75rem' }} fontWeight={500}>
                Input Node
              </Typography>
            </Paper>
            <Paper
              elevation={0}
              draggable
              onDragStart={(e) => handleDragStart(e, 'output')}
              onClick={() => onAddFilter('output')}
              sx={{
                p: 1,
                cursor: 'grab',
                border: '1px solid',
                borderColor: 'divider',
                borderRadius: 1,
                flex: 1,
                display: 'flex',
                alignItems: 'center',
                gap: 0.5,
                '&:hover': {
                  backgroundColor: '#f5f5f5',
                },
                '&:active': {
                  cursor: 'grabbing',
                },
              }}
            >
              <OutputIcon fontSize="small" />
              <Typography variant="body2" sx={{ fontSize: '0.75rem' }} fontWeight={500}>
                Output Node
              </Typography>
            </Paper>
          </Box>
        </Box>

        <Divider sx={{ my: 1.5 }} />

        {/* Filters Section */}
        <Box sx={{ mb: 2 }}>
          <Typography variant="subtitle2" sx={{ fontSize: '0.75rem' }} gutterBottom>
            Available Filters
          </Typography>
          <TextField
            fullWidth
            size="small"
            placeholder="Search filters..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            sx={{ mb: 1.5 }}
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
              // maxHeight: '180px',
              overflow: 'auto',
              border: '1px solid',
              borderColor: 'divider',
              borderRadius: 1,
            }}
          >
            {filteredFilters.map((filter) => (
              <Paper
                key={filter.name}
                elevation={0}
                draggable
                onDragStart={(e) => handleDragStart(e, filter.name)}
                onClick={() => onAddFilter(filter.name)}
                sx={{
                  p: 1,
                  cursor: 'grab',
                  borderBottom: '1px solid',
                  borderColor: 'divider',
                  '&:last-child': {
                    borderBottom: 'none',
                  },
                  '&:hover': {
                    backgroundColor: '#f5f5f5',
                  },
                  '&:active': {
                    cursor: 'grabbing',
                  },
                }}
              >
                <Typography variant="body2" sx={{ fontSize: '0.75rem' }} fontWeight={500}>
                  {filter.name}
                </Typography>
                <Typography variant="caption" sx={{ fontSize: '0.7rem' }} color="text.secondary">
                  {filter.description}
                </Typography>
              </Paper>
            ))}
          </Box>
        </Box>
      </Box>
    </Paper>
  );
}
