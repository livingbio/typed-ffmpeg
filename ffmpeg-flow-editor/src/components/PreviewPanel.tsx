import { Box, Paper, Typography, Button, Tabs, Tab } from '@mui/material';
import { Node, Edge } from 'reactflow';
import { FFmpegCommand } from '../types/ffmpeg';
import { useState, useEffect } from 'react';

interface PreviewPanelProps {
  nodes: Node[];
  edges: Edge[];
}

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`preview-tabpanel-${index}`}
      aria-labelledby={`preview-tab-${index}`}
      {...other}
      style={{ display: value === index ? 'block' : 'none' }}
    >
      <Box sx={{ p: 3 }}>
        {children}
      </Box>
    </div>
  );
}

function generateFFmpegCommand(nodes: Node[], edges: Edge[]): { ffmpeg: FFmpegCommand; python: string } {
  const inputNode = nodes.find(n => n.data.filterType === 'input');
  const outputNode = nodes.find(n => n.data.filterType === 'output');
  const filterNodes = nodes.filter(n => n.data.filterType === 'filter');

  if (!inputNode || !outputNode) {
    return {
      ffmpeg: {
        input: '',
        output: '',
        filters: '',
        options: [],
      },
      python: '',
    };
  }

  // Build filter chain
  const filterChain: string[] = [];
  const padNames: Record<string, string> = {};
  let padCounter = 0;

  // Assign pad names to each node
  nodes.forEach(node => {
    if (node.data.filterType === 'filter') {
      padNames[node.id] = `[${padCounter++}]`;
    }
  });

  // Build filter string for each node
  filterNodes.forEach(node => {
    const filterString = node.data.filterString || '';
    if (filterString) {
      filterChain.push(`${padNames[node.id]}${filterString}`);
    }
  });

  // Connect pads based on edges
  edges.forEach(edge => {
    const sourceNode = nodes.find(n => n.id === edge.source);
    const targetNode = nodes.find(n => n.id === edge.target);
    if (sourceNode && targetNode) {
      const sourcePad = sourceNode.data.filterType === 'input' ? '[0:v]' : padNames[sourceNode.id];
      const targetPad = targetNode.data.filterType === 'output' ? '[outv]' : padNames[targetNode.id];
      filterChain.push(`${sourcePad}${targetPad}`);
    }
  });

  // Generate Python code
  let pythonCode = 'import ffmpeg\n\n';
  pythonCode += 'ffmpeg.input("input.mp4")\n';

  // Sort filter nodes based on edges to maintain correct order
  const sortedFilterNodes: Node[] = [];
  let currentId = inputNode.id;

  while (true) {
    const edge = edges.find(e => e.source === currentId);
    if (!edge) break;

    const nextNode = nodes.find(n => n.id === edge.target);
    if (!nextNode || nextNode.data.filterType !== 'filter') break;

    sortedFilterNodes.push(nextNode);
    currentId = nextNode.id;
  }

  // Add filters in order
  sortedFilterNodes.forEach(node => {
    if (node.data.filterType === 'filter' && node.data.filterName) {
      const filterName = node.data.filterName;
      const parameters = node.data.parameters as Record<string, string> || {};

      // Convert parameters to Python kwargs
      const kwargs = Object.entries(parameters)
        .filter(([_, value]) => value !== '')
        .map(([key, value]) => {
          // Handle numeric values without quotes
          if (!isNaN(Number(value))) {
            return `${key}=${value}`;
          }
          // Handle boolean values
          if (value.toLowerCase() === 'true' || value.toLowerCase() === 'false') {
            return `${key}=${value.toLowerCase()}`;
          }
          // Handle string values with quotes
          return `${key}="${value}"`;
        })
        .join(', ');

      pythonCode += `    .${filterName}(${kwargs})\n`;
    }
  });

  // Add output
  pythonCode += '    .output("output.mp4")\n';
  pythonCode += '    .run()';

  return {
    ffmpeg: {
      input: 'input.mp4',
      output: 'output.mp4',
      filters: filterChain.join(';'),
      options: ['-c:v libx264', '-preset medium', '-crf 23'],
    },
    python: pythonCode,
  };
}

export default function PreviewPanel({ nodes, edges }: PreviewPanelProps) {
  const [tabValue, setTabValue] = useState(0);
  const [previewData, setPreviewData] = useState<{ ffmpeg: FFmpegCommand; python: string }>({
    ffmpeg: {
      input: '',
      output: '',
      filters: '',
      options: [],
    },
    python: '',
  });

  useEffect(() => {
    const newData = generateFFmpegCommand(nodes, edges);
    setPreviewData(newData);
  }, [nodes, edges]);

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  const handleCopy = () => {
    const textToCopy = tabValue === 0
      ? `ffmpeg -i ${previewData.ffmpeg.input} -filter_complex "${previewData.ffmpeg.filters}" ${previewData.ffmpeg.options.join(' ')} ${previewData.ffmpeg.output}`
      : previewData.python;
    navigator.clipboard.writeText(textToCopy);
  };

  return (
    <Paper
      elevation={3}
      sx={{
        position: 'fixed',
        bottom: 20,
        right: 20,
        maxWidth: 600,
        width: '100%',
        backgroundColor: '#fff',
        zIndex: 1000,
      }}
    >
      <Tabs
        value={tabValue}
        onChange={handleTabChange}
        sx={{
          borderBottom: 1,
          borderColor: 'divider',
        }}
      >
        <Tab label="FFmpeg Command" />
        <Tab label="Python Code" />
      </Tabs>

      <TabPanel value={tabValue} index={0}>
        <Typography variant="h6" gutterBottom>
          FFmpeg Command Preview
        </Typography>
        <Box sx={{ mb: 2 }}>
          <Typography variant="body2" color="text.secondary">
            Input: {previewData.ffmpeg.input}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Output: {previewData.ffmpeg.output}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Filter Complex: {previewData.ffmpeg.filters}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Options: {previewData.ffmpeg.options.join(' ')}
          </Typography>
        </Box>
      </TabPanel>

      <TabPanel value={tabValue} index={1}>
        <Typography variant="h6" gutterBottom>
          Python Code Preview
        </Typography>
        <Box sx={{ mb: 2 }}>
          <pre style={{
            backgroundColor: '#f5f5f5',
            padding: '1rem',
            borderRadius: '4px',
            overflow: 'auto',
            whiteSpace: 'pre-wrap',
            fontFamily: 'monospace'
          }}>
            {previewData.python}
          </pre>
        </Box>
      </TabPanel>

      <Box sx={{ p: 2, display: 'flex', justifyContent: 'flex-end' }}>
        <Button
          variant="contained"
          size="small"
          onClick={handleCopy}
        >
          Copy {tabValue === 0 ? 'Command' : 'Code'}
        </Button>
      </Box>
    </Paper>
  );
}
