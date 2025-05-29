"""
Module for analyzing media files with ffprobe.

This module provides functionality to extract detailed metadata from media files
using FFmpeg's ffprobe utility. It returns a structured representation of the
file's format, streams, and other relevant information.
"""

import logging
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import (
    Any,
    TypeVar,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

from ..exceptions import FFMpegExecuteError
from ..utils.escaping import convert_kwargs_to_cmd_line_args
from ..utils.run import command_line
from .schema import ffprobeType

logger = logging.getLogger(__name__)

T = TypeVar("T")


def _xml_to_dict(element: ET.Element) -> dict[str, Any]:
    """
    Convert an XML element to a dictionary, handling nested elements and attributes.
    Always treat repeated tags as lists, even if only one.
    """
    result: dict[str, Any] = {}
    # Add attributes
    for key, value in element.attrib.items():
        result[key] = value
    # Count child tags
    tag_count = {}
    for child in element:
        tag_count[child.tag] = tag_count.get(child.tag, 0) + 1
    # Handle child elements
    for child in element:
        child_dict = _xml_to_dict(child)
        if tag_count[child.tag] > 1:
            if child.tag not in result:
                result[child.tag] = []
            result[child.tag].append(child_dict)
        else:
            result[child.tag] = child_dict
    # If no attributes and no children, use text content
    if not result and element.text and element.text.strip():
        return element.text.strip()
    return result


def _convert_to_dataclass(data: dict[str, Any], cls: type[T]) -> T:
    """
    Recursively convert a dictionary to a dataclass instance, handling nested dataclasses.
    Handles tuple fields that get a single dict by wrapping it in a list.
    """
    if data is None:
        return None
    # If cls is a string, resolve it to the actual class object
    if isinstance(cls, str):
        schema_globals = sys.modules[__name__].__dict__
        if cls in schema_globals:
            cls = schema_globals[cls]
        else:
            raise TypeError(
                f"Cannot resolve class name '{cls}' in _convert_to_dataclass"
            )
    module_globals = sys.modules[cls.__module__].__dict__
    type_hints = get_type_hints(cls, globalns=module_globals)
    kwargs: dict[str, Any] = {}
    for field_name, field_type in type_hints.items():
        if field_name not in data:
            continue
        value = data[field_name]
        # Handle Optional types
        if get_origin(field_type) is Union:
            inner_type = next(t for t in get_args(field_type) if t is not type(None))
            if value is None:
                kwargs[field_name] = None
                continue
            field_type = inner_type
        # Handle tuples of dataclasses
        if get_origin(field_type) is tuple:
            inner_type = get_args(field_type)[0]
            # If value is a dict, wrap in a list
            if isinstance(value, dict):
                value = [value]
            if isinstance(value, list | tuple):
                kwargs[field_name] = tuple(
                    _convert_to_dataclass(item, inner_type) for item in value
                )
            else:
                kwargs[field_name] = ()  # Empty tuple instead of None
            continue
        # Handle nested dataclasses
        if hasattr(field_type, "__dataclass_fields__"):
            kwargs[field_name] = _convert_to_dataclass(value, field_type)
            continue
        # Handle primitive types
        kwargs[field_name] = value
    return cls(**kwargs)


def _normalize_ffprobe_dict(data: Any) -> Any:
    # If it's a list, normalize each item
    if isinstance(data, list):
        return [_normalize_ffprobe_dict(item) for item in data]
    # If it's a dict, check for known fields that need wrapping
    if isinstance(data, dict):
        # Known fields that should be wrapped in a dict with their key
        wrap_fields = [
            ("tags", "tag"),
            ("streams", "stream"),
            ("programs", "program"),
            ("chapters", "chapter"),
            ("library_versions", "library_version"),
            ("pixel_formats", "pixel_format"),
            ("packets", "packet"),
            ("frames", "frame"),
            ("packets_and_frames", "packet"),
        ]
        # First, wrap if needed
        for parent, child in wrap_fields:
            if child in data and parent not in data:
                val = data[child]
                if isinstance(val, list):
                    data[parent] = {child: val}
                else:
                    data[parent] = {child: [val]}
                del data[child]
        # Then, recursively normalize all values (but not inside just-wrapped dicts)
        for k, v in list(data.items()):
            # Don't recurse into just-wrapped dicts
            if any(k == parent for parent, _ in wrap_fields):
                continue
            data[k] = _normalize_ffprobe_dict(v)
        return data
    return data


def probe(
    filename: str | Path,
    cmd: str = "ffprobe",
    timeout: int | None = None,
    **kwargs: Any,
) -> ffprobeType:
    """
    Analyze a media file using ffprobe and return its metadata as an FFProbe dataclass.

    This function executes ffprobe to extract detailed information about a media file,
    including format metadata (container format, duration, bitrate) and stream information
    (codecs, resolution, sample rate, etc). The result is returned as an FFProbe dataclass
    instance containing the parsed information.

    Args:
        filename: Path to the media file to analyze
        cmd: Path or name of the ffprobe executable (default: "ffprobe")
        timeout: Maximum time in seconds to wait for ffprobe to complete (default: None, wait indefinitely)
        **kwargs: Additional arguments to pass to ffprobe as command line parameters
            (e.g., loglevel="quiet", skip_frame="nokey")

    Returns:
        An FFProbe dataclass instance containing the parsed information from ffprobe

    Raises:
        FFMpegExecuteError: If ffprobe returns a non-zero exit code
        subprocess.TimeoutExpired: If the timeout is reached before ffprobe completes

    Example:
        ```python
        info = probe("video.mp4")
        print(f"Program version: {info.program_version.version}")
        print(f"Library versions: {len(info.library_versions.library_version)}")
        ```
    """
    args = [
        cmd,
        "-show_format",
        "-show_streams",
        "-show_chapters",
        "-show_programs",
        "-show_packets",
        "-show_frames",
        "-of",
        "xml",
    ]
    args += convert_kwargs_to_cmd_line_args(kwargs)
    args += [str(filename)]

    logger.info("Running ffprobe command: %s", command_line(args))
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if timeout is not None:
        out, err = p.communicate(timeout=timeout)
    else:
        out, err = p.communicate()

    retcode = p.poll()
    if p.returncode != 0:
        raise FFMpegExecuteError(
            retcode=retcode, cmd=command_line(args), stdout=out, stderr=err
        )

    # Parse XML output
    xml_data = out.decode("utf-8")
    root = ET.fromstring(xml_data)

    # Convert XML to dictionary structure
    data = _xml_to_dict(root)

    # Handle the root element name
    if "ffprobe" in data:
        data = data["ffprobe"]
    data = _normalize_ffprobe_dict(data)

    logger.debug("Parsed XML dict: %r", data)
    return _convert_to_dataclass(data, ffprobeType)
