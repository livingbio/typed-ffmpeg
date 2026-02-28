# GitHub Copilot Instructions for typed-ffmpeg

## Project Overview

typed-ffmpeg is a modern Python FFmpeg wrapper that provides extensive support for complex filters with detailed typing and documentation. The project emphasizes type safety, IDE integration, and comprehensive FFmpeg filter support with zero external dependencies (pure Python standard library).

## Code Style and Standards

### Python Version and Type Safety
- **Python Version**: Minimum Python 3.10, support up to Python 3.13
- **Type Annotations**: All functions, methods, and classes must include complete type annotations
- **Type Checking**: Code must pass mypy type checking with strict settings (see `pyproject.toml`)
- Follow PEP 484 type hinting conventions

### Formatting and Linting
- **Formatter**: Use `black` for code formatting (line length: 88 characters)
- **Linter**: Use `ruff` with the configuration in `pyproject.toml`
- **Import Sorting**: Use `ruff` for import organization (follows isort conventions)
- **Docstrings**: Follow Google-style docstrings for all public functions, classes, and methods
- Run `ruff format` and `ruff check --fix` before committing

### Code Organization
- **Module Structure**: All source code is in `src/ffmpeg/`
- **Tests Location**: Tests are colocated with the code they test in `tests/` subdirectories
- **Scripts**: Development and build scripts are in `src/scripts/` and `scripts/`
- **No External Dependencies**: Core library must remain zero-dependency (standard library only)
- Optional dependencies (like graphviz) should be in `[project.optional-dependencies]`

## Development Workflow

### Setting Up Development Environment
```bash
# Install uv package manager
pip install uv

# Create virtual environment
uv venv

# Install all development dependencies
uv pip install --group dev
```

### Running Tests
```bash
# Run all tests with coverage
pytest src/ffmpeg --cov=./src/ffmpeg --cov-report=xml

# Run specific test file
pytest src/ffmpeg/tests/test_ffmpeg.py

# Run with coverage report
pytest --cov-report=term-missing
```

### Linting and Type Checking
```bash
# Run ruff linter
ruff check src/

# Run ruff formatter
ruff format src/

# Run mypy type checker
mypy src/ffmpeg/

# Run all pre-commit hooks
pre-commit run --all-files
```

### Building the Package
```bash
# Build distribution packages
python -m build

# Install built package
pip install dist/*.whl
```

## Testing Requirements

### Test Structure
- Use `pytest` for all tests
- Tests must be in `tests/` subdirectories within their respective modules
- Test files must start with `test_` prefix
- Use `pytest-cov` for coverage reporting
- Use `syrupy` for snapshot testing when appropriate
- Maintain or improve code coverage with new changes

### Test Markers
- Use `@pytest.mark.dev_only` for tests that should only run on the main branch
- Tests should not require external resources unless mocked or recorded (use `pytest-recording`)

### Fixtures and Test Data
- Use `pytest-datadir` for test data files
- Create reusable fixtures in `conftest.py` files
- Keep test data minimal and focused

## Documentation

### Docstring Format
```python
def function_name(param: str, optional: int = 0) -> bool:
    """Brief one-line summary of the function.

    More detailed description if needed. Explain what the function does,
    not how it does it (that's what code is for).

    Args:
        param: Description of param
        optional: Description of optional parameter (default: 0)

    Returns:
        Description of return value

    Raises:
        FFMpegValueError: When invalid parameters are provided

    Example:
        >>> result = function_name("test", optional=5)
        >>> print(result)
        True
    """
```

### Documentation Files
- **README.md**: High-level overview and quick start
- **docs/**: MkDocs documentation (Material theme)
- **Docstrings**: Must be comprehensive for all public APIs
- Update documentation when changing public APIs or behavior

## FFmpeg-Specific Guidelines

### Filter Implementation
- All FFmpeg filters should have proper type annotations
- Filter parameters should be validated at runtime when possible
- Provide comprehensive docstrings with FFmpeg documentation references
- Support both typed and untyped parameter styles

### Stream Handling
- Use `VideoStream`, `AudioStream`, `AVStream`, and `SubtitleStream` classes appropriately
- Maintain filter graph integrity with proper DAG structures
- Support lazy evaluation patterns for filter chains

### Error Handling
- Use custom exceptions: `FFMpegExecuteError`, `FFMpegTypeError`, `FFMpegValueError`
- Provide clear, actionable error messages
- Include context about what went wrong and how to fix it

## Git and Version Control

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb in imperative mood (e.g., "Add", "Fix", "Update")
- Reference issue numbers when applicable

### File Exclusions
- Never commit `__pycache__/`, `*.pyc`, `.pytest_cache/`
- Never commit build artifacts: `dist/`, `build/`, `*.egg-info/`
- Never commit virtual environments or dependencies: `.venv/`, `venv/`, `node_modules/`
- Never commit IDE-specific files unless they're in `.vscode/` and meant to be shared
- See `.gitignore` for complete list

### Pull Request Guidelines
- Ensure all tests pass before submitting
- Ensure code is formatted with `ruff format`
- Ensure no linting errors with `ruff check`
- Ensure type checking passes with `mypy`
- Update documentation if changing public APIs
- Add tests for new functionality

## Security and Best Practices

### Code Security
- Never commit secrets, API keys, or credentials
- Validate all external inputs
- Use subprocess safely when executing FFmpeg commands
- Be cautious with user-provided file paths

### Performance Considerations
- Keep filter graph construction efficient
- Use lazy evaluation when appropriate
- Avoid unnecessary type conversions
- Cache computed values when safe to do so

## Common Patterns

### Adding a New Filter
1. Generate filter stubs from FFmpeg documentation (see `src/scripts/parse_docs/`)
2. Add proper type annotations
3. Write comprehensive docstrings with examples
4. Add unit tests covering various parameter combinations
5. Update filter index if needed

### Modifying Existing Code
1. Run existing tests to ensure they pass
2. Make minimal, focused changes
3. Update tests to cover new behavior
4. Run linters and type checkers
5. Update documentation as needed

### Debugging Issues
- Use `pytest -v` for verbose test output
- Use `pytest -s` to see print statements
- Use `pytest --pdb` to drop into debugger on failures
- Check FFmpeg output with `ffmpeg.compile()` for command inspection

## Useful Commands Reference

```bash
# Development setup
uv pip install --group dev

# Testing
pytest src/ffmpeg --cov=./src/ffmpeg
pytest -v -s  # verbose with output

# Linting and formatting
ruff check --fix src/
ruff format src/
mypy src/ffmpeg/

# Pre-commit hooks
pre-commit install
pre-commit run --all-files

# Building and publishing
python -m build
```

## Additional Resources

- FFmpeg Documentation: https://ffmpeg.org/documentation.html
- Project Documentation: https://livingbio.github.io/typed-ffmpeg/
- Issue Tracker: https://github.com/livingbio/typed-ffmpeg/issues
