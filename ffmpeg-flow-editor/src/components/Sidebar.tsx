import { Box, Paper, Typography, Divider, TextField, InputAdornment } from '@mui/material';
import { Node, Edge } from 'reactflow';
import { predefinedFilters } from '../types/ffmpeg';
import PreviewPanel from './PreviewPanel';
import { useState, useMemo } from 'react';
import SearchIcon from '@mui/icons-material/Search';

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
        }}
      >
        <Typography variant="h6">FFmpeg Flow Editor</Typography>
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
