import React from 'react';
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import FFmpegFlowEditor from './components/FFmpegFlowEditor';

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <FFmpegFlowEditor />
    </ThemeProvider>
  );
}

export default App;
