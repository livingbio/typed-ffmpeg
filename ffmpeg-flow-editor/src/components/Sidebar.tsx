import { Box, Paper, Typography, Divider, TextField, InputAdornment, Button } from '@mui/material';
import { Node, Edge } from 'reactflow';
import { predefinedFilters } from '../types/ffmpeg';
import PreviewPanel from './PreviewPanel';
import { useState, useMemo } from 'react';
import SearchIcon from '@mui/icons-material/Search';
import InputIcon from '@mui/icons-material/Input';
import OutputIcon from '@mui/icons-material/Output';
import DownloadIcon from '@mui/icons-material/Download';
import { convertToDag } from '../utils/convertToDag';
import { dumps } from '../utils/serialize';

interface SidebarProps {
  nodes: Node[];
  edges: Edge[];
  onAddFilter: (
    filterType: string,
    parameters?: Record<string, string>,
    position?: { x: number; y: number }
  ) => void;
}

export default function Sidebar({ nodes, edges, onAddFilter }: SidebarProps) {
  const [searchQuery, setSearchQuery] = useState('');

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
      const dag = convertToDag(nodes, edges);
      if (!dag) {
        throw new Error('No valid DAG structure found');
      }
      const json = dumps(dag);
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
          p: 2,
          borderBottom: 1,
          borderColor: 'divider',
          backgroundColor: '#f5f5f5',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <Typography variant="h6">FFmpeg Flow Editor</Typography>
        <Button
          variant="contained"
          startIcon={<DownloadIcon />}
          onClick={handleExport}
          size="small"
        >
          Export
        </Button>
      </Box>

      <Box
        sx={{
          flex: 1,
          overflow: 'auto',
          p: 2,
          '&::-webkit-scrollbar': {
            width: '8px',
          },
          '&::-webkit-scrollbar-track': {
            background: '#f1f1f1',
          },
          '&::-webkit-scrollbar-thumb': {
            background: '#888',
            borderRadius: '4px',
          },
          '&::-webkit-scrollbar-thumb:hover': {
            background: '#555',
          },
        }}
      >
        {/* I/O Nodes Section */}
        <Box sx={{ mb: 3 }}>
          <Typography variant="subtitle1" gutterBottom>
            I/O Nodes
          </Typography>
          <Box
            sx={{
              display: 'flex',
              gap: 1,
              mb: 2,
            }}
          >
            <Paper
              elevation={0}
              draggable
              onDragStart={(e) => handleDragStart(e, 'input')}
              onClick={() => onAddFilter('input')}
              sx={{
                p: 1.5,
                cursor: 'grab',
                border: '1px solid',
                borderColor: 'divider',
                borderRadius: 1,
                flex: 1,
                display: 'flex',
                alignItems: 'center',
                gap: 1,
                '&:hover': {
                  backgroundColor: '#f5f5f5',
                },
                '&:active': {
                  cursor: 'grabbing',
                },
              }}
            >
              <InputIcon fontSize="small" />
              <Typography variant="body2" fontWeight={500}>
                Input Node
              </Typography>
            </Paper>
            <Paper
              elevation={0}
              draggable
              onDragStart={(e) => handleDragStart(e, 'output')}
              onClick={() => onAddFilter('output')}
              sx={{
                p: 1.5,
                cursor: 'grab',
                border: '1px solid',
                borderColor: 'divider',
                borderRadius: 1,
                flex: 1,
                display: 'flex',
                alignItems: 'center',
                gap: 1,
                '&:hover': {
                  backgroundColor: '#f5f5f5',
                },
                '&:active': {
                  cursor: 'grabbing',
                },
              }}
            >
              <OutputIcon fontSize="small" />
              <Typography variant="body2" fontWeight={500}>
                Output Node
              </Typography>
            </Paper>
          </Box>
        </Box>

        <Divider sx={{ my: 2 }} />

        {/* Filters Section */}
        <Box sx={{ mb: 3 }}>
          <Typography variant="subtitle1" gutterBottom>
            Available Filters
          </Typography>
          <TextField
            fullWidth
            size="small"
            placeholder="Search filters..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            sx={{ mb: 2 }}
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
              maxHeight: '200px',
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
                  p: 1.5,
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
                <Typography variant="body2" fontWeight={500}>
                  {filter.name}
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  {filter.description}
                </Typography>
              </Paper>
            ))}
          </Box>
        </Box>

        <Divider sx={{ my: 2 }} />

        {/* Preview Section */}
        <Box>
          <Typography variant="subtitle1" gutterBottom>
            Preview
          </Typography>
          <PreviewPanel nodes={nodes} edges={edges} />
        </Box>
      </Box>
    </Paper>
  );
}
