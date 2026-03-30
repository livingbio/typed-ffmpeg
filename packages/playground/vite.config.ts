import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Stub `child_process` imports from @typed-ffmpeg/core's run utilities.
// The playground generates FFmpeg commands but never executes them, so
// Node.js-only modules are not needed and should be stubbed out.
// Vite v8 uses Rolldown for both optimizeDeps pre-bundling and production builds,
// so this single plugin covers both dev and production.
function stubNodeBuiltinsPlugin() {
  const CHILD_PROCESS_STUB = `
export const execFileSync = () => { throw new Error('execFileSync is not available in the browser'); };
export const spawn = () => { throw new Error('spawn is not available in the browser'); };
export default { execFileSync, spawn };
`;
  return {
    name: 'stub-node-builtins',
    enforce: 'pre' as const,
    resolveId(id: string) {
      if (id === 'child_process') return '\0stub:child_process';
    },
    load(id: string) {
      if (id === '\0stub:child_process') return CHILD_PROCESS_STUB;
    },
  };
}

// https://vitejs.dev/config/
export default defineConfig({
  base: '/typed-ffmpeg/typed-ffmpeg-playground/',
  plugins: [stubNodeBuiltinsPlugin(), react()],
  optimizeDeps: {
    include: ['@typed-ffmpeg/core'],
  },
  resolve: {
    alias: {
      '@': '/src',
    },
  },
  server: {
    host: true,
    port: 5173,
    strictPort: true,
  },
  build: {
    assetsDir: 'assets',
    rollupOptions: {
      output: {
        assetFileNames: 'assets/[name]-[hash][extname]',
        chunkFileNames: 'assets/[name]-[hash].js',
        entryFileNames: 'assets/[name]-[hash].js',
      },
    },
  },
});
