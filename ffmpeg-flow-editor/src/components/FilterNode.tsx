import { memo, useState } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip, FormHelperText } from '@mui/material';
import { FFmpegFilter, FilterParameter, predefinedFilters } from '@/types/ffmpeg';

interface FilterNodeData {
  label: string;
  filterType: 'input' | 'filter' | 'output';
  filterName?: string;
  parameters?: Record<string, string>;
}

interface ValidationError {
  [key: string]: string;
}

function FilterNode({ data }: NodeProps<FilterNodeData>) {
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [errors, setErrors] = useState<ValidationError>({});

  const validateParameter = (param: FilterParameter, value: string): string | null => {
    if (!value) {
      return null;
    }

    if (param.type === 'number') {
      const numValue = parseFloat(value);
      if (isNaN(numValue)) {
        return 'Must be a number';
      }
      if (param.validation?.min !== undefined && numValue < param.validation.min) {
        return `Must be at least ${param.validation.min}`;
      }
      if (param.validation?.max !== undefined && numValue > param.validation.max) {
        return `Must be at most ${param.validation.max}`;
      }
    }

    if (param.validation?.pattern && !new RegExp(param.validation.pattern).test(value)) {
      return 'Invalid format';
    }

    return null;
  };

  const handleParameterChange = (paramName: string, value: string) => {
    const filter = predefinedFilters.find(f => f.name === data.filterName);
    if (!filter) return;

    const param = filter.parameters.find(p => p.name === paramName);
    if (!param) return;

    const error = validateParameter(param, value);
    setErrors(prev => ({
      ...prev,
      [paramName]: error || ''
    }));

    setParameters(prev => ({
      ...prev,
      [paramName]: value
    }));
  };

  const getFilterString = () => {
    if (data.filterType === 'filter' && data.filterName) {
      const paramString = Object.entries(parameters)
        .filter(([_, value]) => value !== '')
        .map(([key, value]) => `${key}=${value}`)
        .join(':');
      return `${data.filterName}${paramString ? '=' + paramString : ''}`;
    }
    return '';
  };

  const hasErrors = Object.values(errors).some(error => error !== '');

  return (
    <Paper
      elevation={3}
      sx={{
        padding: 2,
        minWidth: 200,
        backgroundColor: '#fff',
        border: '1px solid #ccc',
      }}
    >
      <Handle type="target" position={Position.Left} />
      <Typography variant="h6" gutterBottom>
        {data.label}
      </Typography>
      {data.filterType === 'filter' && (
        <Box sx={{ mt: 1 }}>
          <Typography variant="body2" color="text.secondary" gutterBottom>
            {data.filterName}
          </Typography>
          {predefinedFilters
            .find(f => f.name === data.filterName)
            ?.parameters.map((param) => (
              <Box key={param.name} sx={{ mt: 1 }}>
                <TextField
                  fullWidth
                  size="small"
                  label={param.name}
                  value={parameters[param.name] || ''}
                  onChange={(e) => handleParameterChange(param.name, e.target.value)}
                  variant="outlined"
                  error={!!errors[param.name]}
                  helperText={errors[param.name]}
                />
              </Box>
            ))}
          <Tooltip title={getFilterString()}>
            <Typography
              variant="caption"
              sx={{
                mt: 1,
                display: 'block',
                color: hasErrors ? 'error.main' : 'text.secondary'
              }}
            >
              {getFilterString()}
            </Typography>
          </Tooltip>
        </Box>
      )}
      <Handle type="source" position={Position.Right} />
    </Paper>
  );
}

export default memo(FilterNode);
