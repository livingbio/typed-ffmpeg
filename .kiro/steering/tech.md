# Technology Stack

## Core Technologies

- **Python**: Minimum version 3.10, supports up to 3.13
- **FFmpeg**: External dependency (must be installed on system)
- **Build System**: setuptools with setuptools-scm for versioning
- **Package Manager**: uv (modern Python package manager)

## Development Dependencies

### Code Quality & Formatting
- **ruff**: Fast Python linter and formatter (replaces black, isort, flake8)
- **mypy**: Static type checking
- **pre-commit**: Git hooks for code quality

### Testing
- **pytest**: Test framework with coverage reporting
- **pytest-cov**: Coverage plugin
- **pytest-datadir**: Test data management
- **pytest-recording**: HTTP request recording for tests
- **syrupy**: Snapshot testing

### Documentation
- **mkdocs**: Documentation site generator
- **mkdocs-material**: Material theme for mkdocs
- **mkdocstrings**: API documentation from docstrings
- **mknotebooks**: Jupyter notebook integration

### Optional Dependencies
- **graphviz**: For filter graph visualization (optional extra)

## Common Commands

### Development Setup
```bash
# Install all development dependencies
uv pip install --group dev

# Install with graph visualization support
pip install 'typed-ffmpeg[graph]'
```

### Code Quality
```bash
# Run linter and formatter
ruff check --fix
ruff format

# Type checking
mypy src/

# Pre-commit hooks
pre-commit run --all-files
```

### Testing
```bash
# Run tests with coverage
pytest --cov=ffmpeg --cov-report=term-missing

# Run specific test markers
pytest -m "not dev_only"
```

### Documentation
```bash
# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

### Build & Release
```bash
# Build package
python -m build

# Generate reference documentation
python scripts/gen_ref_pages.py
```

## Configuration Files

- **pyproject.toml**: Main project configuration (dependencies, build, tools)
- **uv.lock**: Locked dependency versions
- **.pre-commit-config.yaml**: Git hooks configuration
- **mkdocs.yml**: Documentation configuration
- **.coveragerc**: Test coverage configuration