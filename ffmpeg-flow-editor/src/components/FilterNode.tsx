import { memo, useState, useEffect } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip, useTheme, Button } from '@mui/material';
import { FFmpegFilterOption, FFMpegIOType } from '../types/ffmpeg';
import { EdgeType, EDGE_COLORS } from '../types/edge';
import { NodeData } from '../types/node';

/**
 * Interface for validation errors in filter parameters
 */
interface ValidationError {
  [key: string]: string | null;
}

/**
 * FilterNode component renders an FFmpeg filter as a node in the flow editor
 * Displays filter parameters, handles input/output connections, and validates user input
 * 
 * @param {NodeProps<NodeData>} props - The props for the node
 * @returns {JSX.Element} Rendered filter node
 */
function FilterNode({ data, id }: NodeProps<NodeData>) {
  const theme = useTheme();
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [errors, setErrors] = useState<ValidationError>({});
  const [expanded, setExpanded] = useState<boolean>(false);

  // Update local state when data changes
  useEffect(() => {
    setParameters(data.parameters || {});
  }, [data.parameters]);

  // Get the filter definition
  const filter = data.filter;
  if(!filter) {
    throw new Error(`Filter ${data.filterName} not found`);
  }

  /**
   * Validates a parameter value against its defined constraints
   * 
   * @param {FFmpegFilterOption} param - The parameter definition
   * @param {string} value - The parameter value to validate
   * @returns {string | null} Error message or null if valid
   */
  const validateParameter = (param: FFmpegFilterOption, value: string): string | null => {
    if (!value) {
      return null;
    }

    if (
      param.type.value === 'int' ||
      param.type.value === 'float' ||
      param.type.value === 'double'
    ) {
      const numValue = parseFloat(value);
      if (isNaN(numValue)) {
        return 'Must be a number';
      }
      if (param.min !== null) {
        const min = parseFloat(param.min);
        if (!isNaN(min) && numValue < min) {
          return `Must be at least ${min}`;
        }
      }
      if (param.max !== null) {
        const max = parseFloat(param.max);
        if (!isNaN(max) && numValue > max) {
          return `Must be at most ${max}`;
        }
      }
    }

    return null;
  };

  /**
   * Handles parameter value changes, validates input, and updates node data
   * 
   * @param {string} paramName - The name of the parameter being changed
   * @param {string} value - The new parameter value
   */
  const handleParameterChange = (paramName: string, value: string) => {
    const param = filter.options.find((p) => p.name === paramName);
    if (!param) return;

    const error = validateParameter(param, value);
    setErrors((prev) => ({
      ...prev,
      [paramName]: error || '',
    }));

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

  /**
   * Generates the FFmpeg filter string based on current parameters
   * 
   * @returns {string} Formatted FFmpeg filter string
   */
  const getFilterString = () => {
    const paramString = Object.entries(parameters)
      .filter(([, value]) => value !== '')
      .map(([key, value]) => `${key}=${value}`)
      .join(':');

    return `${data.filterName}${paramString ? '=' + paramString : ''}`;
  };

  const hasErrors = Object.values(errors).some((error) => error !== '');

  /**
   * Determines the edge type based on FFmpeg IO type
   * 
   * @param {FFMpegIOType} ioType - The input/output type
   * @returns {EdgeType} Edge type (audio, video, or av)
   */
  const getHandleType = (ioType: FFMpegIOType): EdgeType => {
    const typeValue = ioType.type.value;
    if (typeValue === 'audio') return 'audio';
    if (typeValue === 'video') return 'video';
    return 'av';
  };

  // Get input and output types from filter definition
  const inputTypes = data.handles.inputs.map((input) => input.type);
  const outputTypes = data.handles.outputs.map((output) => output.type);

  // Calculate which options to show
  const visibleOptions = expanded ? filter.options : filter.options.slice(0, 3);

  return (
    <Paper
      elevation={3}
      sx={{
        padding: 2,
        minWidth: 200,
        backgroundColor: theme.palette.background.paper,
        border: `1px solid ${theme.palette.divider}`,
        color: theme.palette.text.primary,
        position: 'relative',
      }}
    >
      {/* Input handles */}
      {inputTypes.map((type, index) => {
        const handleType = getHandleType(type);
        const handleId = `input-${index}`;
        return (
          <Handle
            key={handleId}
            id={handleId}
            data-handle-id={handleId}
            type="target"
            position={Position.Left}
            style={{
              backgroundColor: EDGE_COLORS[handleType],
              width: '10px',
              height: '10px',
              top: `${(index + 1) * (100 / (inputTypes.length + 1))}%`,
              border: '2px solid #fff',
            }}
            data-type={handleType}
            data-handle-type="input"
          />
        );
      })}

      <Box sx={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'flex-start',
        mb: 1
      }}>
        <Typography variant="h6">
          {data.label}
        </Typography>
        
        {filter.options.length > 3 && (
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
        {filter.description && (
          <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
            {filter.description}
          </Typography>
        )}
        {visibleOptions.map((param) => (
          <Box key={param.name} sx={{ mt: 1 }}>
            <TextField
              fullWidth
              size="small"
              label={param.name}
              placeholder={param.default?.toString()}
              value={parameters[param.name] ?? ''}
              onChange={(e) => handleParameterChange(param.name, e.target.value)}
              variant="outlined"
              error={!!errors[param.name]}
              helperText={errors[param.name] || param.description}
              InputProps={{
                sx: {
                  '& input::placeholder': {
                    color: 'text.disabled',
                    opacity: 1,
                  },
                },
              }}
            />
          </Box>
        ))}
        <Tooltip title={getFilterString()}>
          <Typography
            variant="caption"
            sx={{
              mt: 1,
              display: 'block',
              color: hasErrors ? 'error.main' : 'text.secondary',
            }}
          >
            {getFilterString()}
          </Typography>
        </Tooltip>
      </Box>

      {/* Output handles */}
      {outputTypes.map((type, index) => {
        const handleType = getHandleType(type);
        const handleId = `output-${index}`;
        return (
          <Handle
            key={handleId}
            id={handleId}
            data-handle-id={handleId}
            type="source"
            position={Position.Right}
            style={{
              backgroundColor: EDGE_COLORS[handleType],
              width: '10px',
              height: '10px',
              top: `${(index + 1) * (100 / (outputTypes.length + 1))}%`,
              border: '2px solid #fff',
            }}
            data-type={handleType}
            data-handle-type="output"
          />
        );
      })}
    </Paper>
  );
}

export default memo(FilterNode);
