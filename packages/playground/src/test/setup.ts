import '@testing-library/jest-dom';

// ResizeObserver is not available in jsdom; provide a no-op stub so MUI
// components that measure their containers don't crash during tests.
if (typeof ResizeObserver === 'undefined') {
  global.ResizeObserver = class {
    observe() {}
    unobserve() {}
    disconnect() {}
  };
}
