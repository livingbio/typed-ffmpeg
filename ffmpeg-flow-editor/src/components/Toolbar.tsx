import { Button, Menu, MenuItem, Box } from '@mui/material';
import { useState } from 'react';
import { predefinedFilters } from '@/types/ffmpeg';

interface ToolbarProps {
  onAddFilter: (filterType: string, parameters?: Record<string, string>) => void;
}

export default function Toolbar({ onAddFilter }: ToolbarProps) {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleAddFilter = (filter: typeof predefinedFilters[0]) => {
    const initialParameters = filter.parameters.reduce((acc, param) => {
      if (param.default !== undefined) {
        acc[param.name] = param.default.toString();
      }
      return acc;
    }, {} as Record<string, string>);

    onAddFilter(filter.name, initialParameters);
    handleClose();
  };

  return (
    <Box sx={{ position: 'absolute', top: 10, left: 10, zIndex: 5 }}>
      <Button
        variant="contained"
        onClick={handleClick}
        sx={{ mr: 1 }}
      >
        Add Filter
      </Button>
      <Menu
        anchorEl={anchorEl}
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        {predefinedFilters.map((filter) => (
          <MenuItem
            key={filter.name}
            onClick={() => handleAddFilter(filter)}
          >
            {filter.label}
          </MenuItem>
        ))}
      </Menu>
    </Box>
  );
}
