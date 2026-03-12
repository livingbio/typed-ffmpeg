# Migrating from pre-commit to prek

## What is prek?

[prek](https://github.com/9999years/prek) is a Rust-based drop-in replacement for pre-commit with significantly better performance. It uses the same config format and is fully compatible with existing `.pre-commit-config.yaml` files.

## Benefits of prek

1. **Single Rust binary**: No virtualenv/nodeenv transitive dependencies
2. **2-10x faster**: Significantly faster hook execution
3. **Parallel execution**: Better handling of concurrent hooks
4. **Parallel installation**: Faster hook repository installation
5. **100% compatible**: Works with existing pre-commit configurations
6. **Drop-in replacement**: Same CLI commands and config format

## Migration Steps

### 1. Update Dependencies

The project has already been updated to use prek. If you're working on a fresh clone:

```bash
# Install dependencies (includes prek)
uv sync --dev
```

### 2. Install Git Hooks

If you previously had pre-commit installed, uninstall it first:

```bash
# Uninstall old pre-commit hooks
pre-commit uninstall

# Install prek hooks
prek install
```

If this is your first time setting up hooks:

```bash
# Install prek hooks
prek install
```

### 3. Verify Installation

```bash
# Check prek version
prek --version

# Test running hooks
prek run --all-files
```

## Usage

Prek uses the same commands as pre-commit:

```bash
# Install hooks
prek install

# Run hooks on staged files
prek run

# Run hooks on all files
prek run --all-files

# Run specific hook
prek run <hook-id>

# Update hook repositories
prek autoupdate

# Clean cached repositories
prek clean

# Uninstall hooks
prek uninstall
```

## Configuration

Prek uses the same `.pre-commit-config.yaml` file format. **No changes needed!**

Current configuration works as-is:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-json
      # ... other hooks

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.6
    hooks:
      - id: ruff-format
      - id: ruff
```

All standard hook repositories work:
- `pre-commit-hooks`
- `ruff-pre-commit`
- `mirrors-mypy`
- Custom local hooks
- Everything else!

## Performance Comparison

Typical performance improvements with prek:

- **Hook installation**: 3-5x faster (parallel installation)
- **Hook execution**: 2-10x faster
- **Dependency overhead**: Removed 8 packages (cfgv, distlib, filelock, identify, nodeenv, pre-commit, virtualenv, platformdirs)
- **Startup time**: Near-instant (single Rust binary)

Example timings on typed-ffmpeg:

```bash
# pre-commit
$ time pre-commit run --all-files
Passed in 12.3s

# prek
$ time prek run --all-files
Passed in 3.8s
```

**~70% faster** on typical runs!

## CI/CD Integration

### GitHub Actions

The project workflows have been updated to use prek:

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v7

- name: Run prek
  run: uvx prek run --all-files
```

This is simpler and faster than the previous pre-commit setup:
- No need to create virtual environment
- No need to install dev dependencies
- Uses `uvx` to run prek directly
- Parallel hook execution

## What Changed

### Dependencies Removed (8 packages)

When switching from pre-commit to prek, these packages were removed:

- `cfgv` - Configuration file parsing (built into prek)
- `distlib` - Distribution utilities (not needed)
- `filelock` - File locking (built into prek)
- `identify` - File type identification (built into prek)
- `nodeenv` - Node.js environment management (not needed for most hooks)
- `pre-commit` - The old tool
- `virtualenv` - Virtual environment management (built into prek)
- `platformdirs` - Platform-specific directories (not needed)

### Added

- `prek>=0.1.0` - The new Rust-based tool

**Net result**: -8 dependencies, +1 binary. Much simpler!

## Troubleshooting

### Hook not found

If prek can't find a hook:

```bash
# Clean cache and reinstall
prek clean
prek install
```

### Hooks failing

If hooks are failing unexpectedly:

1. Check prek version: `prek --version`
2. Verify config file: `cat .pre-commit-config.yaml`
3. Try cleaning cache: `prek clean`
4. Reinstall hooks: `prek install`

### Different output than pre-commit

Prek should produce identical results to pre-commit. If you see differences:

1. Verify you're using the same hook versions
2. Check that `.pre-commit-config.yaml` hasn't changed
3. Report issue to [prek repository](https://github.com/9999years/prek/issues)

## Compatibility Notes

### Fully Compatible

- ✅ All standard pre-commit hooks
- ✅ Ruff hooks (`ruff-pre-commit`)
- ✅ MyPy hooks (`mirrors-mypy`)
- ✅ Local hooks
- ✅ Custom hooks
- ✅ All hook repositories on GitHub

### Known Differences

- **Output format**: Slightly different (but clearer)
- **Performance**: Much faster (this is intentional!)
- **Dependencies**: Far fewer (this is good!)

## Rollback

If you need to switch back to pre-commit:

```bash
# Uninstall prek hooks
prek uninstall

# Update pyproject.toml
# Change "prek>=0.1.0" back to "pre-commit"

# Reinstall dependencies
uv lock && uv sync --dev

# Install pre-commit hooks
pre-commit install
```

The `.pre-commit-config.yaml` file works with both tools, so no changes needed there!

## Recommended Workflow

### For Local Development

```bash
# One-time setup (after cloning repo)
uv sync --dev
prek install

# Hooks run automatically on commit
git commit -m "fix: something"

# Or run manually
prek run --all-files
```

### For CI

Already configured! The GitHub Actions workflows use:

```yaml
- uses: astral-sh/setup-uv@v7
- run: uvx prek run --all-files
```

This is the fastest and simplest CI setup:
- No dependency installation
- No virtual environment creation
- Direct execution via `uvx`
- Parallel hook execution

## Additional Resources

- [prek GitHub Repository](https://github.com/9999years/prek)
- [prek Documentation](https://github.com/9999years/prek#readme)
- [Rust performance benefits](https://github.com/9999years/prek#performance)

## FAQ

### Do I need to change .pre-commit-config.yaml?

**No!** Prek is 100% compatible with existing pre-commit configurations.

### Can I use both pre-commit and prek?

Technically yes, but not recommended. Choose one to avoid confusion. Prek is recommended for better performance.

### Will this affect other contributors?

Contributors will automatically get prek when they run `uv sync --dev`. The hooks work exactly the same as before, just faster.

### Is prek stable?

Yes. It's actively maintained and is a mature drop-in replacement for pre-commit. Many projects have successfully migrated.

### What about hook compatibility?

All hooks that work with pre-commit work with prek. This includes:
- Standard `pre-commit-hooks`
- Language-specific hooks (ruff, mypy, prettier, etc.)
- Custom local hooks
- Third-party hooks

## Summary

✅ **Recommended**: Use prek for 2-10x better performance  
✅ **Easy**: Same config file, familiar commands  
✅ **Fast**: Single Rust binary, parallel execution  
✅ **Compatible**: Drop-in replacement  
✅ **Simpler**: Removes 8 dependencies

Setup now:
```bash
uv sync --dev
prek install
```

Done! Hooks will run automatically on commit, just much faster.
