# v4 Package Architecture

typed-ffmpeg v4 is a monorepo that publishes separate PyPI packages for each FFmpeg major version. This page explains the structure and how to choose the right package.

## Packages

| PyPI Package | FFmpeg Version | Install |
|---|---|---|
| `typed-ffmpeg` | Latest (v8) | `pip install typed-ffmpeg` |
| `typed-ffmpeg-v5` | FFmpeg 5.x | `pip install typed-ffmpeg-v5` |
| `typed-ffmpeg-v6` | FFmpeg 6.x | `pip install typed-ffmpeg-v6` |
| `typed-ffmpeg-v7` | FFmpeg 7.x | `pip install typed-ffmpeg-v7` |
| `typed-ffmpeg-v8` | FFmpeg 8.x | `pip install typed-ffmpeg-v8` |
| `ffmpeg-core` | (runtime, auto-installed) | — |

## Which Package Should I Install?

**For most users:** `pip install typed-ffmpeg` — this installs the latest bindings (currently v8) and receives updates automatically.

**For production deployments:** install the package that matches your system's FFmpeg version so the typed bindings match exactly what FFmpeg accepts.

```bash
# Check your FFmpeg version
ffmpeg -version | head -1
# ffmpeg version 6.1.1 ...

# Install the matching package
pip install typed-ffmpeg-v6
```

**For CI / testing across versions:** install multiple packages side-by-side (they coexist without conflicts).

## Package Dependency Graph

```
typed-ffmpeg (meta)
    └── typed-ffmpeg-v8
            └── ffmpeg-core

typed-ffmpeg-v5 ──┐
typed-ffmpeg-v6   ├── ffmpeg-core (shared runtime)
typed-ffmpeg-v7 ──┘
```

`ffmpeg-core` contains the hand-written runtime code (DAG, compiler, IR) and is installed automatically as a dependency of any `typed-ffmpeg-vX` package. You do not need to install it directly.

## Repository Structure

```
typed-ffmpeg/          # monorepo root
├── packages/
│   ├── core/          # ffmpeg-core: shared runtime
│   ├── v5/            # typed-ffmpeg-v5
│   ├── v6/            # typed-ffmpeg-v6
│   ├── v7/            # typed-ffmpeg-v7
│   ├── v8/            # typed-ffmpeg-v8
│   └── latest/        # typed-ffmpeg (meta, re-exports v8)
├── docs/
└── scripts/           # code generation tools
```

## Usage

All packages expose the same `ffmpeg` namespace — your code is identical regardless of which package you install:

```python
import ffmpeg

# Probe a file
info = ffmpeg.probe("video.mp4")

# Build and run a filter graph
(
    ffmpeg.input("input.mp4")
    .hflip()
    .output("output.mp4")
    .run()
)
```

See the [Usage section](usage/basic-api-usage.ipynb) for full examples.

## Migrating from typed-ffmpeg 3.x

See the [Migration Guide](migration/v3-to-v4.md).
