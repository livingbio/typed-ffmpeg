import { Box, Paper, Typography, Button } from '@mui/material';
import { Node, Edge } from 'reactflow';
import { FFmpegCommand } from '@/types/ffmpeg';

interface PreviewPanelProps {
  nodes: Node[];
  edges: Edge[];
}

function generateFFmpegCommand(nodes: Node[], edges: Edge[]): FFmpegCommand {
  const inputNode = nodes.find(n => n.data.filterType === 'input');
  const outputNode = nodes.find(n => n.data.filterType === 'output');
  const filterNodes = nodes.filter(n => n.data.filterType === 'filter');

  if (!inputNode || !outputNode) {
    return {
      input: '',
      output: '',
      filters: '',
      options: [],
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

  return {
    input: 'input.mp4',
    output: 'output.mp4',
    filters: filterChain.join(';'),
    options: ['-c:v libx264', '-preset medium', '-crf 23'],
  };
}

export default function PreviewPanel({ nodes, edges }: PreviewPanelProps) {
  const command = generateFFmpegCommand(nodes, edges);

  const handleCopy = () => {
    const fullCommand = `ffmpeg -i ${command.input} -filter_complex "${command.filters}" ${command.options.join(' ')} ${command.output}`;
    navigator.clipboard.writeText(fullCommand);
  };

  return (
    <Paper
      elevation={3}
      sx={{
        position: 'absolute',
        bottom: 20,
        right: 20,
        padding: 2,
        maxWidth: 600,
        backgroundColor: '#fff',
      }}
    >
      <Typography variant="h6" gutterBottom>
        FFmpeg Command Preview
      </Typography>
      <Box sx={{ mb: 2 }}>
        <Typography variant="body2" color="text.secondary">
          Input: {command.input}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Output: {command.output}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Filter Complex: {command.filters}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Options: {command.options.join(' ')}
        </Typography>
      </Box>
      <Button
        variant="contained"
        size="small"
        onClick={handleCopy}
      >
        Copy Command
      </Button>
    </Paper>
  );
}
