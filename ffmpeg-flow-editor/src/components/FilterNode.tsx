import { Box, Paper, TextField, Tooltip, Typography } from "@mui/material";
import { memo, useEffect, useState } from "react";
import { Handle, type NodeProps, Position } from "reactflow";
import { EDGE_COLORS, type EdgeType } from "../types/edge";
import { type FFmpegFilterOption, type FFmpegIOType, predefinedFilters } from "../types/ffmpeg";

interface FilterNodeData {
  label: string;
  filterType: "input" | "filter" | "output";
  filterName?: string;
  parameters?: Record<string, string>;
}

interface ValidationError {
  [key: string]: string | null;
}

function FilterNode({ data, id }: NodeProps<FilterNodeData>) {
  const [parameters, setParameters] = useState<Record<string, string>>(data.parameters || {});
  const [errors, setErrors] = useState<ValidationError>({});

  // Update local state when data changes
  useEffect(() => {
    setParameters(data.parameters || {});
  }, [data.parameters]);

  // Get the filter definition
  const filter = predefinedFilters.find((f) => f.name === data.filterName);

  const validateParameter = (param: FFmpegFilterOption, value: string): string | null => {
    if (!value) {
      return null;
    }

    if (
      param.type.value === "int" ||
      param.type.value === "float" ||
      param.type.value === "double"
    ) {
      const numValue = Number.parseFloat(value);
      if (Number.isNaN(numValue)) {
        return "Must be a number";
      }
      if (param.min !== null) {
        const min = Number.parseFloat(param.min);
        if (!Number.isNaN(min) && numValue < min) {
          return `Must be at least ${min}`;
        }
      }
      if (param.max !== null) {
        const max = Number.parseFloat(param.max);
        if (!Number.isNaN(max) && numValue > max) {
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
      [paramName]: error || "",
    }));

    const newParameters = {
      ...parameters,
      [paramName]: value,
    };
    setParameters(newParameters);

    // Update the node data
    const event = new CustomEvent("updateNodeData", {
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
    if (data.filterType === "filter" && data.filterName) {
      const paramString = Object.entries(parameters)
        .filter(([, value]) => value !== "")
        .map(([key, value]) => `${key}=${value}`)
        .join(":");

      return `${data.filterName}${paramString ? `=${paramString}` : ""}`;
    }
    return "";
  };

  const hasErrors = Object.values(errors).some((error) => error !== "");

  const getHandleType = (ioType: FFmpegIOType): EdgeType => {
    const typeValue = ioType.type.value.toLowerCase();

    if (typeValue === "audio") {
      return "audio";
    }
    if (typeValue === "video") {
      return "video";
    }
    return "av";
  };

  // Get input and output types from filter definition
  const inputTypes = filter?.stream_typings_input || [{ type: { value: "av" } } as FFmpegIOType];
  const outputTypes = filter?.stream_typings_output || [{ type: { value: "av" } } as FFmpegIOType];

  return (
    <Paper
      elevation={3}
      sx={{
        padding: 2,
        minWidth: 200,
        backgroundColor: "#fff",
        border: "1px solid #ccc",
      }}
    >
      {/* Input handles */}
      {data.filterType !== "input" &&
        inputTypes.map((type, index) => {
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
                width: "10px",
                height: "10px",
                top: `${(index + 1) * (100 / (inputTypes.length + 1))}%`,
                border: "2px solid #fff",
              }}
              data-type={handleType}
              data-handle-type="input"
            />
          );
        })}

      <Typography variant="h6" gutterBottom>
        {data.label}
      </Typography>
      {data.filterType === "filter" && (
        <Box sx={{ mt: 1 }}>
          {filter?.description && (
            <Typography variant="caption" color="text.secondary" sx={{ display: "block", mb: 1 }}>
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
                  value={parameters[param.name] ?? ""}
                  onChange={(e) => handleParameterChange(param.name, e.target.value)}
                  variant="outlined"
                  error={!!errors[param.name]}
                  helperText={errors[param.name] || param.description}
                  InputProps={{
                    sx: {
                      "& input::placeholder": {
                        color: "text.disabled",
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
                display: "block",
                color: hasErrors ? "error.main" : "text.secondary",
              }}
            >
              {getFilterString()}
            </Typography>
          </Tooltip>
        </Box>
      )}

      {/* Output handles */}
      {data.filterType !== "output" &&
        outputTypes.map((type, index) => {
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
                width: "10px",
                height: "10px",
                top: `${(index + 1) * (100 / (outputTypes.length + 1))}%`,
                border: "2px solid #fff",
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
