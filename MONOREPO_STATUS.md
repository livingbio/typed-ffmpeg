# Monorepo Architecture - Implementation Status

## ✅ Completed

### 1. Monorepo Structure Created
- Created `packages/` directory with 6 sub-packages
- Each package has its own `pyproject.toml`
- Workspace configuration in `pyproject-workspace.toml`

### 2. Code Organized
- **Core package** (`packages/core/`): Hand-written runtime code
  - DAG layer (factory, nodes, utils)
  - Compile layer
  - IR layer
  - Common utilities
  - FFprobe
  
- **Version packages** (`packages/v{5,6,7,8}/`): Generated FFmpeg bindings
  - filters.py, sources.py
  - streams/ (video, audio)
  - codecs/ (encoders, decoders, schema)
  - formats/ (muxers, demuxers, schema)
  - options/ (codec, format, framesync, timeline)
  - dag/io/ (input, output - generated)
  - dag/global_runnable/global_args.py (generated)

- **Latest package** (`packages/latest/`): Meta-package
  - Re-exports from typed-ffmpeg-v8

### 3. Imports Fixed
- Created `scripts/fix-monorepo-imports.py`
- Fixed all imports in generated code:
  - Core modules: `ffmpeg.dag` → `ffmpeg_core.dag`
  - Generated modules: `ffmpeg.options` → `.options` (relative)
- Modified 56 files total (14 per version × 4 versions)

### 4. Stub Files Created
- Created re-export stubs in version packages:
  - `schema.py` → re-exports from `ffmpeg_core.schema`
  - `types.py` → re-exports from `ffmpeg_core.types`
  - `expressions.py` → re-exports from `ffmpeg_core.expressions`
  - `common/schema.py` → re-exports from `ffmpeg_core.common.schema`

### 5. Package __init__.py Files
- Created main entry points for each version package
- Export: `input`, `output`, `merge_outputs`, `probe`, `filters`, `streams`, `codecs`, `formats`

## ⚠️ Issues Found

### 1. Import Errors (Partially Resolved)
**Problem:** Core package trying to import version-specific modules

**Status:** Partially fixed by:
- Removing generated `dag/io/` from core (it belongs in version packages)
- Keeping hand-written `dag/global_runnable/runnable.py` in core
- Version packages keep generated `dag/global_runnable/global_args.py`

**Remaining Issue:** `ffmpeg_core.dag.nodes` references classes from `dag.io` which is now only in version packages. This creates a circular dependency.

### 2. Architecture Issue: DAG Dependencies
**Core Problem:** 
- `ffmpeg_core.dag.nodes` (hand-written, in core) references:
  - `dag.io.output_args.OutputArgs` (generated, in version packages)
  - `codecs.schema.FFMpegEncoderOption` (in version packages)
  
This means core code depends on version-specific generated code, which breaks the monorepo architecture.

**Two Solutions:**

#### Option A: Keep DAG in Version Packages
- Move all of `dag/` to version packages (including hand-written code)
- Core package only contains: compile, ir, common, utils, ffprobe
- Pros: Clean separation
- Cons: Duplicates hand-written DAG code across versions

#### Option B: Abstract Interfaces in Core
- Create abstract base classes in core for OutputArgs, schema types
- Version packages provide concrete implementations
- Use dependency injection pattern
- Pros: No duplication
- Cons: More complex architecture

## 📋 Next Steps

### Immediate (Choose Architecture)
1. **Decision needed**: Option A or Option B?
2. Implement chosen solution
3. Test imports work correctly

### After Imports Work
1. Update code generation templates
2. Regenerate all version bindings with correct imports
3. Test each package can be imported independently
4. Run test suite for each package

### CI/CD Updates
1. Update GitHub Actions workflows for monorepo
2. Per-package testing
3. Build and publish workflows

### Documentation
1. Update main README
2. Create migration guide for users
3. Update contributing guide

## 🎯 Current Status

**Branch:** refactor/monorepo-architecture  
**Commits:** 1 (initial structure)  
**Ready for:** Architecture decision + additional implementation

**Estimated completion:** 
- Option A: 2-3 hours
- Option B: 4-5 hours

## 💡 Recommendation

**Use Option A (Keep DAG in Version Packages)**

**Reasoning:**
1. Simpler implementation
2. Clear separation (core = pure runtime, version = bindings + integration)
3. DAG code is relatively small (~2KB per version)
4. Easier to maintain and understand
5. No breaking changes to generated code structure

**Implementation:**
1. Move `packages/core/src/ffmpeg_core/dag/` to each version package
2. Update imports in core to reference version-specific DAG
3. Core becomes: compile, ir, common, utils, ffprobe (no DAG)
4. Version packages have complete standalone functionality

This matches the monorepo philosophy: each version package is self-contained and independent.
