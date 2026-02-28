"""
A module for parsing FFmpeg help text output into structured option data.

This module processes the output of commands like `ffmpeg -h full` or `ffmpeg -h filter=scale`
into a structured format. It handles both general FFmpeg options and AVOptions.

The parsing process follows these steps:
1. The help text is parsed into a hierarchical tree structure
2. The tree is then traversed to extract individual options
3. Options are converted into strongly-typed FFMpegOption objects

The module provides two main functions:
- `_parse()`: Internal function that parses help text into structured options
- `extract()`: Public function that runs FFmpeg and extracts all available options

Example usage:
```python
from parse_help import extract

options = extract()
for option in options[:5]:
    print(f"{option.name}: {option.type}")
```
"""

from .schema import FFMpegOption
from .utils import (
    parse_av_option,
    parse_general_option,
    parse_section_tree,
    run_ffmpeg_command,
)


def _parse(help_text: str) -> list[FFMpegOption]:
    """
    Parse FFmpeg help text into a structured list of options.

    This internal function processes both general FFmpeg options and AVOptions from
    the provided help text. It handles complex option hierarchies, including nested
    flags and their associated values.

    Args:
        help_text: Raw help text output from FFmpeg commands like
            `ffmpeg -h full` or `ffmpeg -h filter=scale`

    Returns:
        A list of parsed FFmpeg options with their metadata,
            including name, type, description, default values, and constraints

    Raises:
        ValueError: If the help text cannot be parsed or is malformed
        RuntimeError: If required sections are missing from the help text

    Example:
        ```python
        help_output = '''
        AVOptions:
        -b                 <int64>      E..VA...... set bitrate (in bits/s) (from 0 to I64_MAX) (default 200000)
        -ab                <int64>      E...A...... set bitrate (in bits/s) (from 0 to INT_MAX) (default 128000)
        -bt                <int>        E..VA...... Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to minimum/maximum bitrate. Lowering tolerance too much has an adverse effect on quality. (from 0 to INT_MAX) (default 4000000)
        -flags             <flags>      ED.VAS..... (default 0)
           flush_packets                E.......... reduce the latency by flushing out packets immediately
           ignidx                       .D......... ignore index
           genpts                       .D......... generate pts
        '''
        options = _parse(help_output)
        len(options)  # Returns 6
        options[0].name  # Returns 'b'
        options[0].type  # Returns 'int64'
        ```

    """
    tree = parse_section_tree(help_text)
    output: list[FFMpegOption] = []

    for section in tree:
        if "options" in section:
            output.extend(parse_general_option(section, tree))
        elif "AVOptions" in section:
            # FFmpeg's AVOptions
            output.extend(parse_av_option(section, tree))

    return output


def extract() -> list[FFMpegOption]:
    """
    Extract and parse all options from FFmpeg's full help output.

    This function executes `ffmpeg -h full` and processes its output to create a
    comprehensive list of all available FFmpeg options, including both general
    options and AVOptions. This is the main entry point for extracting FFmpeg
    option metadata.

    Returns:
        A complete list of all available FFmpeg options with
            their metadata, including name, type, description, default values,
            and constraints

    Raises:
        FileNotFoundError: If the FFmpeg executable is not found in the system PATH
        subprocess.CalledProcessError: If the FFmpeg command fails to execute
        ValueError: If the help text output cannot be parsed
        RuntimeError: If the help text is malformed or missing required sections

    Example:
        ```python
        options = extract()
        len(options)  # Should be several hundred options (500+)

        # Find all video codec options
        video_options = [opt for opt in options if "V" in opt.flags]
        len(video_options)  # Returns 100+

        # Find options with default values
        options_with_defaults = [opt for opt in options if opt.default is not None]
        len(options_with_defaults)  # Returns 200+
        ```

    """
    text = run_ffmpeg_command(["-h", "full"])
    return _parse(text)
