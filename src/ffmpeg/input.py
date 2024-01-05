from typing import Any

from .base import InputNode
from .streams.av import AVStream


def input(
    INPUT: str,
    *,
    f: str,
    c: str,
    codec: str,
    t: str,
    to: str,
    ss: str,
    sseof: str,
    seek_timestamp: int,
    accurate_seek: None,
    isync: int,
    itsoffset: str,
    itsscale: float,
    re: None,
    readrate: float,
    readrate_initial_burst: float,
    bitexact: None,
    tag: str,
    reinit_filter: int,
    dump_attachment: str,
    stream_loop: int,
    discard: str,
    thread_queue_size: int,
    find_stream_info: None,
    r: str,
    s: str,
    pix_fmt: str,
    display_rotation: float,
    display_hflip: None,
    display_vflip: None,
    vn: None,
    vcodec: str,
    top: int,
    vtag: str,
    hwaccel: str,
    hwaccel_device: str,
    hwaccel_output_format: str,
    autorotate: bool,
    ar: int,
    ac: int,
    an: None,
    acodec: str,
    sample_fmt: str,
    channel_layout: str,
    ch_layout: str,
    guess_layout_max: int,
    sn: None,
    scodec: str,
    fix_sub_duration: None,
    canvas_size: str,
    dcodec: str,
    dn: None,
    **kwargs: Any
) -> AVStream:
    """
    Input file URL (ffmpeg ``-i`` option)

    Any supplied kwargs are passed to ffmpeg verbatim (e.g. ``t=20``,
    ``f='mp4'``, ``acodec='pcm'``, etc.).

    To tell ffmpeg to read from stdin, use ``pipe:`` as the filename.

    Official documentation: `Main options <https://ffmpeg.org/ffmpeg.html#Main-options>`__

    Parameters:
    ----------
    :param str f: force format
    :param str c: codec name
    :param str codec: codec name
    :param str t: record or transcode \"duration\" seconds of audio/video
    :param str to: record or transcode stop time
    :param str ss: set the start time offset
    :param str sseof: set the start time offset relative to EOF
    :param int seek_timestamp: enable/disable seeking by timestamp with -ss
    :param None accurate_seek: enable/disable accurate seeking with -ss
    :param int isync: Indicate the input index for sync reference
    :param str itsoffset: set the input ts offset
    :param float itsscale: set the input ts scale
    :param None re: read input at native frame rate; equivalent to -readrate 1
    :param float readrate: read input at specified rate
    :param float readrate_initial_burst: The initial amount of input to burst read before imposing any readrate
    :param None bitexact: bitexact mode
    :param str tag: force codec tag/fourcc
    :param int reinit_filter: reinit filtergraph on input parameter changes
    :param str dump_attachment: extract an attachment into a file
    :param int stream_loop: set number of times input stream shall be looped
    :param str discard: discard
    :param int thread_queue_size: set the maximum number of queued packets from the demuxer
    :param None find_stream_info: read and decode the streams to fill missing information with heuristics
    :param str r: set frame rate (Hz value, fraction or abbreviation)
    :param str s: set frame size (WxH or abbreviation)
    :param str pix_fmt: set pixel format
    :param float display_rotation: set pure counter-clockwise rotation in degrees for stream(s)
    :param None display_hflip: set display horizontal flip for stream(s) (overrides any display rotation if it is not set)
    :param None display_vflip: set display vertical flip for stream(s) (overrides any display rotation if it is not set)
    :param None vn: disable video
    :param str vcodec: force video codec ('copy' to copy stream)
    :param int top: deprecated, use the setfield video filter
    :param str vtag: force video tag/fourcc
    :param str hwaccel: use HW accelerated decoding
    :param str hwaccel_device: select a device for HW acceleration
    :param str hwaccel_output_format: select output format used with HW accelerated decoding
    :param bool autorotate: automatically insert correct rotate filters
    :param int ar: set audio sampling rate (in Hz)
    :param int ac: set number of audio channels
    :param None an: disable audio
    :param str acodec: force audio codec ('copy' to copy stream)
    :param str sample_fmt: set sample format
    :param str channel_layout: set channel layout
    :param str ch_layout: set channel layout
    :param int guess_layout_max: set the maximum number of channels to try to guess the channel layout
    :param None sn: disable subtitle
    :param str scodec: force subtitle codec ('copy' to copy stream)
    :param None fix_sub_duration: fix subtitles duration
    :param str canvas_size: set canvas size (WxH or abbreviation)
    :param str dcodec: force data codec ('copy' to copy stream)
    :param None dn: disable data

    """

    return InputNode(name=input.__name__, kwargs=kwargs).stream()
