import { memo, useState, useEffect } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip, useTheme } from '@mui/material';
import { EDGE_COLORS } from '../types/edge';
import { NodeData } from '../types/node';
import options from '../config/options.json';

// Input options are those with flags & (1 << 11)
const INPUT_FLAG = 1 << 11;
const inputOptions = options.filter((option) => 
  (option.flags & INPUT_FLAG) !== 0 && 
  option.type !== "OPT_TYPE_FUNC" // Skip function type options that can't be set through text input
);

function InputNode({ data, id }: NodeProps<NodeData>) {
  const theme = useTheme();
  const [filename, setFilename] = useState<string>(data.filename || '');
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});

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

    return `-i ${filename} ${paramString}`;
  };

  return (
    <Paper 
      elevation={3} 
      sx={{ 
        padding: 2,
        minWidth: 200,
        backgroundColor: '#e8f5e9',
        border: '2px solid #4caf50',
        color: theme.palette.text.primary,
      }}
    >
      <Typography variant="h6" gutterBottom>
        {data.label}
      </Typography>
      
      <Box sx={{ mt: 1 }}>
        <TextField
          fullWidth
          size="small"
          label="Filename"
          value={filename}
          onChange={handleFilenameChange}
          variant="outlined"
          margin="dense"
          helperText="Input file path"
          InputProps={{
            sx: {
              '& input::placeholder': {
                color: 'text.disabled',
                opacity: 1,
              },
            },
          }}
        />

        {inputOptions.map((option) => (
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

export default memo(InputNode); 