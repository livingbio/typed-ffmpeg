/**
 * Test utilities — no Pyodide needed after the TypeScript migration.
 *
 * setupPyodideMock is kept as a no-op so existing test files that call it
 * don't have to change their boilerplate imports.
 */

export function setupPyodideMock(): void {
  // No-op: Pyodide is no longer used.
}

export default { setupPyodideMock };
