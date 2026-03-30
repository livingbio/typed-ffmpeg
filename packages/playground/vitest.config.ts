import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'jsdom',
    include: ['src/**/*.{test,spec}.{js,jsx,ts,tsx}'],
    globals: true,
    testTimeout: 30000,
    coverage: {
      provider: 'istanbul',
      reporter: ['text', 'json', 'html', 'lcov'],
      reportsDirectory: './coverage',
      exclude: [
        'node_modules/',
        'src/scripts/',
        '**/types/*.ts',
        '**/vite.config.ts',
        '**/vitest.config.ts',
      ],
    },
  },
});
