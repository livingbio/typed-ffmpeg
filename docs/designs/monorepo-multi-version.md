# Design: Monorepo Architecture for Multi-Version FFmpeg

**Status:** PROPOSED  
**Date:** 2026-03-21  
**Supersedes:** multi-version-bindings.md  

## Problem Statement

The current "single package with all versions" approach has several issues:

1. **Package Size**: Single package contains all versions (v5, v6, v7, v8), resulting in >10MB download
2. **Class Identity**: Having multiple versions in one package creates class identity problems
3. **User Experience**: Users running FFmpeg 6.x must download v5, v7, v8 code they don't need
4. **Semantic Versioning**: Package version doesn't match FFmpeg version

## Solution: Monorepo with Separate Packages

**One repository, multiple packages.** Each FFmpeg version gets its own PyPI package. Shared code lives in a core package.

```bash
# Users install only what they need
pip install typed-ffmpeg-v6  # For FFmpeg 6.x (~2MB)
pip install typed-ffmpeg-v8  # For FFmpeg 8.x (~2MB)
pip install typed-ffmpeg     # Latest (installs v8)
```

## Architecture

### Repository Structure

```
typed-ffmpeg/  (monorepo)
├── pyproject.toml              # Workspace configuration
├── uv.lock                     # Shared lock file
├── README.md                   # Main README
│
├── packages/
│   ├── core/                   # Shared core runtime
│   │   ├── pyproject.toml      # name: ffmpeg-core
│   │   ├── README.md
│   │   └── src/
│   │       └── ffmpeg_core/
│   │           ├── dag/        # DAG layer (hand-written)
│   │           ├── compile/    # Compilation (hand-written)
│   │           ├── common/     # Common utilities
│   │           ├── ir/         # IR layer
│   │           └── schema.py   # Shared schemas
│   │
│   ├── v5/                     # FFmpeg 5.x bindings
│   │   ├── pyproject.toml      # name: typed-ffmpeg-v5
│   │   ├── README.md
│   │   └── src/
│   │       └── ffmpeg/
│   │           ├── filters.py  # Generated
│   │           ├── sources.py  # Generated
│   │           ├── streams/    # Generated
│   │           ├── codecs/     # Generated
│   │           └── formats/    # Generated
│   │
│   ├── v6/                     # FFmpeg 6.x bindings
│   │   ├── pyproject.toml      # name: typed-ffmpeg-v6
│   │   └── src/ffmpeg/
│   │
│   ├── v7/                     # FFmpeg 7.x bindings
│   │   ├── pyproject.toml      # name: typed-ffmpeg-v7
│   │   └── src/ffmpeg/
│   │
│   ├── v8/                     # FFmpeg 8.x bindings
│   │   ├── pyproject.toml      # name: typed-ffmpeg-v8
│   │   └── src/ffmpeg/
│   │
│   └── latest/                 # Main package (alias to latest)
│       ├── pyproject.toml      # name: typed-ffmpeg
│       ├── README.md
│       └── src/
│           └── ffmpeg/
│               └── __init__.py # Re-exports from typed-ffmpeg-v8
│
└── tools/                      # Development tools
    ├── codegen/                # Code generator
    └── version_diff/           # Version comparison CLI
```

### Package Dependencies

```
typed-ffmpeg (latest package)
    ↓ depends on
typed-ffmpeg-v8
    ↓ depends on
ffmpeg-core (shared runtime)
```

All version packages depend on the same `ffmpeg-core`.

## Benefits

### 1. No Class Identity Problem

Each package is independent. No multiple versions in the same namespace.

```python
# Install only v6
pip install typed-ffmpeg-v6

from ffmpeg.filters import concat
# Only one concat class exists (from v6)
# No class identity issues!
```

### 2. Smaller Package Size

```
Before: typed-ffmpeg (10MB+) - contains all versions
After:  typed-ffmpeg-v6 (2MB) - only v6
        typed-ffmpeg-v8 (2MB) - only v8
```

### 3. Clear Versioning

```python
# Package version matches FFmpeg version
typed-ffmpeg-v6==6.1.0  # FFmpeg 6.1
typed-ffmpeg-v8==8.0.0  # FFmpeg 8.0
```

### 4. Shared Core Development

```python
# All versions share the same core runtime
# Bug fixes in ffmpeg-core benefit all versions
# Only need to maintain one copy of DAG/compile/IR code
```

### 5. User Choice

```python
# Most users: install latest
pip install typed-ffmpeg

# Specific version users
pip install typed-ffmpeg-v6

# Developers: install multiple for testing
pip install typed-ffmpeg-v6 typed-ffmpeg-v8
```

## Package Configurations

### Core Package

```toml
# packages/core/pyproject.toml

[project]
name = "ffmpeg-core"
version = "1.0.0"
description = "Core runtime for typed-ffmpeg (DAG, compilation, IR)"
dependencies = []  # No dependencies (pure Python)

[tool.setuptools.packages.find]
where = ["src"]
include = ["ffmpeg_core*"]
```

### Version Package (Example: v6)

```toml
# packages/v6/pyproject.toml

[project]
name = "typed-ffmpeg-v6"
version = "6.1.0"
description = "Typed FFmpeg bindings for FFmpeg 6.x"
dependencies = [
    "ffmpeg-core>=1.0,<2.0",
]

[tool.setuptools.packages.find]
where = ["src"]
include = ["ffmpeg*"]
```

### Latest Package

```toml
# packages/latest/pyproject.toml

[project]
name = "typed-ffmpeg"
version = "8.0.0"
description = "Typed FFmpeg bindings (latest version)"
dependencies = [
    "typed-ffmpeg-v8==8.*",
]
```

```python
# packages/latest/src/ffmpeg/__init__.py
"""Re-export latest version (v8)."""
from typed_ffmpeg_v8.ffmpeg import *

__version__ = "8.0.0"
```

### Workspace Configuration

```toml
# typed-ffmpeg/pyproject.toml (root)

[tool.uv.workspace]
members = [
    "packages/core",
    "packages/v5",
    "packages/v6", 
    "packages/v7",
    "packages/v8",
    "packages/latest",
]

[project]
name = "typed-ffmpeg-workspace"
version = "1.0.0"
description = "Monorepo for typed-ffmpeg packages"
requires-python = ">=3.10"

[tool.uv]
dev-dependencies = [
    "pytest>=7.0",
    "ruff>=0.9.6",
    "prek>=0.1.0",
]
```

## Import Path Changes

### Core Package Exports

```python
# packages/core/src/ffmpeg_core/__init__.py

from .dag import FilterNode, Stream, InputNode, OutputNode
from .compile import compile_as_list
from .common.serialize import Serializable

__all__ = [
    "FilterNode",
    "Stream",
    "InputNode", 
    "OutputNode",
    "compile_as_list",
    "Serializable",
]
```

### Version Package Imports

```python
# packages/v6/src/ffmpeg/filters.py (generated)

# Import from core package
from ffmpeg_core.dag.factory import filter_node_factory
from ffmpeg_core.common.schema import FFMpegFilterDef
from ffmpeg_core.schema import Default

# Generated filter functions
def concat(...):
    return filter_node_factory(...)
```

## Development Workflow

### Setup

```bash
# Clone repository
git clone https://github.com/livingbio/typed-ffmpeg.git
cd typed-ffmpeg

# Install all packages in development mode
uv sync --all-packages

# Now you can develop all packages simultaneously
```

### Code Generation

```bash
# Generate all versions
python tools/codegen/generate_all.py

# Generate specific version
python tools/codegen/generate.py \
  --version 6 \
  --output packages/v6/src/ffmpeg
```

### Testing

```bash
# Test all packages
pytest packages/

# Test specific package
cd packages/v6 && pytest

# Test core
cd packages/core && pytest
```

### Building

```bash
# Build all packages
for pkg in packages/*/; do
  cd $pkg && uv build
done

# Build specific package
cd packages/v8 && uv build
```

### Publishing

```bash
# Publish order: core first, then versions, then latest
cd packages/core && uv publish
cd packages/v5 && uv publish
cd packages/v6 && uv publish
cd packages/v7 && uv publish
cd packages/v8 && uv publish
cd packages/latest && uv publish
```

## Migration Plan

### Phase 1: Create Monorepo Structure (Week 1)

1. Create `packages/` directory structure
2. Create package `pyproject.toml` files
3. Set up workspace configuration

### Phase 2: Split Core from Versions (Week 1-2)

1. Move hand-written code to `packages/core/src/ffmpeg_core/`
   - `dag/` → `ffmpeg_core/dag/`
   - `compile/` → `ffmpeg_core/compile/`
   - `common/` → `ffmpeg_core/common/`
   - `ir/` → `ffmpeg_core/ir/`

2. Move version-specific code to version packages
   - `v5/` → `packages/v5/src/ffmpeg/`
   - `v6/` → `packages/v6/src/ffmpeg/`
   - `v7/` → `packages/v7/src/ffmpeg/`
   - `v8/` → `packages/v8/src/ffmpeg/`

### Phase 3: Update Import Paths (Week 2)

1. Update generated code templates
   - Change `from ffmpeg.dag import` → `from ffmpeg_core.dag import`
   - Change `from ffmpeg.common import` → `from ffmpeg_core.common import`

2. Regenerate all version bindings with new imports

### Phase 4: Create Latest Package (Week 2)

1. Create `packages/latest/`
2. Implement re-export from `typed-ffmpeg-v8`
3. Test that it works as expected

### Phase 5: Update CI/CD (Week 3)

1. Update workflows for monorepo structure
2. Add per-package testing
3. Add publishing workflow

### Phase 6: Documentation (Week 3)

1. Update README with new installation instructions
2. Create migration guide for existing users
3. Update contributing guide

### Phase 7: Cleanup (Week 3)

1. Remove old single-package structure
2. Archive old branches
3. Update issue templates

## User Migration

### For New Users

No changes needed. Just install:

```bash
pip install typed-ffmpeg  # Gets latest (v8)
```

### For Existing Users

```bash
# Old way (single package)
pip install typed-ffmpeg

from ffmpeg.filters import concat  # Got v8 mixed with all versions

# New way (after migration)
pip uninstall typed-ffmpeg
pip install typed-ffmpeg  # Now just installs typed-ffmpeg-v8

from ffmpeg.filters import concat  # Clean v8, no other versions
```

**No code changes needed!** Import paths stay the same.

### For Version-Specific Users

```bash
# New capability: install specific version
pip install typed-ffmpeg-v6  # For FFmpeg 6.x users
```

## PyPI Packages

Will publish these packages:

1. **ffmpeg-core** - Core runtime (hand-written code)
2. **typed-ffmpeg-v5** - FFmpeg 5.x bindings
3. **typed-ffmpeg-v6** - FFmpeg 6.x bindings
4. **typed-ffmpeg-v7** - FFmpeg 7.x bindings
5. **typed-ffmpeg-v8** - FFmpeg 8.x bindings
6. **typed-ffmpeg** - Meta-package (installs latest)

## Success Criteria

- ✅ Each version package is <3MB
- ✅ No class identity issues
- ✅ All existing tests pass
- ✅ User code requires no changes
- ✅ `pip install typed-ffmpeg` works (installs latest)
- ✅ `pip install typed-ffmpeg-v6` works (installs v6 only)
- ✅ Core package shared across all versions
- ✅ CI/CD builds and tests all packages
- ✅ Documentation updated

## Open Questions

1. **Core package naming**: `ffmpeg-core` vs `typed-ffmpeg-core`?
2. **Latest package strategy**: Meta-package or copy of v8?
3. **Version comparison tool**: Separate package or in core?
4. **Deprecation policy**: How long to support old versions?

## Next Steps

1. Get approval on monorepo design
2. Create prototype with v6 and v8 only
3. Test installation and imports
4. Full migration
5. Update CI/CD
6. Publish to PyPI
