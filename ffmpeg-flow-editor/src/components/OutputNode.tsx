import { memo, useState, useEffect } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip, Button, useTheme } from '@mui/material';
import { EDGE_COLORS } from '../types/edge';
import { NodeData } from '../types/node';
import options from '../config/options.json';

// Output options are those with flags & (1 << 12)
const OUTPUT_FLAG = 1 << 12;
const outputOptions = options.filter((option) => 
  (option.flags & OUTPUT_FLAG) !== 0 && 
  option.type !== "OPT_TYPE_FUNC" // Skip function type options that can't be set through text input
);

function OutputNode({ data, id }: NodeProps<NodeData>) {
  const theme = useTheme();
  const [filename, setFilename] = useState<string>(data.filename || '');
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [expanded, setExpanded] = useState<boolean>(false);

  // Update local state when data changes
  useEffect(() => {
    setFilename(data.filename || '');
    setParameters(data.parameters || {});
  }, [data.filename, data.parameters]);

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
          filename,
          parameters: newParameters,
        },
      },
    });
    window.dispatchEvent(event);
  };

  const handleFilenameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newFilename = e.target.value;
    setFilename(newFilename);
    
    // Update the node data
    const event = new CustomEvent('updateNodeData', {
      detail: {
        id,
        data: {
          ...data,
          filename: newFilename,
          parameters,
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

    return `${paramString} ${filename}`;
  };

  // Calculate which options to show
  const visibleOptions = expanded ? outputOptions : outputOptions.slice(0, 3);

  return (
    <Paper 
      elevation={3} 
      sx={{ 
        padding: 2,
        minWidth: 200,
        backgroundColor: '#e3f2fd',
        border: `2px solid #2196f3`,
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
        
        {outputOptions.length > 3 && (
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
        <TextField
          fullWidth
          size="small"
          label="Filename"
          value={filename}
          onChange={handleFilenameChange}
          variant="outlined"
          margin="dense"
          helperText="Output file path"
          InputProps={{
            sx: {
              '& input::placeholder': {
                color: 'text.disabled',
                opacity: 1,
              },
            },
          }}
        />

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
          id={`input-${index}`}
          style={{
            backgroundColor: EDGE_COLORS[handle.type],
            width: '10px',
            height: '10px',
            border: '2px solid #fff',
            top: `${(index + 1) * (100 / (data.handles.inputs.length + 1))}%`,
          }}
        />
      ))}
      {/* Output handle */}
      <Handle
        type="source"
        position={Position.Right}
        id={data.handles.outputs[0].id}
        style={{
          backgroundColor: EDGE_COLORS[data.handles.outputs[0].type],
          width: '10px',
          height: '10px',
          border: '2px solid #fff',
        }}
      />
    </Paper>
  );
}

export default memo(OutputNode); 