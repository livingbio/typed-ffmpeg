import { memo, useState, useEffect } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip, Button, useTheme } from '@mui/material';
import { EDGE_COLORS } from '../types/edge';
import { NodeData } from '../types/node';
import options from '../config/options.json';

// Input and output flags
const INPUT_FLAG = 1 << 11;
const OUTPUT_FLAG = 1 << 12;

// Global options are those which are neither input nor output options
const globalOptions = options.filter((option) => 
  (option.flags & INPUT_FLAG) === 0 && 
  (option.flags & OUTPUT_FLAG) === 0 &&
  option.type !== "OPT_TYPE_FUNC" // Skip function type options that can't be set through text input
);

function GlobalNode({ data, id }: NodeProps<NodeData>) {
  const theme = useTheme();
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [expanded, setExpanded] = useState<boolean>(false);

  // Update local state when data changes
  useEffect(() => {
    setParameters(data.parameters || {});
  }, [data.parameters]);

  const handleParameterChange = (paramName: string, value: string) => {
    const newParameters = {
      ...parameters,
      [paramName]: value,
    };
    setParameters(newParameters);

    // Update the node data
    const event = new CustomEvent('updateNodeData', {
      detail: {
        id,
        data: {
          ...data,
          parameters: newParameters,
        },
      },
    });
    window.dispatchEvent(event);
  };

  // Get command line representation
  const getCommandString = () => {
    const paramString = Object.entries(parameters)
      .filter(([, value]) => value !== '')
      .map(([key, value]) => `-${key} ${value}`)
      .join(' ');

    return paramString;
  };

  // Calculate which options to show
  const visibleOptions = expanded ? globalOptions : globalOptions.slice(0, 3);

  return (
    <Paper 
      elevation={3} 
      sx={{ 
        padding: 2,
        minWidth: 200,
        backgroundColor: '#f3e5f5',
        border: `2px solid #9c27b0`,
        color: theme.palette.text.primary,
        position: 'relative',
      }}
    >
      <Box sx={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'flex-start',
        mb: 1
      }}>
        <Typography variant="h6">
          {data.label}
        </Typography>
        
        {globalOptions.length > 3 && (
          <Button 
            size="small" 
            onClick={() => setExpanded(!expanded)}
            sx={{ 
              minWidth: 'auto', 
              fontSize: '0.75rem',
              padding: '2px 8px',
            }}
          >
            {expanded ? 'Less' : 'More'}
          </Button>
        )}
      </Box>

      <Box sx={{ mt: 1 }}>
        {visibleOptions.map((option) => (
          <Box key={option.name} sx={{ mt: 1 }}>
            <TextField
              fullWidth
              size="small"
              label={option.name}
              placeholder={option.argname || ''}
              value={parameters[option.name] || ''}
              onChange={(e) => handleParameterChange(option.name, e.target.value)}
              variant="outlined"
              margin="dense"
              helperText={option.help}
              InputProps={{
                sx: {
                  '& input::placeholder': {
                    color: 'text.disabled',
                    opacity: 0.7,
                  },
                },
              }}
            />
          </Box>
        ))}
        
        <Tooltip title={getCommandString()}>
          <Typography
            variant="caption"
            sx={{
              mt: 1,
              display: 'block',
              color: 'text.secondary',
            }}
          >
            {getCommandString()}
          </Typography>
        </Tooltip>
      </Box>

      {/* Input handles */}
      {data.handles.inputs.map((handle, index) => (
        <Handle
          key={handle.id}
          type="target"
          position={Position.Left}
          id={handle.id}
          style={{
            backgroundColor: EDGE_COLORS[handle.type],
            width: '10px',
            height: '10px',
            border: '2px solid #fff',
            top: `${(index + 1) * (100 / (data.handles.inputs.length + 1))}%`,
          }}
        />
      ))}
    </Paper>
  );
}

export default memo(GlobalNode); 