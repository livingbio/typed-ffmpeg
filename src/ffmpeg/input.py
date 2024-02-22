from typing import Any

from .dag.nodes import InputNode
from .schema import _to_tuple
from .streams.av import AVStream


def input(
    filename: str,
    *,
    f: str,
    c: str | dict[str, str],
    codec: str | dict[str, str],
    t: str,
    to: str,
    ss: str,
    sseof: str,
    seek_timestamp: int,
    accurate_seek: bool,
    isync: int,
    itsoffset: str,
    itsscale: float | dict[str, float],
    re: bool,
    readrate: float,
    readrate_initial_burst: float,
    bitexact: bool,
    tag: str | dict[str, str],
    reinit_filter: int | dict[str, int],
    dump_attachment: str | dict[str, str],
    stream_loop: int,
    discard: str | dict[str, str],
    thread_queue_size: int,
    find_stream_info: bool,
    r: str | dict[str, str],
    s: str | dict[str, str],
    pix_fmt: str | dict[str, str],
    display_rotation: float | dict[str, float],
    display_hflip: bool | dict[str, bool],
    display_vflip: bool | dict[str, bool],
    vn: bool,
    vcodec: str,
    top: int | dict[str, int],
    vtag: str,
    hwaccel: str | dict[str, str],
    hwaccel_device: str | dict[str, str],
    hwaccel_output_format: str | dict[str, str],
    autorotate: bool | dict[str, bool],
    ar: int | dict[str, int],
    ac: int | dict[str, int],
    an: bool,
    acodec: str,
    sample_fmt: str | dict[str, str],
    channel_layout: str | dict[str, str],
    ch_layout: str | dict[str, str],
    guess_layout_max: int | dict[str, int],
    sn: bool,
    scodec: str,
    fix_sub_duration: bool | dict[str, bool],
    canvas_size: str | dict[str, str],
    dcodec: str,
    dn: bool,
    **kwargs: Any
) -> AVStream:
    """
    Input file URL (ffmpeg `-i` option)

    Args:
        filename: Input file URL
        f: force format
        c: codec name
        codec: codec name
        t: record or transcode \"duration\" seconds of audio/video
        to: record or transcode stop time
        ss: set the start time offset
        sseof: set the start time offset relative to EOF
        seek_timestamp: enable/disable seeking by timestamp with -ss
        accurate_seek: enable/disable accurate seeking with -ss
        isync: Indicate the input index for sync reference
        itsoffset: set the input ts offset
        itsscale: set the input ts scale
        re: read input at native frame rate; equivalent to -readrate 1
        readrate: read input at specified rate
        readrate_initial_burst: The initial amount of input to burst read before imposing any readrate
        bitexact: bitexact mode
        tag: force codec tag/fourcc
        reinit_filter: reinit filtergraph on input parameter changes
        dump_attachment: extract an attachment into a file
        stream_loop: set number of times input stream shall be looped
        discard: discard
        thread_queue_size: set the maximum number of queued packets from the demuxer
        find_stream_info: read and decode the streams to fill missing information with heuristics
        r: set frame rate (Hz value, fraction or abbreviation)
        s: set frame size (WxH or abbreviation)
        pix_fmt: set pixel format
        display_rotation: set pure counter-clockwise rotation in degrees for stream(s)
        display_hflip: set display horizontal flip for stream(s) (overrides any display rotation if it is not set)
        display_vflip: set display vertical flip for stream(s) (overrides any display rotation if it is not set)
        vn: disable video
        vcodec: force video codec ('copy' to copy stream)
        top: deprecated, use the setfield video filter
        vtag: force video tag/fourcc
        hwaccel: use HW accelerated decoding
        hwaccel_device: select a device for HW acceleration
        hwaccel_output_format: select output format used with HW accelerated decoding
        autorotate: automatically insert correct rotate filters
        ar: set audio sampling rate (in Hz)
        ac: set number of audio channels
        an: disable audio
        acodec: force audio codec ('copy' to copy stream)
        sample_fmt: set sample format
        channel_layout: set channel layout
        ch_layout: set channel layout
        guess_layout_max: set the maximum number of channels to try to guess the channel layout
        sn: disable subtitle
        scodec: force subtitle codec ('copy' to copy stream)
        fix_sub_duration: fix subtitles duration
        canvas_size: set canvas size (WxH or abbreviation)
        dcodec: force data codec ('copy' to copy stream)
        dn: disable data

        **kwargs: Additional options

    Returns:
        Input stream

    Examples:
    ```py
    >>> input("input.mp4")
    <AVStream: input.mp4>
    ```
    """

    return InputNode(
        filename=filename,
        kwargs=_to_tuple(
            (
                {
                    "f": f,
                    "c": c,
                    "codec": codec,
                    "t": t,
                    "to": to,
                    "ss": ss,
                    "sseof": sseof,
                    "seek_timestamp": seek_timestamp,
                    "accurate_seek": accurate_seek,
                    "isync": isync,
                    "itsoffset": itsoffset,
                    "itsscale": itsscale,
                    "re": re,
                    "readrate": readrate,
                    "readrate_initial_burst": readrate_initial_burst,
                    "bitexact": bitexact,
                    "tag": tag,
                    "reinit_filter": reinit_filter,
                    "dump_attachment": dump_attachment,
                    "stream_loop": stream_loop,
                    "discard": discard,
                    "thread_queue_size": thread_queue_size,
                    "find_stream_info": find_stream_info,
                    "r": r,
                    "s": s,
                    "pix_fmt": pix_fmt,
                    "display_rotation": display_rotation,
                    "display_hflip": display_hflip,
                    "display_vflip": display_vflip,
                    "vn": vn,
                    "vcodec": vcodec,
                    "top": top,
                    "vtag": vtag,
                    "hwaccel": hwaccel,
                    "hwaccel_device": hwaccel_device,
                    "hwaccel_output_format": hwaccel_output_format,
                    "autorotate": autorotate,
                    "ar": ar,
                    "ac": ac,
                    "an": an,
                    "acodec": acodec,
                    "sample_fmt": sample_fmt,
                    "channel_layout": channel_layout,
                    "ch_layout": ch_layout,
                    "guess_layout_max": guess_layout_max,
                    "sn": sn,
                    "scodec": scodec,
                    "fix_sub_duration": fix_sub_duration,
                    "canvas_size": canvas_size,
                    "dcodec": dcodec,
                    "dn": dn,
                }
                | kwargs
            )
        ),
    ).stream()
