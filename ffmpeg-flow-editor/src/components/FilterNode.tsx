import { memo, useState, useEffect } from "react";
import { Handle, Position, NodeProps, useEdges } from "reactflow";
import { Paper, Typography, TextField, Box, Tooltip } from "@mui/material";
import { FFmpegFilterOption, predefinedFilters } from "../types/ffmpeg";

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
  const [parameters, setParameters] = useState<Record<string, string>>(
    data.parameters || {}
  );
  const [errors, setErrors] = useState<ValidationError>({});
  const edges = useEdges();

  // Update local state when data changes
  useEffect(() => {
    setParameters(data.parameters || {});
  }, [data.parameters]);

  // Check if input is connected
  const isInputConnected = edges.some((edge) => edge.target === id);

  // Check if output is connected
  const isOutputConnected = edges.some((edge) => edge.source === id);

  const validateParameter = (
    param: FFmpegFilterOption,
    value: string
  ): string | null => {
    if (!value) {
      return null;
    }

    if (
      param.type.value === "int" ||
      param.type.value === "float" ||
      param.type.value === "double"
    ) {
      const numValue = parseFloat(value);
      if (isNaN(numValue)) {
        return "Must be a number";
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

      return `${data.filterName}${paramString ? "=" + paramString : ""}`;
    }
    return "";
  };

  const hasErrors = Object.values(errors).some((error) => error !== "");
  const filter = predefinedFilters.find((f) => f.name === data.filterName);

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
      {/* Input handle - only show if not an input node and not already connected */}
      {data.filterType !== "input" && !isInputConnected && (
        <Handle
          type="target"
          position={Position.Left}
          style={{
            backgroundColor: "#555",
            width: "8px",
            height: "8px",
          }}
        />
      )}

      <Typography variant="h6" gutterBottom>
        {data.label}
      </Typography>
      {data.filterType === "filter" && (
        <Box sx={{ mt: 1 }}>
          {filter?.description && (
            <Typography
              variant="caption"
              color="text.secondary"
              sx={{ display: "block", mb: 1 }}
            >
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
                  onChange={(e) =>
                    handleParameterChange(param.name, e.target.value)
                  }
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

      {/* Output handle - only show if not an output node and not already connected */}
      {data.filterType !== "output" && !isOutputConnected && (
        <Handle
          type="source"
          position={Position.Right}
          style={{
            backgroundColor: "#555",
            width: "8px",
            height: "8px",
          }}
        />
      )}
    </Paper>
  );
}

export default memo(FilterNode);
