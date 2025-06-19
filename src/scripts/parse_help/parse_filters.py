import re

from .schema import FFMpegAVOption, FFMpegFilter
from .utils import parse_av_option, parse_section_tree, run_ffmpeg_command


def _parse_list(text: str) -> list[FFMpegFilter]:
    """
    Parse the help text for filters.

    Args:
        text: The help text to parse from ffmpeg command output

    Returns:
        A list of format instances

    Example:
        ```
        Filters:
        T.. = Timeline support
        .S. = Slice threading
        ..C = Command support
        A = Audio input/output
        V = Video input/output
        N = Dynamic number and/or type of input/output
        | = Source or sink filter
        ... abench            A->A       Benchmark part of a filtergraph.
        ..C acompressor       A->A       Audio compressor.
        ... acontrast         A->A       Simple audio dynamic range compression/expansion filter.
        ... acopy             A->A       Copy the input audio unchanged to the output.
        ... acue              A->A       Delay filtering to match a cue.
        ... acrossfade        AA->A      Cross fade two input audio streams.
        .S. acrossover        A->N       Split audio into per-bands streams.
        ```
    """
    output: list[FFMpegFilter] = []
    lines = text.splitlines()
    re_pattern = re.compile(
        r"^\s*(?P<flag>[\w\.]{3})\s*(?P<name>\w+)\s+(?P<io_flags>[\w\|]+\-\>[\w\|]+)\s+(?P<help>.*)$"
    )

    for line in lines:
        match = re_pattern.match(line)
        if match:
            flags, name, io_flags, description = match.groups()
            output.append(
                FFMpegFilter(
                    name=name, flags=flags, io_flags=io_flags, help=description
                )
            )
    return output


def _extract_list() -> list[FFMpegFilter]:
    """
    Get the help text for all filters.

    Returns:
        A list of filters
    """
    return _parse_list(run_ffmpeg_command(["-filters"]))


def _parse_filter(text: str) -> list[FFMpegAVOption]:
    """
    Parse the help text for a filter.
    """
    tree = parse_section_tree(text)
    for section in tree:
        if "AVOptions" in section:
            return parse_av_option(section, tree)
    return []

def _extract_filter(filter: str) -> list[FFMpegAVOption]:
    """
    Get the help text for a filter.
    """
    return _parse_filter(run_ffmpeg_command(["-h", f"filter={filter}"]))

def extract() -> list[FFMpegFilter]:
    """
    Get the help text for all filters.
    """
    output: list[FFMpegFilter] = []
    for filter in _extract_list():
        options = _extract_filter(filter.name)
        output.append(
            FFMpegFilter(
                name=filter.name, flags=filter.flags, io_flags=filter.io_flags, help=filter.help, options=tuple(options)
            )
        )
    return output