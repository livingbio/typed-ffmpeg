from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum
from typing import Literal

from ffmpeg.common.serialize import Serializable, serializable


@serializable
class FFMpegOptionType(str, Enum):
    """
    Enumeration of possible data types for FFmpeg AV options (e.g. codec, format, filter options).

    https://ffmpeg.org/ffmpeg-all.html#AVOptions
    """

    boolean = "boolean"
    duration = "duration"
    color = "color"
    flags = "flags"
    dictionary = "dictionary"
    pix_fmt = "pix_fmt"
    int = "int"
    int64 = "int64"
    double = "double"
    float = "float"
    string = "string"
    video_rate = "video_rate"
    image_size = "image_size"
    rational = "rational"
    sample_fmt = "sample_fmt"
    binary = "binary"
    channel_layout = "channel_layout"
    pixel_format = "pixel_format"
    sample_rate = "sample_rate"


@dataclass(frozen=True, kw_only=True)
class FFMpegOption(Serializable):
    """
    Represents FFMpeg Options in the help text, there are different types of options:

    ```
    ### (General) options:
    Has no type in help text, no flags in help text, has varname, support -no(option) syntax

    Example:
    Advanced global options:
    -cpuflags flags     force specific cpu flags
    -cpucount count     force specific cpu count

    ### AVOptions:
    Has type, has flags, no varname, per-stream, not support -no(option) syntax
    (ref: https://ffmpeg.org/ffmpeg-all.html#AVOptions)

    Example:
    AVCodecContext AVOptions:
    -b                 <int64>      E..VA...... set bitrate (in bits/s) (from 0 to I64_MAX) (default 200000)
    -ab                <int64>      E...A...... set bitrate (in bits/s) (from 0 to INT_MAX) (default 128000)
    -bt                <int>        E..VA...... Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to minimum/maximum bitrate. Lowering tolerance too much has an adverse effect on quality. (from 0 to INT_MAX) (default 4000000)
    -flags             <flags>      ED.VAS..... (default 0)

    ### AVFilter AVOptions
    Has type, has flags, no varname, per-stream, has specially syntax

    Example:
    tmedian AVOptions:
        radius            <int>        ..FV....... set median filter radius (from 1 to 127) (default 1)
        planes            <int>        ..FV.....T. set planes to filter (from 0 to 15) (default 15)
        percentile        <float>      ..FV.....T. set percentile (from 0 to 1) (default 0.5)

    ### BSF AVFilters:
    not investigated yet
    ```
    """

    section: str
    """
    The section of the option based on the help text. e.g. "Advanced global options", "AVOptions", "AVFilter AVOptions", "BSF AVFilters"
    """
    name: str
    """
    The name of the option. e.g. "-b", "radius", "preset"
    """
    type: FFMpegOptionType | None = None
    """
    The type of the option. e.g. "int", "float", "string"
    """
    flags: str | None = None
    """
    The flags of the option. e.g. "E..VA......", "..FV.......", "..F.A......" or None if not specified
    """
    help: str
    """
    The help of the option. e.g. "set bitrate (in bits/s) (from 0 to I64_MAX) (default 200000)"
    """
    varname: str | None = None
    """
    The varname of the option. e.g. "flags", "count", None if not specified
    """


@dataclass(frozen=True, kw_only=True)
class FFMpegOptionChoice(Serializable):
    """
    Represents a choice for an AVOption.
    NOTE: there are 2 types of choices (flags, enum)

    ```
    ### Example flags:
    -fflags            <flags>      ED......... (default autobsf)
       flush_packets                E.......... reduce the latency by flushing out packets immediately
       ignidx                       .D......... ignore index
       genpts                       .D......... generate pts

    ### Example enum:
    preset            <int>        ..F.A...... set equalizer preset (from -1 to 17) (default flat)
     custom          -1           ..F.A......
     flat            0            ..F.A......
     acoustic        1            ..F.A......
     bass            2            ..F.A......
     beats           3            ..F.A......
     classic         4            ..F.A......
     clear           5            ..F.A......
     deep bass       6            ..F.A......
     dubstep         7            ..F.A......
     electronic      8            ..F.A......
     hardstyle       9            ..F.A......
    ```
    """

    name: str
    help: str
    flags: str
    value: str


@dataclass(frozen=True, kw_only=True)
class FFMpegAVOption(FFMpegOption):
    """
    Represents an AVOption.

    ```
    Example (AVFormatContext AVOptions):
    AVFormatContext AVOptions:
    -fflags            <flags>      ED......... (default autobsf)
        flush_packets                E.......... reduce the latency by flushing out packets immediately

    Example (AVCodecContext AVOptions):
    AVCodecContext AVOptions:
    -b                 <int64>      E..VA...... set bitrate (in bits/s) (from 0 to I64_MAX) (default 200000)
    -ab                <int64>      E...A...... set bitrate (in bits/s) (from 0 to INT_MAX) (default 128000)
    -bt                <int>        E..VA...... Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to minimum/maximum bitrate. Lowering tolerance too much has an adverse effect on quality. (from 0 to INT_MAX) (default 4000000)
    -flags             <flags>      ED.VAS..... (default 0)

    Example (AVFilter AVOptions):
    tmedian AVOptions:
        radius            <int>        ..FV....... set median filter radius (from 1 to 127) (default 1)
        planes            <int>        ..FV.....T. set planes to filter (from 0 to 15) (default 15)
        percentile        <float>      ..FV.....T. set percentile (from 0 to 1) (default 0.5)

    Example (BSF AVFilters):
    ```
    """

    min: str | None = None
    max: str | None = None
    default: str | None = None
    choices: tuple[FFMpegOptionChoice, ...] = ()

    @property
    def code_gen_type(self) -> str:
        def handle_choices() -> str:
            if self.type != FFMpegOptionType.flags:
                # NOTE: flags not supported yet
                if self.choices:
                    return "| Literal[{}]".format(
                        ", ".join(f'"{choice.name}"' for choice in self.choices)
                    )
            return ""

        def handle_type() -> str:
            match self.type:
                case FFMpegOptionType.boolean:
                    return "bool | None"
                case FFMpegOptionType.int:
                    return "int | None"
                case FFMpegOptionType.int64:
                    return "int | None"
                case FFMpegOptionType.float:
                    return "float | None"
                case FFMpegOptionType.double:
                    return "float | None"
                case FFMpegOptionType.string:
                    return "str | None"
                case FFMpegOptionType.channel_layout:
                    return "str | None"
                case FFMpegOptionType.flags:
                    return "str | None"
                case FFMpegOptionType.duration:
                    return "str | None"
                case FFMpegOptionType.dictionary:
                    return "str | None"
                case FFMpegOptionType.image_size:
                    return "str | None"
                case FFMpegOptionType.pixel_format:
                    return "str | None"
                case FFMpegOptionType.sample_rate:
                    return "int | None"
                case FFMpegOptionType.sample_fmt:
                    return "str | None"
                case FFMpegOptionType.binary:
                    return "str | None"
                case FFMpegOptionType.rational:
                    return "str | None"
                case FFMpegOptionType.color:
                    return "str | None"
                case FFMpegOptionType.video_rate:
                    return "str | None"
                case FFMpegOptionType.pix_fmt:
                    return "str | None"
                case _:
                    raise ValueError(f"Invalid option type: {self.type}")

        return f"{handle_type()}{handle_choices()}"


@dataclass(frozen=True, kw_only=True)
class FFMpegOptionSet(Serializable):
    """
    Represents a set of options set. such as formats, codecs, filters, etc.

    ```
    Example:
    -formats
    File formats:
    D. = Demuxing supported
    .E = Muxing supported
    --
    D  3dostr          3DO STR
    ```
    """

    name: str
    flags: str
    help: str
    options: tuple[FFMpegAVOption, ...] = ()


@dataclass(frozen=True, kw_only=True)
class FFMpegCodec(FFMpegOptionSet):
    """
    Represents a codec.
    Example:
    -encoders
    V..... = Video
    A..... = Audio
    S..... = Subtitle
    .F.... = Frame-level multithreading
    ..S... = Slice-level multithreading
    ...X.. = Codec is experimental
    ....B. = Supports draw_horiz_band
    .....D = Supports direct rendering method 1
    ------
    V....D a64multi             Multicolor charset for Commodore 64 (codec a64_multi)
    V....D a64multi5            Multicolor charset for Commodore 64, extended with 5th color (colram) (codec a64_multi5)
    """

    def filterd_options(self) -> Iterable[FFMpegAVOption]:
        # NOTE: the nvenv_hevc has alias for some options, so we need to filter them out
        passed = set()
        for option in self.options:
            if option.name.replace("-", "_") in passed:
                continue
            passed.add(option.name.replace("-", "_"))
            yield option

    @property
    def codec_type(self) -> Literal["video", "audio", "subtitle"]:
        match self.flags[0]:
            case "V":
                return "video"
            case "A":
                return "audio"
            case "S":
                return "subtitle"
            case _:
                raise ValueError(f"Invalid stream type: {self.flags[0]}")

    @property
    def is_encoder(self) -> bool:
        return isinstance(self, FFMpegEncoder)

    @property
    def is_decoder(self) -> bool:
        return isinstance(self, FFMpegDecoder)


@dataclass(frozen=True, kw_only=True)
class FFMpegEncoder(FFMpegCodec):
    pass


@dataclass(frozen=True, kw_only=True)
class FFMpegDecoder(FFMpegCodec):
    pass


@dataclass(frozen=True, kw_only=True)
class FFMpegFormat(FFMpegOptionSet):
    """
    Represents a format.
    Example:
    -formats
    File formats:
    D. = Demuxing supported
    .E = Muxing supported
    --
    D  3dostr          3DO STR
    E 3g2             3GP2 (3GPP2 file format)
    E 3gp             3GP (3GPP file format)
    D  4xm             4X Technologies
    E a64             a64 - video for Commodore 64
    """

    @property
    def is_muxer(self) -> bool:
        return isinstance(self, FFMpegMuxer)

    @property
    def is_demuxer(self) -> bool:
        return isinstance(self, FFMpegDemuxer)


@dataclass(frozen=True, kw_only=True)
class FFMpegDemuxer(FFMpegFormat):
    pass


@dataclass(frozen=True, kw_only=True)
class FFMpegMuxer(FFMpegFormat):
    pass


@dataclass(frozen=True, kw_only=True)
class FFMpegFilter(FFMpegOptionSet):
    """
    Represents a filter.
    Example:
    Filters:
    T.. = Timeline support
    .S. = Slice threading
    ..C = Command support
    A = Audio input/output
    V = Video input/output
    N = Dynamic number and/or type of input/output
    | = Source or sink filter
    ... abench            A->A       Benchmark part of a filtergraph.
    ..C acompressor       A->A       Audio compressor.
    ... acontrast         A->A       Simple audio dynamic range compression/expansion filter.
    ... acopy             A->A       Copy the input audio unchanged to the output.
    ... acue              A->A       Delay filtering to match a cue.
    ... acrossfade        AA->A      Cross fade two input audio streams.
    .S. acrossover        A->N       Split audio into per-bands streams.
    T.C acrusher          A->A       Reduce audio bit resolution.
    TS. adeclick          A->A       Remove impulsive noise from input audio.
    """

    pass
