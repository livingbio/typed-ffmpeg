import { memo, useState, useEffect } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, Box, Tooltip } from '@mui/material';
import { FFmpegFilterOption, predefinedFilters, FFmpegIOType } from '../types/ffmpeg';
import { EdgeType, EDGE_COLORS } from '../types/edge';

interface FilterNodeData {
  label: string;
  filterType: 'input' | 'filter' | 'output';
  filterName?: string;
  parameters?: Record<string, string>;
  inputTypes?: EdgeType[];
  outputTypes?: EdgeType[];
}

interface ValidationError {
  [key: string]: string | null;
}

interface EvaluationContext {
  StreamType: {
    video: string;
    audio: string;
    av: string;
  };
  re: {
    findall: (pattern: string, str: string) => string[];
    split: (pattern: string, str: string) => string[];
  };
  len: (arr: unknown[] | string | null | undefined) => number;
  int: (val: string | number) => number;
  str: (val: unknown) => string;
  max: (...args: number[]) => number;
  min: (...args: number[]) => number;
  multiply: (arr: string[], count: number) => string[];
  [key: string]: unknown;
}

function FilterNode({ data, id }: NodeProps<FilterNodeData>) {
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [errors, setErrors] = useState<ValidationError>({});
  const [evaluatedInputTypes, setEvaluatedInputTypes] = useState<FFmpegIOType[]>([]);
  const [evaluatedOutputTypes, setEvaluatedOutputTypes] = useState<FFmpegIOType[]>([]);

  // Update local state when data changes
  useEffect(() => {
    setParameters(data.parameters || {});
  }, [data.parameters]);

  // Get the filter definition
  const filter = predefinedFilters.find((f) => f.name === data.filterName);

  // Evaluate dynamic typings when parameters change
  useEffect(() => {
    if (!filter) return;

    // Evaluate input typings
    if (filter.formula_typings_input) {
      try {
        // Create a safe evaluation context
        const context: EvaluationContext = {
          StreamType: {
            video: 'video',
            audio: 'audio',
            av: 'av',
          },
          re: {
            findall: (pattern: string, str: string) => {
              const regex = new RegExp(pattern, 'g');
              return Array.from(str.matchAll(regex)).map((m) => m[0]);
            },
            split: (pattern: string, str: string) => str.split(new RegExp(pattern)),
          },
          ...parameters,
          len: (arr: unknown[] | string | null | undefined) => arr?.length || 0,
          int: (val: string | number) => parseInt(String(val), 10) || 0,
          str: (val: unknown) => String(val),
          max: Math.max,
          min: Math.min,
          multiply: (arr: string[], count: number) => Array(count).fill(arr).flat(),
        };

        // Evaluate the formula
        const result = new Function(
          'context',
          `
          with(context) {
            const StreamType = context.StreamType;
            const inputs = int(context.inputs || 2);
            return multiply([StreamType.audio], inputs);
          }
        `
        )(context);

        // Convert result to FFmpegIOType array
        const inputTypes = Array.isArray(result)
          ? result.map((type) => ({
              __class__: 'FFMpegIOType' as const,
              name: 'default',
              type: {
                __class__: 'StreamType' as const,
                value: type,
              },
            }))
          : filter.stream_typings_input;

        console.log('Evaluated input types:', {
          formula: filter.formula_typings_input,
          result,
          inputTypes,
          parameters,
        });

        setEvaluatedInputTypes(inputTypes);
      } catch (e) {
        console.error('Failed to evaluate input typings formula:', e);
        setEvaluatedInputTypes(filter.stream_typings_input);
      }
    } else {
      setEvaluatedInputTypes(filter.stream_typings_input);
    }

    // Evaluate output typings
    if (filter.formula_typings_output) {
      try {
        // Create a safe evaluation context
        const context: EvaluationContext = {
          StreamType: {
            video: 'video',
            audio: 'audio',
            av: 'av',
          },
          re: {
            findall: (pattern: string, str: string) => {
              const regex = new RegExp(pattern, 'g');
              return Array.from(str.matchAll(regex)).map((m) => m[0]);
            },
            split: (pattern: string, str: string) => str.split(new RegExp(pattern)),
          },
          ...parameters,
          len: (arr: unknown[] | string | null | undefined) => arr?.length || 0,
          int: (val: string | number) => parseInt(String(val), 10) || 0,
          str: (val: unknown) => String(val),
          max: Math.max,
          min: Math.min,
          multiply: (arr: string[], count: number) => Array(count).fill(arr).flat(),
        };

        // Evaluate the formula
        const result = new Function(
          'context',
          `
          with(context) {
            const StreamType = context.StreamType;
            const outputs = int(context.outputs || 2);
            return multiply([StreamType.audio], outputs);
          }
        `
        )(context);

        // Convert result to FFmpegIOType array
        const outputTypes = Array.isArray(result)
          ? result.map((type) => ({
              __class__: 'FFMpegIOType' as const,
              name: 'default',
              type: {
                __class__: 'StreamType' as const,
                value: type,
              },
            }))
          : filter.stream_typings_output;

        console.log('Evaluated output types:', {
          formula: filter.formula_typings_output,
          result,
          outputTypes,
          parameters,
        });

        setEvaluatedOutputTypes(outputTypes);
      } catch (e) {
        console.error('Failed to evaluate output typings formula:', e);
        setEvaluatedOutputTypes(filter.stream_typings_output);
      }
    } else {
      setEvaluatedOutputTypes(filter.stream_typings_output);
    }
  }, [filter, parameters]);

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

  // Convert FFmpegIOType to EdgeType
  const getEdgeType = (ioType: FFmpegIOType): EdgeType => {
    const typeValue = ioType.type.value.toLowerCase() as 'audio' | 'video' | 'av';
    if (typeValue === 'audio') return 'audio';
    if (typeValue === 'video') return 'video';
    return 'av';
  };

  // Get current input and output typesq
  const currentInputTypes =
    evaluatedInputTypes.length > 0 ? evaluatedInputTypes.map(getEdgeType) : data.inputTypes || [];

  const currentOutputTypes =
    evaluatedOutputTypes.length > 0
      ? evaluatedOutputTypes.map(getEdgeType)
      : data.outputTypes || [];

  // Validate connection between two edge types
  const isValidEdgeConnection = (sourceType: EdgeType, targetType: EdgeType): boolean => {
    return sourceType === targetType || sourceType === 'av' || targetType === 'av';
  };

  console.log('Filter node types:', {
    filterName: data.filterName,
    filterType: data.filterType,
    inputTypes: currentInputTypes,
    outputTypes: currentOutputTypes,
  });

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
      {/* Input handles */}
      {data.filterType !== 'input' && (
        <>
          {currentInputTypes.map((type, index) => {
            const handleId = `input-${index}`;
            return (
              <Handle
                key={handleId}
                id={handleId}
                type="target"
                position={Position.Left}
                style={{
                  backgroundColor: EDGE_COLORS[type],
                  width: '10px',
                  height: '10px',
                  top: `${(index + 1) * (100 / (currentInputTypes.length + 1))}%`,
                  border: '2px solid #fff',
                }}
                data-type={type}
                data-handle-type="input"
                isValidConnection={(connection) => {
                  const sourceType = connection.sourceHandle?.split('-')[0] as EdgeType;
                  return isValidEdgeConnection(sourceType, type);
                }}
              />
            );
          })}
        </>
      )}

      <Typography variant="h6" gutterBottom>
        {data.label}
      </Typography>
      {data.filterType === 'filter' && (
        <Box sx={{ mt: 1 }}>
          {filter?.description && (
            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
              {filter.description}
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
                color: hasErrors ? 'error.main' : 'text.secondary',
              }}
            >
              {getFilterString()}
            </Typography>
          </Tooltip>
        </Box>
      )}

      {/* Output handles */}
      {data.filterType !== 'output' && (
        <>
          {currentOutputTypes.map((type, index) => {
            const handleId = `output-${index}`;
            return (
              <Handle
                key={handleId}
                id={handleId}
                type="source"
                position={Position.Right}
                style={{
                  backgroundColor: EDGE_COLORS[type],
                  width: '10px',
                  height: '10px',
                  top: `${(index + 1) * (100 / (currentOutputTypes.length + 1))}%`,
                  border: '2px solid #fff',
                }}
                data-type={type}
                data-handle-type="output"
                isValidConnection={(connection) => {
                  const targetType = connection.targetHandle?.split('-')[0] as EdgeType;
                  return isValidEdgeConnection(type, targetType);
                }}
              />
            );
          })}
        </>
      )}

      {/* Special case for input node - output handle */}
      {data.filterType === 'input' && (
        <Handle
          id="output-0"
          type="source"
          position={Position.Right}
          style={{
            backgroundColor: EDGE_COLORS.av,
            width: '10px',
            height: '10px',
            top: '50%',
            border: '2px solid #fff',
          }}
          data-type="av"
          data-handle-type="output"
          isValidConnection={() => true}
        />
      )}

      {/* Special case for output node - input handle */}
      {data.filterType === 'output' && (
        <Handle
          id="input-0"
          type="target"
          position={Position.Left}
          style={{
            backgroundColor: EDGE_COLORS.av,
            width: '10px',
            height: '10px',
            top: '50%',
            border: '2px solid #fff',
          }}
          data-type="av"
          data-handle-type="input"
          isValidConnection={() => true}
        />
      )}
    </Paper>
  );
}

export default memo(FilterNode);
