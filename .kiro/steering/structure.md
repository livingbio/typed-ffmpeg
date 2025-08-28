# Project Structure

## Source Code Organization

### Main Package (`src/ffmpeg/`)
- **`__init__.py`**: Main API exports and public interface
- **`base.py`**: Core functions for filter creation (`input`, `output`, `vfilter`, `afilter`)
- **`filters.py`**: Auto-generated filter definitions (comprehensive FFmpeg filter support)
- **`exceptions.py`**: Custom exception classes (`FFMpegExecuteError`, `FFMpegTypeError`, etc.)
- **`schema.py`**: Type definitions and validation schemas
- **`types.py`**: Core type definitions

### Core Modules
- **`dag/`**: Directed Acyclic Graph implementation for filter chains
  - Stream representation and manipulation
  - Node types (FilterNode, GlobalNode, etc.)
  - Input/output handling
- **`streams/`**: Stream type implementations
  - `VideoStream`, `AudioStream`, `AVStream`, `SubtitleStream`
- **`compile/`**: FFmpeg command compilation and execution
- **`ffprobe/`**: Media file analysis and metadata extraction

### Generated Code
- **`codecs/`**: Auto-generated codec definitions
- **`formats/`**: Auto-generated format definitions  
- **`muxers/`**: Auto-generated muxer/demuxer definitions
- **`options/`**: Auto-generated option definitions
- **`sources.py`**: Auto-generated source definitions
- **`expressions.py`**: Auto-generated expression helpers

### Utilities
- **`utils/`**: Helper utilities and common functionality
- **`common/`**: Shared constants and cached data

## Code Generation (`scripts/`)
- **`code_gen/`**: Code generation tools for FFmpeg bindings
- **`compile-readme.py`**: README compilation from notebooks
- **`gen_ref_pages.py`**: Documentation reference generation

## Testing Structure
- **`src/ffmpeg/tests/`**: Unit tests organized by module
- **Snapshot testing**: Uses syrupy for regression testing
- **Test markers**: `dev_only` for development-specific tests

## Documentation (`docs/`)
- **`index.md`**: Main documentation entry point
- **`usage/`**: Usage examples and guides
- **`media/`**: Images and media assets
- **`faq.md`**: Frequently asked questions

## Configuration Files
- **Root level**: Project metadata and configuration
- **`.kiro/`**: Kiro-specific configuration and steering
- **`.github/`**: GitHub Actions and workflows
- **`.devcontainer/`**: Development container setup

## Key Architectural Patterns

### Stream-Based API
- Fluent interface with method chaining
- Type-safe stream operations
- Immutable stream objects

### Code Generation
- FFmpeg documentation parsing
- Automatic filter/codec binding generation
- Cached generation results for performance

### Type Safety
- Comprehensive type annotations
- Runtime type validation
- Static analysis with mypy

### Modular Design
- Clear separation between core, generated, and utility code
- Plugin-style architecture for filters and codecs
- Extensible through custom filter functions