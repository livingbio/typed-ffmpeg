# TODOS

## Multi-Version Support Follow-ups

### Schema Deduplication (parse_help vs code_gen)
**What:** Unify or create explicit adapters between the two parallel schema hierarchies — `parse_help.schema.FFMpegAVOption` and `code_gen.schema.FFMpegAVOption`.
**Why:** Both define similar dataclasses with different fields, causing conversion overhead in cli.py (the ~38-line option-wrapping blocks). A unified schema or adapter pattern would reduce confusion and the DRY violations.
**Pros:** Cleaner pipeline, less conversion code, easier to extend.
**Cons:** Refactoring risk — both schemas are load-bearing. Needs careful testing.
**Context:** The `load_codecs()` and `load_formats()` functions in cli.py contain nearly identical conversion blocks. The DRY helper extraction (decided in eng review) partially addresses this, but the root cause is the dual schema hierarchy.
**Depends on:** Nothing — can be done independently.

### Root-Level Re-Export Modules
**What:** Generate thin re-export modules at root (`ffmpeg/filters.py`) that forward symbols from the default version submodule (`ffmpeg/v8/filters.py`).
**Why:** Allows `from ffmpeg.filters import X` to automatically track the latest version without users changing imports.
**Status:** DEFERRED — the `reexport` CLI command exists but causes class identity issues: `ffmpeg.v8.streams.video.VideoStream` is not the same class as `ffmpeg.streams.video.VideoStream`, breaking `isinstance` checks in `validate.py` and `serialize.py`'s `CLASS_REGISTRY`. Needs a shared base class or registry unification before this can work.
**Depends on:** Resolving the class identity problem between root and version-specific stream types.

## Completed

### CI Auto-Generation Matrix ✓
Implemented in `.github/workflows/ci-codegen-versions.yml`. Tests code-gen against FFmpeg 5, 6, 7 using Docker images. Triggers on push/PR to main when codegen files change, plus manual dispatch.

### Version Diff Tooling ✓
Implemented in `src/scripts/code_gen/version_diff.py` with `diff` CLI command and `build_version_metadata()` for cross-version docstring annotations.

### Deprecation Hints ✓
Generated docstrings include "New in FFmpeg X.0" and "Removed in FFmpeg X.0" notes based on cross-version metadata.

### Pre-Generated Bindings ✓
Typed bindings for FFmpeg 5.x, 6.x, 7.x, 8.x committed under `src/ffmpeg/v{5,6,7,8}/`.
