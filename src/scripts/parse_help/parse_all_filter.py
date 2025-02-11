import re
import subprocess

from ffmpeg.common.schema import FFMpegFilter, FFMpegIOType, StreamType


def extract_all_filters_text() -> str:
    """
    Get the help text for all filters.

    Returns:
        The help text.
    """

    result = subprocess.run(
        ["ffmpeg", "-filters", "-hide_banner"], stdout=subprocess.PIPE, text=True
    )
    return result.stdout


def _extract_io(io: str) -> tuple[tuple[FFMpegIOType, ...], tuple[FFMpegIOType, ...]]:
    """
    Extract the input or output stream type from the help text.

    Args:
        io: The input or output text.

    Returns:
        The stream type.
    """
    io = io.strip()
    input, output = io.split("->")

    def _parse_io(text: str) -> tuple[FFMpegIOType, ...]:
        if text == "|":
            return ()
        elif text == "N":
            return ()

        output = []
        for part in text:
            if part == "V":
                output.append(FFMpegIOType(type=StreamType.video))
            elif part == "A":
                output.append(FFMpegIOType(type=StreamType.audio))
            else:
                raise ValueError(f"Unknown stream type: {part}")

        return tuple(output)

    return _parse_io(input), _parse_io(output)


def extract_filter_info(text: str) -> list[FFMpegFilter]:
    """
    Extract the filter information from the help text.

    Args:
        text: The help text.

    Returns:
        The filter information.

    """

    lines = text.splitlines()[8:]

    output: list[FFMpegFilter] = []

    for line in lines:
        match: list[tuple[str, str, str, str]] = re.findall(
            r"(?P<flags>[^\s]+)\s+(?P<name>[\w]+)\s+(?P<io>[^ ]+) (?P<desc>.*)", line
        )
        assert match, f"Failed to parse line: {line}"
        flags, name, io, desc = [k.strip() for k in match[0]]

        input_typing, output_typing = _extract_io(io)
        output.append(
            FFMpegFilter(
                name=name,
                description=desc,
                # Flags
                is_support_timeline="T" in flags,
                is_support_slice_threading="S" in flags,
                is_support_command="C" in flags,
                # NOTE: cannot get framesync from the help text
                is_filter_sink="->|" in io,
                is_filter_source="|->" in io,
                # IO Typing
                is_dynamic_input="N->" in io,
                is_dynamic_output="->N" in io,
                stream_typings_input=input_typing,
                stream_typings_output=output_typing,
            )
        )

    return output


def extract() -> list[FFMpegFilter]:
    """
    Extract all the filter information.

    Returns:
        The filter information.
    """
    return extract_filter_info(extract_all_filters_text())
