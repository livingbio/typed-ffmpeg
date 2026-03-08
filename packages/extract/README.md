# ffmpeg-extract

Extract structured metadata from FFmpeg sources.

## Overview

`ffmpeg-extract` is a Python package that extracts structured metadata from various FFmpeg sources including:

- **C Header Files**: Parse FFmpeg source code headers to extract filter, codec, and format definitions
- **Help Output**: Parse `ffmpeg --help` output for options and parameters
- **Documentation**: Parse FFmpeg documentation for descriptions and examples

The extracted metadata is output as standardized JSON schemas that can be consumed by code generation tools.

## Installation

```bash
# Install from source
cd packages/extract
uv pip install -e .

# Or install from PyPI (when published)
uv pip install ffmpeg-extract
```

## Usage

### Command Line

```bash
# Extract all metadata from FFmpeg source
ffmpeg-extract --source /path/to/ffmpeg --output metadata/

# Extract only filters
ffmpeg-extract filters --source /path/to/ffmpeg --output filters.json

# Parse help output
ffmpeg-extract parse-help --help-output help.txt --output options.json

# Parse documentation
ffmpeg-extract parse-docs --docs-dir /path/to/docs --output docs.json
```

### Python API

```python
from ffmpeg_extract.parse_c import parse_filters
from ffmpeg_extract.parse_help import parse_help_output
from ffmpeg_extract.parse_docs import parse_documentation

# Parse C headers
filters = parse_filters("/path/to/ffmpeg/libavfilter")

# Parse help output
options = parse_help_output("ffmpeg --help full")

# Parse documentation
docs = parse_documentation("/path/to/ffmpeg/doc")
```

## Output Schema

The extracted metadata follows a standardized JSON schema:

### Filter Schema

```json
{
  "name": "hflip",
  "description": "Horizontally flip the input video",
  "inputs": [
    {"type": "video", "name": "default"}
  ],
  "outputs": [
    {"type": "video", "name": "default"}
  ],
  "options": [
    {
      "name": "enable",
      "type": "string",
      "description": "Enable expression"
    }
  ]
}
```

### Codec Schema

```json
{
  "name": "libx264",
  "type": "video",
  "description": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
  "encoder": true,
  "decoder": false,
  "options": [...]
}
```

## Components

### parse_c

Parses FFmpeg C header files to extract:
- Filter definitions from `libavfilter/`
- Codec definitions from `libavcodec/`
- Format definitions from `libavformat/`

### parse_help

Parses FFmpeg help output to extract:
- Global options
- Input/output options
- Codec-specific options

### parse_docs

Parses FFmpeg documentation to extract:
- Filter descriptions
- Usage examples
- Parameter details

## Development

```bash
# Install development dependencies
cd packages/extract
uv pip install -e ".[dev]"

# Run tests
pytest

# Run linting
ruff check src/

# Type checking
mypy src/
```

## License

MIT License - see LICENSE file for details

## Contributing

See the main repository's CONTRIBUTING.md for guidelines.
