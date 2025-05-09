import { memo, useState } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, useTheme } from '@mui/material';
import { EdgeType, EDGE_COLORS } from '../types/edge';
import { OutputNodeData } from '../types/node';

function OutputNode({ data }: NodeProps<OutputNodeData>) {
  const theme = useTheme();
  const [filename, setFilename] = useState<string>(data.filename);

  return (
    <Paper 
      elevation={3} 
      sx={{ 
        width: '100%',
        height: '100%',
        boxSizing: 'border-box',
        padding: 2, 
        backgroundColor: theme.palette.background.paper,
        border: `1px solid ${theme.palette.divider}`,
        color: theme.palette.text.primary,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'stretch',
      }}
    >
      <Typography variant="h6" gutterBottom>
        {data.label}
      </Typography>
      
      <TextField
        label="Filename"
        value={filename}
        onChange={(e) => setFilename(e.target.value)}
        fullWidth
        margin="normal"
        size="small"
      />

      {/* Input handle */}
      <Handle
        type="target"
        position={Position.Left}
        id={data.handles.inputs[0].id}
        style={{
          backgroundColor: EDGE_COLORS[data.handles.inputs[0].type],
          width: '10px',
          height: '10px',
          border: '2px solid #fff',
        }}
      />
    </Paper>
  );
}

export default memo(OutputNode); 