import React from 'react';
import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import FFmpegFlowEditor from './components/FFmpegFlowEditor';

/**
 * Default theme for the application using Material-UI
 */
const theme = createTheme();

/**
 * Root component for the FFmpeg Flow Editor application
 * Sets up theming and renders the main editor component
 * 
 * @returns {JSX.Element} The rendered application
 */
function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <FFmpegFlowEditor />
    </ThemeProvider>
  );
}

export default App;
