import { memo, useState } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, TextField, useTheme } from '@mui/material';
import { EDGE_COLORS } from '../types/edge';
import { NodeData } from '../types/node';

function OutputNode({ data }: NodeProps<NodeData>) {
  const theme = useTheme();
  const [filename, setFilename] = useState<string>(data.filename || '');

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

      {/* Input handles */}
      {data.handles.inputs.map((handle, index) => (
        <Handle
          key={handle.id}
          type="target"
          position={Position.Left}
          id={`input-${index}`}
          style={{
            backgroundColor: EDGE_COLORS[handle.type],
            width: '10px',
            height: '10px',
            border: '2px solid #fff',
            top: `${(index + 1) * (100 / (data.handles.inputs.length + 1))}%`,
          }}
        />
      ))}
      {/* Output handle */}
      <Handle
        type="source"
        position={Position.Right}
        id={data.handles.outputs[0].id}
        style={{
          backgroundColor: EDGE_COLORS[data.handles.outputs[0].type],
          width: '10px',
          height: '10px',
          border: '2px solid #fff',
        }}
      />
    </Paper>
  );
}

export default memo(OutputNode); 