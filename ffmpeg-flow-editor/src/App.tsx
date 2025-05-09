import React from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import FFmpegFlowEditor from './components/FFmpegFlowEditor';

const theme = createTheme({
  palette: {
    mode: 'light',
  },
});

const App: React.FC = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <FFmpegFlowEditor />
    </ThemeProvider>
  );
};

export default App;
