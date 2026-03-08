# Restructure into Monorepo: Extract, Codegen, and Python SDK

## 🎯 Overview

This PR restructures typed-ffmpeg into a monorepo containing three focused packages:

1. **ffmpeg-extract** - FFmpeg metadata extraction
2. **ffmpeg-codegen** - Code generation framework
3. **typed-ffmpeg** - Python SDK (unchanged for users)

## 🏗️ New Structure

```
typed-ffmpeg/
├── packages/
│   ├── extract/              # NEW: Metadata extraction package
│   │   ├── src/ffmpeg_extract/
│   │   │   ├── parse_c/      # Moved from src/scripts/parse_c/
│   │   │   ├── parse_help/   # Moved from src/scripts/parse_help/
│   │   │   └── parse_docs/   # Moved from src/scripts/parse_docs/
│   │   ├── tests/
│   │   ├── README.md
│   │   └── pyproject.toml
│   │
│   ├── codegen/              # NEW: Code generation package
│   │   ├── src/ffmpeg_codegen/
│   │   │   └── ...           # Moved from src/scripts/code_gen/
│   │   ├── tests/
│   │   ├── README.md
│   │   └── pyproject.toml
│   │
│   └── python/               # Python SDK (existing, relocated)
│       ├── src/ffmpeg/       # Moved from src/ffmpeg/
│       ├── tests/            # Moved from tests/
│       ├── docs/             # Moved from docs/
│       ├── README.md         # Moved from README.md
│       └── pyproject.toml    # Moved from pyproject.toml
│
├── scripts/                   # Workspace scripts
│   ├── setup-workspace.sh
│   └── test-all.sh
│
├── .github/workflows/
│   ├── extract.yml           # NEW: Extract package CI
│   ├── codegen.yml           # NEW: Codegen package CI
│   └── integration.yml       # NEW: Integration tests
│
├── pyproject-workspace.toml  # NEW: Workspace configuration
├── README-WORKSPACE.md       # NEW: Monorepo README
├── MIGRATION_GUIDE.md        # NEW: Migration guide
└── MONOREPO_DESIGN.md        # NEW: Design document
```

## 📦 Package Details

### 1. extract - FFmpeg Metadata Extraction

**Location**: `packages/extract/`

**Purpose**: Extract structured metadata from FFmpeg sources

**Features**:
- Parse C headers for filter/codec/format definitions
- Parse FFmpeg help output for options
- Parse documentation for descriptions
- Output standardized JSON schemas

**CLI**:
```bash
ffmpeg-extract --source /path/to/ffmpeg --output metadata/
```

**Dependencies**: None (standalone)

### 2. codegen - Code Generation Framework

**Location**: `packages/codegen/`

**Purpose**: Generate language-specific SDKs from metadata

**Features**:
- Template-based code generation
- Support for Python (implemented)
- Support for TypeScript (future)
- Extensible backend system

**CLI**:
```bash
ffmpeg-codegen --metadata metadata/ --target python --output packages/python/src/
```

**Dependencies**: ffmpeg-extract (consumes its output)

### 3. python - Python SDK (typed-ffmpeg)

**Location**: `packages/python/`

**Purpose**: Python implementation (main user-facing package)

**Features**:
- Same as before - no changes to functionality
- Generated code + handwritten runtime
- DAG, compile, IR layers

**Distribution**: Published to PyPI as `typed-ffmpeg`

**Dependencies**: None (runtime), codegen output (build-time)

## ✅ Backward Compatibility

### For End Users

**✅ 100% Backward Compatible - No changes required!**

- Package name: Still `typed-ffmpeg`
- Import path: Still `import ffmpeg`
- API: Completely unchanged
- PyPI: Same package name

**Users don't need to do anything** - this is purely an internal restructuring.

### For Contributors

- File locations changed (see migration guide)
- Import paths updated for internal tools
- Development workflow slightly different
- CI/CD split into package-specific workflows

**See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for detailed instructions**

## 🎁 Benefits

### 1. Clear Separation of Concerns

- **Extract**: Parse FFmpeg (independent)
- **Codegen**: Generate code (independent)
- **Python SDK**: Runtime (independent)

Each package has a single, focused responsibility.

### 2. Independent Development

- Change extraction logic without affecting SDK
- Update code generation without touching runtime
- Develop packages independently

### 3. Multi-Language Support

- **Foundation for TypeScript SDK**: Codegen can now target TypeScript
- **Foundation for Rust/Go SDKs**: Easy to add new backends
- **Shared metadata**: Single source of truth for all languages

### 4. Better Testing

- Test each package in isolation
- Package-specific CI workflows
- Integration tests for full pipeline
- Faster CI (only test affected packages)

### 5. Clearer Architecture

- Package boundaries make architecture explicit
- Dependencies are clear (extract → codegen → SDK)
- Easier onboarding for new contributors

## 📊 Changes Summary

### Files Added

- `packages/extract/` - Complete extract package (21 files)
- `packages/codegen/` - Complete codegen package (15 files)
- `packages/python/` - Relocated Python SDK (existing files)
- `.github/workflows/extract.yml` - Extract CI
- `.github/workflows/codegen.yml` - Codegen CI
- `.github/workflows/integration.yml` - Integration CI
- `scripts/setup-workspace.sh` - Setup script
- `scripts/test-all.sh` - Test script
- `pyproject-workspace.toml` - Workspace config
- `README-WORKSPACE.md` - Monorepo README
- `MIGRATION_GUIDE.md` - Migration guide
- `MONOREPO_DESIGN.md` - Design document

### Files Moved

| Old Path | New Path |
|----------|----------|
| `src/ffmpeg/` | `packages/python/src/ffmpeg/` |
| `src/scripts/parse_c/` | `packages/extract/src/ffmpeg_extract/parse_c/` |
| `src/scripts/parse_help/` | `packages/extract/src/ffmpeg_extract/parse_help/` |
| `src/scripts/parse_docs/` | `packages/extract/src/ffmpeg_extract/parse_docs/` |
| `src/scripts/code_gen/` | `packages/codegen/src/ffmpeg_codegen/` |
| `tests/` | `packages/python/tests/` |
| `docs/` | `packages/python/docs/` |

### Files Unchanged

- `.gitignore` - No changes
- `LICENSE` - No changes (copied to packages)
- Root documentation files - Preserved

## 🧪 Testing

### Package Tests

Each package has its own test suite:

```bash
# Test extract
cd packages/extract && pytest

# Test codegen
cd packages/codegen && pytest

# Test Python SDK
cd packages/python && pytest
```

### Integration Tests

Full pipeline testing:

```bash
# Test all packages
./scripts/test-all.sh

# Or use pytest
pytest packages/
```

### CI/CD

- **Extract CI**: Runs on changes to `packages/extract/`
- **Codegen CI**: Runs on changes to `packages/codegen/`
- **Python SDK CI**: Runs on changes to `packages/python/`
- **Integration CI**: Runs on all changes, tests full pipeline

## 🚀 Development Workflow

### Workspace Setup

```bash
# Clone repository
git clone https://github.com/livingbio/typed-ffmpeg.git
cd typed-ffmpeg

# Setup workspace (installs all packages)
./scripts/setup-workspace.sh

# Test everything
./scripts/test-all.sh
```

### Working on Specific Package

```bash
# Work on extract
cd packages/extract
uv pip install -e ".[dev]"
# Make changes, run tests
pytest

# Work on Python SDK
cd packages/python
uv pip install -e ".[dev]"
# Make changes, run tests
pytest
```

## 📚 Documentation

### New Documentation

- **README-WORKSPACE.md** - Monorepo overview and quick start
- **MONOREPO_DESIGN.md** - Architecture and design decisions
- **MIGRATION_GUIDE.md** - Migration guide for contributors

### Package Documentation

- **packages/extract/README.md** - Extract package docs
- **packages/codegen/README.md** - Codegen package docs
- **packages/python/README.md** - Python SDK docs (existing)

## 🔄 Migration Path

### For Contributors with Open PRs

1. **Rebase** your branch on new main
2. **Check** if your files moved (see MIGRATION_GUIDE.md)
3. **Update** import paths if needed
4. **Test** in new structure
5. **Update** PR description

**See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for detailed steps**

### For New Contributors

1. **Clone** repository
2. **Run** `./scripts/setup-workspace.sh`
3. **Choose** package to work on
4. **Develop** as usual

## 🔮 Future Work

This monorepo structure enables:

1. **TypeScript SDK** - Add `packages/typescript/` for Node.js support
2. **Rust Bindings** - Add `packages/rust/` for high-performance bindings
3. **CLI Tool** - Add `packages/cli/` for unified command-line tool
4. **Additional Backends** - Easy to add Go, Java, C++ backends

## 📝 Checklist

- [x] Create packages directory structure
- [x] Move extract code to packages/extract/
- [x] Move codegen code to packages/codegen/
- [x] Move Python SDK to packages/python/
- [x] Create package pyproject.toml files
- [x] Create package READMEs
- [x] Create package __init__.py files
- [x] Create workspace configuration
- [x] Create CI workflows for each package
- [x] Create integration CI workflow
- [x] Create workspace setup script
- [x] Create test-all script
- [x] Create migration guide
- [x] Create design document
- [x] Create workspace README
- [x] All packages have proper structure
- [x] No breaking changes to public API

## 💬 Questions for Reviewers

1. Is the package separation clear and logical?
2. Should we publish extract/codegen to PyPI or keep them internal?
3. Any suggestions for the workspace configuration?
4. Should we use UV workspace or keep packages independent?

## 🎉 Impact

This restructuring:
- ✅ Maintains full backward compatibility
- ✅ Enables multi-language support
- ✅ Improves code organization
- ✅ Makes CI/CD more efficient
- ✅ Prepares for future growth

**Zero breaking changes for users, significant architectural improvements for maintainability and extensibility!**

---

See [MONOREPO_DESIGN.md](MONOREPO_DESIGN.md) for complete architecture details and [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) for migration instructions.
