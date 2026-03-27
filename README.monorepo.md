# typed-ffmpeg Monorepo

Modern, type-safe FFmpeg wrappers for Python with multi-version support.

## 📦 Package Structure

This is a monorepo containing multiple packages:

| Package | Description | Install |
|---------|-------------|---------|
| **typed-ffmpeg** | Latest version (v8) | `pip install typed-ffmpeg` |
| **typed-ffmpeg-v5** | FFmpeg 5.x bindings | `pip install typed-ffmpeg-v5` |
| **typed-ffmpeg-v6** | FFmpeg 6.x bindings | `pip install typed-ffmpeg-v6` |
| **typed-ffmpeg-v7** | FFmpeg 7.x bindings | `pip install typed-ffmpeg-v7` |
| **typed-ffmpeg-v8** | FFmpeg 8.x bindings | `pip install typed-ffmpeg-v8` |
| **ffmpeg-core** | Core runtime (auto-installed) | - |

## 🚀 For Users

### Installation

```bash
# Install latest version (recommended for most users)
pip install typed-ffmpeg

# Install specific version matching your FFmpeg
pip install typed-ffmpeg-v6  # For FFmpeg 6.x
pip install typed-ffmpeg-v7  # For FFmpeg 7.x
```

### Usage

```python
import ffmpeg

# All imports work the same regardless of version
input_file = ffmpeg.input("input.mp4")
output_file = input_file.hflip().output("output.mp4")
output_file.run()
```

## 💻 For Developers

### Setup

```bash
# Clone repository
git clone https://github.com/livingbio/typed-ffmpeg.git
cd typed-ffmpeg

# Install all packages in development mode
uv sync --all-packages
```

### Repository Structure

```
typed-ffmpeg/
├── packages/
│   ├── core/           # Shared runtime (DAG, compile, IR)
│   ├── v5/             # FFmpeg 5.x bindings
│   ├── v6/             # FFmpeg 6.x bindings
│   ├── v7/             # FFmpeg 7.x bindings
│   ├── v8/             # FFmpeg 8.x bindings
│   └── latest/         # Main package (re-exports v8)
└── tools/              # Development tools

# Each package has:
packages/*/
├── pyproject.toml      # Package configuration
├── src/                # Source code
├── tests/              # Tests
└── README.md           # Package documentation
```

### Development Workflow

```bash
# Test all packages
pytest packages/

# Test specific package
cd packages/v8 && pytest

# Build all packages
for pkg in packages/*/; do
  cd $pkg && uv build
done

# Build specific package
cd packages/v8 && uv build
```

### Code Generation

```bash
# Generate all versions (future)
python tools/codegen/generate_all.py

# Generate specific version
python tools/codegen/generate.py \
  --version 8 \
  --output packages/v8/src/ffmpeg
```

## 📚 Documentation

- [Monorepo Design](docs/designs/monorepo-multi-version.md)
- [Migration Guide](docs/migration/to-monorepo.md) (coming soon)
- [Contributing Guide](CONTRIBUTING.md)

## 🎯 Key Benefits

### For Users

✅ **Smaller packages** - Download only what you need (~2MB vs ~10MB)  
✅ **Clear versioning** - Package version matches FFmpeg version  
✅ **No breaking changes** - All imports work the same  
✅ **Choose your version** - Install specific FFmpeg version support

### For Developers

✅ **Shared core** - Bug fixes benefit all versions  
✅ **Independent testing** - Test each version separately  
✅ **Clear architecture** - Core vs version-specific code  
✅ **Easier maintenance** - No class identity issues

## 🔄 Migration from Single Package

If you were using the old single-package `typed-ffmpeg`:

```bash
# Old (single package with all versions)
pip install typed-ffmpeg==0.x.x

# New (latest version only)
pip uninstall typed-ffmpeg
pip install typed-ffmpeg
```

**No code changes needed!** Your imports continue to work.

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgements

See main [README.md](packages/latest/README.md) for acknowledgements.
