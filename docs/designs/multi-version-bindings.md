# Design: Multi-Version FFmpeg Typed Bindings

**Status:** APPROVED
**Date:** 2026-03-20
**Branch:** main
**Reviews:** Eng Review (CLEAR), CEO Review (CLEAR, SELECTIVE EXPANSION)

## Problem Statement

typed-ffmpeg ships typed bindings generated from a single FFmpeg version. Users running different FFmpeg versions (5.x, 6.x, 7.x, 8.x) get types that may not match their installed FFmpeg — filters, codecs, and options that don't exist in their version, or missing ones that do. Since the library's core value is IDE autocompletion and static type checking, this mismatch undermines the entire proposition.

## Approach

**Single package, version submodules.** Ship all versions inside `typed-ffmpeg` under version-namespaced modules. Default `ffmpeg.filters` points to latest via explicit re-exports. Users import from `ffmpeg.v6.filters` for version-specific types.

```python
# Default (latest FFmpeg)
from ffmpeg.filters import concat, overlay

# Version-specific
from ffmpeg.v6.filters import concat, overlay
```

## Architecture

```
src/ffmpeg/
├── v5/          # Generated for FFmpeg 5.x
│   ├── filters.py, streams/, codecs/, formats/, options/, dag/io/
│   └── py.typed
├── v6/          # Generated for FFmpeg 6.x
├── v7/          # Generated for FFmpeg 7.x
├── v8/          # Generated for FFmpeg 8.x
├── filters.py   # Explicit re-exports from latest (v8)
├── versions.py  # Available versions, default version
├── dag/         # Shared hand-written core
├── types.py     # Shared
├── schema.py    # Shared
└── common/      # Shared (cache, serialization)
```

**Key decisions (from eng review):**
1. Absolute imports for shared core (`from ffmpeg.dag.factory import ...`)
2. Thin explicit re-export modules at root level (no star imports)
3. All generated code moves into version dirs (including dag/io)
4. py.typed markers in each version directory
5. Cache files excluded from published package

**Key decisions (from CEO review):**
1. Sequential pipeline: load all version caches → compute diffs → generate all versions
2. Graceful degradation when partial version caches exist
3. New `version_diff.py` module for cross-version comparison logic
4. Minor version bump (not major) when multi-version ships

## Scope

### Core
- Modify `render()` to output to `src/ffmpeg/v{N}/`
- Fix import paths (relative → absolute for shared core)
- Create explicit re-export modules for default namespace
- Update `pyproject.toml` to include version subpackages
- Extract DRY helper for load_codecs/load_formats
- Add clear error messages for code gen pipeline failures
- Write import resolver tests before implementing

### Accepted Expansions
- **py.typed** marker files in each version submodule
- **ffmpeg.versions** module with `available()` and `default`
- **Per-version documentation** pages for mkdocs
- **Deprecation hints** in generated docstrings (cross-version annotations)
- **Migration CLI** command (`typed-ffmpeg diff v6 v7`)

### Deferred (TODOS.md)
- CI auto-generation matrix
- Schema deduplication (parse_help vs code_gen)

## Implementation Order

1. Write import resolver tests (version_prefix parameter)
2. Modify `get_relative_import()` to support absolute imports
3. Extract DRY helper for load_codecs/load_formats option conversion
4. Parameterize `render()` to output to `src/ffmpeg/v{N}/`
5. Update templates (`_components.jinja`) for version context
6. Create explicit re-export modules for root namespace
7. Add py.typed markers and versions.py module
8. Build version_diff.py for cross-version comparison
9. Add deprecation hints to template generation
10. Build migration CLI command
11. Generate per-version documentation pages
12. Update pyproject.toml, exclude cache from dist
13. Test IDE integration (VS Code, PyCharm, neovim)
14. Update README with version selection docs

## Success Criteria

- `from ffmpeg.v{N}.filters import X` provides correct autocompletion
- `from ffmpeg.filters import X` works via re-exports (latest)
- mypy strict mode passes on both import paths
- Pre-generated bindings for FFmpeg 5.x, 6.x, 7.x, 8.x in single package
- `typed-ffmpeg diff v6 v7` shows filter/codec changes
- Per-version docs pages generated
