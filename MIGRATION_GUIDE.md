# Monorepo Migration Guide

This guide explains the changes from the previous single-package structure to the new monorepo structure.

## For End Users

### ✅ No Changes Required

If you're using `typed-ffmpeg` as a library:

- Package name stays the same: `pip install typed-ffmpeg`
- Import path unchanged: `import ffmpeg`
- API is 100% compatible
- No breaking changes

**You don't need to do anything!**

## For Contributors

### Repository Structure Changes

#### Before (Single Package)

```
typed-ffmpeg/
├── src/
│   ├── ffmpeg/          # Python SDK code
│   └── scripts/         # Extraction and codegen
├── tests/               # All tests
├── docs/                # All documentation
└── pyproject.toml       # Single project config
```

#### After (Monorepo)

```
typed-ffmpeg/
├── packages/
│   ├── extract/         # Extraction package
│   │   ├── src/ffmpeg_extract/
│   │   ├── tests/
│   │   └── pyproject.toml
│   ├── codegen/         # Code generation package
│   │   ├── src/ffmpeg_codegen/
│   │   ├── tests/
│   │   └── pyproject.toml
│   └── python/          # Python SDK package
│       ├── src/ffmpeg/
│       ├── tests/
│       ├── docs/
│       └── pyproject.toml
├── pyproject-workspace.toml  # Workspace config
└── README-WORKSPACE.md       # Workspace README
```

### File Movements

| Old Location | New Location | Notes |
|-------------|--------------|-------|
| `src/ffmpeg/` | `packages/python/src/ffmpeg/` | Python SDK code |
| `src/scripts/parse_c/` | `packages/extract/src/ffmpeg_extract/parse_c/` | C parsing |
| `src/scripts/parse_help/` | `packages/extract/src/ffmpeg_extract/parse_help/` | Help parsing |
| `src/scripts/parse_docs/` | `packages/extract/src/ffmpeg_extract/parse_docs/` | Docs parsing |
| `src/scripts/code_gen/` | `packages/codegen/src/ffmpeg_codegen/` | Code generation |
| `tests/` | `packages/python/tests/` | Python SDK tests |
| `docs/` | `packages/python/docs/` | Python SDK docs |

### Import Changes

#### For Extract Code

**Before**:
```python
from scripts.parse_c import parse_filters
```

**After**:
```python
from ffmpeg_extract.parse_c import parse_filters
```

#### For Codegen Code

**Before**:
```python
from scripts.code_gen import CodeGenerator
```

**After**:
```python
from ffmpeg_codegen import CodeGenerator
```

#### For Python SDK

**No changes** - imports remain the same:
```python
import ffmpeg  # Still works exactly the same
```

### Development Workflow Changes

#### Before: Single Package Development

```bash
# Clone and install
git clone https://github.com/livingbio/typed-ffmpeg.git
cd typed-ffmpeg
uv pip install -e ".[dev]"

# Run tests
pytest

# Run specific tests
pytest src/ffmpeg/tests/
```

#### After: Monorepo Development

**Option 1: Workspace Development (Recommended)**

```bash
# Clone
git clone https://github.com/livingbio/typed-ffmpeg.git
cd typed-ffmpeg

# Sync entire workspace
uv sync --all-packages

# Run all tests
pytest packages/

# Run package-specific tests
pytest packages/python/tests/
pytest packages/extract/tests/
pytest packages/codegen/tests/
```

**Option 2: Individual Package Development**

```bash
# Work on Python SDK only
cd packages/python
uv pip install -e ".[dev]"
pytest

# Work on extract only
cd packages/extract
uv pip install -e ".[dev]"
pytest
```

### CI/CD Changes

#### Before: Single Workflow

```yaml
# .github/workflows/ci-package.yml
- name: Test
  run: pytest
```

#### After: Multiple Workflows

```yaml
# .github/workflows/python-sdk.yml
- name: Test Python SDK
  run: pytest packages/python/

# .github/workflows/extract.yml
- name: Test Extract
  run: pytest packages/extract/

# .github/workflows/integration.yml
- name: Integration Test
  run: ./scripts/test-integration.sh
```

### PR and Branch Strategies

#### Package-Specific Changes

When changing only one package:

```bash
# Create branch with package prefix
git checkout -b python/fix-filter-bug
git checkout -b extract/add-new-parser
git checkout -b codegen/typescript-backend
```

#### Cross-Package Changes

When changes span multiple packages:

```bash
git checkout -b feature/new-filter-type
# Changes to extract, codegen, and python packages
```

### Testing Strategy

#### Before: Single Test Suite

```bash
pytest  # Runs all tests
```

#### After: Package-Scoped Testing

```bash
# Test individual package
cd packages/python && pytest

# Test all packages
pytest packages/

# Test with markers
pytest packages/ -m "not integration"  # Skip integration tests
pytest packages/ -m integration        # Only integration tests
```

### Common Migration Tasks

#### Updating an Existing PR

If you have an open PR from before the monorepo migration:

1. **Rebase on new main**:
   ```bash
   git checkout your-branch
   git fetch origin
   git rebase origin/main
   ```

2. **Check if your files moved**:
   - Compare old paths with new structure
   - Update import statements if needed

3. **Test in new structure**:
   ```bash
   cd packages/python  # or relevant package
   pytest
   ```

4. **Update PR description** to reflect new structure

#### Adding a New Feature

**To Python SDK**:
```bash
cd packages/python
# Make changes to src/ffmpeg/
pytest tests/
```

**To Extract**:
```bash
cd packages/extract
# Make changes to src/ffmpeg_extract/
pytest tests/
```

**To Codegen**:
```bash
cd packages/codegen
# Make changes to src/ffmpeg_codegen/
pytest tests/
```

### Troubleshooting

#### Import Errors

**Error**: `ModuleNotFoundError: No module named 'scripts'`

**Solution**: Update imports to use package names:
- `scripts.parse_c` → `ffmpeg_extract.parse_c`
- `scripts.code_gen` → `ffmpeg_codegen`

#### Test Discovery Issues

**Error**: `pytest` not finding tests

**Solution**: Run pytest from package directory or specify path:
```bash
cd packages/python && pytest
# Or
pytest packages/python/tests/
```

#### Dependency Issues

**Error**: Package not found

**Solution**: Install from workspace or package:
```bash
# Workspace install
uv sync --all-packages

# Individual package install
cd packages/python
uv pip install -e ".[dev]"
```

### Getting Help

- **Documentation**: See [MONOREPO_DESIGN.md](MONOREPO_DESIGN.md) for architecture details
- **Issues**: Open an issue on GitHub with `[monorepo]` tag
- **Discussions**: Use GitHub Discussions for questions

## Timeline

1. **Week 1**: Monorepo structure created, packages separated
2. **Week 2**: CI/CD updated, documentation updated
3. **Week 3**: All PRs migrated, cleanup complete
4. **Week 4**: Old structure removed, monorepo fully operational

## FAQ

### Q: Do I need to reinstall typed-ffmpeg?

**A**: No, if you're using PyPI. The PyPI package name and API remain unchanged.

### Q: Can I still develop on a single package?

**A**: Yes! You can `cd packages/python` and work there independently.

### Q: Will my existing PRs break?

**A**: They'll need rebasing and possibly small import updates, but the changes should be minimal.

### Q: Why switch to a monorepo?

**A**: Better separation of concerns, multi-language support, independent package development, and clearer architecture.

### Q: What if I don't want the whole workspace?

**A**: Just work in the package you need. Each package can be developed independently.

## Support

If you encounter issues during migration:

1. Check this guide first
2. Search existing issues
3. Ask in GitHub Discussions
4. Open a new issue with `[migration]` tag

---

Last updated: 2024-03-08
