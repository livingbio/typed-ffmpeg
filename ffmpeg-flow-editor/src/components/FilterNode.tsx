import { memo, useState, useEffect } from 'react';
import { Handle, Position, NodeProps, useUpdateNodeInternals } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip, useTheme, Button } from '@mui/material';
import { FFMpegFilterOption } from '../types/ffmpeg';
import { EDGE_COLORS } from '../types/edge';
import { NodeData } from '../types/node';

interface ValidationError {
  [key: string]: string | null;
}

function FilterNode({ data, id }: NodeProps<NodeData>) {
  const theme = useTheme();
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [errors, setErrors] = useState<ValidationError>({});
  const [expanded, setExpanded] = useState<boolean>(false);
  const updateNodeInternals = useUpdateNodeInternals();

  // Update local state when data changes
  useEffect(() => {
    setParameters(data.parameters || {});
    // Update node internals when handles change
    updateNodeInternals(id);
  }, [data.parameters, data.handles, id, updateNodeInternals]);

  // Get the filter definition
  const filter = data.filter;
  if (!filter) {
    throw new Error(`Filter ${data.filterName} not found`);
  }

  const validateParameter = (param: FFMpegFilterOption, value: string): string | null => {
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

  const getFilterString = () => {
    const paramString = Object.entries(parameters)
      .filter(([, value]) => value !== '')
      .map(([key, value]) => `${key}=${value}`)
      .join(':');

    return `${data.filterName}${paramString ? '=' + paramString : ''}`;
  };

  const hasErrors = Object.values(errors).some((error) => error !== '');

  // Calculate which options to show
  const visibleOptions = expanded ? filter.options : filter.options.slice(0, 3);

  return (
    <Paper
      elevation={3}
      sx={{
        padding: 2,
        minWidth: 200,
        maxWidth: 400,
        backgroundColor: theme.palette.background.paper,
        border: `1px solid ${theme.palette.divider}`,
        color: theme.palette.text.primary,
        position: 'relative',
        '& .MuiTypography-root': {
          wordBreak: 'break-word',
          overflowWrap: 'break-word',
        },
      }}
    >
      {/* Input handles */}
      {data.handles.inputs.map((handle, index) => (
        <Handle
          key={handle.id}
          id={handle.id}
          data-handle-id={handle.id}
          type="target"
          position={Position.Left}
          style={{
            backgroundColor: EDGE_COLORS[handle.type],
            width: '10px',
            height: '10px',
            top: `${(index + 1) * (100 / (data.handles.inputs.length + 1))}%`,
            border: '2px solid #fff',
          }}
          data-type={handle.type}
          data-handle-type="input"
        />
      ))}

      <Box
        sx={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'flex-start',
          mb: 1,
        }}
      >
        <Typography variant="h6">{data.label}</Typography>

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
      {data.handles.outputs.map((handle, index) => (
        <Handle
          key={handle.id}
          id={handle.id}
          data-handle-id={handle.id}
          type="source"
          position={Position.Right}
          style={{
            backgroundColor: EDGE_COLORS[handle.type],
            width: '10px',
            height: '10px',
            top: `${(index + 1) * (100 / (data.handles.outputs.length + 1))}%`,
            border: '2px solid #fff',
          }}
          data-type={handle.type}
          data-handle-type="output"
        />
      ))}
    </Paper>
  );
}

export default memo(FilterNode);
