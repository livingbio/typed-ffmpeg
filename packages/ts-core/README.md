# @typed-ffmpeg/core

Core runtime for typed-ffmpeg TypeScript bindings.

Provides the DAG model, compilation pipeline, validation, and execution utilities for building type-safe FFmpeg filter graphs in TypeScript.

## Installation

```bash
npm install @typed-ffmpeg/core
```

This package is automatically installed as a dependency of the version-specific packages (`@typed-ffmpeg/v5` through `@typed-ffmpeg/v8`). Most users should install a version package directly rather than using `@typed-ffmpeg/core` alone.

## Builds

Three builds are shipped, selected automatically via the `exports` field:

- **CJS** — `dist/index.js` (Node.js default)
- **ESM** — `dist/esm/index.js` (Node.js ESM)
- **Browser** — `dist/browser/index.browser.js` (browser-safe ESM)

## Key Exports

- `InputNode`, `OutputNode`, `FilterNode` — DAG node types
- `VideoStream`, `AudioStream`, `AVStream` — Stream types
- `compile()`, `compileAsList()` — Compile filter graphs to FFmpeg arguments
- `validate()`, `fixGraph()` — Validate and auto-correct filter graphs
- `run()`, `runAsync()` — Execute FFmpeg commands
- `StreamType` — Enum for stream types (Video, Audio)

See the [TypeScript documentation](https://livingbio.github.io/typed-ffmpeg/typescript/) for usage examples.
