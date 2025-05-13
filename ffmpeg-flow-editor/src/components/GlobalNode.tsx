import { memo } from 'react';
import { Handle, Position, NodeProps } from 'reactflow';
import { Paper, Typography, useTheme } from '@mui/material';
import { EDGE_COLORS } from '../types/edge';
import { NodeData } from '../types/node';
function GlobalNode({ data }: NodeProps<NodeData>) {
  const theme = useTheme();

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

      {/* Input handles */}
      {data.handles.inputs.map((handle, index) => (
        <Handle
          key={handle.id}
          type="target"
          position={Position.Left}
          id={handle.id}
          style={{
            backgroundColor: EDGE_COLORS[handle.type],
            width: '10px',
            height: '10px',
            border: '2px solid #fff',
            top: `${(index + 1) * (100 / (data.handles.inputs.length + 1))}%`,
          }}
        />
      ))}
    </Paper>
  );
}

export default memo(GlobalNode); 