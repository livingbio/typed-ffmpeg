import { Button, Box, TextField, InputAdornment, Paper } from '@mui/material';
import { useState, useRef, useEffect } from 'react';
import { predefinedFilters } from '../types/ffmpeg';
import SearchIcon from '@mui/icons-material/Search';

interface ToolbarProps {
  onAddFilter: (filterType: string, parameters?: Record<string, string>) => void;
}

export default function Toolbar({ onAddFilter }: ToolbarProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const searchInputRef = useRef<HTMLInputElement>(null);
  const dropdownRef = useRef<HTMLDivElement>(null);

  const handleClick = () => {
    setIsOpen(true);
  };

  const handleClose = () => {
    setIsOpen(false);
    setSearchQuery('');
  };

  useEffect(() => {
    if (isOpen && searchInputRef.current) {
      searchInputRef.current.focus();
    }
  }, [isOpen]);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        handleClose();
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const handleAddFilter = (filter: typeof predefinedFilters[0]) => {
    onAddFilter(filter.name);
    handleClose();
  };

  const filteredFilters = predefinedFilters.filter(filter =>
    filter.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    filter.label.toLowerCase().includes(searchQuery.toLowerCase()) ||
    filter.description.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <Box sx={{ position: 'absolute', top: 10, left: 10, zIndex: 5 }}>
      <Button
        variant="contained"
        onClick={handleClick}
        sx={{ mr: 1 }}
      >
        Add Filter
      </Button>
      {isOpen && (
        <Paper
          ref={dropdownRef}
          sx={{
            position: 'absolute',
            top: '100%',
            left: 0,
            width: 400,
            maxHeight: 500,
            overflow: 'auto',
            mt: 1,
            boxShadow: 3,
          }}
        >
          <Box sx={{ p: 1 }}>
            <TextField
              fullWidth
              size="small"
              placeholder="Search filters..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              inputRef={searchInputRef}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchIcon />
                  </InputAdornment>
                ),
              }}
              sx={{ mb: 1 }}
            />
          </Box>
          {filteredFilters.map((filter) => (
            <Box
              key={filter.name}
              onClick={() => handleAddFilter(filter)}
              sx={{
                p: 1,
                cursor: 'pointer',
                '&:hover': {
                  bgcolor: 'action.hover',
                },
                whiteSpace: 'normal',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'flex-start',
              }}
            >
              <Box sx={{ fontWeight: 'bold' }}>{filter.name}</Box>
              <Box sx={{ fontSize: '0.8rem', color: 'text.secondary' }}>{filter.description}</Box>
            </Box>
          ))}
        </Paper>
      )}
    </Box>
  );
}
