import { memo, useState, useEffect } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip, Button, useTheme } from '@mui/material';
import { EDGE_COLORS } from '../types/edge';
import { NodeData } from '../types/node';
import options from '../config/options.json';

// Input options are those with flags & (1 << 11)
const INPUT_FLAG = 1 << 11;
/**
 * Filters FFmpeg input options from the complete options list
 * Excludes function-type options that can't be set through text input
 */
const inputOptions = options.filter((option) => 
  (option.flags & INPUT_FLAG) !== 0 && 
  option.type !== "OPT_TYPE_FUNC" // Skip function type options that can't be set through text input
);

/**
 * InputNode component represents an input file in the FFmpeg processing chain
 * Allows setting input filename and various FFmpeg input parameters
 * 
 * @param {NodeProps<NodeData>} props - The props for the node
 * @returns {JSX.Element} Rendered input node
 */
function InputNode({ data, id }: NodeProps<NodeData>) {
  const theme = useTheme();
  const [filename, setFilename] = useState<string>(data.filename || '');
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [expanded, setExpanded] = useState<boolean>(false);

  // Update local state when data changes
  useEffect(() => {
    setFilename(data.filename || '');
    setParameters(data.parameters || {});
  }, [data.filename, data.parameters]);

  /**
   * Handles parameter value changes and updates node data
   * 
   * @param {string} paramName - The name of the parameter being changed
   * @param {string} value - The new parameter value
   */
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

  /**
   * Handles filename changes and updates node data
   * 
   * @param {React.ChangeEvent<HTMLInputElement>} e - The change event
   */
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

  /**
   * Generates the FFmpeg command string for this input node
   * 
   * @returns {string} Formatted FFmpeg command string with input options and filename
   */
  const getCommandString = () => {
    const paramString = Object.entries(parameters)
      .filter(([, value]) => value !== '')
      .map(([key, value]) => `-${key} ${value}`)
      .join(' ');

    return `-i ${filename} ${paramString}`;
  };

  // Calculate which options to show
  const visibleOptions = expanded ? inputOptions : inputOptions.slice(0, 3);

  return (
    <Paper 
      elevation={3} 
      sx={{ 
        padding: 2,
        minWidth: 200,
        backgroundColor: '#e8f5e9',
        border: '2px solid #4caf50',
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
        
        {inputOptions.length > 3 && (
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