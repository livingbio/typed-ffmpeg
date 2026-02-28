"""FFprobe XML schema definitions."""

# !/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True, frozen=True)
class ffprobeType:
    """Root type for FFprobe XML output."""

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


@dataclass(kw_only=True, frozen=True)
class packetsType:
    """Container for packet information."""

    packet: tuple["packetType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class framesType:
    """Container for frame information."""

    frame: tuple["frameType", ...] | None = None
    subtitle: tuple["subtitleType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class packetsAndFramesType:
    """Container for both packet and frame information."""

    packet: tuple["packetType", ...] | None = None
    frame: tuple["frameType", ...] | None = None
    subtitle: tuple["subtitleType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class tagsType:
    """Container for tag information."""

    tag: tuple["tagType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class packetType:
    """Information about a single packet."""

    tags: Optional["tagsType"] = None
    side_data_list: Optional["packetSideDataListType"] = None
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


@dataclass(kw_only=True, frozen=True)
class packetSideDataListType:
    """Container for packet side data information."""

    side_data: tuple["packetSideDataType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class packetSideDataType:
    """Information about packet side data."""

    side_datum: tuple["packetSideDatumType", ...] | None = None
    type: str | None = None


@dataclass(kw_only=True, frozen=True)
class packetSideDatumType:
    """Individual packet side data item."""

    key: str | None = None
    value: str | None = None


@dataclass(kw_only=True, frozen=True)
class frameType:
    """Information about a single frame."""

    tags: Optional["tagsType"] = None
    logs: Optional["logsType"] = None
    side_data_list: Optional["frameSideDataListType"] = None
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


@dataclass(kw_only=True, frozen=True)
class logsType:
    """Container for log information."""

    log: tuple["logType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class logType:
    """Information about a single log entry."""

    context: str | None = None
    level: int | None = None
    category: int | None = None
    parent_context: str | None = None
    parent_category: int | None = None
    message: str | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDataListType:
    """Container for frame side data information."""

    side_data: tuple["frameSideDataType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDataType:
    """Information about frame side data."""

    timecodes: Optional["frameSideDataTimecodeList"] = None
    components: Optional["frameSideDataComponentList"] = None
    side_datum: tuple["frameSideDatumType", ...] | None = None
    side_data_type: str | None = None
    side_data_size: int | None = None
    timecode: str | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDatumType:
    """Individual frame side data item."""

    key: str | None = None
    value: str | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDataTimecodeList:
    """Container for frame side data timecode information."""

    timecode: tuple["frameSideDataTimecodeType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDataTimecodeType:
    """Information about frame side data timecode."""

    value: str | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDataComponentList:
    """Container for frame side data component information."""

    component: tuple["frameSideDataComponentType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDataComponentType:
    """Information about frame side data component."""

    pieces: Optional["frameSideDataPieceList"] = None
    side_datum: tuple["frameSideDatumType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDataPieceList:
    """Container for frame side data piece information."""

    piece: tuple["frameSideDataPieceType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class frameSideDataPieceType:
    """Information about frame side data piece."""

    side_datum: tuple["frameSideDatumType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class subtitleType:
    """Information about a subtitle frame."""

    media_type: str | None = None
    pts: int | None = None
    pts_time: float | None = None
    format: int | None = None
    start_display_time: int | None = None
    end_display_time: int | None = None
    num_rects: int | None = None


@dataclass(kw_only=True, frozen=True)
class streamsType:
    """Container for stream information."""

    stream: tuple["streamType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class programsType:
    """Container for program information."""

    program: tuple["programType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class streamDispositionType:
    """Information about stream disposition flags."""

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


@dataclass(kw_only=True, frozen=True)
class streamType:
    """Information about a single stream."""

    disposition: Optional["streamDispositionType"] = None
    tags: Optional["tagsType"] = None
    side_data_list: Optional["packetSideDataListType"] = None
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


@dataclass(kw_only=True, frozen=True)
class programType:
    """Information about a single program."""

    tags: Optional["tagsType"] = None
    streams: Optional["streamsType"] = None
    program_id: int | None = None
    program_num: int | None = None
    nb_streams: int | None = None
    pmt_pid: int | None = None
    pcr_pid: int | None = None


@dataclass(kw_only=True, frozen=True)
class formatType:
    """Information about the media format."""

    tags: Optional["tagsType"] = None
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


@dataclass(kw_only=True, frozen=True)
class tagType:
    """Information about a single tag."""

    key: str | None = None
    value: str | None = None


@dataclass(kw_only=True, frozen=True)
class errorType:
    """Information about an error."""

    code: int | None = None
    string: str | None = None


@dataclass(kw_only=True, frozen=True)
class programVersionType:
    """Information about the program version."""

    version: str | None = None
    copyright: str | None = None
    build_date: str | None = None
    build_time: str | None = None
    compiler_ident: str | None = None
    configuration: str | None = None


@dataclass(kw_only=True, frozen=True)
class chaptersType:
    """Container for chapter information."""

    chapter: tuple["chapterType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class chapterType:
    """Information about a single chapter."""

    tags: tuple["tagsType", ...] | None = None
    id: int | None = None
    time_base: str | None = None
    start: int | None = None
    start_time: float | None = None
    end: int | None = None
    end_time: float | None = None


@dataclass(kw_only=True, frozen=True)
class libraryVersionType:
    """Information about a library version."""

    name: str | None = None
    major: int | None = None
    minor: int | None = None
    micro: int | None = None
    version: int | None = None
    ident: str | None = None


@dataclass(kw_only=True, frozen=True)
class libraryVersionsType:
    """Container for library version information."""

    library_version: tuple["libraryVersionType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class pixelFormatFlagsType:
    """Information about pixel format flags."""

    big_endian: int | None = None
    palette: int | None = None
    bitstream: int | None = None
    hwaccel: int | None = None
    planar: int | None = None
    rgb: int | None = None
    alpha: int | None = None


@dataclass(kw_only=True, frozen=True)
class pixelFormatComponentType:
    """Information about a pixel format component."""

    index: int | None = None
    bit_depth: int | None = None


@dataclass(kw_only=True, frozen=True)
class pixelFormatComponentsType:
    """Container for pixel format component information."""

    component: tuple["pixelFormatComponentType", ...] | None = None


@dataclass(kw_only=True, frozen=True)
class pixelFormatType:
    """Information about a pixel format."""

    flags: Optional["pixelFormatFlagsType"] = None
    components: Optional["pixelFormatComponentsType"] = None
    name: str | None = None
    nb_components: int | None = None
    log2_chroma_w: int | None = None
    log2_chroma_h: int | None = None
    bits_per_pixel: int | None = None


@dataclass(kw_only=True, frozen=True)
class pixelFormatsType:
    """Container for pixel format information."""

    pixel_format: tuple["pixelFormatType", ...] | None = None


registered_types = {
    "None": None,
    "bool": bool,
    "chapterType": chapterType,
    "chaptersType": chaptersType,
    "errorType": errorType,
    "ffprobeType": ffprobeType,
    "float": float,
    "formatType": formatType,
    "frameSideDataComponentList": frameSideDataComponentList,
    "frameSideDataComponentType": frameSideDataComponentType,
    "frameSideDataListType": frameSideDataListType,
    "frameSideDataPieceList": frameSideDataPieceList,
    "frameSideDataPieceType": frameSideDataPieceType,
    "frameSideDataTimecodeList": frameSideDataTimecodeList,
    "frameSideDataTimecodeType": frameSideDataTimecodeType,
    "frameSideDataType": frameSideDataType,
    "frameSideDatumType": frameSideDatumType,
    "frameType": frameType,
    "framesType": framesType,
    "int": int,
    "libraryVersionType": libraryVersionType,
    "libraryVersionsType": libraryVersionsType,
    "logType": logType,
    "logsType": logsType,
    "packetSideDataListType": packetSideDataListType,
    "packetSideDataType": packetSideDataType,
    "packetSideDatumType": packetSideDatumType,
    "packetType": packetType,
    "packetsAndFramesType": packetsAndFramesType,
    "packetsType": packetsType,
    "pixelFormatComponentType": pixelFormatComponentType,
    "pixelFormatComponentsType": pixelFormatComponentsType,
    "pixelFormatFlagsType": pixelFormatFlagsType,
    "pixelFormatType": pixelFormatType,
    "pixelFormatsType": pixelFormatsType,
    "programType": programType,
    "programVersionType": programVersionType,
    "programsType": programsType,
    "str": str,
    "streamDispositionType": streamDispositionType,
    "streamType": streamType,
    "streamsType": streamsType,
    "subtitleType": subtitleType,
    "tagType": tagType,
    "tagsType": tagsType,
}
