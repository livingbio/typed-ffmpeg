from typing import Any

from .base import InputNode
from .streams.av import AVStream


def input(
    INPUT: str,
    *,
    f: str,
    c: str | dict[str, str],
    codec: str | dict[str, str],
    t: str,
    to: str,
    ss: str,
    sseof: str,
    seek_timestamp: int,
    accurate_seek: None,
    isync: int,
    itsoffset: str,
    itsscale: float | dict[str, float],
    re: None,
    readrate: float,
    readrate_initial_burst: float,
    bitexact: None,
    tag: str | dict[str, str],
    reinit_filter: int | dict[str, int],
    dump_attachment: str | dict[str, str],
    stream_loop: int,
    discard: str | dict[str, str],
    thread_queue_size: int,
    find_stream_info: None,
    r: str | dict[str, str],
    s: str | dict[str, str],
    pix_fmt: str | dict[str, str],
    display_rotation: float | dict[str, float],
    display_hflip: None | dict[str, None],
    display_vflip: None | dict[str, None],
    vn: None,
    vcodec: str,
    top: int | dict[str, int],
    vtag: str,
    hwaccel: str | dict[str, str],
    hwaccel_device: str | dict[str, str],
    hwaccel_output_format: str | dict[str, str],
    autorotate: bool | dict[str, bool],
    ar: int | dict[str, int],
    ac: int | dict[str, int],
    an: None,
    acodec: str,
    sample_fmt: str | dict[str, str],
    channel_layout: str | dict[str, str],
    ch_layout: str | dict[str, str],
    guess_layout_max: int | dict[str, int],
    sn: None,
    scodec: str,
    fix_sub_duration: None | dict[str, None],
    canvas_size: str | dict[str, str],
    dcodec: str,
    dn: None,
    **kwargs: Any
) -> AVStream:
    """
    Parameters:
    ----------
    :param str f: force format
    :param str | dict[str, str] c: codec name
    :param str | dict[str, str] codec: codec name
    :param str t: record or transcode \"duration\" seconds of audio/video
    :param str to: record or transcode stop time
    :param str ss: set the start time offset
    :param str sseof: set the start time offset relative to EOF
    :param int seek_timestamp: enable/disable seeking by timestamp with -ss
    :param None accurate_seek: enable/disable accurate seeking with -ss
    :param int isync: Indicate the input index for sync reference
    :param str itsoffset: set the input ts offset
    :param float | dict[str, float] itsscale: set the input ts scale
    :param None re: read input at native frame rate; equivalent to -readrate 1
    :param float readrate: read input at specified rate
    :param float readrate_initial_burst: The initial amount of input to burst read before imposing any readrate
    :param None bitexact: bitexact mode
    :param str | dict[str, str] tag: force codec tag/fourcc
    :param int | dict[str, int] reinit_filter: reinit filtergraph on input parameter changes
    :param str | dict[str, str] dump_attachment: extract an attachment into a file
    :param int stream_loop: set number of times input stream shall be looped
    :param str | dict[str, str] discard: discard
    :param int thread_queue_size: set the maximum number of queued packets from the demuxer
    :param None find_stream_info: read and decode the streams to fill missing information with heuristics
    :param str | dict[str, str] r: set frame rate (Hz value, fraction or abbreviation)
    :param str | dict[str, str] s: set frame size (WxH or abbreviation)
    :param str | dict[str, str] pix_fmt: set pixel format
    :param float | dict[str, float] display_rotation: set pure counter-clockwise rotation in degrees for stream(s)
    :param None | dict[str, None] display_hflip: set display horizontal flip for stream(s) (overrides any display rotation if it is not set)
    :param None | dict[str, None] display_vflip: set display vertical flip for stream(s) (overrides any display rotation if it is not set)
    :param None vn: disable video
    :param str vcodec: force video codec ('copy' to copy stream)
    :param int | dict[str, int] top: deprecated, use the setfield video filter
    :param str vtag: force video tag/fourcc
    :param str | dict[str, str] hwaccel: use HW accelerated decoding
    :param str | dict[str, str] hwaccel_device: select a device for HW acceleration
    :param str | dict[str, str] hwaccel_output_format: select output format used with HW accelerated decoding
    :param bool | dict[str, bool] autorotate: automatically insert correct rotate filters
    :param int | dict[str, int] ar: set audio sampling rate (in Hz)
    :param int | dict[str, int] ac: set number of audio channels
    :param None an: disable audio
    :param str acodec: force audio codec ('copy' to copy stream)
    :param str | dict[str, str] sample_fmt: set sample format
    :param str | dict[str, str] channel_layout: set channel layout
    :param str | dict[str, str] ch_layout: set channel layout
    :param int | dict[str, int] guess_layout_max: set the maximum number of channels to try to guess the channel layout
    :param None sn: disable subtitle
    :param str scodec: force subtitle codec ('copy' to copy stream)
    :param None | dict[str, None] fix_sub_duration: fix subtitles duration
    :param str | dict[str, str] canvas_size: set canvas size (WxH or abbreviation)
    :param str dcodec: force data codec ('copy' to copy stream)
    :param None dn: disable data

    """

    return InputNode(name=input.__name__, kwargs=kwargs).stream()
