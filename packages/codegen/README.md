# ffmpeg-codegen

Code generation framework for FFmpeg SDKs.

## Overview

`ffmpeg-codegen` is a Python package that generates language-specific SDKs from extracted FFmpeg metadata. It provides a flexible, template-based code generation system that can target multiple programming languages.

## Supported Targets

- **Python**: Generate typed-ffmpeg Python SDK
- **TypeScript**: Generate TypeScript SDK (future)
- **Extensible**: Easy to add new language backends

## Installation

```bash
# Install from source
cd packages/codegen
uv pip install -e .

# Or install from PyPI (when published)
uv pip install ffmpeg-codegen
```

## Usage

### Command Line

```bash
# Generate Python SDK
ffmpeg-codegen \
  --metadata metadata/ \
  --target python \
  --output packages/python/src/ffmpeg/

# Generate TypeScript SDK (future)
ffmpeg-codegen \
  --metadata metadata/ \
  --target typescript \
  --output packages/typescript/src/
```

### Python API

```python
from ffmpeg_codegen import CodeGenerator
from ffmpeg_codegen.backends.python import PythonBackend

# Load metadata
metadata = load_metadata("metadata/")

# Create generator
generator = CodeGenerator(
    backend=PythonBackend(),
    metadata=metadata,
)

# Generate code
output_files = generator.generate()

# Write to files
for path, content in output_files.items():
    path.write_text(content)
```

## Architecture

### Pipeline

```
Metadata (JSON) → CodeGenerator → Backend → Output Files
```

### Backends

Each backend implements the code generation for a specific language:

- **PythonBackend**: Generates Python code with type hints
- **TypeScriptBackend**: Generates TypeScript code with interfaces (future)

### Templates

Code generation uses Jinja2 templates for flexibility:

```
templates/
├── python/
│   ├── filter.py.j2        # Filter class template
│   ├── codec.py.j2         # Codec class template
│   └── format.py.j2        # Format class template
└── typescript/
    ├── filter.ts.j2        # Filter interface template
    └── codec.ts.j2         # Codec interface template
```

## Template Variables

Templates have access to metadata and utility functions:

```jinja2
{# Python filter template #}
class {{ filter.name | to_class_name }}(FilterNode):
    """{{ filter.description }}"""
    
    {% for option in filter.options %}
    {{ option.name }}: {{ option.type | to_python_type }}
    {% endfor %}
```

## Customization

### Adding a New Backend

```python
from ffmpeg_codegen.backends.base import Backend

class MyLanguageBackend(Backend):
    """Generate code for MyLanguage."""
    
    def generate_filter(self, filter_def):
        """Generate filter code."""
        template = self.env.get_template("mylang/filter.template")
        return template.render(filter=filter_def)
    
    def generate_codec(self, codec_def):
        """Generate codec code."""
        # Implementation...
```

### Custom Templates

Place custom templates in `templates/<backend>/`:

```bash
templates/
└── mylang/
    ├── filter.template
    └── codec.template
```

## Development

```bash
# Install development dependencies
cd packages/codegen
uv pip install -e ".[dev]"

# Run tests
pytest

# Test code generation
pytest tests/test_backends.py -v

# Run linting
ruff check src/
```

## Generated Code Structure

### Python SDK

```
src/ffmpeg/
├── filters/
│   ├── __init__.py
│   ├── video.py         # Generated video filters
│   ├── audio.py         # Generated audio filters
│   └── ...
├── codecs/
│   ├── encoders.py      # Generated encoders
│   └── decoders.py      # Generated decoders
└── formats/
    ├── muxers.py        # Generated muxers
    └── demuxers.py      # Generated demuxers
```

## Configuration

Create a `codegen.toml` configuration file:

```toml
[backend.python]
output_dir = "packages/python/src/ffmpeg"
template_dir = "templates/python"
type_hints = true
docstrings = true

[backend.typescript]
output_dir = "packages/typescript/src"
template_dir = "templates/typescript"
interfaces = true
jsdoc = true
```

## License

MIT License - see LICENSE file for details

## Contributing

See the main repository's CONTRIBUTING.md for guidelines.
