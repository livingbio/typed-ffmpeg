import re
from typing import Literal

from .schema import FFMpegAVOption, FFMpegCodec, FFMpegDecoder, FFMpegEncoder
from .utils import parse_av_option, parse_section_tree, run_ffmpeg_command


def _parse_list(text: str) -> list[FFMpegCodec]:
    """
        Parse the help text for encoders or decoders.

        Args:
            text: The help text to parse from ffmpeg command output

        Example:
    Codecs:
     D..... = Decoding supported
     .E.... = Encoding supported
     ..V... = Video codec
     ..A... = Audio codec
     ..S... = Subtitle codec
     ..D... = Data codec
     ..T... = Attachment codec
     ...I.. = Intra frame-only codec
     ....L. = Lossy compression
     .....S = Lossless compression
     -------
     D.VI.S 012v                 Uncompressed 4:2:2 10-bit
     D.V.L. 4xm                  4X Movie
     D.VI.S 8bps                 QuickTime 8BPS video

        Returns:
            A list of codec instances
    """
    output: list[FFMpegCodec] = []
    lines = text.splitlines()
    re_pattern = re.compile(r"^\s*([\w\.]{6})\s(\w+)\s+(.*)$")

    for line in lines:
        match = re_pattern.findall(line)
        if match:
            flags, name, description = match[0]
            output.append(FFMpegCodec(name=name, flags=flags, help=description))
    return output


def _extract_list(
    type: Literal["encoders", "decoders", "codecs"],
) -> list[FFMpegCodec]:
    """
    Get the help text for all codecs.

    Args:
        type: The type of codec

    Returns:
        A list of codecs
    """
    return _parse_list(run_ffmpeg_command([f"-{type}"]))


def _parse_codec(text: str) -> list[FFMpegAVOption]:
    """
        Parse the help text for a codec option.

        Example:
        Encoder amv [AMV Video]:
        General capabilities:
        Threading capabilities: none
        Supported pixel formats: yuvj420p
    amv encoder AVOptions:
      -mpv_flags         <flags>      E..V....... Flags common for all mpegvideo-based encoders. (default 0)
         skip_rd                      E..V....... RD optimal MB level residual skipping
         strict_gop                   E..V....... Strictly enforce gop size
         qp_rd                        E..V....... Use rate distortion optimization for qp selection
         cbp_rd                       E..V....... use rate distortion optimization for CBP
         naq                          E..V....... normalize adaptive quantization
         mv0                          E..V....... always try a mb with mv=<0,0>
      -luma_elim_threshold <int>        E..V....... single coefficient elimination threshold for luminance (negative values also consider dc coefficie
    nt) (from INT_MIN to INT_MAX) (default 0)

    """
    tree = parse_section_tree(text)
    for section in tree:
        if "AVOptions" in section:
            return parse_av_option(section, tree)
    return []


def _extract_codec(
    codec: str, type: Literal["encoder", "decoder"]
) -> list[FFMpegAVOption]:
    """
    Get the help text for a codec option.

    Args:
        codec: The codec name
        type: The type of codec

    Returns:
        A list of codec options
    """
    return _parse_codec(run_ffmpeg_command(["-h", f"{type}={codec}"]))


def extract() -> list[FFMpegCodec]:
    output: list[FFMpegCodec] = []

    for codec in _extract_list("encoders"):
        options = _extract_codec(codec.name, "encoder")
        output.append(
            FFMpegEncoder(
                name=codec.name,
                flags=codec.flags,
                help=codec.help,
                options=tuple(options),
            )
        )

    for codec in _extract_list("decoders"):
        options = _extract_codec(codec.name, "decoder")
        output.append(
            FFMpegDecoder(
                name=codec.name,
                flags=codec.flags,
                help=codec.help,
                options=tuple(options),
            )
        )

    return output
