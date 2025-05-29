from dataclasses import dataclass
from typing import Optional


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
    packet: tuple["packetType", ...] = ()


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
    tag: tuple["tagType", ...] = ()


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
    side_data: tuple["packetSideDataType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class packetSideDataType:
    type: str | None = None
    side_datum: tuple["packetSideDatumType", ...] = ()


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
    log: tuple["logType", ...] = ()


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
    side_data: tuple["frameSideDataType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class frameSideDataType:
    side_data_type: str | None = None
    side_data_size: int | None = None
    timecode: str | None = None
    timecodes: Optional["frameSideDataTimecodeList"] = None
    components: Optional["frameSideDataComponentList"] = None
    side_datum: tuple["frameSideDatumType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class frameSideDatumType:
    key: str | None = None
    value: str | None = None


@dataclass(frozen=True, kw_only=True)
class frameSideDataTimecodeList:
    timecode: tuple["frameSideDataTimecodeType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class frameSideDataTimecodeType:
    value: str | None = None


@dataclass(frozen=True, kw_only=True)
class frameSideDataComponentList:
    component: tuple["frameSideDataComponentType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class frameSideDataComponentType:
    pieces: Optional["frameSideDataPieceList"] = None
    side_datum: tuple["frameSideDatumType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class frameSideDataPieceList:
    piece: tuple["frameSideDataPieceType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class frameSideDataPieceType:
    side_datum: tuple["frameSideDatumType", ...] = ()


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
    stream: tuple["streamType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class programsType:
    program: tuple["programType", ...] = ()


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
    chapter: tuple["chapterType", ...] = ()


@dataclass(frozen=True, kw_only=True)
class chapterType:
    id: int | None = None
    time_base: str | None = None
    start: int | None = None
    start_time: float | None = None
    end: int | None = None
    end_time: float | None = None
    tags: tuple["tagsType", ...] = ()


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
    library_version: tuple["libraryVersionType", ...] = ()


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
    component: tuple["pixelFormatComponentType", ...] = ()


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
    pixel_format: tuple["pixelFormatType", ...] = ()
