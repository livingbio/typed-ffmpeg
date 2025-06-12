# NOTE: this file is auto-generated, do not modify
from typing import Literal

from ..utils.frozendict import FrozenDict
from .schema import FFMpegDecoderOption


def _012v() -> FFMpegDecoderOption:
    """
    Uncompressed 4:2:2 10-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def _4xm() -> FFMpegDecoderOption:
    """
    4X Movie


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def _8bps() -> FFMpegDecoderOption:
    """
    QuickTime 8BPS video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aasc() -> FFMpegDecoderOption:
    """
    Autodesk RLE


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def agm() -> FFMpegDecoderOption:
    """
    Amuse Graphics Movie


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aic() -> FFMpegDecoderOption:
    """
    Apple Intermediate Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def alias_pix() -> FFMpegDecoderOption:
    """
    Alias/Wavefront PIX image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def amv() -> FFMpegDecoderOption:
    """
    AMV Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def anm() -> FFMpegDecoderOption:
    """
    Deluxe Paint Animation


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ansi() -> FFMpegDecoderOption:
    """
    ASCII/ANSI art


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def apng() -> FFMpegDecoderOption:
    """
    APNG (Animated Portable Network Graphics) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def arbc() -> FFMpegDecoderOption:
    """
    Gryphon's Anim Compressor


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def argo() -> FFMpegDecoderOption:
    """
    Argonaut Games Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def asv1() -> FFMpegDecoderOption:
    """
    ASUS V1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def asv2() -> FFMpegDecoderOption:
    """
    ASUS V2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aura() -> FFMpegDecoderOption:
    """
    Auravision AURA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aura2() -> FFMpegDecoderOption:
    """
    Auravision Aura 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libdav1d(
    tilethreads: int | None = None,
    framethreads: int | None = None,
    max_frame_delay: int | None = None,
    filmgrain: bool | None = None,
    oppoint: int | None = None,
    alllayers: bool | None = None,
) -> FFMpegDecoderOption:
    """
    dav1d AV1 decoder by VideoLAN (codec av1)

    Args:
        tilethreads: Tile threads (from 0 to 256) (default 0)
        framethreads: Frame threads (from 0 to 256) (default 0)
        max_frame_delay: Max frame delay (from 0 to 256) (default 0)
        filmgrain: Apply Film Grain (default auto)
        oppoint: Select an operating point of the scalable bitstream (from -1 to 31) (default -1)
        alllayers: Output all spatial layers (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def av1(
    operating_point: int | None = None,
) -> FFMpegDecoderOption:
    """
    Alliance for Open Media AV1

    Args:
        operating_point: Select an operating point of the scalable bitstream (from 0 to 31) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def av1_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID AV1 decoder (codec av1)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def avrn() -> FFMpegDecoderOption:
    """
    Avid AVI Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def avrp() -> FFMpegDecoderOption:
    """
    Avid 1:1 10-bit RGB Packer


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def avs() -> FFMpegDecoderOption:
    """
    AVS (Audio Video Standard) video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def avui() -> FFMpegDecoderOption:
    """
    Avid Meridien Uncompressed


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ayuv() -> FFMpegDecoderOption:
    """
    Uncompressed packed MS 4:4:4:4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def bethsoftvid() -> FFMpegDecoderOption:
    """
    Bethesda VID video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def bfi() -> FFMpegDecoderOption:
    """
    Brute Force & Ignorance


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def binkvideo() -> FFMpegDecoderOption:
    """
    Bink video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def bintext() -> FFMpegDecoderOption:
    """
    Binary text


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def bitpacked() -> FFMpegDecoderOption:
    """
    Bitpacked


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def bmp() -> FFMpegDecoderOption:
    """
    BMP (Windows and OS/2 bitmap)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def bmv_video() -> FFMpegDecoderOption:
    """
    Discworld II BMV video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def brender_pix() -> FFMpegDecoderOption:
    """
    BRender PIX image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def c93() -> FFMpegDecoderOption:
    """
    Interplay C93


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cavs() -> FFMpegDecoderOption:
    """
    Chinese AVS (Audio Video Standard) (AVS1-P2, JiZhun profile)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cdgraphics() -> FFMpegDecoderOption:
    """
    CD Graphics video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cdtoons() -> FFMpegDecoderOption:
    """
    CDToons video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cdxl() -> FFMpegDecoderOption:
    """
    Commodore CDXL video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cfhd() -> FFMpegDecoderOption:
    """
    GoPro CineForm HD


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cinepak() -> FFMpegDecoderOption:
    """
    Cinepak


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def clearvideo() -> FFMpegDecoderOption:
    """
    Iterated Systems ClearVideo


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cljr() -> FFMpegDecoderOption:
    """
    Cirrus Logic AccuPak


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cllc() -> FFMpegDecoderOption:
    """
    Canopus Lossless Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def eacmv() -> FFMpegDecoderOption:
    """
    Electronic Arts CMV video (codec cmv)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cpia() -> FFMpegDecoderOption:
    """
    CPiA video format


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cri() -> FFMpegDecoderOption:
    """
    Cintel RAW


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def camstudio() -> FFMpegDecoderOption:
    """
    CamStudio (codec cscd)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cyuv() -> FFMpegDecoderOption:
    """
    Creative YUV (CYUV)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dds() -> FFMpegDecoderOption:
    """
    DirectDraw Surface image decoder


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dfa() -> FFMpegDecoderOption:
    """
    Chronomaster DFA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dirac() -> FFMpegDecoderOption:
    """
    BBC Dirac VC-2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dnxhd() -> FFMpegDecoderOption:
    """
    VC3/DNxHD


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dpx() -> FFMpegDecoderOption:
    """
    DPX (Digital Picture Exchange) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dsicinvideo() -> FFMpegDecoderOption:
    """
    Delphine Software International CIN video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dvvideo() -> FFMpegDecoderOption:
    """
    DV (Digital Video)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dxa() -> FFMpegDecoderOption:
    """
    Feeble Files/ScummVM DXA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dxtory() -> FFMpegDecoderOption:
    """
    Dxtory


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dxv() -> FFMpegDecoderOption:
    """
    Resolume DXV


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def escape124() -> FFMpegDecoderOption:
    """
    Escape 124


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def escape130() -> FFMpegDecoderOption:
    """
    Escape 130


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def exr(
    layer: str | None = None,
    part: int | None = None,
    gamma: float | None = None,
    apply_trc: int
    | None
    | Literal[
        "bt709",
        "gamma",
        "gamma22",
        "gamma28",
        "smpte170m",
        "smpte240m",
        "linear",
        "log",
        "log_sqrt",
        "iec61966_2_4",
        "bt1361",
        "iec61966_2_1",
        "bt2020_10bit",
        "bt2020_12bit",
        "smpte2084",
        "smpte428_1",
    ] = None,
) -> FFMpegDecoderOption:
    """
    OpenEXR image

    Args:
        layer: Set the decoding layer (default "")
        part: Set the decoding part (from 0 to INT_MAX) (default 0)
        gamma: Set the float gamma value when decoding (from 0.001 to FLT_MAX) (default 1)
        apply_trc: color transfer characteristics to apply to EXR linear input (from 1 to 18) (default gamma)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ffv1() -> FFMpegDecoderOption:
    """
    FFmpeg video codec #1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ffvhuff() -> FFMpegDecoderOption:
    """
    Huffyuv FFmpeg variant


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def fic(
    skip_cursor: bool | None = None,
) -> FFMpegDecoderOption:
    """
    Mirillis FIC

    Args:
        skip_cursor: skip the cursor (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def fits(
    blank_value: int | None = None,
) -> FFMpegDecoderOption:
    """
    Flexible Image Transport System

    Args:
        blank_value: value that is used to replace BLANK pixels in data array (from 0 to 65535) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def flashsv() -> FFMpegDecoderOption:
    """
    Flash Screen Video v1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def flashsv2() -> FFMpegDecoderOption:
    """
    Flash Screen Video v2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def flic() -> FFMpegDecoderOption:
    """
    Autodesk Animator Flic video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def flv() -> FFMpegDecoderOption:
    """
    FLV / Sorenson Spark / Sorenson H.263 (Flash Video) (codec flv1)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def fmvc() -> FFMpegDecoderOption:
    """
    FM Screen Capture Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def fraps() -> FFMpegDecoderOption:
    """
    Fraps


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def frwu(
    change_field_order: bool | None = None,
) -> FFMpegDecoderOption:
    """
    Forward Uncompressed

    Args:
        change_field_order: Change field order (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def g2m() -> FFMpegDecoderOption:
    """
    Go2Meeting


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def gdv() -> FFMpegDecoderOption:
    """
    Gremlin Digital Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def gem() -> FFMpegDecoderOption:
    """
    GEM Raster image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def gif(
    trans_color: int | None = None,
) -> FFMpegDecoderOption:
    """
    GIF (Graphics Interchange Format)

    Args:
        trans_color: color value (ARGB) that is used instead of transparent color (from 0 to UINT32_MAX) (default 16777215)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def h261() -> FFMpegDecoderOption:
    """
    H.261


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def h263() -> FFMpegDecoderOption:
    """
    H.263 / H.263-1996, H.263+ / H.263-1998 / H.263 version 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def h263_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem H.263 decoder wrapper (codec h263)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def h263i() -> FFMpegDecoderOption:
    """
    Intel H.263


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def h263p() -> FFMpegDecoderOption:
    """
    H.263 / H.263-1996, H.263+ / H.263-1998 / H.263 version 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def h264(
    is_avc: bool | None = None,
    nal_length_size: int | None = None,
    enable_er: bool | None = None,
    x264_build: int | None = None,
) -> FFMpegDecoderOption:
    """
    H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10

    Args:
        is_avc: is avc (default false)
        nal_length_size: nal_length_size (from 0 to 4) (default 0)
        enable_er: Enable error resilience on damaged frames (unsafe) (default auto)
        x264_build: Assume this x264 version if no x264 version found in any SEI (from -1 to INT_MAX) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def h264_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem H.264 decoder wrapper (codec h264)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def h264_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID H264 decoder (codec h264)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hap() -> FFMpegDecoderOption:
    """
    Vidvox Hap


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hdr() -> FFMpegDecoderOption:
    """
    HDR (Radiance RGBE format) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hevc(
    apply_defdispwin: bool | None = None,
    strict_displaywin: bool | None = None,
) -> FFMpegDecoderOption:
    """
    HEVC (High Efficiency Video Coding)

    Args:
        apply_defdispwin: Apply default display window from VUI (default false)
        strict_displaywin: stricly apply default display window size (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hevc_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem HEVC decoder wrapper (codec hevc)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hevc_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID HEVC decoder (codec hevc)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hnm4video() -> FFMpegDecoderOption:
    """
    HNM 4 video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hq_hqa() -> FFMpegDecoderOption:
    """
    Canopus HQ/HQA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hqx() -> FFMpegDecoderOption:
    """
    Canopus HQX


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def huffyuv() -> FFMpegDecoderOption:
    """
    Huffyuv / HuffYUV


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hymt() -> FFMpegDecoderOption:
    """
    HuffYUV MT


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def idcinvideo() -> FFMpegDecoderOption:
    """
    id Quake II CIN video (codec idcin)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def idf() -> FFMpegDecoderOption:
    """
    iCEDraw text


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def iff() -> FFMpegDecoderOption:
    """
    IFF ACBM/ANIM/DEEP/ILBM/PBM/RGB8/RGBN (codec iff_ilbm)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def imm4() -> FFMpegDecoderOption:
    """
    Infinity IMM4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def imm5() -> FFMpegDecoderOption:
    """
    Infinity IMM5


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def indeo2() -> FFMpegDecoderOption:
    """
    Intel Indeo 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def indeo3() -> FFMpegDecoderOption:
    """
    Intel Indeo 3


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def indeo4() -> FFMpegDecoderOption:
    """
    Intel Indeo Video Interactive 4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def indeo5() -> FFMpegDecoderOption:
    """
    Intel Indeo Video Interactive 5


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def interplayvideo() -> FFMpegDecoderOption:
    """
    Interplay MVE video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ipu() -> FFMpegDecoderOption:
    """
    IPU Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def jpeg2000(
    lowres: int | None = None,
) -> FFMpegDecoderOption:
    """
    JPEG 2000

    Args:
        lowres: Lower the decoding resolution by a power of two (from 0 to 33) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def jpegls() -> FFMpegDecoderOption:
    """
    JPEG-LS


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libjxl() -> FFMpegDecoderOption:
    """
    libjxl JPEG XL (codec jpegxl)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def jv() -> FFMpegDecoderOption:
    """
    Bitmap Brothers JV video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def kgv1() -> FFMpegDecoderOption:
    """
    Kega Game Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def kmvc() -> FFMpegDecoderOption:
    """
    Karl Morton's video codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def lagarith() -> FFMpegDecoderOption:
    """
    Lagarith lossless


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def loco() -> FFMpegDecoderOption:
    """
    LOCO


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def lscr() -> FFMpegDecoderOption:
    """
    LEAD Screen Capture


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def m101() -> FFMpegDecoderOption:
    """
    Matrox Uncompressed SD


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def eamad() -> FFMpegDecoderOption:
    """
    Electronic Arts Madcow Video (codec mad)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def magicyuv() -> FFMpegDecoderOption:
    """
    MagicYUV video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mdec() -> FFMpegDecoderOption:
    """
    Sony PlayStation MDEC (Motion DECoder)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def media100() -> FFMpegDecoderOption:
    """
    Media 100


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mimic() -> FFMpegDecoderOption:
    """
    Mimic


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mjpeg(
    extern_huff: bool | None = None,
) -> FFMpegDecoderOption:
    """
    MJPEG (Motion JPEG)

    Args:
        extern_huff: Use external huffman table. (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mjpeg_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID MJPEG decoder (codec mjpeg)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mjpegb() -> FFMpegDecoderOption:
    """
    Apple MJPEG-B


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mmvideo() -> FFMpegDecoderOption:
    """
    American Laser Games MM Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mobiclip() -> FFMpegDecoderOption:
    """
    MobiClip Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def motionpixels() -> FFMpegDecoderOption:
    """
    Motion Pixels video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg1video() -> FFMpegDecoderOption:
    """
    MPEG-1 video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg1_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem MPEG1 decoder wrapper (codec mpeg1video)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg1_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID MPEG1VIDEO decoder (codec mpeg1video)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg2video() -> FFMpegDecoderOption:
    """
    MPEG-2 video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpegvideo() -> FFMpegDecoderOption:
    """
    MPEG-1 video (codec mpeg2video)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg2_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem MPEG2 decoder wrapper (codec mpeg2video)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg2_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID MPEG2VIDEO decoder (codec mpeg2video)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg4() -> FFMpegDecoderOption:
    """
    MPEG-4 part 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg4_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem MPEG4 decoder wrapper (codec mpeg4)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpeg4_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID MPEG4 decoder (codec mpeg4)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def msa1() -> FFMpegDecoderOption:
    """
    MS ATC Screen


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mscc() -> FFMpegDecoderOption:
    """
    Mandsoft Screen Capture Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def msmpeg4v1() -> FFMpegDecoderOption:
    """
    MPEG-4 part 2 Microsoft variant version 1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def msmpeg4v2() -> FFMpegDecoderOption:
    """
    MPEG-4 part 2 Microsoft variant version 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def msmpeg4() -> FFMpegDecoderOption:
    """
    MPEG-4 part 2 Microsoft variant version 3 (codec msmpeg4v3)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def msp2() -> FFMpegDecoderOption:
    """
    Microsoft Paint (MSP) version 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def msrle() -> FFMpegDecoderOption:
    """
    Microsoft RLE


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mss1() -> FFMpegDecoderOption:
    """
    MS Screen 1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mss2() -> FFMpegDecoderOption:
    """
    MS Windows Media Video V9 Screen


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def msvideo1() -> FFMpegDecoderOption:
    """
    Microsoft Video 1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mszh() -> FFMpegDecoderOption:
    """
    LCL (LossLess Codec Library) MSZH


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mts2() -> FFMpegDecoderOption:
    """
    MS Expression Encoder Screen


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mv30() -> FFMpegDecoderOption:
    """
    MidiVid 3.0


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mvc1() -> FFMpegDecoderOption:
    """
    Silicon Graphics Motion Video Compressor 1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mvc2() -> FFMpegDecoderOption:
    """
    Silicon Graphics Motion Video Compressor 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mvdv() -> FFMpegDecoderOption:
    """
    MidiVid VQ


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mvha() -> FFMpegDecoderOption:
    """
    MidiVid Archive Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mwsc() -> FFMpegDecoderOption:
    """
    MatchWare Screen Capture Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mxpeg() -> FFMpegDecoderOption:
    """
    Mobotix MxPEG video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def notchlc() -> FFMpegDecoderOption:
    """
    NotchLC


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def nuv() -> FFMpegDecoderOption:
    """
    NuppelVideo/RTJPEG


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def paf_video() -> FFMpegDecoderOption:
    """
    Amazing Studio Packed Animation File Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pam() -> FFMpegDecoderOption:
    """
    PAM (Portable AnyMap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pbm() -> FFMpegDecoderOption:
    """
    PBM (Portable BitMap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcx() -> FFMpegDecoderOption:
    """
    PC Paintbrush PCX image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pdv() -> FFMpegDecoderOption:
    """
    PDV (PlayDate Video)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pfm() -> FFMpegDecoderOption:
    """
    PFM (Portable FloatMap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pgm() -> FFMpegDecoderOption:
    """
    PGM (Portable GrayMap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pgmyuv() -> FFMpegDecoderOption:
    """
    PGMYUV (Portable GrayMap YUV) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pgx() -> FFMpegDecoderOption:
    """
    PGX (JPEG2000 Test Format)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def phm() -> FFMpegDecoderOption:
    """
    PHM (Portable HalfFloatMap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def photocd(
    lowres: int | None = None,
) -> FFMpegDecoderOption:
    """
    Kodak Photo CD

    Args:
        lowres: Lower the decoding resolution by a power of two (from 0 to 4) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pictor() -> FFMpegDecoderOption:
    """
    Pictor/PC Paint


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pixlet() -> FFMpegDecoderOption:
    """
    Apple Pixlet


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def png() -> FFMpegDecoderOption:
    """
    PNG (Portable Network Graphics) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ppm() -> FFMpegDecoderOption:
    """
    PPM (Portable PixelMap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def prores() -> FFMpegDecoderOption:
    """
    Apple ProRes (iCodec Pro)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def prosumer() -> FFMpegDecoderOption:
    """
    Brooktree ProSumer Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def psd() -> FFMpegDecoderOption:
    """
    Photoshop PSD file


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ptx() -> FFMpegDecoderOption:
    """
    V.Flash PTX image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def qdraw() -> FFMpegDecoderOption:
    """
    Apple QuickDraw


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def qoi() -> FFMpegDecoderOption:
    """
    QOI (Quite OK Image format) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def qpeg() -> FFMpegDecoderOption:
    """
    Q-team QPEG


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def qtrle() -> FFMpegDecoderOption:
    """
    QuickTime Animation (RLE) video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def r10k() -> FFMpegDecoderOption:
    """
    AJA Kona 10-bit RGB Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def r210() -> FFMpegDecoderOption:
    """
    Uncompressed RGB 10-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rasc(
    skip_cursor: bool | None = None,
) -> FFMpegDecoderOption:
    """
    RemotelyAnywhere Screen Capture

    Args:
        skip_cursor: skip the cursor (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rawvideo(
    top: bool | None = None,
) -> FFMpegDecoderOption:
    """
    raw video

    Args:
        top: top field first (default auto)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rl2() -> FFMpegDecoderOption:
    """
    RL2 video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def roqvideo() -> FFMpegDecoderOption:
    """
    id RoQ video (codec roq)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rpza() -> FFMpegDecoderOption:
    """
    QuickTime video (RPZA)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rscc() -> FFMpegDecoderOption:
    """
    innoHeim/Rsupport Screen Capture Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rtv1() -> FFMpegDecoderOption:
    """
    RTV1 (RivaTuner Video)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rv10() -> FFMpegDecoderOption:
    """
    RealVideo 1.0


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rv20() -> FFMpegDecoderOption:
    """
    RealVideo 2.0


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rv30() -> FFMpegDecoderOption:
    """
    RealVideo 3.0


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rv40() -> FFMpegDecoderOption:
    """
    RealVideo 4.0


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sanm() -> FFMpegDecoderOption:
    """
    LucasArts SANM/Smush video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def scpr() -> FFMpegDecoderOption:
    """
    ScreenPressor


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def screenpresso() -> FFMpegDecoderOption:
    """
    Screenpresso


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sga() -> FFMpegDecoderOption:
    """
    Digital Pictures SGA Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sgi() -> FFMpegDecoderOption:
    """
    SGI image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sgirle() -> FFMpegDecoderOption:
    """
    Silicon Graphics RLE 8-bit video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sheervideo() -> FFMpegDecoderOption:
    """
    BitJazz SheerVideo


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def simbiosis_imx() -> FFMpegDecoderOption:
    """
    Simbiosis Interactive IMX Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def smackvid() -> FFMpegDecoderOption:
    """
    Smacker video (codec smackvideo)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def smc() -> FFMpegDecoderOption:
    """
    QuickTime Graphics (SMC)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def smvjpeg() -> FFMpegDecoderOption:
    """
    SMV JPEG


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def snow() -> FFMpegDecoderOption:
    """
    Snow


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sp5x() -> FFMpegDecoderOption:
    """
    Sunplus JPEG (SP5X)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def speedhq() -> FFMpegDecoderOption:
    """
    NewTek SpeedHQ


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def srgc() -> FFMpegDecoderOption:
    """
    Screen Recorder Gold Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sunrast() -> FFMpegDecoderOption:
    """
    Sun Rasterfile image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def librsvg(
    width: int | None = None,
    height: int | None = None,
    keep_ar: bool | None = None,
) -> FFMpegDecoderOption:
    """
    Librsvg rasterizer (codec svg)

    Args:
        width: Width to render to (0 for default) (from 0 to INT_MAX) (default 0)
        height: Height to render to (0 for default) (from 0 to INT_MAX) (default 0)
        keep_ar: Keep aspect ratio with custom width/height (default true)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def svq1() -> FFMpegDecoderOption:
    """
    Sorenson Vector Quantizer 1 / Sorenson Video 1 / SVQ1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def svq3() -> FFMpegDecoderOption:
    """
    Sorenson Vector Quantizer 3 / Sorenson Video 3 / SVQ3


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def targa() -> FFMpegDecoderOption:
    """
    Truevision Targa image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def targa_y216() -> FFMpegDecoderOption:
    """
    Pinnacle TARGA CineWave YUV16


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def tdsc() -> FFMpegDecoderOption:
    """
    TDSC


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def eatgq() -> FFMpegDecoderOption:
    """
    Electronic Arts TGQ video (codec tgq)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def eatgv() -> FFMpegDecoderOption:
    """
    Electronic Arts TGV video (codec tgv)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def theora() -> FFMpegDecoderOption:
    """
    Theora


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def thp() -> FFMpegDecoderOption:
    """
    Nintendo Gamecube THP video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def tiertexseqvideo() -> FFMpegDecoderOption:
    """
    Tiertex Limited SEQ video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def tiff(
    subimage: bool | None = None,
    thumbnail: bool | None = None,
    page: int | None = None,
) -> FFMpegDecoderOption:
    """
    TIFF image

    Args:
        subimage: decode subimage instead if available (default false)
        thumbnail: decode embedded thumbnail subimage instead if available (default false)
        page: page number of multi-page image to decode (starting from 1) (from 0 to 65535) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def tmv() -> FFMpegDecoderOption:
    """
    8088flex TMV


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def eatqi() -> FFMpegDecoderOption:
    """
    Electronic Arts TQI Video (codec tqi)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def truemotion1() -> FFMpegDecoderOption:
    """
    Duck TrueMotion 1.0


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def truemotion2() -> FFMpegDecoderOption:
    """
    Duck TrueMotion 2.0


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def truemotion2rt() -> FFMpegDecoderOption:
    """
    Duck TrueMotion 2.0 Real Time


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def camtasia() -> FFMpegDecoderOption:
    """
    TechSmith Screen Capture Codec (codec tscc)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def tscc2() -> FFMpegDecoderOption:
    """
    TechSmith Screen Codec 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def txd() -> FFMpegDecoderOption:
    """
    Renderware TXD (TeXture Dictionary) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ultimotion() -> FFMpegDecoderOption:
    """
    IBM UltiMotion (codec ulti)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def utvideo() -> FFMpegDecoderOption:
    """
    Ut Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def v210(
    custom_stride: int | None = None,
) -> FFMpegDecoderOption:
    """
    Uncompressed 4:2:2 10-bit

    Args:
        custom_stride: Custom V210 stride (from -1 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def v210x() -> FFMpegDecoderOption:
    """
    Uncompressed 4:2:2 10-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def v308() -> FFMpegDecoderOption:
    """
    Uncompressed packed 4:4:4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def v408() -> FFMpegDecoderOption:
    """
    Uncompressed packed QT 4:4:4:4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def v410() -> FFMpegDecoderOption:
    """
    Uncompressed 4:4:4 10-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vb() -> FFMpegDecoderOption:
    """
    Beam Software VB


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vble() -> FFMpegDecoderOption:
    """
    VBLE Lossless Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vbn() -> FFMpegDecoderOption:
    """
    Vizrt Binary Image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vc1() -> FFMpegDecoderOption:
    """
    SMPTE VC-1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vc1_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem VC1 decoder wrapper (codec vc1)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vc1_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID VC1 decoder (codec vc1)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vc1image() -> FFMpegDecoderOption:
    """
    Windows Media Video 9 Image v2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vcr1() -> FFMpegDecoderOption:
    """
    ATI VCR1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xl() -> FFMpegDecoderOption:
    """
    Miro VideoXL (codec vixl)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vmdvideo() -> FFMpegDecoderOption:
    """
    Sierra VMD video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vmix() -> FFMpegDecoderOption:
    """
    vMix Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vmnc() -> FFMpegDecoderOption:
    """
    VMware Screen Codec / VMware Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vnull() -> FFMpegDecoderOption:
    """
    null video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp3() -> FFMpegDecoderOption:
    """
    On2 VP3


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp4() -> FFMpegDecoderOption:
    """
    On2 VP4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp5() -> FFMpegDecoderOption:
    """
    On2 VP5


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp6() -> FFMpegDecoderOption:
    """
    On2 VP6


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp6a() -> FFMpegDecoderOption:
    """
    On2 VP6 (Flash version, with alpha channel)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp6f() -> FFMpegDecoderOption:
    """
    On2 VP6 (Flash version)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp7() -> FFMpegDecoderOption:
    """
    On2 VP7


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp8() -> FFMpegDecoderOption:
    """
    On2 VP8


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp8_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem VP8 decoder wrapper (codec vp8)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libvpx() -> FFMpegDecoderOption:
    """
    libvpx VP8 (codec vp8)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp8_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID VP8 decoder (codec vp8)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp9() -> FFMpegDecoderOption:
    """
    Google VP9


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp9_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegDecoderOption:
    """
    V4L2 mem2mem VP9 decoder wrapper (codec vp9)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 2 to INT_MAX) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vp9_cuvid(
    deint: int | None | Literal["weave", "bob", "adaptive"] = None,
    gpu: str | None = None,
    surfaces: int | None = None,
    drop_second_field: bool | None = None,
    crop: str | None = None,
    resize: str | None = None,
) -> FFMpegDecoderOption:
    """
    Nvidia CUVID VP9 decoder (codec vp9)

    Args:
        deint: Set deinterlacing mode (from 0 to 2) (default weave)
        gpu: GPU to be used for decoding
        surfaces: Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)
        drop_second_field: Drop second field when deinterlacing (default false)
        crop: Crop (top)x(bottom)x(left)x(right)
        resize: Resize (width)x(height)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vqc() -> FFMpegDecoderOption:
    """
    ViewQuest VQC


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wbmp() -> FFMpegDecoderOption:
    """
    WBMP (Wireless Application Protocol Bitmap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wcmv() -> FFMpegDecoderOption:
    """
    WinCAM Motion Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def webp() -> FFMpegDecoderOption:
    """
    WebP image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmv1() -> FFMpegDecoderOption:
    """
    Windows Media Video 7


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmv2() -> FFMpegDecoderOption:
    """
    Windows Media Video 8


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmv3() -> FFMpegDecoderOption:
    """
    Windows Media Video 9


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmv3image() -> FFMpegDecoderOption:
    """
    Windows Media Video 9 Image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wnv1() -> FFMpegDecoderOption:
    """
    Winnov WNV1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wrapped_avframe() -> FFMpegDecoderOption:
    """
    AVPacket to AVFrame passthrough


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vqavideo() -> FFMpegDecoderOption:
    """
    Westwood Studios VQA (Vector Quantized Animation) video (codec ws_vqa)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xan_wc3() -> FFMpegDecoderOption:
    """
    Wing Commander III / Xan


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xan_wc4() -> FFMpegDecoderOption:
    """
    Wing Commander IV / Xxan


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xbin() -> FFMpegDecoderOption:
    """
    eXtended BINary text


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xbm() -> FFMpegDecoderOption:
    """
    XBM (X BitMap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xface() -> FFMpegDecoderOption:
    """
    X-face image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xpm() -> FFMpegDecoderOption:
    """
    XPM (X PixMap) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xwd() -> FFMpegDecoderOption:
    """
    XWD (X Window Dump) image


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def y41p() -> FFMpegDecoderOption:
    """
    Uncompressed YUV 4:1:1 12-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ylc() -> FFMpegDecoderOption:
    """
    YUY2 Lossless Codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def yop() -> FFMpegDecoderOption:
    """
    Psygnosis YOP Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def yuv4() -> FFMpegDecoderOption:
    """
    Uncompressed packed 4:2:0


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def zerocodec() -> FFMpegDecoderOption:
    """
    ZeroCodec Lossless Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def zlib() -> FFMpegDecoderOption:
    """
    LCL (LossLess Codec Library) ZLIB


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def zmbv() -> FFMpegDecoderOption:
    """
    Zip Motion Blocks Video


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def _8svx_exp() -> FFMpegDecoderOption:
    """
    8SVX exponential


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def _8svx_fib() -> FFMpegDecoderOption:
    """
    8SVX fibonacci


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aac(
    dual_mono_mode: int | None | Literal["auto", "main", "sub", "both"] = None,
    channel_order: int | None | Literal["default", "coded"] = None,
) -> FFMpegDecoderOption:
    """
    AAC (Advanced Audio Coding)

    Args:
        dual_mono_mode: Select the channel to decode for dual mono (from -1 to 2) (default auto)
        channel_order: Order in which the channels are to be exported (from 0 to 1) (default default)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aac_fixed(
    dual_mono_mode: int | None | Literal["auto", "main", "sub", "both"] = None,
    channel_order: int | None | Literal["default", "coded"] = None,
) -> FFMpegDecoderOption:
    """
    AAC (Advanced Audio Coding) (codec aac)

    Args:
        dual_mono_mode: Select the channel to decode for dual mono (from -1 to 2) (default auto)
        channel_order: Order in which the channels are to be exported (from 0 to 1) (default default)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aac_latm() -> FFMpegDecoderOption:
    """
    AAC LATM (Advanced Audio Coding LATM syntax)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ac3() -> FFMpegDecoderOption:
    """
    ATSC A/52A (AC-3)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ac3_fixed() -> FFMpegDecoderOption:
    """
    ATSC A/52A (AC-3) (codec ac3)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_4xm() -> FFMpegDecoderOption:
    """
    ADPCM 4X Movie


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_adx() -> FFMpegDecoderOption:
    """
    SEGA CRI ADX ADPCM


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_afc() -> FFMpegDecoderOption:
    """
    ADPCM Nintendo Gamecube AFC


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_agm() -> FFMpegDecoderOption:
    """
    ADPCM AmuseGraphics Movie


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_aica() -> FFMpegDecoderOption:
    """
    ADPCM Yamaha AICA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_argo() -> FFMpegDecoderOption:
    """
    ADPCM Argonaut Games


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ct() -> FFMpegDecoderOption:
    """
    ADPCM Creative Technology


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_dtk() -> FFMpegDecoderOption:
    """
    ADPCM Nintendo Gamecube DTK


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ea() -> FFMpegDecoderOption:
    """
    ADPCM Electronic Arts


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ea_maxis_xa() -> FFMpegDecoderOption:
    """
    ADPCM Electronic Arts Maxis CDROM XA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ea_r1() -> FFMpegDecoderOption:
    """
    ADPCM Electronic Arts R1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ea_r2() -> FFMpegDecoderOption:
    """
    ADPCM Electronic Arts R2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ea_r3() -> FFMpegDecoderOption:
    """
    ADPCM Electronic Arts R3


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ea_xas() -> FFMpegDecoderOption:
    """
    ADPCM Electronic Arts XAS


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def g722(
    bits_per_codeword: int | None = None,
) -> FFMpegDecoderOption:
    """
    G.722 ADPCM (codec adpcm_g722)

    Args:
        bits_per_codeword: Bits per G722 codeword (from 6 to 8) (default 8)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def g726() -> FFMpegDecoderOption:
    """
    G.726 ADPCM (codec adpcm_g726)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def g726le() -> FFMpegDecoderOption:
    """
    G.726 ADPCM little-endian (codec adpcm_g726le)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_acorn() -> FFMpegDecoderOption:
    """
    ADPCM IMA Acorn Replay


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_alp() -> FFMpegDecoderOption:
    """
    ADPCM IMA High Voltage Software ALP


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_amv() -> FFMpegDecoderOption:
    """
    ADPCM IMA AMV


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_apc() -> FFMpegDecoderOption:
    """
    ADPCM IMA CRYO APC


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_apm() -> FFMpegDecoderOption:
    """
    ADPCM IMA Ubisoft APM


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_cunning() -> FFMpegDecoderOption:
    """
    ADPCM IMA Cunning Developments


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_dat4() -> FFMpegDecoderOption:
    """
    ADPCM IMA Eurocom DAT4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_dk3() -> FFMpegDecoderOption:
    """
    ADPCM IMA Duck DK3


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_dk4() -> FFMpegDecoderOption:
    """
    ADPCM IMA Duck DK4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_ea_eacs() -> FFMpegDecoderOption:
    """
    ADPCM IMA Electronic Arts EACS


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_ea_sead() -> FFMpegDecoderOption:
    """
    ADPCM IMA Electronic Arts SEAD


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_iss() -> FFMpegDecoderOption:
    """
    ADPCM IMA Funcom ISS


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_moflex() -> FFMpegDecoderOption:
    """
    ADPCM IMA MobiClip MOFLEX


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_mtf() -> FFMpegDecoderOption:
    """
    ADPCM IMA Capcom's MT Framework


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_oki() -> FFMpegDecoderOption:
    """
    ADPCM IMA Dialogic OKI


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_qt() -> FFMpegDecoderOption:
    """
    ADPCM IMA QuickTime


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_rad() -> FFMpegDecoderOption:
    """
    ADPCM IMA Radical


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_smjpeg() -> FFMpegDecoderOption:
    """
    ADPCM IMA Loki SDL MJPEG


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_ssi() -> FFMpegDecoderOption:
    """
    ADPCM IMA Simon & Schuster Interactive


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_wav() -> FFMpegDecoderOption:
    """
    ADPCM IMA WAV


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_ws() -> FFMpegDecoderOption:
    """
    ADPCM IMA Westwood


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_ms() -> FFMpegDecoderOption:
    """
    ADPCM Microsoft


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_mtaf() -> FFMpegDecoderOption:
    """
    ADPCM MTAF


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_psx() -> FFMpegDecoderOption:
    """
    ADPCM Playstation


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_sbpro_2() -> FFMpegDecoderOption:
    """
    ADPCM Sound Blaster Pro 2-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_sbpro_3() -> FFMpegDecoderOption:
    """
    ADPCM Sound Blaster Pro 2.6-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_sbpro_4() -> FFMpegDecoderOption:
    """
    ADPCM Sound Blaster Pro 4-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_swf() -> FFMpegDecoderOption:
    """
    ADPCM Shockwave Flash


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_thp() -> FFMpegDecoderOption:
    """
    ADPCM Nintendo THP


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_thp_le() -> FFMpegDecoderOption:
    """
    ADPCM Nintendo THP (little-endian)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_vima() -> FFMpegDecoderOption:
    """
    LucasArts VIMA audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_xa() -> FFMpegDecoderOption:
    """
    ADPCM CDROM XA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_xmd() -> FFMpegDecoderOption:
    """
    ADPCM Konami XMD


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_yamaha() -> FFMpegDecoderOption:
    """
    ADPCM Yamaha


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def adpcm_zork() -> FFMpegDecoderOption:
    """
    ADPCM Zork


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def alac(
    extra_bits_bug: bool | None = None,
) -> FFMpegDecoderOption:
    """
    ALAC (Apple Lossless Audio Codec)

    Args:
        extra_bits_bug: Force non-standard decoding process (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def amrnb() -> FFMpegDecoderOption:
    """
    AMR-NB (Adaptive Multi-Rate NarrowBand) (codec amr_nb)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def amrwb() -> FFMpegDecoderOption:
    """
    AMR-WB (Adaptive Multi-Rate WideBand) (codec amr_wb)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def anull() -> FFMpegDecoderOption:
    """
    null audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def apac() -> FFMpegDecoderOption:
    """
    Marian's A-pac audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ape(
    max_samples: int | None | Literal["all"] = None,
) -> FFMpegDecoderOption:
    """
    Monkey's Audio

    Args:
        max_samples: maximum number of samples decoded per call (from 1 to INT_MAX) (default 4608)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aptx() -> FFMpegDecoderOption:
    """
    aptX (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def aptx_hd() -> FFMpegDecoderOption:
    """
    aptX HD (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def atrac1() -> FFMpegDecoderOption:
    """
    ATRAC1 (Adaptive TRansform Acoustic Coding)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def atrac3() -> FFMpegDecoderOption:
    """
    ATRAC3 (Adaptive TRansform Acoustic Coding 3)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def atrac3al() -> FFMpegDecoderOption:
    """
    ATRAC3 AL (Adaptive TRansform Acoustic Coding 3 Advanced Lossless)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def atrac3plus() -> FFMpegDecoderOption:
    """
    ATRAC3+ (Adaptive TRansform Acoustic Coding 3+) (codec atrac3p)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def atrac3plusal() -> FFMpegDecoderOption:
    """
    ATRAC3+ AL (Adaptive TRansform Acoustic Coding 3+ Advanced Lossless) (codec atrac3pal)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def atrac9() -> FFMpegDecoderOption:
    """
    ATRAC9 (Adaptive TRansform Acoustic Coding 9)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def on2avc() -> FFMpegDecoderOption:
    """
    On2 Audio for Video Codec (codec avc)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def binkaudio_dct() -> FFMpegDecoderOption:
    """
    Bink Audio (DCT)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def binkaudio_rdft() -> FFMpegDecoderOption:
    """
    Bink Audio (RDFT)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def bmv_audio() -> FFMpegDecoderOption:
    """
    Discworld II BMV audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def bonk() -> FFMpegDecoderOption:
    """
    Bonk audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cbd2_dpcm() -> FFMpegDecoderOption:
    """
    DPCM Cuberoot-Delta-Exact


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libcodec2() -> FFMpegDecoderOption:
    """
    codec2 decoder using libcodec2 (codec codec2)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def comfortnoise() -> FFMpegDecoderOption:
    """
    RFC 3389 comfort noise generator


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cook() -> FFMpegDecoderOption:
    """
    Cook / Cooker / Gecko (RealAudio G2)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def derf_dpcm() -> FFMpegDecoderOption:
    """
    DPCM Xilam DERF


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dfpwm() -> FFMpegDecoderOption:
    """
    DFPWM1a audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dolby_e(
    channel_order: int | None | Literal["default", "coded"] = None,
) -> FFMpegDecoderOption:
    """
    Dolby E

    Args:
        channel_order: Order in which the channels are to be exported (from 0 to 1) (default default)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dsd_lsbf() -> FFMpegDecoderOption:
    """
    DSD (Direct Stream Digital), least significant bit first


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dsd_lsbf_planar() -> FFMpegDecoderOption:
    """
    DSD (Direct Stream Digital), least significant bit first, planar


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dsd_msbf() -> FFMpegDecoderOption:
    """
    DSD (Direct Stream Digital), most significant bit first


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dsd_msbf_planar() -> FFMpegDecoderOption:
    """
    DSD (Direct Stream Digital), most significant bit first, planar


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dsicinaudio() -> FFMpegDecoderOption:
    """
    Delphine Software International CIN audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dss_sp() -> FFMpegDecoderOption:
    """
    Digital Speech Standard - Standard Play mode (DSS SP)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dst() -> FFMpegDecoderOption:
    """
    DST (Digital Stream Transfer)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dca(
    core_only: bool | None = None,
    channel_order: int | None | Literal["default", "coded"] = None,
    downmix: str | None = None,
) -> FFMpegDecoderOption:
    """
    DCA (DTS Coherent Acoustics) (codec dts)

    Args:
        core_only: Decode core only without extensions (default false)
        channel_order: Order in which the channels are to be exported (from 0 to 1) (default default)
        downmix: Request a specific channel layout from the decoder

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dvaudio() -> FFMpegDecoderOption:
    """
    Ulead DV Audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def eac3() -> FFMpegDecoderOption:
    """
    ATSC A/52B (AC-3, E-AC-3)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def evrc(
    postfilter: bool | None = None,
) -> FFMpegDecoderOption:
    """
    EVRC (Enhanced Variable Rate Codec)

    Args:
        postfilter: enable postfilter (default true)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def fastaudio() -> FFMpegDecoderOption:
    """
    MobiClip FastAudio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def flac(
    use_buggy_lpc: bool | None = None,
) -> FFMpegDecoderOption:
    """
    FLAC (Free Lossless Audio Codec)

    Args:
        use_buggy_lpc: emulate old buggy lavc behavior (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ftr() -> FFMpegDecoderOption:
    """
    FTR Voice


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def g723_1(
    postfilter: bool | None = None,
) -> FFMpegDecoderOption:
    """
    G.723.1

    Args:
        postfilter: enable postfilter (default true)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def g729() -> FFMpegDecoderOption:
    """
    G.729


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def gremlin_dpcm() -> FFMpegDecoderOption:
    """
    DPCM Gremlin


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def gsm() -> FFMpegDecoderOption:
    """
    GSM


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libgsm() -> FFMpegDecoderOption:
    """
    libgsm GSM (codec gsm)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def gsm_ms() -> FFMpegDecoderOption:
    """
    GSM Microsoft variant


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libgsm_ms() -> FFMpegDecoderOption:
    """
    libgsm GSM Microsoft variant (codec gsm_ms)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hca() -> FFMpegDecoderOption:
    """
    CRI HCA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def hcom() -> FFMpegDecoderOption:
    """
    HCOM Audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def iac() -> FFMpegDecoderOption:
    """
    IAC (Indeo Audio Coder)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ilbc() -> FFMpegDecoderOption:
    """
    iLBC (Internet Low Bitrate Codec)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def imc() -> FFMpegDecoderOption:
    """
    IMC (Intel Music Coder)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def interplay_dpcm() -> FFMpegDecoderOption:
    """
    DPCM Interplay


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def interplayacm() -> FFMpegDecoderOption:
    """
    Interplay ACM


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mace3() -> FFMpegDecoderOption:
    """
    MACE (Macintosh Audio Compression/Expansion) 3:1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mace6() -> FFMpegDecoderOption:
    """
    MACE (Macintosh Audio Compression/Expansion) 6:1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def metasound() -> FFMpegDecoderOption:
    """
    Voxware MetaSound


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def misc4() -> FFMpegDecoderOption:
    """
    Micronas SC-4 Audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mlp(
    downmix: str | None = None,
) -> FFMpegDecoderOption:
    """
    MLP (Meridian Lossless Packing)

    Args:
        downmix: Request a specific channel layout from the decoder

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp1() -> FFMpegDecoderOption:
    """
    MP1 (MPEG audio layer 1)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp1float() -> FFMpegDecoderOption:
    """
    MP1 (MPEG audio layer 1) (codec mp1)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp2() -> FFMpegDecoderOption:
    """
    MP2 (MPEG audio layer 2)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp2float() -> FFMpegDecoderOption:
    """
    MP2 (MPEG audio layer 2) (codec mp2)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp3float() -> FFMpegDecoderOption:
    """
    MP3 (MPEG audio layer 3) (codec mp3)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp3() -> FFMpegDecoderOption:
    """
    MP3 (MPEG audio layer 3)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp3adufloat() -> FFMpegDecoderOption:
    """
    ADU (Application Data Unit) MP3 (MPEG audio layer 3) (codec mp3adu)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp3adu() -> FFMpegDecoderOption:
    """
    ADU (Application Data Unit) MP3 (MPEG audio layer 3)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp3on4float() -> FFMpegDecoderOption:
    """
    MP3onMP4 (codec mp3on4)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mp3on4() -> FFMpegDecoderOption:
    """
    MP3onMP4


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def als() -> FFMpegDecoderOption:
    """
    MPEG-4 Audio Lossless Coding (ALS) (codec mp4als)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def msnsiren() -> FFMpegDecoderOption:
    """
    MSN Siren


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpc7() -> FFMpegDecoderOption:
    """
    Musepack SV7 (codec musepack7)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpc8() -> FFMpegDecoderOption:
    """
    Musepack SV8 (codec musepack8)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def nellymoser() -> FFMpegDecoderOption:
    """
    Nellymoser Asao


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def opus(
    apply_phase_inv: bool | None = None,
) -> FFMpegDecoderOption:
    """
    Opus

    Args:
        apply_phase_inv: Apply intensity stereo phase inversion (default true)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libopus(
    apply_phase_inv: bool | None = None,
) -> FFMpegDecoderOption:
    """
    libopus Opus (codec opus)

    Args:
        apply_phase_inv: Apply intensity stereo phase inversion (default true)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def osq() -> FFMpegDecoderOption:
    """
    OSQ (Original Sound Quality)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def paf_audio() -> FFMpegDecoderOption:
    """
    Amazing Studio Packed Animation File Audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_alaw() -> FFMpegDecoderOption:
    """
    PCM A-law / G.711 A-law


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_bluray() -> FFMpegDecoderOption:
    """
    PCM signed 16|20|24-bit big-endian for Blu-ray media


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_dvd() -> FFMpegDecoderOption:
    """
    PCM signed 16|20|24-bit big-endian for DVD media


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_f16le() -> FFMpegDecoderOption:
    """
    PCM 16.8 floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_f24le() -> FFMpegDecoderOption:
    """
    PCM 24.0 floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_f32be() -> FFMpegDecoderOption:
    """
    PCM 32-bit floating point big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_f32le() -> FFMpegDecoderOption:
    """
    PCM 32-bit floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_f64be() -> FFMpegDecoderOption:
    """
    PCM 64-bit floating point big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_f64le() -> FFMpegDecoderOption:
    """
    PCM 64-bit floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_lxf() -> FFMpegDecoderOption:
    """
    PCM signed 20-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_mulaw() -> FFMpegDecoderOption:
    """
    PCM mu-law / G.711 mu-law


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s16be() -> FFMpegDecoderOption:
    """
    PCM signed 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s16be_planar() -> FFMpegDecoderOption:
    """
    PCM signed 16-bit big-endian planar


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s16le() -> FFMpegDecoderOption:
    """
    PCM signed 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s16le_planar() -> FFMpegDecoderOption:
    """
    PCM signed 16-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s24be() -> FFMpegDecoderOption:
    """
    PCM signed 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s24daud() -> FFMpegDecoderOption:
    """
    PCM D-Cinema audio signed 24-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s24le() -> FFMpegDecoderOption:
    """
    PCM signed 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s24le_planar() -> FFMpegDecoderOption:
    """
    PCM signed 24-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s32be() -> FFMpegDecoderOption:
    """
    PCM signed 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s32le() -> FFMpegDecoderOption:
    """
    PCM signed 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s32le_planar() -> FFMpegDecoderOption:
    """
    PCM signed 32-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s64be() -> FFMpegDecoderOption:
    """
    PCM signed 64-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s64le() -> FFMpegDecoderOption:
    """
    PCM signed 64-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s8() -> FFMpegDecoderOption:
    """
    PCM signed 8-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_s8_planar() -> FFMpegDecoderOption:
    """
    PCM signed 8-bit planar


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_sga() -> FFMpegDecoderOption:
    """
    PCM SGA


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_u16be() -> FFMpegDecoderOption:
    """
    PCM unsigned 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_u16le() -> FFMpegDecoderOption:
    """
    PCM unsigned 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_u24be() -> FFMpegDecoderOption:
    """
    PCM unsigned 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_u24le() -> FFMpegDecoderOption:
    """
    PCM unsigned 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_u32be() -> FFMpegDecoderOption:
    """
    PCM unsigned 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_u32le() -> FFMpegDecoderOption:
    """
    PCM unsigned 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_u8() -> FFMpegDecoderOption:
    """
    PCM unsigned 8-bit


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pcm_vidc() -> FFMpegDecoderOption:
    """
    PCM Archimedes VIDC


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def qcelp() -> FFMpegDecoderOption:
    """
    QCELP / PureVoice


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def qdm2() -> FFMpegDecoderOption:
    """
    QDesign Music Codec 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def qdmc() -> FFMpegDecoderOption:
    """
    QDesign Music Codec 1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def real_144() -> FFMpegDecoderOption:
    """
    RealAudio 1.0 (14.4K) (codec ra_144)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def real_288() -> FFMpegDecoderOption:
    """
    RealAudio 2.0 (28.8K) (codec ra_288)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ralf() -> FFMpegDecoderOption:
    """
    RealAudio Lossless


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def rka() -> FFMpegDecoderOption:
    """
    RKA (RK Audio)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def roq_dpcm() -> FFMpegDecoderOption:
    """
    DPCM id RoQ


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def s302m(
    non_pcm_mode: int
    | None
    | Literal["copy", "drop", "decode_copy", "decode_drop"] = None,
) -> FFMpegDecoderOption:
    """
    SMPTE 302M

    Args:
        non_pcm_mode: Chooses what to do with NON-PCM (from 0 to 3) (default decode_drop)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sbc() -> FFMpegDecoderOption:
    """
    SBC (low-complexity subband codec)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sdx2_dpcm() -> FFMpegDecoderOption:
    """
    DPCM Squareroot-Delta-Exact


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def shorten() -> FFMpegDecoderOption:
    """
    Shorten


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sipr() -> FFMpegDecoderOption:
    """
    RealAudio SIPR / ACELP.NET


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def siren() -> FFMpegDecoderOption:
    """
    Siren


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def smackaud() -> FFMpegDecoderOption:
    """
    Smacker audio (codec smackaudio)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sol_dpcm() -> FFMpegDecoderOption:
    """
    DPCM Sol


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sonic() -> FFMpegDecoderOption:
    """
    Sonic


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def speex() -> FFMpegDecoderOption:
    """
    Speex


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libspeex() -> FFMpegDecoderOption:
    """
    libspeex Speex (codec speex)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def tak() -> FFMpegDecoderOption:
    """
    TAK (Tom's lossless Audio Kompressor)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def truehd(
    downmix: str | None = None,
) -> FFMpegDecoderOption:
    """
    TrueHD

    Args:
        downmix: Request a specific channel layout from the decoder

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def truespeech() -> FFMpegDecoderOption:
    """
    DSP Group TrueSpeech


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def tta(
    password: str | None = None,
) -> FFMpegDecoderOption:
    """
    TTA (True Audio)

    Args:
        password: Set decoding password

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def twinvq() -> FFMpegDecoderOption:
    """
    VQF TwinVQ


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vmdaudio() -> FFMpegDecoderOption:
    """
    Sierra VMD audio


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vorbis() -> FFMpegDecoderOption:
    """
    Vorbis


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libvorbis() -> FFMpegDecoderOption:
    """
    libvorbis (codec vorbis)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wady_dpcm() -> FFMpegDecoderOption:
    """
    DPCM Marble WADY


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wavarc() -> FFMpegDecoderOption:
    """
    Waveform Archiver


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wavesynth() -> FFMpegDecoderOption:
    """
    Wave synthesis pseudo-codec


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wavpack() -> FFMpegDecoderOption:
    """
    WavPack


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ws_snd1() -> FFMpegDecoderOption:
    """
    Westwood Audio (SND1) (codec westwood_snd1)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmalossless() -> FFMpegDecoderOption:
    """
    Windows Media Audio Lossless


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmapro() -> FFMpegDecoderOption:
    """
    Windows Media Audio 9 Professional


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmav1() -> FFMpegDecoderOption:
    """
    Windows Media Audio 1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmav2() -> FFMpegDecoderOption:
    """
    Windows Media Audio 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def wmavoice() -> FFMpegDecoderOption:
    """
    Windows Media Audio Voice


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xan_dpcm() -> FFMpegDecoderOption:
    """
    DPCM Xan


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xma1() -> FFMpegDecoderOption:
    """
    Xbox Media Audio 1


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xma2() -> FFMpegDecoderOption:
    """
    Xbox Media Audio 2


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ssa() -> FFMpegDecoderOption:
    """
    ASS (Advanced SubStation Alpha) subtitle (codec ass)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def ass() -> FFMpegDecoderOption:
    """
    ASS (Advanced SubStation Alpha) subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dvbsub(
    compute_edt: bool | None = None,
    compute_clut: bool | None = None,
    dvb_substream: int | None = None,
) -> FFMpegDecoderOption:
    """
    DVB subtitles (codec dvb_subtitle)

    Args:
        compute_edt: compute end of time using pts or timeout (default false)
        compute_clut: compute clut when not available(-1) or only once (-2) or always(1) or never(0) (default auto)
        dvb_substream: (from -1 to 63) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def libzvbi_teletextdec(
    txt_page: str | None = None,
    txt_default_region: int | None = None,
    txt_chop_top: int | None = None,
    txt_format: int | None | Literal["bitmap", "text", "ass"] = None,
    txt_left: int | None = None,
    txt_top: int | None = None,
    txt_chop_spaces: int | None = None,
    txt_duration: int | None = None,
    txt_transparent: int | None = None,
    txt_opacity: int | None = None,
) -> FFMpegDecoderOption:
    """
    Libzvbi DVB teletext decoder (codec dvb_teletext)

    Args:
        txt_page: page numbers to decode, subtitle for subtitles, * for all (default "*")
        txt_default_region: default G0 character set used for decoding (from -1 to 87) (default -1)
        txt_chop_top: discards the top teletext line (from 0 to 1) (default 1)
        txt_format: format of the subtitles (bitmap or text or ass) (from 0 to 2) (default bitmap)
        txt_left: x offset of generated bitmaps (from 0 to 65535) (default 0)
        txt_top: y offset of generated bitmaps (from 0 to 65535) (default 0)
        txt_chop_spaces: chops leading and trailing spaces from text (from 0 to 1) (default 1)
        txt_duration: display duration of teletext pages in msecs (from -1 to 8.64e+07) (default -1)
        txt_transparent: force transparent background of the teletext (from 0 to 1) (default 0)
        txt_opacity: set opacity of the transparent background (from -1 to 255) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def dvdsub(
    palette: str | None = None,
    ifo_palette: str | None = None,
    forced_subs_only: bool | None = None,
) -> FFMpegDecoderOption:
    """
    DVD subtitles (codec dvd_subtitle)

    Args:
        palette: set the global palette
        ifo_palette: obtain the global palette from .IFO file
        forced_subs_only: Only show forced subtitles (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def cc_dec(
    real_time: bool | None = None,
    real_time_latency_msec: int | None = None,
    data_field: int | None | Literal["auto", "first", "second"] = None,
) -> FFMpegDecoderOption:
    """
    Closed Caption (EIA-608 / CEA-708) (codec eia_608)

    Args:
        real_time: emit subtitle events as they are decoded for real-time display (default false)
        real_time_latency_msec: minimum elapsed time between emitting real-time subtitle events (from 0 to 500) (default 200)
        data_field: select data field (from -1 to 1) (default auto)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pgssub(
    forced_subs_only: bool | None = None,
) -> FFMpegDecoderOption:
    """
    HDMV Presentation Graphic Stream subtitles (codec hdmv_pgs_subtitle)

    Args:
        forced_subs_only: Only show forced subtitles (default false)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def jacosub() -> FFMpegDecoderOption:
    """
    JACOsub subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def microdvd() -> FFMpegDecoderOption:
    """
    MicroDVD subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mov_text(
    width: int | None = None,
    height: int | None = None,
) -> FFMpegDecoderOption:
    """
    3GPP Timed Text subtitle

    Args:
        width: Frame width, usually video width (from 0 to INT_MAX) (default 0)
        height: Frame height, usually video height (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def mpl2() -> FFMpegDecoderOption:
    """
    MPL2 subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def pjs() -> FFMpegDecoderOption:
    """
    PJS subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def realtext() -> FFMpegDecoderOption:
    """
    RealText subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def sami() -> FFMpegDecoderOption:
    """
    SAMI subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def stl() -> FFMpegDecoderOption:
    """
    Spruce subtitle format


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def srt() -> FFMpegDecoderOption:
    """
    SubRip subtitle (codec subrip)


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def subrip() -> FFMpegDecoderOption:
    """
    SubRip subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def subviewer() -> FFMpegDecoderOption:
    """
    SubViewer subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def subviewer1() -> FFMpegDecoderOption:
    """
    SubViewer1 subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def text() -> FFMpegDecoderOption:
    """
    Raw text subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def vplayer() -> FFMpegDecoderOption:
    """
    VPlayer subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def webvtt() -> FFMpegDecoderOption:
    """
    WebVTT subtitle


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))


def xsub() -> FFMpegDecoderOption:
    """
    XSUB


    Returns:
        the set codec options
    """
    return FFMpegDecoderOption(kwargs=FrozenDict(locals()))
