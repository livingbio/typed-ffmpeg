# NOTE: this file is auto-generated, do not modify
"""Input node."""

from pathlib import Path
from typing import Any

from ...codecs.schema import FFMpegDecoderOption
from ...formats.schema import FFMpegDemuxerOption
from ...options.codec import (
    FFMpegAVCodecContextDecoderOption,
)
from ...options.format import (
    FFMpegAVFormatContextDecoderOption,
)
from ...streams.av import AVStream
from ...types import (
    Boolean,
    Double,
    Float,
    Int,
    String,
    Time,
)
from ...utils.frozendict import merge
from ..nodes import (
    InputNode,
)


def input(
    filename: str | Path,
    *,
    f: String = None,
    c: String = None,
    codec: String = None,
    t: Time = None,
    to: Time = None,
    ss: Time = None,
    sseof: Time = None,
    seek_timestamp: Int = None,
    accurate_seek: Boolean = None,
    isync: Int = None,
    itsoffset: Time = None,
    itsscale: Double = None,
    re: Boolean = None,
    readrate: Float = None,
    readrate_initial_burst: Double = None,
    bitexact: Boolean = None,
    tag: String = None,
    reinit_filter: Int = None,
    dump_attachment: String = None,
    stream_loop: Int = None,
    discard: String = None,
    thread_queue_size: Int = None,
    find_stream_info: Boolean = None,
    r: String = None,
    s: String = None,
    pix_fmt: String = None,
    display_rotation: Double = None,
    display_hflip: Boolean = None,
    display_vflip: Boolean = None,
    vn: Boolean = None,
    vcodec: String = None,
    vtag: String = None,
    hwaccel: String = None,
    hwaccel_device: String = None,
    hwaccel_output_format: String = None,
    autorotate: Boolean = None,
    ar: Int = None,
    ac: Int = None,
    an: Boolean = None,
    acodec: String = None,
    sample_fmt: String = None,
    channel_layout: String = None,
    ch_layout: String = None,
    guess_layout_max: Int = None,
    sn: Boolean = None,
    scodec: String = None,
    fix_sub_duration: Boolean = None,
    canvas_size: String = None,
    bsf: String = None,
    dcodec: String = None,
    dn: Boolean = None,
    top: Int = None,
    decoder_options: FFMpegDecoderOption | None = None,
    demuxer_options: FFMpegDemuxerOption | None = None,
    format_options: FFMpegAVFormatContextDecoderOption | None = None,
    codec_options: FFMpegAVCodecContextDecoderOption | None = None,
    extra_options: dict[str, Any] | None = None,
) -> AVStream:
    """
    Input file URL (ffmpeg ``-i`` option).

    Args:
        filename: Input file URL
        f: force container format (auto-detected otherwise)
        c: select encoder/decoder ('copy' to copy stream without reencoding)
        codec: alias for -c (select encoder/decoder)
        t: stop transcoding after specified duration
        to: stop transcoding after specified time is reached
        ss: start transcoding at specified time
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
        r: override input framerate/convert to given output framerate (Hz value, fraction or abbreviation)
        s: set frame size (WxH or abbreviation)
        pix_fmt: set pixel format
        display_rotation: set pure counter-clockwise rotation in degrees for stream(s)
        display_hflip: set display horizontal flip for stream(s) (overrides any display rotation if it is not set)
        display_vflip: set display vertical flip for stream(s) (overrides any display rotation if it is not set)
        vn: disable video
        vcodec: alias for -c:v (select encoder/decoder for video streams)
        vtag: force video tag/fourcc
        hwaccel: use HW accelerated decoding
        hwaccel_device: select a device for HW acceleration
        hwaccel_output_format: select output format used with HW accelerated decoding
        autorotate: automatically insert correct rotate filters
        ar: set audio sampling rate (in Hz)
        ac: set number of audio channels
        an: disable audio
        acodec: alias for -c:a (select encoder/decoder for audio streams)
        sample_fmt: set sample format
        channel_layout: set channel layout
        ch_layout: set channel layout
        guess_layout_max: set the maximum number of channels to try to guess the channel layout
        sn: disable subtitle
        scodec: alias for -c:s (select encoder/decoder for subtitle streams)
        fix_sub_duration: fix subtitles duration
        canvas_size: set canvas size (WxH or abbreviation)
        bsf: A comma-separated list of bitstream filters
        dcodec: alias for -c:d (select encoder/decoder for data streams)
        dn: disable data
        top: deprecated, use the setfield video filter
        decoder_options: ffmpeg's decoder options
        demuxer_options: ffmpeg's demuxer options
        format_options: ffmpeg's AVFormatContext options
        codec_options: ffmpeg's AVCodecContext options
        extra_options: ffmpeg's input file options

    Returns:
        Input stream

    Examples:
    ```py
    >>> input('input.mp4')
    <AVStream:input.mp4:0>
    ```

    """
    return InputNode(
        filename=str(filename),
        kwargs=merge(
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
                "bsf": bsf,
                "dcodec": dcodec,
                "dn": dn,
                "top": top,
            },
            decoder_options,
            demuxer_options,
            format_options,
            codec_options,
            extra_options,
        ),
    ).stream()
