"""
Module for analyzing media files with ffprobe.

This module provides functionality to extract detailed metadata from media files
using FFmpeg's ffprobe utility. It returns a structured representation of the
file's format, streams, and other relevant information.
"""

import json
import logging
import subprocess
from pathlib import Path
from typing import (
    Any,
    Optional,
    TypeVar,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

from .exceptions import FFMpegExecuteError
from .utils.escaping import convert_kwargs_to_cmd_line_args
from .utils.run import command_line

logger = logging.getLogger(__name__)
from dataclasses import dataclass, field

T = TypeVar("T")
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    pass


@dataclass(frozen=True, kw_only=True)
class ffprobeType:
    program_version: Optional["programVersionType"] = None
    library_versions: Optional["libraryVersionsType"] = None
    pixel_formats: Optional["pixelFormatsType"] = None
    packets: Optional["packetsType"] = None
    frames: Optional["framesType"] = None
    packets_and_frames: Optional["packetsAndFramesType"] = None
    programs: Optional["programsType"] = None
    streams: Optional["streamsType"] = None
    chapters: Optional["chaptersType"] = None
    format: Optional["formatType"] = None
    error: Optional["errorType"] = None


@dataclass(frozen=True, kw_only=True)
class packetsType:
    packet: tuple["packetType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class framesType:
    frame: Optional["frameType"] = None
    subtitle: Optional["subtitleType"] = None


@dataclass(frozen=True, kw_only=True)
class packetsAndFramesType:
    packet: Optional["packetType"] = None
    frame: Optional["frameType"] = None
    subtitle: Optional["subtitleType"] = None


@dataclass(frozen=True, kw_only=True)
class tagsType:
    tag: tuple["tagType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class packetType:
    codec_type: str | None = None
    stream_index: int | None = None
    pts: int | None = None
    pts_time: float | None = None
    dts: int | None = None
    dts_time: float | None = None
    duration: int | None = None
    duration_time: float | None = None
    size: int | None = None
    pos: int | None = None
    flags: str | None = None
    data: str | None = None
    data_hash: str | None = None
    tags: Optional["tagsType"] = None
    side_data_list: Optional["packetSideDataListType"] = None


@dataclass(frozen=True, kw_only=True)
class packetSideDataListType:
    side_data: tuple["packetSideDataType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class packetSideDataType:
    type: str | None = None
    side_datum: tuple["packetSideDatumType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class packetSideDatumType:
    key: str | None = None
    value: str | None = None


@dataclass(frozen=True, kw_only=True)
class frameType:
    media_type: str | None = None
    stream_index: int | None = None
    key_frame: int | None = None
    pts: int | None = None
    pts_time: float | None = None
    pkt_dts: int | None = None
    pkt_dts_time: float | None = None
    best_effort_timestamp: int | None = None
    best_effort_timestamp_time: float | None = None
    pkt_duration: int | None = None
    pkt_duration_time: float | None = None
    duration: int | None = None
    duration_time: float | None = None
    pkt_pos: int | None = None
    pkt_size: int | None = None
    sample_fmt: str | None = None
    nb_samples: int | None = None
    channels: int | None = None
    channel_layout: str | None = None
    width: int | None = None
    height: int | None = None
    crop_top: int | None = None
    crop_bottom: int | None = None
    crop_left: int | None = None
    crop_right: int | None = None
    pix_fmt: str | None = None
    sample_aspect_ratio: str | None = None
    pict_type: str | None = None
    coded_picture_number: int | None = None
    display_picture_number: int | None = None
    interlaced_frame: int | None = None
    top_field_first: int | None = None
    repeat_pict: int | None = None
    color_range: str | None = None
    color_space: str | None = None
    color_primaries: str | None = None
    color_transfer: str | None = None
    chroma_location: str | None = None
    tags: Optional["tagsType"] = None
    logs: Optional["logsType"] = None
    side_data_list: Optional["frameSideDataListType"] = None


@dataclass(frozen=True, kw_only=True)
class logsType:
    log: tuple["logType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class logType:
    context: str | None = None
    level: int | None = None
    category: int | None = None
    parent_context: str | None = None
    parent_category: int | None = None
    message: str | None = None


@dataclass(frozen=True, kw_only=True)
class frameSideDataListType:
    side_data: tuple["frameSideDataType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class frameSideDataType:
    side_data_type: str | None = None
    side_data_size: int | None = None
    timecode: str | None = None
    timecodes: Optional["frameSideDataTimecodeList"] = None
    components: Optional["frameSideDataComponentList"] = None
    side_datum: tuple["frameSideDatumType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class frameSideDatumType:
    key: str | None = None
    value: str | None = None


@dataclass(frozen=True, kw_only=True)
class frameSideDataTimecodeList:
    timecode: tuple["frameSideDataTimecodeType", ...] | None = field(
        default_factory=tuple
    )


@dataclass(frozen=True, kw_only=True)
class frameSideDataTimecodeType:
    value: str | None = None


@dataclass(frozen=True, kw_only=True)
class frameSideDataComponentList:
    component: tuple["frameSideDataComponentType", ...] | None = field(
        default_factory=tuple
    )


@dataclass(frozen=True, kw_only=True)
class frameSideDataComponentType:
    pieces: Optional["frameSideDataPieceList"] = None
    side_datum: tuple["frameSideDatumType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class frameSideDataPieceList:
    piece: tuple["frameSideDataPieceType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class frameSideDataPieceType:
    side_datum: tuple["frameSideDatumType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class subtitleType:
    media_type: str | None = None
    pts: int | None = None
    pts_time: float | None = None
    format: int | None = None
    start_display_time: int | None = None
    end_display_time: int | None = None
    num_rects: int | None = None


@dataclass(frozen=True, kw_only=True)
class streamsType:
    stream: tuple["streamType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class programsType:
    program: tuple["programType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class streamDispositionType:
    default: int | None = None
    dub: int | None = None
    original: int | None = None
    comment: int | None = None
    lyrics: int | None = None
    karaoke: int | None = None
    forced: int | None = None
    hearing_impaired: int | None = None
    visual_impaired: int | None = None
    clean_effects: int | None = None
    attached_pic: int | None = None
    timed_thumbnails: int | None = None
    non_diegetic: int | None = None
    captions: int | None = None
    descriptions: int | None = None
    metadata: int | None = None
    dependent: int | None = None
    still_image: int | None = None


@dataclass(frozen=True, kw_only=True)
class streamType:
    index: int | None = None
    codec_name: str | None = None
    codec_long_name: str | None = None
    profile: str | None = None
    codec_type: str | None = None
    codec_tag: str | None = None
    codec_tag_string: str | None = None
    extradata: str | None = None
    extradata_size: int | None = None
    extradata_hash: str | None = None
    width: int | None = None
    height: int | None = None
    coded_width: int | None = None
    coded_height: int | None = None
    closed_captions: bool | None = None
    film_grain: bool | None = None
    has_b_frames: int | None = None
    sample_aspect_ratio: str | None = None
    display_aspect_ratio: str | None = None
    pix_fmt: str | None = None
    level: int | None = None
    color_range: str | None = None
    color_space: str | None = None
    color_transfer: str | None = None
    color_primaries: str | None = None
    chroma_location: str | None = None
    field_order: str | None = None
    refs: int | None = None
    sample_fmt: str | None = None
    sample_rate: int | None = None
    channels: int | None = None
    channel_layout: str | None = None
    bits_per_sample: int | None = None
    initial_padding: int | None = None
    id: str | None = None
    r_frame_rate: str | None = None
    avg_frame_rate: str | None = None
    time_base: str | None = None
    start_pts: int | None = None
    start_time: float | None = None
    duration_ts: int | None = None
    duration: float | None = None
    bit_rate: int | None = None
    max_bit_rate: int | None = None
    bits_per_raw_sample: int | None = None
    nb_frames: int | None = None
    nb_read_frames: int | None = None
    nb_read_packets: int | None = None
    disposition: Optional["streamDispositionType"] = None
    tags: Optional["tagsType"] = None
    side_data_list: Optional["packetSideDataListType"] = None


@dataclass(frozen=True, kw_only=True)
class programType:
    program_id: int | None = None
    program_num: int | None = None
    nb_streams: int | None = None
    pmt_pid: int | None = None
    pcr_pid: int | None = None
    tags: Optional["tagsType"] = None
    streams: Optional["streamsType"] = None


@dataclass(frozen=True, kw_only=True)
class formatType:
    filename: str | None = None
    nb_streams: int | None = None
    nb_programs: int | None = None
    nb_stream_groups: int | None = None
    format_name: str | None = None
    format_long_name: str | None = None
    start_time: float | None = None
    duration: float | None = None
    size: int | None = None
    bit_rate: int | None = None
    probe_score: int | None = None
    tags: Optional["tagsType"] = None


@dataclass(frozen=True, kw_only=True)
class tagType:
    key: str | None = None
    value: str | None = None


@dataclass(frozen=True, kw_only=True)
class errorType:
    code: int | None = None
    string: str | None = None


@dataclass(frozen=True, kw_only=True)
class programVersionType:
    version: str | None = None
    copyright: str | None = None
    build_date: str | None = None
    build_time: str | None = None
    compiler_ident: str | None = None
    configuration: str | None = None


@dataclass(frozen=True, kw_only=True)
class chaptersType:
    chapter: tuple["chapterType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class chapterType:
    id: int | None = None
    time_base: str | None = None
    start: int | None = None
    start_time: float | None = None
    end: int | None = None
    end_time: float | None = None
    tags: tuple["tagsType", ...] | None = field(default_factory=tuple)


@dataclass(frozen=True, kw_only=True)
class libraryVersionType:
    name: str | None = None
    major: int | None = None
    minor: int | None = None
    micro: int | None = None
    version: int | None = None
    ident: str | None = None


@dataclass(frozen=True, kw_only=True)
class libraryVersionsType:
    library_version: tuple["libraryVersionType", ...] | None = field(
        default_factory=tuple
    )


@dataclass(frozen=True, kw_only=True)
class pixelFormatFlagsType:
    big_endian: int | None = None
    palette: int | None = None
    bitstream: int | None = None
    hwaccel: int | None = None
    planar: int | None = None
    rgb: int | None = None
    alpha: int | None = None


@dataclass(frozen=True, kw_only=True)
class pixelFormatComponentType:
    index: int | None = None
    bit_depth: int | None = None


@dataclass(frozen=True, kw_only=True)
class pixelFormatComponentsType:
    component: tuple["pixelFormatComponentType", ...] | None = field(
        default_factory=tuple
    )


@dataclass(frozen=True, kw_only=True)
class pixelFormatType:
    name: str | None = None
    nb_components: int | None = None
    log2_chroma_w: int | None = None
    log2_chroma_h: int | None = None
    bits_per_pixel: int | None = None
    flags: Optional["pixelFormatFlagsType"] = None
    components: Optional["pixelFormatComponentsType"] = None


@dataclass(frozen=True, kw_only=True)
class pixelFormatsType:
    pixel_format: tuple["pixelFormatType", ...] | None = field(default_factory=tuple)


def _convert_to_dataclass(data: dict[str, Any], cls: type[T]) -> T:
    """
    Recursively convert a dictionary to a dataclass instance, handling nested dataclasses.

    Args:
        data: Dictionary containing the data to convert
        cls: The dataclass type to convert to

    Returns:
        An instance of the specified dataclass with all nested structures converted
    """
    if data is None:
        return None

    type_hints = get_type_hints(cls)
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
    args = [cmd, "-show_format", "-show_streams", "-of", "json"]
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

    data = json.loads(out.decode("utf-8"))
    return _convert_to_dataclass(data, ffprobeType)
