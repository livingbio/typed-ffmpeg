import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import FFmpegFlowEditor from './components/FFmpegFlowEditor';
import 'reactflow/dist/style.css';

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
