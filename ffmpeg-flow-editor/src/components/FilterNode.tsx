import { memo, useState, useEffect } from 'react';
import { Handle, Position, NodeProps, useUpdateNodeInternals } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip } from '@mui/material';
import { FFmpegFilterOption, predefinedFilters, FFmpegIOType } from '../types/ffmpeg';
import { EdgeType, EDGE_COLORS } from '../types/edge';
import { evaluateFormula, parseStringParameter } from '../utils/formulaEvaluator';

interface FilterNodeData {
  label: string;
  filterType: 'input' | 'filter' | 'output';
  filterName?: string;
  parameters?: Record<string, string>;
}

interface ValidationError {
  [key: string]: string | null;
}

function FilterNode({ data, id }: NodeProps<FilterNodeData>) {
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [errors, setErrors] = useState<ValidationError>({});
  const [dynamicInputTypes, setDynamicInputTypes] = useState<FFmpegIOType[]>([]);
  const [dynamicOutputTypes, setDynamicOutputTypes] = useState<FFmpegIOType[]>([]);
  const [formulaError, setFormulaError] = useState<string | null>(null);
  const updateNodeInternals = useUpdateNodeInternals();

  // Update local state when data changes
  useEffect(() => {
    setParameters(data.parameters || {});
  }, [data.parameters]);

  // Get the filter definition
  const filter = predefinedFilters.find((f) => f.name === data.filterName);

  // Convert FFmpegIOType to EdgeType
  const getHandleType = (ioType: FFmpegIOType): EdgeType => {
    const typeValue = ioType.type.value.toLowerCase();
    if (typeValue === 'audio') return 'audio';
    if (typeValue === 'video') return 'video';
    return 'av';
  };

  // Evaluate dynamic formulas when parameters change
  useEffect(() => {
    const evaluateDynamicTypes = async () => {
      if (!filter) return;

      try {
        setFormulaError(null);

        // Convert string parameters to appropriate types
        const parsedParams = Object.entries(parameters).reduce(
          (acc, [key, value]) => ({
            ...acc,
            [key]: parseStringParameter(value),
          }),
          {} as Record<string, string | number | boolean>
        );

        if (filter.is_dynamic_input && filter.formula_typings_input) {
          const inputTypes = await evaluateFormula(filter.formula_typings_input, parsedParams);
          setDynamicInputTypes(inputTypes);
        }

        if (filter.is_dynamic_output && filter.formula_typings_output) {
          const outputTypes = await evaluateFormula(filter.formula_typings_output, parsedParams);
          setDynamicOutputTypes(outputTypes);
        }

        // Update node internals after handle changes
        updateNodeInternals(id);
      } catch (error) {
        console.error('Error evaluating formula:', error);
        setFormulaError(error instanceof Error ? error.message : 'Error evaluating formula');
      }
    };

    evaluateDynamicTypes();
  }, [filter, parameters, id, updateNodeInternals]);

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

  const handleParameterChange = (paramName: string, value: string) => {
    const filter = predefinedFilters.find((f) => f.name === data.filterName);
    if (!filter) return;

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
    if (data.filterType === 'filter' && data.filterName) {
      const paramString = Object.entries(parameters)
        .filter(([, value]) => value !== '')
        .map(([key, value]) => `${key}=${value}`)
        .join(':');

      return `${data.filterName}${paramString ? '=' + paramString : ''}`;
    }
    return '';
  };

  const hasErrors = Object.values(errors).some((error) => error !== '');

  // Get input and output types from filter definition or dynamic evaluation
  const inputTypes = filter?.is_dynamic_input
    ? dynamicInputTypes
    : filter?.stream_typings_input || [{ type: { value: 'av' } } as FFmpegIOType];
  const outputTypes = filter?.is_dynamic_output
    ? dynamicOutputTypes
    : filter?.stream_typings_output || [{ type: { value: 'av' } } as FFmpegIOType];

  console.log('Filter node types:', {
    filterName: data.filterName,
    inputTypes: inputTypes.map((t) => ({
      value: t.type.value,
      type: getHandleType(t),
      rawType: t.type,
    })),
    outputTypes: outputTypes.map((t) => ({
      value: t.type.value,
      type: getHandleType(t),
      rawType: t.type,
    })),
  });

  return (
    <Paper
      elevation={3}
      sx={{
        padding: 2,
        minWidth: 200,
        maxWidth: 300,
        border: '1px solid',
        borderColor: hasErrors || formulaError ? 'error.main' : 'divider',
      }}
    >
      <Typography variant="subtitle1" gutterBottom>
        {data.label}
      </Typography>

      {formulaError && (
        <Typography variant="caption" color="error" sx={{ display: 'block', mb: 1 }}>
          {formulaError}
        </Typography>
      )}

      {/* Input handles */}
      {data.filterType !== 'input' &&
        inputTypes.map((type, index) => (
          <Handle
            key={`input-${index}`}
            type="target"
            position={Position.Left}
            id={`input-${index}`}
            style={{
              background: EDGE_COLORS[getHandleType(type)],
              width: 10,
              height: 10,
              top: `${(index + 1) * (100 / (inputTypes.length + 1))}%`,
            }}
          />
        ))}

      {/* Output handles */}
      {data.filterType !== 'output' &&
        outputTypes.map((type, index) => (
          <Handle
            key={`output-${index}`}
            type="source"
            position={Position.Right}
            id={`output-${index}`}
            style={{
              background: EDGE_COLORS[getHandleType(type)],
              width: 10,
              height: 10,
              top: `${(index + 1) * (100 / (outputTypes.length + 1))}%`,
            }}
          />
        ))}

      {data.filterType === 'filter' && (
        <Box sx={{ mt: 1 }}>
          {filter?.description && (
            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
              {filter.description}
            </Typography>
          )}
          {filter?.is_dynamic_input && filter.formula_typings_input && (
            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
              Dynamic inputs: {filter.formula_typings_input}
            </Typography>
          )}
          {filter?.is_dynamic_output && filter.formula_typings_output && (
            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
              Dynamic outputs: {filter.formula_typings_output}
            </Typography>
          )}
          {predefinedFilters
            .find((f) => f.name === data.filterName)
            ?.options.map((param) => (
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
                color: hasErrors || formulaError ? 'error.main' : 'text.secondary',
              }}
            >
              {getFilterString()}
            </Typography>
          </Tooltip>
        </Box>
      )}
    </Paper>
  );
}

export default memo(FilterNode);
