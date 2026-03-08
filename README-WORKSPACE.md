# typed-ffmpeg Monorepo

Modern, type-safe FFmpeg wrappers with comprehensive support for complex filters, complete typing, and multi-language SDKs.

## 🏗️ Monorepo Structure

This repository is organized as a monorepo containing multiple related packages:

```
typed-ffmpeg/
├── packages/
│   ├── extract/       # FFmpeg metadata extraction
│   ├── codegen/       # Code generation framework
│   └── python/        # Python SDK (typed-ffmpeg)
```

## 📦 Packages

### [extract](packages/extract/) - FFmpeg Metadata Extraction

Extracts structured metadata from FFmpeg sources (C headers, help output, documentation).

```bash
cd packages/extract
uv pip install -e .
ffmpeg-extract --source /path/to/ffmpeg --output metadata/
```

**Purpose**: Parse FFmpeg internals to extract filter/codec/format definitions  
**Output**: Standardized JSON schemas  
**Dependencies**: None (standalone)

### [codegen](packages/codegen/) - Code Generation Framework

Generates language-specific SDKs from extracted metadata.

```bash
cd packages/codegen
uv pip install -e .
ffmpeg-codegen --metadata metadata/ --target python --output packages/python/src/
```

**Purpose**: Template-based code generation for multiple languages  
**Targets**: Python, TypeScript (future), others  
**Dependencies**: ffmpeg-extract (consumes its output)

### [python](packages/python/) - Python SDK

The main Python implementation of typed-ffmpeg.

```bash
cd packages/python
uv pip install -e .
```

**Purpose**: Type-safe Python FFmpeg wrapper  
**Distribution**: Published to PyPI as `typed-ffmpeg`  
**Dependencies**: None (runtime), uses codegen output (build-time)

## 🚀 Quick Start

### For Users (Python SDK)

```bash
# Install from PyPI
pip install typed-ffmpeg

# Or install from source
cd packages/python
uv pip install -e .
```

```python
import ffmpeg

# Use typed-ffmpeg as normal
ffmpeg.input("input.mp4").hflip().output("output.mp4").run()
```

### For Contributors

```bash
# Clone the repository
git clone https://github.com/livingbio/typed-ffmpeg.git
cd typed-ffmpeg

# Install workspace with all packages
uv sync --all-packages

# Or install specific package
cd packages/python
uv pip install -e ".[dev]"
```

## 🔧 Development Workflow

### Extract Metadata

```bash
cd packages/extract
ffmpeg-extract --source /path/to/ffmpeg --output ../../metadata/
```

### Generate Code

```bash
cd packages/codegen
ffmpeg-codegen \
  --metadata ../../metadata/ \
  --target python \
  --output ../python/src/ffmpeg/generated/
```

### Test Python SDK

```bash
cd packages/python
pytest
```

### Full Pipeline

```bash
# From repository root
./scripts/generate-all.sh
```

## 🧪 Testing

### Test Individual Packages

```bash
# Test extract
cd packages/extract && pytest

# Test codegen
cd packages/codegen && pytest

# Test python SDK
cd packages/python && pytest
```

### Test All Packages

```bash
# From repository root
pytest packages/
```

### Integration Tests

```bash
# Test full pipeline: extract → codegen → SDK
pytest packages/ -m integration
```

## 📝 Package Dependencies

```
extract (standalone)
   │
   ├─> metadata/ (JSON files)
   │
   └─> codegen (consumes metadata)
          │
          └─> generated code → python SDK
```

## 🏛️ Architecture

### Separation of Concerns

- **Extract**: Parse FFmpeg internals (independent of code generation)
- **Codegen**: Generate code for any language (independent of runtime)
- **Python**: Runtime implementation (independent of extraction/generation)

### Benefits

1. **Independent Development**: Changes to extraction don't affect SDK
2. **Multi-Language Support**: Easy to add TypeScript, Rust, Go backends
3. **Better Testing**: Test each component in isolation
4. **Clear Responsibilities**: Each package has a focused purpose

## 🔄 CI/CD

Each package has its own CI workflow:

- **extract**: `.github/workflows/extract.yml`
- **codegen**: `.github/workflows/codegen.yml`
- **python**: `.github/workflows/python-sdk.yml`
- **integration**: `.github/workflows/integration.yml`

## 📚 Documentation

- [Monorepo Design](MONOREPO_DESIGN.md) - Architecture and design decisions
- [Extract Package](packages/extract/README.md) - Metadata extraction
- [Codegen Package](packages/codegen/README.md) - Code generation
- [Python SDK](packages/python/README.md) - Python SDK documentation

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 🔮 Future Packages

Planned additions to the monorepo:

- **packages/typescript/** - TypeScript SDK for Node.js
- **packages/rust/** - Rust bindings (future)
- **packages/cli/** - Unified CLI tool (future)

## ⚙️ Workspace Management

### Using UV Workspace

```bash
# Sync all packages
uv sync --all-packages

# Sync specific package
uv sync --package ffmpeg-extract

# Add dependency to specific package
cd packages/python
uv add numpy
```

### Independent Development

Each package can also be developed independently:

```bash
cd packages/python
uv pip install -e ".[dev]"
pytest
```

## 📊 Status

| Package | Version | Status | Distribution |
|---------|---------|--------|--------------|
| extract | 0.1.0   | ✅ Active | Internal |
| codegen | 0.1.0   | ✅ Active | Internal |
| python  | (current) | ✅ Active | PyPI |

---

**Note**: The monorepo structure maintains full backward compatibility. Users of the Python SDK see no changes - it's still published as `typed-ffmpeg` with the same API.
