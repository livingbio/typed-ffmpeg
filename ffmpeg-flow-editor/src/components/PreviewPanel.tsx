import { Box, Typography, Button } from "@mui/material";
import { Node, Edge } from "reactflow";
import { FFmpegCommand } from "../types/ffmpeg";
import { useState, useEffect } from "react";

// Add type declarations for Pyodide
declare global {
  interface Window {
    loadPyodide: (options: { indexURL: string }) => Promise<{
      runPythonAsync: (code: string) => Promise<string>;
      loadPackage: (packageName: string) => Promise<void>;
    }>;
  }
}

interface PreviewPanelProps {
  nodes: Node[];
  edges: Edge[];
}

function generateFFmpegCommand(
  nodes: Node[],
  edges: Edge[]
): { ffmpeg: FFmpegCommand; python: string } {
  const inputNode = nodes.find((n) => n.data.filterType === "input");
  const outputNode = nodes.find((n) => n.data.filterType === "output");
  const filterNodes = nodes.filter((n) => n.data.filterType === "filter");

  if (!inputNode || !outputNode) {
    return {
      ffmpeg: {
        input: "",
        output: "",
        filters: "",
        options: [],
      },
      python: "",
    };
  }

  // Build filter chain
  const filterChain: string[] = [];
  const padNames: Record<string, string> = {};
  let padCounter = 0;

  // Assign pad names to each node
  nodes.forEach((node) => {
    if (node.data.filterType === "filter") {
      padNames[node.id] = `[${padCounter++}]`;
    }
  });

  // Build filter string for each node
  filterNodes.forEach((node) => {
    const filterString = node.data.filterString || "";
    if (filterString) {
      filterChain.push(`${padNames[node.id]}${filterString}`);
    }
  });

  // Connect pads based on edges
  edges.forEach((edge) => {
    const sourceNode = nodes.find((n) => n.id === edge.source);
    const targetNode = nodes.find((n) => n.id === edge.target);
    if (sourceNode && targetNode) {
      const sourcePad =
        sourceNode.data.filterType === "input"
          ? "[0:v]"
          : padNames[sourceNode.id];
      const targetPad =
        targetNode.data.filterType === "output"
          ? "[outv]"
          : padNames[targetNode.id];
      filterChain.push(`${sourcePad}${targetPad}`);
    }
  });

  // Generate Python code
  let pythonCode = "import ffmpeg\n\n";
  pythonCode += '(ffmpeg.input("input.mp4")\n';

  // Sort filter nodes based on edges to maintain correct order
  const sortedFilterNodes: Node[] = [];
  let currentId = inputNode.id;

  while (true) {
    const edge = edges.find((e) => e.source === currentId);
    if (!edge) break;

    const nextNode = nodes.find((n) => n.id === edge.target);
    if (!nextNode || nextNode.data.filterType !== "filter") break;

    sortedFilterNodes.push(nextNode);
    currentId = nextNode.id;
  }

  // Add filters in order
  sortedFilterNodes.forEach((node) => {
    if (node.data.filterType === "filter" && node.data.filterName) {
      const filterName = node.data.filterName;
      const parameters = (node.data.parameters as Record<string, string>) || {};

      // Convert parameters to Python kwargs
      const kwargs = Object.entries(parameters)
        .filter(([, value]) => value !== "")
        .map(([key, value]) => {
          // Handle numeric values without quotes
          if (!isNaN(Number(value))) {
            return `${key}=${value}`;
          }
          // Handle boolean values
          if (
            value.toLowerCase() === "true" ||
            value.toLowerCase() === "false"
          ) {
            return `${key}=${value.toLowerCase()}`;
          }
          // Handle string values with quotes
          return `${key}="${value}"`;
        })
        .join(", ");

      pythonCode += `    .${filterName}(${kwargs})\n`;
    }
  });

  // Add output
  pythonCode += '    .output(filename="output.mp4")\n';
  pythonCode += "    .compile_line())";

  return {
    ffmpeg: {
      input: "input.mp4",
      output: "output.mp4",
      filters: filterChain.join(";"),
      options: ["-c:v libx264", "-preset medium", "-crf 23"],
    },
    python: pythonCode,
  };
}

export default function PreviewPanel({ nodes, edges }: PreviewPanelProps) {
  const [previewData, setPreviewData] = useState<{
    ffmpeg: FFmpegCommand;
    python: string;
  }>({
    ffmpeg: {
      input: "",
      output: "",
      filters: "",
      options: [],
    },
    python: "",
  });

  const [pyodide, setPyodide] = useState<Awaited<
    ReturnType<typeof window.loadPyodide>
  > | null>(null);
  const [result, setResult] = useState<string>("");
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    async function loadPyodide() {
      try {
        setIsLoading(true);
        const pyodide = await window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.1/full/",
        });
        await pyodide.loadPackage("micropip");
        await pyodide.runPythonAsync(`
          import micropip
          await micropip.install('typed-ffmpeg')
        `);
        setPyodide(pyodide);
      } catch (error) {
        console.error("Failed to load Pyodide:", error);
        setResult("Failed to load Python environment");
      } finally {
        setIsLoading(false);
      }
    }
    loadPyodide();
  }, []);

  useEffect(() => {
    const newData = generateFFmpegCommand(nodes, edges);
    setPreviewData(newData);
  }, [nodes, edges]);

  const handleCopy = (type: "ffmpeg" | "python") => {
    const textToCopy =
      type === "ffmpeg"
        ? `ffmpeg -i ${previewData.ffmpeg.input} -filter_complex "${
            previewData.ffmpeg.filters
          }" ${previewData.ffmpeg.options.join(" ")} ${
            previewData.ffmpeg.output
          }`
        : previewData.python;
    navigator.clipboard.writeText(textToCopy);
  };

  const handleRunPython = async () => {
    if (!pyodide) {
      setResult("Python environment not loaded");
      return;
    }

    try {
      setIsLoading(true);
      const output = await pyodide.runPythonAsync(previewData.python);
      setResult(output.toString());
    } catch (error) {
      console.error("Python execution error:", error);
      setResult(
        `Error: ${error instanceof Error ? error.message : String(error)}`
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Box>
      {/* FFmpeg Command */}
      <Box sx={{ mb: 3 }}>
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            mb: 1,
          }}
        >
          <Typography variant="subtitle2">FFmpeg Command</Typography>
          <Button
            variant="outlined"
            size="small"
            onClick={() => handleCopy("ffmpeg")}
          >
            Copy
          </Button>
        </Box>
        <Box
          sx={{
            p: 1.5,
            backgroundColor: "#f5f5f5",
            borderRadius: 1,
          }}
        >
          <pre
            style={{
              margin: 0,
              padding: 0,
              fontFamily: "monospace",
              fontSize: "0.875rem",
              lineHeight: 1.5,
              whiteSpace: "pre-wrap",
              wordBreak: "break-word",
            }}
          >
            {`ffmpeg -i ${previewData.ffmpeg.input} -filter_complex "${
              previewData.ffmpeg.filters
            }" ${previewData.ffmpeg.options.join(" ")} ${
              previewData.ffmpeg.output
            }`}
          </pre>
        </Box>
      </Box>

      {/* Python Code */}
      <Box sx={{ mb: 3 }}>
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            mb: 1,
          }}
        >
          <Typography variant="subtitle2">Python Code</Typography>
          <Box>
            <Button
              variant="outlined"
              size="small"
              onClick={() => handleCopy("python")}
              sx={{ mr: 1 }}
            >
              Copy
            </Button>
            <Button
              variant="contained"
              size="small"
              onClick={handleRunPython}
              disabled={isLoading || !pyodide}
            >
              {isLoading ? "Running..." : "Run"}
            </Button>
          </Box>
        </Box>
        <Box
          sx={{
            p: 1.5,
            backgroundColor: "#f5f5f5",
            borderRadius: 1,
          }}
        >
          <pre
            style={{
              margin: 0,
              padding: 0,
              fontFamily: "monospace",
              fontSize: "0.875rem",
              lineHeight: 1.5,
              whiteSpace: "pre-wrap",
              wordBreak: "break-word",
            }}
          >
            {previewData.python}
          </pre>
        </Box>
      </Box>

      {/* Result */}
      {result && (
        <Box>
          <Typography variant="subtitle2" sx={{ mb: 1 }}>
            Result
          </Typography>
          <Box
            sx={{
              p: 1.5,
              backgroundColor: "#f5f5f5",
              borderRadius: 1,
            }}
          >
            <pre
              style={{
                margin: 0,
                padding: 0,
                fontFamily: "monospace",
                fontSize: "0.875rem",
                lineHeight: 1.5,
                whiteSpace: "pre-wrap",
                wordBreak: "break-word",
              }}
            >
              {result}
            </pre>
          </Box>
        </Box>
      )}
    </Box>
  );
}
