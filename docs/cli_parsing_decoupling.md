# CLI Parsing and Validation Decoupling

This document explains the refactored CLI parsing functionality that separates syntax parsing from option validation, enabling more flexible usage scenarios and potential package size reduction.

## Overview

The CLI parsing functionality has been refactored to decouple:
- **Syntax Parsing**: Tokenizing and extracting option names/values from command-line strings
- **Validation**: Checking whether options exist and are valid for their context (input/output/global)

This separation enables:
1. **Parse-only scenarios** where you only need to extract the structure without validation
2. **Package size reduction** by not requiring the bundled options dictionary when validation is disabled
3. **Flexible validation** where you can validate later or use custom validation logic
4. **Backward compatibility** with all existing code

## API Changes

### Main Parse Function

The main `parse()` function now accepts an optional `validate` parameter:

```python
from ffmpeg.compile.compile_cli import parse

# Default behavior (with validation) - backward compatible
stream = parse("ffmpeg -i input.mp4 -vcodec libx264 output.mp4")

# Parse without validation - enables package size reduction
stream = parse("ffmpeg -i input.mp4 -vcodec libx264 output.mp4", validate=False)
```

### New Syntax-Only Parsing Functions

These functions extract option structure without requiring the options dictionary:

```python
from ffmpeg.compile.compile_cli import (
    parse_options,
    parse_input_syntax, 
    parse_output_syntax,
    parse_global_syntax
)

# Parse command-line options into structured format
tokens = ["-vcodec", "libx264", "-b:v", "1000k", "-y"]
parsed = parse_options(tokens)
# Result: {"vcodec": ["libx264"], "b:v": ["1000k"], "y": [None]}

# Parse input file specifications 
input_tokens = ["-ss", "10", "-i", "input.mp4"]
inputs = parse_input_syntax(input_tokens)
# Result: [("input.mp4", {"ss": ["10"]})]

# Parse output file specifications
output_tokens = ["-vcodec", "libx264", "output.mp4"]
outputs = parse_output_syntax(output_tokens)
# Result: [("output.mp4", {"vcodec": ["libx264"]})]

# Parse global options
global_tokens = ["-y", "-loglevel", "error", "-i", "input.mp4"]
global_opts, remaining = parse_global_syntax(global_tokens)
# Result: ({"y": [None], "loglevel": ["error"]}, ["-i", "input.mp4"])
```

### New Validation Utilities

These functions validate parsed options against the FFmpeg options dictionary:

```python
from ffmpeg.compile.compile_cli import (
    validate_parsed_options,
    validate_input_options,
    validate_output_options, 
    validate_global_options,
    get_options_dict
)

# Parse options first
parsed = parse_options(["-vcodec", "libx264", "-unknown", "value"])

# Load options dictionary (can be cached/reused)
ffmpeg_options = get_options_dict()

# Validate with filtering by context
valid_output = validate_parsed_options(parsed, ffmpeg_options, "output")
# Result: {"vcodec": "libx264"}  # unknown option filtered out

# Convenience functions for specific contexts
valid_input = validate_input_options(parsed, ffmpeg_options)
valid_output = validate_output_options(parsed, ffmpeg_options)  
valid_global = validate_global_options(parsed, ffmpeg_options)

# Validate without options dict (will load it)
valid_output = validate_output_options(parsed)
```

## Usage Scenarios

### 1. Backward Compatibility (Default)

Existing code continues to work unchanged:

```python
# This still works exactly as before
stream = parse("ffmpeg -i input.mp4 -vcodec libx264 output.mp4")
```

### 2. Parse-Only for Analysis

Extract command structure without validation:

```python
# Parse command structure without requiring options data
stream = parse(command, validate=False)

# Unknown/custom options are preserved
command_with_custom = "ffmpeg -i input.mp4 -custom_option value output.mp4"
stream = parse(command_with_custom, validate=False)
compiled = compile(stream)
# Result includes -custom_option value
```

### 3. Custom Validation Logic

Parse first, then apply custom validation:

```python
# Parse without validation
parsed_global, remaining = parse_global_syntax(tokens)
parsed_inputs = parse_input_syntax(remaining[:input_end])
parsed_outputs = parse_output_syntax(remaining[input_end:])

# Apply custom validation logic
if custom_validation_needed:
    # Your custom validation here
    validated_inputs = custom_validate_inputs(parsed_inputs)
    validated_outputs = custom_validate_outputs(parsed_outputs)
else:
    # Use standard validation
    ffmpeg_options = get_options_dict()
    validated_inputs = [
        validate_input_options(opts, ffmpeg_options) 
        for filename, opts in parsed_inputs
    ]
```

### 4. Package Size Reduction

For applications that only need parsing without validation:

```python
# This doesn't load the bundled options dictionary
# Reducing memory usage and potential package size
stream = parse(command, validate=False)

# Or use the low-level functions directly
options = parse_options(tokens)  # No options dict required
```

## Implementation Details

### Validation Behavior

When validation is enabled (default):
- Unknown options are filtered out
- Options are checked against their valid contexts (input/output/global)
- Boolean options are properly converted
- Stream specifiers are handled correctly

When validation is disabled:
- All parsed options are preserved
- Unknown/custom options pass through unchanged
- No options dictionary loading is required
- Useful for parse-only scenarios

### Performance Considerations

- **With validation**: Options dictionary is loaded once and cached
- **Without validation**: No options loading, faster startup
- **Mixed usage**: Load options dict once, reuse for multiple validations

### Error Handling

Syntax parsing errors (malformed command structure) still raise exceptions.
Only validation errors are controlled by the `validate` parameter.

## Migration Guide

### For Existing Code
No changes required - all existing code continues to work unchanged.

### For New Parse-Only Use Cases
```python
# Old: Would load options dict even if not needed
stream = parse(command)

# New: Skip validation for parse-only scenarios  
stream = parse(command, validate=False)
```

### For Custom Validation Needs
```python
# Old: Had to work around built-in validation
# (difficult/impossible)

# New: Parse first, validate later with custom logic
global_opts, remaining = parse_global_syntax(tokens)
# ... apply custom validation logic
validated = custom_validate(global_opts)
```

## Testing

Comprehensive tests cover:
- All syntax-only parsing functions
- All validation utilities  
- Main parse function with both validation modes
- Backward compatibility scenarios
- Package size reduction scenarios
- Complex integration cases

Run the tests:
```bash
pytest src/ffmpeg/compile/tests/test_syntax_validation_decoupling.py -v
```

## Future Enhancements

This decoupled architecture enables future enhancements:
- Plugin-based validation systems
- Context-aware option suggestions
- Incremental/streaming parsing
- Alternative validation backends
- Reduced package distributions (parse-only builds)