import type { Edge, Node } from "reactflow";

export function generateFFmpegCommand(nodes: Node[], edges: Edge[]): { python: string } {
  // Find all input and output nodes
  const inputNodes = nodes.filter((n) => n.data.filterType === "input");
  const outputNodes = nodes.filter((n) => n.data.filterType === "output");

  if (inputNodes.length === 0 || outputNodes.length === 0) {
    return {
      python: "",
    };
  }

  // Generate Python code
  let pythonCode = "import ffmpeg\n\n";

  // Create input streams
  const inputStreams = inputNodes.map((_node, index) => {
    return `input${index} = ffmpeg.input("input${index}.mp4")`;
  });

  pythonCode += `${inputStreams.join("\n")}\n\n`;

  // Track processed streams by node ID
  const nodeStreams: Record<string, string> = {};

  // Initialize with input streams
  inputNodes.forEach((node, index) => {
    nodeStreams[node.id] = `input${index}`;
  });

  // Process each input node's filter chain
  inputNodes.forEach((inputNode) => {
    // Find all edges starting from this input
    const inputEdges = edges.filter((e) => e.source === inputNode.id);

    // Process each branch from the input
    inputEdges.forEach((edge) => {
      let currentId = edge.target;
      let currentStream = nodeStreams[inputNode.id];

      while (true) {
        const nextNode = nodes.find((n) => n.id === currentId);
        if (!nextNode || nextNode.data.filterType !== "filter") break;

        if (nextNode.data.filterType === "filter" && nextNode.data.filterName) {
          const filterName = nextNode.data.filterName;
          const parameters = (nextNode.data.parameters as Record<string, string>) || {};

          // Convert parameters to Python kwargs
          const kwargs = Object.entries(parameters)
            .filter(([, value]) => value !== "")
            .map(([key, value]) => {
              // Handle numeric values without quotes
              if (!Number.isNaN(Number(value))) {
                return `${key}=${value}`;
              }
              // Handle boolean values
              if (value.toLowerCase() === "true" || value.toLowerCase() === "false") {
                return `${key}=${value.toLowerCase()}`;
              }
              // Handle string values with quotes
              return `${key}="${value}"`;
            })
            .join(", ");

          // Create a new variable for the processed stream with valid Python identifier
          const nodeId = nextNode.id.replace(/-/g, "_");
          const newStreamName = `stream_${nodeId}`;
          pythonCode += `${newStreamName} = ${currentStream}.${filterName}(${kwargs})\n`;
          nodeStreams[nextNode.id] = newStreamName;
          currentStream = newStreamName;
        }

        // Find the next edge in this branch
        const nextEdge = edges.find((e) => e.source === currentId);
        if (!nextEdge) break;
        currentId = nextEdge.target;
      }
    });
  });

  pythonCode += "\n";

  // Create output streams
  outputNodes.forEach((node, index) => {
    // Find all streams that connect to this output
    const connectedStreams = edges
      .filter((edge) => edge.target === node.id)
      .map((edge) => {
        const sourceNode = nodes.find((n) => n.id === edge.source);
        if (!sourceNode) return null;
        return nodeStreams[sourceNode.id];
      })
      .filter((stream): stream is string => stream !== null);

    if (connectedStreams.length > 0) {
      pythonCode += `output${index} = ffmpeg.output(${connectedStreams.join(", ")}, filename="output${index}.mp4")\n`;
    }
  });

  pythonCode += "\n";

  // Add compile line
  pythonCode += "# Compile the command\n";
  const validOutputs = outputNodes
    .map((node, index) => {
      const hasConnections = edges.some((edge) => edge.target === node.id);
      return hasConnections ? `output${index}` : null;
    })
    .filter((output): output is string => output !== null);

  if (validOutputs.length > 1) {
    pythonCode += `ffmpeg.merge_outputs(${validOutputs.join(", ")}).compile_line()`;
  } else if (validOutputs.length === 1) {
    pythonCode += `${validOutputs[0]}.compile_line()`;
  } else {
    pythonCode += "# No valid outputs to compile";
  }

  return {
    python: pythonCode,
  };
}
