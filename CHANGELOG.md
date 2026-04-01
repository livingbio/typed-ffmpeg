# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.0a2] - 2026-04-01

### Added

- **`parse()` in Python and TypeScript** — parse an FFmpeg CLI command string back into a typed filter graph (`ffmpeg -i in.mp4 -vf scale=1280:720 out.mp4` → DAG)
- **TypeScript `parse()`** in `@typed-ffmpeg/core` supporting `-i`, `-vf`, `-af`, `-filter_complex`, `-map`, global/output options, and pre-input options (`-ss`, `-t`)
- **Python `parse()`** parity across `typed-ffmpeg-v5`..`v8` and `ffmpeg-core`
- **Playground parse UI** — paste an FFmpeg command into the sidebar to import it as a visual graph
- **TypeScript playground** (`packages/playground`) with Vite + React + ReactFlow

### Fixed

- Python `parse()`: pre-input options (`-ss`, `-t`) were silently dropped
- Python `parse()`: O(n²) `-map` injection loop replaced with O(n) pass
- TypeScript browser bundle: `parse()` was missing from `index.browser.ts`

### Changed

- Playground E2E tests now use `vite preview` (pre-built static files) in CI for fast, reliable test runs

## [1.0.0a1] - 2026-03-25

Major rewrite: monorepo architecture with multi-version FFmpeg support.

### Added

- **Multi-version FFmpeg support** — separate packages for FFmpeg 5.x, 6.x, 7.x, and 8.x
- **Monorepo architecture** — split into `ffmpeg-core`, `typed-ffmpeg-v5`..`v8`, and `typed-ffmpeg` (latest)
- **Per-version cache data packages** (`ffmpeg-data-v5`..`v8`) for offline filter/codec metadata
- **Version-aware code generation** pipeline producing version-specific bindings
- **Texinfo parser** for enriching filter documentation from FFmpeg source docs
- **New CLI commands**: `generate --version-dir`, `diff`, `reexport`
- **Cross-version diff module** for migration hints between FFmpeg versions
- **CUDA toolkit support** in Docker builds for full CUDA filter coverage
- **Enhanced Docker builder** with Vulkan and plugin support

### Changed

- Package renamed from `typed-ffmpeg` (single package) to a monorepo with per-version packages
- Import paths updated for multi-version support
- Replaced pre-commit with [prek](https://github.com/9999years/prek) (2–10x faster)
- Switched to [uv](https://github.com/astral-sh/uv) package manager
- Improved `ffmpeg-core` test coverage from 74% to 92%
- Regenerated bindings for all supported FFmpeg versions

### Fixed

- FFmpeg 8.0 compatibility (unsigned types, array options, 2-char filter flags)
- Filters without docs no longer silently dropped during codegen
- Backward compatibility with 3.x API preserved where possible
- Docker runtime library dependencies for v7/v8

### Breaking Changes

- New package names: install `typed-ffmpeg` (latest) or `typed-ffmpeg-v8`, `typed-ffmpeg-v7`, etc.
- Shared runtime is now `ffmpeg-core` (installed automatically as a dependency)

## [3.11] - 2026-01-21

### Fixed

- Bool muxer option handling

## [3.10] - 2025-12-31

### Fixed

- Memory leak in ffprobe on subprocess timeout
- Runtime cache folder error with PyInstaller builds

## [3.9] - 2025-12-29

### Added

- Flexible sample format support

### Changed

- Test coverage improvements

## [3.8.2] - 2025-12-19

### Fixed

- Minor bug fixes and stability improvements

## [3.8.1] - 2025-12-07

### Fixed

- Patch release with bug fixes

## [3.8.0] - 2025-12-05

### Added

- AsyncIO subprocess support (`run_async_awaitable()`)
- Enhanced type checking with mypy

## [3.7.1] - 2025-10-17

### Fixed

- Patch release with bug fixes

## [3.7] - 2025-10-16

### Added

- JSON serialization of filter graphs
- Comprehensive filter documentation improvements
