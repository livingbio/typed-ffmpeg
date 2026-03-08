# Monorepo Structure Design

## Overview

Restructure typed-ffmpeg into a monorepo containing multiple packages with clear separation of concerns:

1. **ffmpeg-extract** - FFmpeg metadata extraction (parsing C headers, help output, documentation)
2. **ffmpeg-codegen** - Code generation framework (language-agnostic)
3. **typed-ffmpeg** - Python SDK implementation
4. **typed-ffmpeg-ts** - TypeScript SDK implementation (future)

## Monorepo Structure

```
typed-ffmpeg/
├── README.md                      # Root README with monorepo overview
├── .github/
│   └── workflows/
│       ├── extract.yml            # CI for extract package
│       ├── codegen.yml            # CI for codegen package
│       ├── python-sdk.yml         # CI for Python SDK
│       └── integration.yml        # Cross-package integration tests
├── packages/
│   ├── extract/                   # FFmpeg metadata extraction
│   │   ├── README.md
│   │   ├── pyproject.toml
│   │   ├── uv.lock
│   │   ├── src/
│   │   │   └── ffmpeg_extract/
│   │   │       ├── __init__.py
│   │   │       ├── parse_c/       # C header parsing
│   │   │       ├── parse_help/    # FFmpeg --help parsing
│   │   │       ├── parse_docs/    # Documentation parsing
│   │   │       └── schema.py      # Extracted metadata schemas
│   │   └── tests/
│   │
│   ├── codegen/                   # Code generation framework
│   │   ├── README.md
│   │   ├── pyproject.toml
│   │   ├── uv.lock
│   │   ├── src/
│   │   │   └── ffmpeg_codegen/
│   │   │       ├── __init__.py
│   │   │       ├── ir/            # Intermediate representation
│   │   │       ├── backends/      # Backend generators
│   │   │       │   ├── python.py  # Python code generator
│   │   │       │   └── typescript.py  # TypeScript code generator
│   │   │       ├── templates/     # Code templates
│   │   │       └── cli.py         # CLI for code generation
│   │   └── tests/
│   │
│   └── python/                    # Python SDK (typed-ffmpeg)
│       ├── README.md
│       ├── pyproject.toml
│       ├── uv.lock
│       ├── src/
│       │   └── ffmpeg/            # Generated + handwritten code
│       │       ├── __init__.py
│       │       ├── dag/           # DAG layer
│       │       ├── compile/       # Compilation
│       │       ├── filters/       # Generated filters
│       │       ├── codecs/        # Generated codecs
│       │       ├── formats/       # Generated formats
│       │       └── ir/            # IR layer (from previous PR)
│       ├── tests/
│       └── docs/
│
├── scripts/                       # Shared scripts
│   ├── setup-workspace.sh
│   ├── run-all-tests.sh
│   └── generate-all.sh
│
├── docs/                          # Shared documentation
│   ├── architecture/
│   │   ├── monorepo-structure.md
│   │   └── package-dependencies.md
│   └── development/
│       └── contributing.md
│
└── tools/                         # Development tools
    └── workspace-tools/
```

## Package Details

### 1. packages/extract/ - FFmpeg Metadata Extraction

**Purpose**: Extract structured metadata from FFmpeg sources

**Responsibilities**:
- Parse FFmpeg C headers for filter/codec/format definitions
- Parse FFmpeg help output for options and parameters
- Parse FFmpeg documentation for descriptions
- Output standardized JSON schemas

**Dependencies**: None (standalone)

**Output**: JSON files with filter/codec/format metadata

**CLI**:
```bash
ffmpeg-extract --source /path/to/ffmpeg --output metadata/
ffmpeg-extract filters --help-output help.txt --output filters.json
```

### 2. packages/codegen/ - Code Generation Framework

**Purpose**: Generate language-specific SDKs from extracted metadata

**Responsibilities**:
- Load metadata from extract package
- Generate code for target languages (Python, TypeScript, etc.)
- Template-based code generation
- CLI for running code generation

**Dependencies**: 
- ffmpeg-extract (consumes its output)

**Output**: Generated source code files

**CLI**:
```bash
ffmpeg-codegen --metadata metadata/ --target python --output packages/python/src/ffmpeg/
ffmpeg-codegen --metadata metadata/ --target typescript --output packages/typescript/src/
```

### 3. packages/python/ - Python SDK

**Purpose**: Python implementation of typed-ffmpeg

**Responsibilities**:
- Generated code (filters, codecs, formats)
- Handwritten runtime (DAG, compile, IR)
- Tests and documentation
- PyPI package

**Dependencies**:
- Uses output from codegen
- Runtime has no external dependencies

**Distribution**: Published to PyPI as `typed-ffmpeg`

### 4. packages/typescript/ - TypeScript SDK (Future)

**Purpose**: TypeScript implementation for Node.js

**Responsibilities**:
- Generated TypeScript types and classes
- Handwritten runtime for fluent-ffmpeg compatibility
- Tests and documentation
- NPM package

**Distribution**: Published to NPM as `@typed-ffmpeg/core`

## Package Dependencies

```
extract (standalone)
   │
   ├─> metadata files (JSON)
   │
   └─> codegen (consumes metadata)
          │
          ├─> generated Python code ─> python SDK
          │
          └─> generated TypeScript code ─> typescript SDK
```

## Workspace Management

### Using UV Workspace

**Root `pyproject.toml`**:
```toml
[tool.uv.workspace]
members = [
    "packages/extract",
    "packages/codegen",
    "packages/python",
]

[tool.uv]
dev-dependencies = [
    "pytest",
    "ruff",
    "mypy",
]
```

This allows:
- Shared virtual environment
- Cross-package development
- Unified dependency management
- Single `uv.lock` at root (or per-package)

### Alternative: Independent Packages

Each package has its own:
- `pyproject.toml`
- `uv.lock`
- Virtual environment
- Independent versioning

## Migration Strategy

### Phase 1: Extract Package (Week 1)
1. Create `packages/extract/` structure
2. Move `src/scripts/parse_*` to `packages/extract/src/ffmpeg_extract/`
3. Update imports and tests
4. Add extract-specific CI workflow
5. Test extraction independently

### Phase 2: Codegen Package (Week 1-2)
1. Create `packages/codegen/` structure
2. Move `src/scripts/code_gen/` to `packages/codegen/src/ffmpeg_codegen/`
3. Refactor to use extract package output
4. Add codegen-specific CI workflow
5. Test code generation

### Phase 3: Python SDK Package (Week 2)
1. Create `packages/python/` structure
2. Move `src/ffmpeg/` to `packages/python/src/ffmpeg/`
3. Move current `tests/`, `docs/` to `packages/python/`
4. Update Python package CI workflow
5. Ensure PyPI publishing still works

### Phase 4: Root Integration (Week 2-3)
1. Update root README with monorepo overview
2. Add workspace configuration
3. Create cross-package integration tests
4. Update documentation
5. Migrate GitHub workflows

### Phase 5: Cleanup (Week 3)
1. Remove old structure
2. Update all documentation
3. Verify all CI passes
4. Create migration guide for contributors

## Benefits

### 1. Clear Separation of Concerns
- Extraction logic isolated from generation
- Code generation separate from runtime
- Each package has focused responsibility

### 2. Independent Development
- Extract improvements don't affect SDK
- Codegen changes are isolated
- Language SDKs evolve independently

### 3. Multi-Language Support
- Easy to add new language backends
- Shared extraction and generation logic
- Consistent metadata across languages

### 4. Better Testing
- Test extraction independently
- Test code generation separately
- Test each SDK in isolation
- Integration tests for full pipeline

### 5. Versioning & Releases
- Independent package versions
- Extract can be v1.0, SDK can be v0.5
- Breaking changes isolated
- Semantic versioning per package

## CI/CD Strategy

### Per-Package CI

**packages/extract/.github/workflows/extract.yml**:
- Run extraction tests
- Validate output schemas
- Publish extract package (optional)

**packages/codegen/.github/workflows/codegen.yml**:
- Run generation tests
- Validate generated code
- Test all backends

**packages/python/.github/workflows/python-sdk.yml**:
- Run Python SDK tests
- Type checking
- Coverage
- Publish to PyPI

### Integration CI

**.github/workflows/integration.yml**:
- Full pipeline: extract → codegen → test SDK
- Cross-package integration tests
- End-to-end validation

## Documentation Structure

### Root README.md
- Monorepo overview
- Quick start for each package
- Links to package READMEs

### Package READMEs
- Package-specific documentation
- Installation and usage
- Development guide

### Shared Docs
- Architecture docs in root `docs/`
- Development workflows
- Contributing guide

## Backward Compatibility

### For Users (Python SDK)
- Package name stays `typed-ffmpeg`
- Import paths unchanged: `import ffmpeg`
- No breaking changes in API
- Transparent migration

### For Contributors
- Migration guide for existing PRs
- Updated contributing docs
- Clear package boundaries

## File Movement Map

### Current → New

```
src/scripts/parse_c/       → packages/extract/src/ffmpeg_extract/parse_c/
src/scripts/parse_help/    → packages/extract/src/ffmpeg_extract/parse_help/
src/scripts/parse_docs/    → packages/extract/src/ffmpeg_extract/parse_docs/
src/scripts/code_gen/      → packages/codegen/src/ffmpeg_codegen/
src/ffmpeg/                → packages/python/src/ffmpeg/
tests/ (python SDK tests)  → packages/python/tests/
docs/ (SDK docs)           → packages/python/docs/
```

## Open Questions

1. **Workspace vs. Independent?**
   - Use UV workspace for shared deps?
   - Or fully independent packages?

2. **Publishing Strategy**
   - Publish extract/codegen to PyPI?
   - Or keep internal tools?

3. **Shared Code**
   - Where to put shared schemas?
   - Should extract define IR?

4. **Versioning**
   - Synchronized versions?
   - Or independent semver?

## Next Steps

1. Create packages/extract/ structure
2. Move and refactor extraction code
3. Create packages/codegen/ structure
4. Move and refactor generation code
5. Create packages/python/ structure
6. Update CI/CD workflows
7. Update documentation
8. Test full pipeline
9. Create migration guide
10. Merge to main
