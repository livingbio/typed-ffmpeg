import React from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import MinimalFlowEditor from './components/MinimalFlowEditor';

const theme = createTheme({
  palette: {
    mode: 'dark',
  },
});

const App: React.FC = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <MinimalFlowEditor />
    </ThemeProvider>
  );
};

export default App;
