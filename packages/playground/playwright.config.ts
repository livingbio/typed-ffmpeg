import { defineConfig, devices } from '@playwright/test';

const isCI = !!process.env.CI;
// In CI: serve pre-built static files via `vite preview` (port 4173).
// Locally: use the dev server (port 5173) with hot-reload.
const serverPort = isCI ? 4173 : 5173;
const serverCommand = isCI ? 'npm run preview' : 'npm run dev';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: isCI,
  retries: isCI ? 2 : 0,
  workers: isCI ? 1 : undefined,
  reporter: 'html',
  expect: {
    timeout: 15000,
  },
  use: {
    baseURL: `http://localhost:${serverPort}`,
    trace: 'on-first-retry',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
  webServer: {
    command: serverCommand,
    url: `http://localhost:${serverPort}/typed-ffmpeg/typed-ffmpeg-playground/`,
    reuseExistingServer: !isCI,
    timeout: 120 * 1000,
  },
});
