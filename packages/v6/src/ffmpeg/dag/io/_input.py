# NOTE: this file is auto-generated, do not modify
"""
Input node.
"""



from pathlib import Path
from typing import Any


from ...types import Binary, Boolean, Color, Dictionary, Double, Duration, Flags, Float, Func, Image_size, Int, Int64, Pix_fmt, Rational, Sample_fmt, String, Time, Video_rate

from ..factory import filter_node_factory

from ...utils.frozendict import FrozenDict, merge
from ...utils.typing import override
from ...schema import Default, StreamType, Auto, FFMpegOptionGroup
from ...common.schema import FFMpegFilterDef
from ...options.framesync import FFMpegFrameSyncOption
from ...options.timeline import FFMpegTimelineOption

from ...options.codec import FFMpegAVCodecContextEncoderOption, FFMpegAVCodecContextDecoderOption


from ...options.format import FFMpegAVFormatContextEncoderOption, FFMpegAVFormatContextDecoderOption


from ...streams.av import AVStream

from ...streams.channel_layout import CHANNEL_LAYOUT
from ...codecs.schema import FFMpegEncoderOption, FFMpegDecoderOption
from ...formats.schema import FFMpegMuxerOption, FFMpegDemuxerOption

from ..nodes import FilterableStream, FilterNode, OutputStream, OutputNode, InputNode, GlobalNode, GlobalStream


from ...streams.video import VideoStream


from ...streams.audio import AudioStream



def input(
    filename: str | Path,
    *,L: Func = None,h: Func = None,_q: Func = None,help: Func = None,_help: Func = None,version: Func = None,buildconf: Func = None,formats: Func = None,muxers: Func = None,demuxers: Func = None,devices: Func = None,codecs: Func = None,decoders: Func = None,encoders: Func = None,bsfs: Func = None,protocols: Func = None,filters: Func = None,pix_fmts: Func = None,layouts: Func = None,sample_fmts: Func = None,dispositions: Func = None,colors: Func = None,sources: Func = None,sinks: Func = None,hwaccels: Func = None,decoder_options: FFMpegDecoderOption | None = None,
    demuxer_options: FFMpegDemuxerOption | None = None,
    format_options: FFMpegAVFormatContextDecoderOption | None = None,
    codec_options: FFMpegAVCodecContextDecoderOption | None = None,
    extra_options: dict[str, Any] | None = None,
) -> AVStream:
    """
    Input file URL (ffmpeg ``-i`` option)

    Args:
        filename: Input file URL
        L: show license
        h: show help
        _q: show help
        help: show help
        _help: show help
        version: show version
        buildconf: show build configuration
        formats: show available formats
        muxers: show available muxers
        demuxers: show available demuxers
        devices: show available devices
        codecs: show available codecs
        decoders: show available decoders
        encoders: show available encoders
        bsfs: show available bit stream filters
        protocols: show available protocols
        filters: show available filters
        pix_fmts: show available pixel formats
        layouts: show standard channel layouts
        sample_fmts: show available audio sample formats
        dispositions: show available stream dispositions
        colors: show available color names
        sources: list sources of the input device
        sinks: list sinks of the output device
        hwaccels: show available HW acceleration methods
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
        kwargs=merge({
            "L": L,

                "h": h,

                "?": _q,

                "help": help,

                "-help": _help,

                "version": version,

                "buildconf": buildconf,

                "formats": formats,

                "muxers": muxers,

                "demuxers": demuxers,

                "devices": devices,

                "codecs": codecs,

                "decoders": decoders,

                "encoders": encoders,

                "bsfs": bsfs,

                "protocols": protocols,

                "filters": filters,

                "pix_fmts": pix_fmts,

                "layouts": layouts,

                "sample_fmts": sample_fmts,

                "dispositions": dispositions,

                "colors": colors,








                "sources": sources,

                "sinks": sinks,

























































































































                "hwaccels": hwaccels,









































        }, decoder_options, demuxer_options, format_options, codec_options, extra_options )
    ).stream()
