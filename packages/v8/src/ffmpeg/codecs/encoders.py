# NOTE: this file is auto-generated, do not modify
"""
FFmpeg encoders.
"""



from typing import Literal


from ..types import Binary, Boolean, Color, Dictionary, Double, Duration, Flags, Float, Func, Image_size, Int, Int64, Pix_fmt, Rational, Sample_fmt, String, Time, Video_rate

from ..dag.factory import filter_node_factory

from ..utils.frozendict import FrozenDict, merge
from ..utils.typing import override
from ..schema import Default, StreamType, Auto, FFMpegOptionGroup
from ..common.schema import FFMpegFilterDef
from ..options.framesync import FFMpegFrameSyncOption
from ..options.timeline import FFMpegTimelineOption

from ..options.codec import FFMpegAVCodecContextEncoderOption, FFMpegAVCodecContextDecoderOption


from ..options.format import FFMpegAVFormatContextEncoderOption, FFMpegAVFormatContextDecoderOption


from ..streams.av import AVStream

from ..streams.channel_layout import CHANNEL_LAYOUT
from .schema import FFMpegEncoderOption, FFMpegDecoderOption
from ..formats.schema import FFMpegMuxerOption, FFMpegDemuxerOption

from ..dag.nodes import FilterableStream, FilterNode, OutputStream, OutputNode, InputNode, GlobalNode, GlobalStream


from ..streams.video import VideoStream


from ..streams.audio import AudioStream





def a64multi(

) -> FFMpegEncoderOption:
    """
    Multicolor charset for Commodore 64 (codec a64_multi)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def a64multi5(

) -> FFMpegEncoderOption:
    """
    Multicolor charset for Commodore 64, extended with 5th color (colram) (codec a64_multi5)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def alias_pix(

) -> FFMpegEncoderOption:
    """
    Alias/Wavefront PIX image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def amv(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

) -> FFMpegEncoderOption:
    """
    AMV Video

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

    }))



def apng(

    dpi: int | None = None,

    dpm: int | None = None,

    pred: int | None| Literal["none", "sub", "up", "avg", "paeth", "mixed"] = None,

) -> FFMpegEncoderOption:
    """
    APNG (Animated Portable Network Graphics) image

    Args:
        dpi: Set image resolution (in dots per inch) (from 0 to 65536) (default 0)
        dpm: Set image resolution (in dots per meter) (from 0 to 65536) (default 0)
        pred: Prediction method (from 0 to 5) (default paeth)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "dpi": dpi,

        "dpm": dpm,

        "pred": pred,

    }))



def asv1(

) -> FFMpegEncoderOption:
    """
    ASUS V1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def asv2(

) -> FFMpegEncoderOption:
    """
    ASUS V2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def libsvtav1(

    preset: int | None = None,

    crf: int | None = None,

    qp: int | None = None,

    svtav1_params: str | None = None,

    dolbyvision: bool | None| Literal["auto"] = None,

) -> FFMpegEncoderOption:
    """
    SVT-AV1(Scalable Video Technology for AV1) encoder (codec av1)

    Args:
        preset: Encoding preset (from -2 to 13) (default -2)
        crf: Constant Rate Factor value (from 0 to 63) (default 0)
        qp: Initial Quantizer level value (from 0 to 63) (default 0)
        svtav1_params: Set the SVT-AV1 configuration using a :-separated list of key=value parameters
        dolbyvision: Enable Dolby Vision RPU coding (default auto)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "preset": preset,

        "crf": crf,

        "qp": qp,

        "svtav1-params": svtav1_params,

        "dolbyvision": dolbyvision,

    }))



def avrp(

) -> FFMpegEncoderOption:
    """
    Avid 1:1 10-bit RGB Packer


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def avui(

) -> FFMpegEncoderOption:
    """
    Avid Meridien Uncompressed


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def bitpacked(

) -> FFMpegEncoderOption:
    """
    Bitpacked


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def bmp(

) -> FFMpegEncoderOption:
    """
    BMP (Windows and OS/2 bitmap)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def cfhd(

    quality: int | None| Literal["film3+", "film3", "film2+", "film2", "film1.5", "film1+", "film1", "high+", "high", "medium+", "medium", "low+", "low"] = None,

) -> FFMpegEncoderOption:
    """
    GoPro CineForm HD

    Args:
        quality: set quality (from 0 to 12) (default film3+)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "quality": quality,

    }))



def cinepak(

    max_extra_cb_iterations: int | None = None,

    skip_empty_cb: bool | None = None,

    max_strips: int | None = None,

    min_strips: int | None = None,

    strip_number_adaptivity: int | None = None,

) -> FFMpegEncoderOption:
    """
    Cinepak

    Args:
        max_extra_cb_iterations: Max extra codebook recalculation passes, more is better and slower (from 0 to INT_MAX) (default 2)
        skip_empty_cb: Avoid wasting bytes, ignore vintage MacOS decoder (default false)
        max_strips: Limit strips/frame, vintage compatible is 1..3, otherwise the more the better (from 1 to 32) (default 3)
        min_strips: Enforce min strips/frame, more is worse and faster, must be <= max_strips (from 1 to 32) (default 1)
        strip_number_adaptivity: How fast the strip number adapts, more is slightly better, much slower (from 0 to 31) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "max_extra_cb_iterations": max_extra_cb_iterations,

        "skip_empty_cb": skip_empty_cb,

        "max_strips": max_strips,

        "min_strips": min_strips,

        "strip_number_adaptivity": strip_number_adaptivity,

    }))



def cljr(

    dither_type: int | None = None,

) -> FFMpegEncoderOption:
    """
    Cirrus Logic AccuPak

    Args:
        dither_type: Dither type (from 0 to 2) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "dither_type": dither_type,

    }))



def vc2(

    tolerance: float | None = None,

    slice_width: int | None = None,

    slice_height: int | None = None,

    wavelet_depth: int | None = None,

    wavelet_type: int | None| Literal["9_7", "5_3", "haar", "haar_noshift"] = None,

    qm: int | None| Literal["default", "color", "flat"] = None,

) -> FFMpegEncoderOption:
    """
    SMPTE VC-2 (codec dirac)

    Args:
        tolerance: Max undershoot in percent (from 0 to 45) (default 5)
        slice_width: Slice width (from 32 to 1024) (default 32)
        slice_height: Slice height (from 8 to 1024) (default 16)
        wavelet_depth: Transform depth (from 1 to 5) (default 4)
        wavelet_type: Transform type (from 0 to 7) (default 9_7)
        qm: Custom quantization matrix (from 0 to 3) (default default)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "tolerance": tolerance,

        "slice_width": slice_width,

        "slice_height": slice_height,

        "wavelet_depth": wavelet_depth,

        "wavelet_type": wavelet_type,

        "qm": qm,

    }))



def dnxhd(

    nitris_compat: bool | None = None,

    ibias: int | None = None,

    profile: int | None| Literal["dnxhd", "dnxhr_444", "dnxhr_hqx", "dnxhr_hq", "dnxhr_sq", "dnxhr_lb"] = None,

) -> FFMpegEncoderOption:
    """
    VC3/DNxHD

    Args:
        nitris_compat: encode with Avid Nitris compatibility (default false)
        ibias: intra quant bias (from INT_MIN to INT_MAX) (default 0)
        profile: (from 0 to 5) (default dnxhd)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "nitris_compat": nitris_compat,

        "ibias": ibias,

        "profile": profile,

    }))



def dpx(

) -> FFMpegEncoderOption:
    """
    DPX (Digital Picture Exchange) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def dvvideo(

    quant_deadzone: int | None = None,

) -> FFMpegEncoderOption:
    """
    DV (Digital Video)

    Args:
        quant_deadzone: Quantizer dead zone (from 0 to 1024) (default 7)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "quant_deadzone": quant_deadzone,

    }))



def dxv(

    format: int | None| Literal["dxt1"] = None,

) -> FFMpegEncoderOption:
    """
    Resolume DXV

    Args:
        format: (from 1.14664e+09 to 1.14664e+09) (default dxt1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "format": format,

    }))



def exr(

    compression: int | None| Literal["none", "rle", "zip1", "zip16"] = None,

    format: int | None| Literal["half", "float"] = None,

    gamma: float | None = None,

) -> FFMpegEncoderOption:
    """
    OpenEXR image

    Args:
        compression: set compression type (from 0 to 3) (default none)
        format: set pixel type (from 1 to 2) (default float)
        gamma: set gamma (from 0.001 to FLT_MAX) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "compression": compression,

        "format": format,

        "gamma": gamma,

    }))



def ffv1(

    slicecrc: int | None = None,

    coder: int | None| Literal["rice", "range_def", "range_tab", "ac"] = None,

    context: int | None = None,

    qtable: int | None| Literal["default", "8bit", "greater8bit"] = None,

    remap_mode: int | None| Literal["auto", "off", "dualrle", "flipdualrle"] = None,

    remap_optimizer: int | None = None,

) -> FFMpegEncoderOption:
    """
    FFmpeg video codec #1

    Args:
        slicecrc: Protect slices with CRCs (from -1 to 2) (default -1)
        coder: Coder type (from -2 to 2) (default rice)
        context: Context model (from 0 to 1) (default 0)
        qtable: Quantization table (from -1 to 2) (default default)
        remap_mode: Remap Mode (from -1 to 2) (default auto)
        remap_optimizer: Remap Optimizer (from 0 to 5) (default 3)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "slicecrc": slicecrc,

        "coder": coder,

        "context": context,

        "qtable": qtable,

        "remap_mode": remap_mode,

        "remap_optimizer": remap_optimizer,

    }))



def ffvhuff(

    context: int | None = None,

    non_deterministic: bool | None = None,

    pred: int | None| Literal["left", "plane", "median"] = None,

) -> FFMpegEncoderOption:
    """
    Huffyuv FFmpeg variant

    Args:
        context: Set per-frame huffman tables (from 0 to 1) (default 0)
        non_deterministic: Allow multithreading for e.g. context=1 at the expense of determinism (default false)
        pred: Prediction method (from 0 to 2) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "context": context,

        "non_deterministic": non_deterministic,

        "pred": pred,

    }))



def fits(

) -> FFMpegEncoderOption:
    """
    Flexible Image Transport System


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def flashsv(

) -> FFMpegEncoderOption:
    """
    Flash Screen Video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def flashsv2(

) -> FFMpegEncoderOption:
    """
    Flash Screen Video Version 2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def flv(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    FLV / Sorenson Spark / Sorenson H.263 (Flash Video) (codec flv1)

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def gif(

    gifflags: str | None = None,

    gifimage: bool | None = None,

    global_palette: bool | None = None,

) -> FFMpegEncoderOption:
    """
    GIF (Graphics Interchange Format)

    Args:
        gifflags: set GIF flags (default offsetting+transdiff)
        gifimage: enable encoding only images per frame (default false)
        global_palette: write a palette to the global gif header where feasible (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "gifflags": gifflags,

        "gifimage": gifimage,

        "global_palette": global_palette,

    }))



def h261(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    H.261

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def h263(

    obmc: bool | None = None,

    mb_info: int | None = None,

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    H.263 / H.263-1996

    Args:
        obmc: use overlapped block motion compensation. (default false)
        mb_info: emit macroblock info for RFC 2190 packetization, the parameter value is the maximum payload size (from 0 to INT_MAX) (default 0)
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "obmc": obmc,

        "mb_info": mb_info,

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def h263p(

    umv: bool | None = None,

    aiv: bool | None = None,

    obmc: bool | None = None,

    structured_slices: bool | None = None,

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    H.263+ / H.263-1998 / H.263 version 2

    Args:
        umv: Use unlimited motion vectors. (default false)
        aiv: Use alternative inter VLC. (default false)
        obmc: use overlapped block motion compensation. (default false)
        structured_slices: Write slice start position at every GOB header instead of just GOB number. (default false)
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "umv": umv,

        "aiv": aiv,

        "obmc": obmc,

        "structured_slices": structured_slices,

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def libx264(

    preset: str | None = None,

    tune: str | None = None,

    profile: str | None = None,

    fastfirstpass: bool | None = None,

    level: str | None = None,

    passlogfile: str | None = None,

    wpredp: str | None = None,

    a53cc: bool | None = None,

    x264opts: str | None = None,

    crf: float | None = None,

    crf_max: float | None = None,

    qp: int | None = None,

    aq_mode: int | None| Literal["none", "variance", "autovariance", "autovariance-biased"] = None,

    aq_strength: float | None = None,

    psy: bool | None = None,

    psy_rd: str | None = None,

    rc_lookahead: int | None = None,

    weightb: bool | None = None,

    weightp: int | None| Literal["none", "simple", "smart"] = None,

    ssim: bool | None = None,

    intra_refresh: bool | None = None,

    bluray_compat: bool | None = None,

    b_bias: int | None = None,

    b_pyramid: int | None| Literal["none", "strict", "normal"] = None,

    mixed_refs: bool | None = None,

    _8x8dct: bool | None = None,

    fast_pskip: bool | None = None,

    aud: bool | None = None,

    mbtree: bool | None = None,

    deblock: str | None = None,

    cplxblur: float | None = None,

    partitions: str | None = None,

    direct_pred: int | None| Literal["none", "spatial", "temporal", "auto"] = None,

    slice_max_size: int | None = None,

    stats: str | None = None,

    nal_hrd: int | None| Literal["none", "vbr", "cbr"] = None,

    avcintra_class: int | None = None,

    me_method: int | None| Literal["dia", "hex", "umh", "esa", "tesa"] = None,

    forced_idr: bool | None = None,

    coder: int | None| Literal["default", "cavlc", "cabac", "vlc", "ac"] = None,

    b_strategy: int | None = None,

    chromaoffset: int | None = None,

    sc_threshold: int | None = None,

    noise_reduction: int | None = None,

    udu_sei: bool | None = None,

    x264_params: str | None = None,

    mb_info: bool | None = None,

) -> FFMpegEncoderOption:
    """
    libx264 H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 (codec h264)

    Args:
        preset: Set the encoding preset (cf. x264 --fullhelp) (default "medium")
        tune: Tune the encoding params (cf. x264 --fullhelp)
        profile: Set profile restrictions (cf. x264 --fullhelp)
        fastfirstpass: Use fast settings when encoding first pass (default true)
        level: Specify level (as defined by Annex A)
        passlogfile: Filename for 2 pass stats
        wpredp: Weighted prediction for P-frames
        a53cc: Use A53 Closed Captions (if available) (default true)
        x264opts: x264 options
        crf: Select the quality for constant quality mode (from -1 to FLT_MAX) (default -1)
        crf_max: In CRF mode, prevents VBV from lowering quality beyond this point. (from -1 to FLT_MAX) (default -1)
        qp: Constant quantization parameter rate control method (from -1 to INT_MAX) (default -1)
        aq_mode: AQ method (from -1 to INT_MAX) (default -1)
        aq_strength: AQ strength. Reduces blocking and blurring in flat and textured areas. (from -1 to FLT_MAX) (default -1)
        psy: Use psychovisual optimizations. (default auto)
        psy_rd: Strength of psychovisual optimization, in <psy-rd>:<psy-trellis> format.
        rc_lookahead: Number of frames to look ahead for frametype and ratecontrol (from -1 to INT_MAX) (default -1)
        weightb: Weighted prediction for B-frames. (default auto)
        weightp: Weighted prediction analysis method. (from -1 to INT_MAX) (default -1)
        ssim: Calculate and print SSIM stats. (default auto)
        intra_refresh: Use Periodic Intra Refresh instead of IDR frames. (default auto)
        bluray_compat: Bluray compatibility workarounds. (default auto)
        b_bias: Influences how often B-frames are used (from INT_MIN to INT_MAX) (default INT_MIN)
        b_pyramid: Keep some B-frames as references. (from -1 to INT_MAX) (default -1)
        mixed_refs: One reference per partition, as opposed to one reference per macroblock (default auto)
        _8x8dct: High profile 8x8 transform. (default auto)
        fast_pskip: (default auto)
        aud: Use access unit delimiters. (default auto)
        mbtree: Use macroblock tree ratecontrol. (default auto)
        deblock: Loop filter parameters, in <alpha:beta> form.
        cplxblur: Reduce fluctuations in QP (before curve compression) (from -1 to FLT_MAX) (default -1)
        partitions: A comma-separated list of partitions to consider. Possible values: p8x8, p4x4, b8x8, i8x8, i4x4, none, all
        direct_pred: Direct MV prediction mode (from -1 to INT_MAX) (default -1)
        slice_max_size: Limit the size of each slice in bytes (from -1 to INT_MAX) (default -1)
        stats: Filename for 2 pass stats
        nal_hrd: Signal HRD information (requires vbv-bufsize; cbr not allowed in .mp4) (from -1 to INT_MAX) (default -1)
        avcintra_class: AVC-Intra class 50/100/200/300/480 (from -1 to 480) (default -1)
        me_method: Set motion estimation method (from -1 to 4) (default -1)
        forced_idr: If forcing keyframes, force them as IDR frames. (default false)
        coder: Coder type (from -1 to 1) (default default)
        b_strategy: Strategy to choose between I/P/B-frames (from -1 to 2) (default -1)
        chromaoffset: QP difference between chroma and luma (from INT_MIN to INT_MAX) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default -1)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default -1)
        udu_sei: Use user data unregistered SEI if available (default false)
        x264_params: Override the x264 configuration using a :-separated list of key=value parameters
        mb_info: Set mb_info data through AVSideData, only useful when used from the API (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "preset": preset,

        "tune": tune,

        "profile": profile,

        "fastfirstpass": fastfirstpass,

        "level": level,

        "passlogfile": passlogfile,

        "wpredp": wpredp,

        "a53cc": a53cc,

        "x264opts": x264opts,

        "crf": crf,

        "crf_max": crf_max,

        "qp": qp,

        "aq-mode": aq_mode,

        "aq-strength": aq_strength,

        "psy": psy,

        "psy-rd": psy_rd,

        "rc-lookahead": rc_lookahead,

        "weightb": weightb,

        "weightp": weightp,

        "ssim": ssim,

        "intra-refresh": intra_refresh,

        "bluray-compat": bluray_compat,

        "b-bias": b_bias,

        "b-pyramid": b_pyramid,

        "mixed-refs": mixed_refs,

        "8x8dct": _8x8dct,

        "fast-pskip": fast_pskip,

        "aud": aud,

        "mbtree": mbtree,

        "deblock": deblock,

        "cplxblur": cplxblur,

        "partitions": partitions,

        "direct-pred": direct_pred,

        "slice-max-size": slice_max_size,

        "stats": stats,

        "nal-hrd": nal_hrd,

        "avcintra-class": avcintra_class,

        "me_method": me_method,

        "forced-idr": forced_idr,

        "coder": coder,

        "b_strategy": b_strategy,

        "chromaoffset": chromaoffset,

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "udu_sei": udu_sei,

        "x264-params": x264_params,

        "mb_info": mb_info,

    }))



def libx264rgb(

    preset: str | None = None,

    tune: str | None = None,

    profile: str | None = None,

    fastfirstpass: bool | None = None,

    level: str | None = None,

    passlogfile: str | None = None,

    wpredp: str | None = None,

    a53cc: bool | None = None,

    x264opts: str | None = None,

    crf: float | None = None,

    crf_max: float | None = None,

    qp: int | None = None,

    aq_mode: int | None| Literal["none", "variance", "autovariance", "autovariance-biased"] = None,

    aq_strength: float | None = None,

    psy: bool | None = None,

    psy_rd: str | None = None,

    rc_lookahead: int | None = None,

    weightb: bool | None = None,

    weightp: int | None| Literal["none", "simple", "smart"] = None,

    ssim: bool | None = None,

    intra_refresh: bool | None = None,

    bluray_compat: bool | None = None,

    b_bias: int | None = None,

    b_pyramid: int | None| Literal["none", "strict", "normal"] = None,

    mixed_refs: bool | None = None,

    _8x8dct: bool | None = None,

    fast_pskip: bool | None = None,

    aud: bool | None = None,

    mbtree: bool | None = None,

    deblock: str | None = None,

    cplxblur: float | None = None,

    partitions: str | None = None,

    direct_pred: int | None| Literal["none", "spatial", "temporal", "auto"] = None,

    slice_max_size: int | None = None,

    stats: str | None = None,

    nal_hrd: int | None| Literal["none", "vbr", "cbr"] = None,

    avcintra_class: int | None = None,

    me_method: int | None| Literal["dia", "hex", "umh", "esa", "tesa"] = None,

    forced_idr: bool | None = None,

    coder: int | None| Literal["default", "cavlc", "cabac", "vlc", "ac"] = None,

    b_strategy: int | None = None,

    chromaoffset: int | None = None,

    sc_threshold: int | None = None,

    noise_reduction: int | None = None,

    udu_sei: bool | None = None,

    x264_params: str | None = None,

    mb_info: bool | None = None,

) -> FFMpegEncoderOption:
    """
    libx264 H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 RGB (codec h264)

    Args:
        preset: Set the encoding preset (cf. x264 --fullhelp) (default "medium")
        tune: Tune the encoding params (cf. x264 --fullhelp)
        profile: Set profile restrictions (cf. x264 --fullhelp)
        fastfirstpass: Use fast settings when encoding first pass (default true)
        level: Specify level (as defined by Annex A)
        passlogfile: Filename for 2 pass stats
        wpredp: Weighted prediction for P-frames
        a53cc: Use A53 Closed Captions (if available) (default true)
        x264opts: x264 options
        crf: Select the quality for constant quality mode (from -1 to FLT_MAX) (default -1)
        crf_max: In CRF mode, prevents VBV from lowering quality beyond this point. (from -1 to FLT_MAX) (default -1)
        qp: Constant quantization parameter rate control method (from -1 to INT_MAX) (default -1)
        aq_mode: AQ method (from -1 to INT_MAX) (default -1)
        aq_strength: AQ strength. Reduces blocking and blurring in flat and textured areas. (from -1 to FLT_MAX) (default -1)
        psy: Use psychovisual optimizations. (default auto)
        psy_rd: Strength of psychovisual optimization, in <psy-rd>:<psy-trellis> format.
        rc_lookahead: Number of frames to look ahead for frametype and ratecontrol (from -1 to INT_MAX) (default -1)
        weightb: Weighted prediction for B-frames. (default auto)
        weightp: Weighted prediction analysis method. (from -1 to INT_MAX) (default -1)
        ssim: Calculate and print SSIM stats. (default auto)
        intra_refresh: Use Periodic Intra Refresh instead of IDR frames. (default auto)
        bluray_compat: Bluray compatibility workarounds. (default auto)
        b_bias: Influences how often B-frames are used (from INT_MIN to INT_MAX) (default INT_MIN)
        b_pyramid: Keep some B-frames as references. (from -1 to INT_MAX) (default -1)
        mixed_refs: One reference per partition, as opposed to one reference per macroblock (default auto)
        _8x8dct: High profile 8x8 transform. (default auto)
        fast_pskip: (default auto)
        aud: Use access unit delimiters. (default auto)
        mbtree: Use macroblock tree ratecontrol. (default auto)
        deblock: Loop filter parameters, in <alpha:beta> form.
        cplxblur: Reduce fluctuations in QP (before curve compression) (from -1 to FLT_MAX) (default -1)
        partitions: A comma-separated list of partitions to consider. Possible values: p8x8, p4x4, b8x8, i8x8, i4x4, none, all
        direct_pred: Direct MV prediction mode (from -1 to INT_MAX) (default -1)
        slice_max_size: Limit the size of each slice in bytes (from -1 to INT_MAX) (default -1)
        stats: Filename for 2 pass stats
        nal_hrd: Signal HRD information (requires vbv-bufsize; cbr not allowed in .mp4) (from -1 to INT_MAX) (default -1)
        avcintra_class: AVC-Intra class 50/100/200/300/480 (from -1 to 480) (default -1)
        me_method: Set motion estimation method (from -1 to 4) (default -1)
        forced_idr: If forcing keyframes, force them as IDR frames. (default false)
        coder: Coder type (from -1 to 1) (default default)
        b_strategy: Strategy to choose between I/P/B-frames (from -1 to 2) (default -1)
        chromaoffset: QP difference between chroma and luma (from INT_MIN to INT_MAX) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default -1)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default -1)
        udu_sei: Use user data unregistered SEI if available (default false)
        x264_params: Override the x264 configuration using a :-separated list of key=value parameters
        mb_info: Set mb_info data through AVSideData, only useful when used from the API (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "preset": preset,

        "tune": tune,

        "profile": profile,

        "fastfirstpass": fastfirstpass,

        "level": level,

        "passlogfile": passlogfile,

        "wpredp": wpredp,

        "a53cc": a53cc,

        "x264opts": x264opts,

        "crf": crf,

        "crf_max": crf_max,

        "qp": qp,

        "aq-mode": aq_mode,

        "aq-strength": aq_strength,

        "psy": psy,

        "psy-rd": psy_rd,

        "rc-lookahead": rc_lookahead,

        "weightb": weightb,

        "weightp": weightp,

        "ssim": ssim,

        "intra-refresh": intra_refresh,

        "bluray-compat": bluray_compat,

        "b-bias": b_bias,

        "b-pyramid": b_pyramid,

        "mixed-refs": mixed_refs,

        "8x8dct": _8x8dct,

        "fast-pskip": fast_pskip,

        "aud": aud,

        "mbtree": mbtree,

        "deblock": deblock,

        "cplxblur": cplxblur,

        "partitions": partitions,

        "direct-pred": direct_pred,

        "slice-max-size": slice_max_size,

        "stats": stats,

        "nal-hrd": nal_hrd,

        "avcintra-class": avcintra_class,

        "me_method": me_method,

        "forced-idr": forced_idr,

        "coder": coder,

        "b_strategy": b_strategy,

        "chromaoffset": chromaoffset,

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "udu_sei": udu_sei,

        "x264-params": x264_params,

        "mb_info": mb_info,

    }))



def h264_videotoolbox(

    profile: int | None| Literal["baseline", "constrained_baseline", "main", "high", "constrained_high", "extended"] = None,

    level: int | None| Literal["1.3", "3.0", "3.1", "3.2", "4.0", "4.1", "4.2", "5.0", "5.1", "5.2"] = None,

    coder: int | None| Literal["cavlc", "vlc", "cabac", "ac"] = None,

    a53cc: bool | None = None,

    constant_bit_rate: bool | None = None,

    max_slice_bytes: int | None = None,

    allow_sw: bool | None = None,

    require_sw: bool | None = None,

    realtime: bool | None = None,

    frames_before: bool | None = None,

    frames_after: bool | None = None,

    prio_speed: bool | None = None,

    power_efficient: int | None = None,

    spatial_aq: int | None = None,

    max_ref_frames: int | None = None,

) -> FFMpegEncoderOption:
    """
    VideoToolbox H.264 Encoder (codec h264)

    Args:
        profile: Profile (from -99 to INT_MAX) (default -99)
        level: Level (from 0 to 52) (default 0)
        coder: Entropy coding (from 0 to 2) (default 0)
        a53cc: Use A53 Closed Captions (if available) (default true)
        constant_bit_rate: Require constant bit rate (macOS 13 or newer) (default false)
        max_slice_bytes: Set the maximum number of bytes in an H.264 slice. (from -1 to INT_MAX) (default -1)
        allow_sw: Allow software encoding (default false)
        require_sw: Require software encoding (default false)
        realtime: Hint that encoding should happen in real-time if not faster (e.g. capturing from camera). (default false)
        frames_before: Other frames will come before the frames in this session. This helps smooth concatenation issues. (default false)
        frames_after: Other frames will come after the frames in this session. This helps smooth concatenation issues. (default false)
        prio_speed: prioritize encoding speed (default auto)
        power_efficient: Set to 1 to enable more power-efficient encoding if supported. (from -1 to 1) (default -1)
        spatial_aq: Set to 1 to enable spatial AQ if supported. (from -1 to 1) (default -1)
        max_ref_frames: Sets the maximum number of reference frames. This only has an effect when the value is less than the maximum allowed by the profile/level. (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "profile": profile,

        "level": level,

        "coder": coder,

        "a53cc": a53cc,

        "constant_bit_rate": constant_bit_rate,

        "max_slice_bytes": max_slice_bytes,

        "allow_sw": allow_sw,

        "require_sw": require_sw,

        "realtime": realtime,

        "frames_before": frames_before,

        "frames_after": frames_after,

        "prio_speed": prio_speed,

        "power_efficient": power_efficient,

        "spatial_aq": spatial_aq,

        "max_ref_frames": max_ref_frames,

    }))



def hdr(

) -> FFMpegEncoderOption:
    """
    HDR (Radiance RGBE format) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def libx265(

    crf: float | None = None,

    qp: int | None = None,

    forced_idr: bool | None = None,

    preset: str | None = None,

    tune: str | None = None,

    profile: str | None = None,

    x265_stats: str | None = None,

    udu_sei: bool | None = None,

    a53cc: bool | None = None,

    x265_params: str | None = None,

    dolbyvision: bool | None| Literal["auto"] = None,

) -> FFMpegEncoderOption:
    """
    libx265 H.265 / HEVC (codec hevc)

    Args:
        crf: set the x265 crf (from -1 to FLT_MAX) (default -1)
        qp: set the x265 qp (from -1 to INT_MAX) (default -1)
        forced_idr: if forcing keyframes, force them as IDR frames (default false)
        preset: set the x265 preset
        tune: set the x265 tune parameter
        profile: set the x265 profile
        x265_stats: Filename for 2 pass stats
        udu_sei: Use user data unregistered SEI if available (default false)
        a53cc: Use A53 Closed Captions (if available) (default false)
        x265_params: set the x265 configuration using a :-separated list of key=value parameters
        dolbyvision: Enable Dolby Vision RPU coding (default auto)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "crf": crf,

        "qp": qp,

        "forced-idr": forced_idr,

        "preset": preset,

        "tune": tune,

        "profile": profile,

        "x265-stats": x265_stats,

        "udu_sei": udu_sei,

        "a53cc": a53cc,

        "x265-params": x265_params,

        "dolbyvision": dolbyvision,

    }))



def hevc_videotoolbox(

    profile: int | None| Literal["main", "main10", "main42210", "rext"] = None,

    alpha_quality: float | None = None,

    constant_bit_rate: bool | None = None,

    allow_sw: bool | None = None,

    require_sw: bool | None = None,

    realtime: bool | None = None,

    frames_before: bool | None = None,

    frames_after: bool | None = None,

    prio_speed: bool | None = None,

    power_efficient: int | None = None,

    spatial_aq: int | None = None,

    max_ref_frames: int | None = None,

) -> FFMpegEncoderOption:
    """
    VideoToolbox H.265 Encoder (codec hevc)

    Args:
        profile: Profile (from -99 to INT_MAX) (default -99)
        alpha_quality: Compression quality for the alpha channel (from 0 to 1) (default 0)
        constant_bit_rate: Require constant bit rate (macOS 13 or newer) (default false)
        allow_sw: Allow software encoding (default false)
        require_sw: Require software encoding (default false)
        realtime: Hint that encoding should happen in real-time if not faster (e.g. capturing from camera). (default false)
        frames_before: Other frames will come before the frames in this session. This helps smooth concatenation issues. (default false)
        frames_after: Other frames will come after the frames in this session. This helps smooth concatenation issues. (default false)
        prio_speed: prioritize encoding speed (default auto)
        power_efficient: Set to 1 to enable more power-efficient encoding if supported. (from -1 to 1) (default -1)
        spatial_aq: Set to 1 to enable spatial AQ if supported. (from -1 to 1) (default -1)
        max_ref_frames: Sets the maximum number of reference frames. This only has an effect when the value is less than the maximum allowed by the profile/level. (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "profile": profile,

        "alpha_quality": alpha_quality,

        "constant_bit_rate": constant_bit_rate,

        "allow_sw": allow_sw,

        "require_sw": require_sw,

        "realtime": realtime,

        "frames_before": frames_before,

        "frames_after": frames_after,

        "prio_speed": prio_speed,

        "power_efficient": power_efficient,

        "spatial_aq": spatial_aq,

        "max_ref_frames": max_ref_frames,

    }))



def huffyuv(

    non_deterministic: bool | None = None,

    pred: int | None| Literal["left", "plane", "median"] = None,

) -> FFMpegEncoderOption:
    """
    Huffyuv / HuffYUV

    Args:
        non_deterministic: Allow multithreading for e.g. context=1 at the expense of determinism (default false)
        pred: Prediction method (from 0 to 2) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "non_deterministic": non_deterministic,

        "pred": pred,

    }))



def jpeg2000(

    format: int | None| Literal["j2k", "jp2"] = None,

    tile_width: int | None = None,

    tile_height: int | None = None,

    pred: int | None| Literal["dwt97int", "dwt53"] = None,

    sop: int | None = None,

    eph: int | None = None,

    prog: int | None| Literal["lrcp", "rlcp", "rpcl", "pcrl", "cprl"] = None,

    layer_rates: str | None = None,

) -> FFMpegEncoderOption:
    """
    JPEG 2000

    Args:
        format: Codec Format (from 0 to 1) (default jp2)
        tile_width: Tile Width (from 1 to 1.07374e+09) (default 256)
        tile_height: Tile Height (from 1 to 1.07374e+09) (default 256)
        pred: DWT Type (from 0 to 1) (default dwt97int)
        sop: SOP marker (from 0 to 1) (default 0)
        eph: EPH marker (from 0 to 1) (default 0)
        prog: Progression Order (from 0 to 4) (default lrcp)
        layer_rates: Layer Rates

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "format": format,

        "tile_width": tile_width,

        "tile_height": tile_height,

        "pred": pred,

        "sop": sop,

        "eph": eph,

        "prog": prog,

        "layer_rates": layer_rates,

    }))



def jpegls(

    pred: int | None| Literal["left", "plane", "median"] = None,

) -> FFMpegEncoderOption:
    """
    JPEG-LS

    Args:
        pred: Prediction method (from 0 to 2) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "pred": pred,

    }))



def ljpeg(

    pred: int | None| Literal["left", "plane", "median"] = None,

) -> FFMpegEncoderOption:
    """
    Lossless JPEG

    Args:
        pred: Prediction method (from 1 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "pred": pred,

    }))



def magicyuv(

    pred: int | None| Literal["left", "gradient", "median"] = None,

) -> FFMpegEncoderOption:
    """
    MagicYUV video

    Args:
        pred: Prediction method (from 1 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "pred": pred,

    }))



def mjpeg(

    huffman: int | None| Literal["default", "optimal"] = None,

    force_duplicated_matrix: bool | None = None,

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

) -> FFMpegEncoderOption:
    """
    MJPEG (Motion JPEG)

    Args:
        huffman: Huffman table strategy (from 0 to 1) (default optimal)
        force_duplicated_matrix: Always write luma and chroma matrix for mjpeg, useful for rtp streaming. (default false)
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "huffman": huffman,

        "force_duplicated_matrix": force_duplicated_matrix,

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

    }))



def mpeg1video(

    gop_timecode: str | None = None,

    drop_frame_timecode: bool | None = None,

    scan_offset: bool | None = None,

    timecode_frame_start: int | None = None,

    b_strategy: int | None = None,

    b_sensitivity: int | None = None,

    brd_scale: int | None = None,

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    MPEG-1 video

    Args:
        gop_timecode: MPEG GOP Timecode in hh:mm:ss[:;.]ff format. Overrides timecode_frame_start.
        drop_frame_timecode: Timecode is in drop frame format. (default false)
        scan_offset: Reserve space for SVCD scan offset user data. (default false)
        timecode_frame_start: GOP timecode frame start number, in non-drop-frame format (from -1 to I64_MAX) (default -1)
        b_strategy: Strategy to choose between I/P/B-frames (from 0 to 2) (default 0)
        b_sensitivity: Adjust sensitivity of b_frame_strategy 1 (from 1 to INT_MAX) (default 40)
        brd_scale: Downscale frames for dynamic B-frame decision (from 0 to 3) (default 0)
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "gop_timecode": gop_timecode,

        "drop_frame_timecode": drop_frame_timecode,

        "scan_offset": scan_offset,

        "timecode_frame_start": timecode_frame_start,

        "b_strategy": b_strategy,

        "b_sensitivity": b_sensitivity,

        "brd_scale": brd_scale,

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def mpeg2video(

    gop_timecode: str | None = None,

    drop_frame_timecode: bool | None = None,

    scan_offset: bool | None = None,

    timecode_frame_start: int | None = None,

    b_strategy: int | None = None,

    b_sensitivity: int | None = None,

    brd_scale: int | None = None,

    intra_dc_precision: int | None = None,

    intra_vlc: bool | None = None,

    non_linear_quant: bool | None = None,

    alternate_scan: bool | None = None,

    a53cc: bool | None = None,

    seq_disp_ext: int | None| Literal["auto", "never", "always"] = None,

    video_format: int | None| Literal["component", "pal", "ntsc", "secam", "mac", "unspecified"] = None,

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    MPEG-2 video

    Args:
        gop_timecode: MPEG GOP Timecode in hh:mm:ss[:;.]ff format. Overrides timecode_frame_start.
        drop_frame_timecode: Timecode is in drop frame format. (default false)
        scan_offset: Reserve space for SVCD scan offset user data. (default false)
        timecode_frame_start: GOP timecode frame start number, in non-drop-frame format (from -1 to I64_MAX) (default -1)
        b_strategy: Strategy to choose between I/P/B-frames (from 0 to 2) (default 0)
        b_sensitivity: Adjust sensitivity of b_frame_strategy 1 (from 1 to INT_MAX) (default 40)
        brd_scale: Downscale frames for dynamic B-frame decision (from 0 to 3) (default 0)
        intra_dc_precision: Precision of the DC coefficient - 8 (from -1 to 3) (default -1)
        intra_vlc: Use MPEG-2 intra VLC table. (default false)
        non_linear_quant: Use nonlinear quantizer. (default false)
        alternate_scan: Enable alternate scantable. (default false)
        a53cc: Use A53 Closed Captions (if available) (default true)
        seq_disp_ext: Write sequence_display_extension blocks. (from -1 to 1) (default auto)
        video_format: Video_format in the sequence_display_extension indicating the source of the video. (from 0 to 7) (default unspecified)
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "gop_timecode": gop_timecode,

        "drop_frame_timecode": drop_frame_timecode,

        "scan_offset": scan_offset,

        "timecode_frame_start": timecode_frame_start,

        "b_strategy": b_strategy,

        "b_sensitivity": b_sensitivity,

        "brd_scale": brd_scale,

        "intra_dc_precision": intra_dc_precision,

        "intra_vlc": intra_vlc,

        "non_linear_quant": non_linear_quant,

        "alternate_scan": alternate_scan,

        "a53cc": a53cc,

        "seq_disp_ext": seq_disp_ext,

        "video_format": video_format,

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def mpeg4(

    data_partitioning: bool | None = None,

    alternate_scan: bool | None = None,

    mpeg_quant: int | None = None,

    b_strategy: int | None = None,

    b_sensitivity: int | None = None,

    brd_scale: int | None = None,

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    MPEG-4 part 2

    Args:
        data_partitioning: Use data partitioning. (default false)
        alternate_scan: Enable alternate scantable. (default false)
        mpeg_quant: Use MPEG quantizers instead of H.263 (from 0 to 1) (default 0)
        b_strategy: Strategy to choose between I/P/B-frames (from 0 to 2) (default 0)
        b_sensitivity: Adjust sensitivity of b_frame_strategy 1 (from 1 to INT_MAX) (default 40)
        brd_scale: Downscale frames for dynamic B-frame decision (from 0 to 3) (default 0)
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "data_partitioning": data_partitioning,

        "alternate_scan": alternate_scan,

        "mpeg_quant": mpeg_quant,

        "b_strategy": b_strategy,

        "b_sensitivity": b_sensitivity,

        "brd_scale": brd_scale,

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def msmpeg4v2(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    MPEG-4 part 2 Microsoft variant version 2

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def msmpeg4(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    MPEG-4 part 2 Microsoft variant version 3 (codec msmpeg4v3)

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def msrle(

) -> FFMpegEncoderOption:
    """
    Microsoft RLE


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def msvideo1(

) -> FFMpegEncoderOption:
    """
    Microsoft Video-1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pam(

) -> FFMpegEncoderOption:
    """
    PAM (Portable AnyMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pbm(

) -> FFMpegEncoderOption:
    """
    PBM (Portable BitMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcx(

) -> FFMpegEncoderOption:
    """
    PC Paintbrush PCX image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pfm(

) -> FFMpegEncoderOption:
    """
    PFM (Portable FloatMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pgm(

) -> FFMpegEncoderOption:
    """
    PGM (Portable GrayMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pgmyuv(

) -> FFMpegEncoderOption:
    """
    PGMYUV (Portable GrayMap YUV) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def phm(

) -> FFMpegEncoderOption:
    """
    PHM (Portable HalfFloatMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def png(

    dpi: int | None = None,

    dpm: int | None = None,

    pred: int | None| Literal["none", "sub", "up", "avg", "paeth", "mixed"] = None,

) -> FFMpegEncoderOption:
    """
    PNG (Portable Network Graphics) image

    Args:
        dpi: Set image resolution (in dots per inch) (from 0 to 65536) (default 0)
        dpm: Set image resolution (in dots per meter) (from 0 to 65536) (default 0)
        pred: Prediction method (from 0 to 5) (default paeth)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "dpi": dpi,

        "dpm": dpm,

        "pred": pred,

    }))



def ppm(

) -> FFMpegEncoderOption:
    """
    PPM (Portable PixelMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def prores(

    vendor: str | None = None,

) -> FFMpegEncoderOption:
    """
    Apple ProRes

    Args:
        vendor: vendor ID (default "fmpg")

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "vendor": vendor,

    }))



def prores_aw(

    vendor: str | None = None,

) -> FFMpegEncoderOption:
    """
    Apple ProRes (codec prores)

    Args:
        vendor: vendor ID (default "fmpg")

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "vendor": vendor,

    }))



def prores_ks(

    mbs_per_slice: int | None = None,

    profile: int | None| Literal["auto", "proxy", "lt", "standard", "hq", "4444", "4444xq"] = None,

    vendor: str | None = None,

    bits_per_mb: int | None = None,

    quant_mat: int | None| Literal["auto", "proxy", "lt", "standard", "hq", "default"] = None,

    alpha_bits: int | None = None,

) -> FFMpegEncoderOption:
    """
    Apple ProRes (iCodec Pro) (codec prores)

    Args:
        mbs_per_slice: macroblocks per slice (from 1 to 8) (default 8)
        profile: (from -1 to 5) (default auto)
        vendor: vendor ID (default "Lavc")
        bits_per_mb: desired bits per macroblock (from 0 to 8192) (default 0)
        quant_mat: quantiser matrix (from -1 to 6) (default auto)
        alpha_bits: bits for alpha plane (from 0 to 16) (default 16)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mbs_per_slice": mbs_per_slice,

        "profile": profile,

        "vendor": vendor,

        "bits_per_mb": bits_per_mb,

        "quant_mat": quant_mat,

        "alpha_bits": alpha_bits,

    }))



def prores_videotoolbox(

    profile: int | None| Literal["auto", "proxy", "lt", "standard", "hq", "4444", "xq"] = None,

    allow_sw: bool | None = None,

    require_sw: bool | None = None,

    realtime: bool | None = None,

    frames_before: bool | None = None,

    frames_after: bool | None = None,

    prio_speed: bool | None = None,

    power_efficient: int | None = None,

    spatial_aq: int | None = None,

    max_ref_frames: int | None = None,

) -> FFMpegEncoderOption:
    """
    VideoToolbox ProRes Encoder (codec prores)

    Args:
        profile: Profile (from -99 to 5) (default auto)
        allow_sw: Allow software encoding (default false)
        require_sw: Require software encoding (default false)
        realtime: Hint that encoding should happen in real-time if not faster (e.g. capturing from camera). (default false)
        frames_before: Other frames will come before the frames in this session. This helps smooth concatenation issues. (default false)
        frames_after: Other frames will come after the frames in this session. This helps smooth concatenation issues. (default false)
        prio_speed: prioritize encoding speed (default auto)
        power_efficient: Set to 1 to enable more power-efficient encoding if supported. (from -1 to 1) (default -1)
        spatial_aq: Set to 1 to enable spatial AQ if supported. (from -1 to 1) (default -1)
        max_ref_frames: Sets the maximum number of reference frames. This only has an effect when the value is less than the maximum allowed by the profile/level. (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "profile": profile,

        "allow_sw": allow_sw,

        "require_sw": require_sw,

        "realtime": realtime,

        "frames_before": frames_before,

        "frames_after": frames_after,

        "prio_speed": prio_speed,

        "power_efficient": power_efficient,

        "spatial_aq": spatial_aq,

        "max_ref_frames": max_ref_frames,

    }))



def qoi(

) -> FFMpegEncoderOption:
    """
    QOI (Quite OK Image format) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def qtrle(

) -> FFMpegEncoderOption:
    """
    QuickTime Animation (RLE) video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def r10k(

) -> FFMpegEncoderOption:
    """
    AJA Kona 10-bit RGB Codec


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def r210(

) -> FFMpegEncoderOption:
    """
    Uncompressed RGB 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def rawvideo(

) -> FFMpegEncoderOption:
    """
    raw video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def roqvideo(

    quake3_compat: bool | None = None,

) -> FFMpegEncoderOption:
    """
    id RoQ video (codec roq)

    Args:
        quake3_compat: Whether to respect known limitations in Quake 3 decoder (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "quake3_compat": quake3_compat,

    }))



def rpza(

    skip_frame_thresh: int | None = None,

    continue_one_color_thresh: int | None = None,

    sixteen_color_thresh: int | None = None,

) -> FFMpegEncoderOption:
    """
    QuickTime video (RPZA)

    Args:
        skip_frame_thresh: (from 0 to 24) (default 1)
        continue_one_color_thresh: (from 0 to 24) (default 0)
        sixteen_color_thresh: (from 0 to 24) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "skip_frame_thresh": skip_frame_thresh,

        "continue_one_color_thresh": continue_one_color_thresh,

        "sixteen_color_thresh": sixteen_color_thresh,

    }))



def rv10(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    RealVideo 1.0

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def rv20(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    RealVideo 2.0

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def sgi(

    rle: int | None = None,

) -> FFMpegEncoderOption:
    """
    SGI image

    Args:
        rle: Use run-length compression (from 0 to 1) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "rle": rle,

    }))



def smc(

) -> FFMpegEncoderOption:
    """
    QuickTime Graphics (SMC)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def snow(

    motion_est: int | None| Literal["zero", "epzs", "xone", "iter"] = None,

    memc_only: bool | None = None,

    no_bitstream: bool | None = None,

    intra_penalty: int | None = None,

    iterative_dia_size: int | None = None,

    sc_threshold: int | None = None,

    pred: int | None| Literal["dwt97", "dwt53"] = None,

    rc_eq: str | None = None,

) -> FFMpegEncoderOption:
    """
    Snow

    Args:
        motion_est: motion estimation algorithm (from 0 to 3) (default epzs)
        memc_only: Only do ME/MC (I frames -> ref, P frame -> ME+MC). (default false)
        no_bitstream: Skip final bitstream writeout. (default false)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to INT_MAX) (default 0)
        iterative_dia_size: Dia size for the iterative ME (from 0 to INT_MAX) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        pred: Spatial decomposition type (from 0 to 1) (default dwt97)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "motion_est": motion_est,

        "memc_only": memc_only,

        "no_bitstream": no_bitstream,

        "intra_penalty": intra_penalty,

        "iterative_dia_size": iterative_dia_size,

        "sc_threshold": sc_threshold,

        "pred": pred,

        "rc_eq": rc_eq,

    }))



def speedhq(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    NewTek SpeedHQ

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def sunrast(

    rle: int | None = None,

) -> FFMpegEncoderOption:
    """
    Sun Rasterfile image

    Args:
        rle: Use run-length compression (from 0 to 1) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "rle": rle,

    }))



def svq1(

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

) -> FFMpegEncoderOption:
    """
    Sorenson Vector Quantizer 1 / Sorenson Video 1 / SVQ1

    Args:
        motion_est: Motion estimation algorithm (from 0 to 2) (default epzs)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "motion-est": motion_est,

    }))



def targa(

    rle: int | None = None,

) -> FFMpegEncoderOption:
    """
    Truevision Targa image

    Args:
        rle: Use run-length compression (from 0 to 1) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "rle": rle,

    }))



def tiff(

    dpi: int | None = None,

    compression_algo: int | None| Literal["packbits", "raw", "lzw", "deflate"] = None,

) -> FFMpegEncoderOption:
    """
    TIFF image

    Args:
        dpi: set the image resolution (in dpi) (from 1 to 65536) (default 72)
        compression_algo: (from 1 to 32946) (default packbits)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "dpi": dpi,

        "compression_algo": compression_algo,

    }))



def utvideo(

    pred: int | None| Literal["none", "left", "median"] = None,

) -> FFMpegEncoderOption:
    """
    Ut Video

    Args:
        pred: Prediction method (from 0 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "pred": pred,

    }))



def v210(

) -> FFMpegEncoderOption:
    """
    Uncompressed 4:2:2 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def v308(

) -> FFMpegEncoderOption:
    """
    Uncompressed packed 4:4:4


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def v408(

) -> FFMpegEncoderOption:
    """
    Uncompressed packed QT 4:4:4:4


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def v410(

) -> FFMpegEncoderOption:
    """
    Uncompressed 4:4:4 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def vbn(

    format: int | None| Literal["raw", "dxt1", "dxt5"] = None,

) -> FFMpegEncoderOption:
    """
    Vizrt Binary Image

    Args:
        format: Texture format (from 0 to 3) (default dxt5)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "format": format,

    }))



def vnull(

) -> FFMpegEncoderOption:
    """
    null video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def libvpx(

    lag_in_frames: int | None = None,

    arnr_maxframes: int | None = None,

    arnr_strength: int | None = None,

    arnr_type: int | None| Literal["backward", "forward", "centered"] = None,

    tune: int | None| Literal["psnr", "ssim"] = None,

    deadline: int | None| Literal["best", "good", "realtime"] = None,

    error_resilient: str | None = None,

    max_intra_rate: int | None = None,

    crf: int | None = None,

    static_thresh: int | None = None,

    drop_threshold: int | None = None,

    noise_sensitivity: int | None = None,

    undershoot_pct: int | None = None,

    overshoot_pct: int | None = None,

    ts_parameters: str | None = None,

    auto_alt_ref: int | None = None,

    cpu_used: int | None = None,

    screen_content_mode: int | None = None,

    speed: int | None = None,

    quality: int | None| Literal["best", "good", "realtime"] = None,

    vp8flags: str | None = None,

    arnr_max_frames: int | None = None,

    rc_lookahead: int | None = None,

    sharpness: int | None = None,

) -> FFMpegEncoderOption:
    """
    libvpx VP8 (codec vp8)

    Args:
        lag_in_frames: Number of frames to look ahead for alternate reference frame selection (from -1 to INT_MAX) (default -1)
        arnr_maxframes: altref noise reduction max frame count (from -1 to INT_MAX) (default -1)
        arnr_strength: altref noise reduction filter strength (from -1 to INT_MAX) (default -1)
        arnr_type: altref noise reduction filter type (from -1 to INT_MAX) (default -1)
        tune: Tune the encoding to a specific scenario (from -1 to INT_MAX) (default -1)
        deadline: Time to spend encoding, in microseconds. (from INT_MIN to INT_MAX) (default good)
        error_resilient: Error resilience configuration (default 0)
        max_intra_rate: Maximum I-frame bitrate (pct) 0=unlimited (from -1 to INT_MAX) (default -1)
        crf: Select the quality for constant quality mode (from -1 to 63) (default -1)
        static_thresh: A change threshold on blocks below which they will be skipped by the encoder (from 0 to INT_MAX) (default 0)
        drop_threshold: Frame drop threshold (from INT_MIN to INT_MAX) (default 0)
        noise_sensitivity: Noise sensitivity (from 0 to 4) (default 0)
        undershoot_pct: Datarate undershoot (min) target (%) (from -1 to 100) (default -1)
        overshoot_pct: Datarate overshoot (max) target (%) (from -1 to 1000) (default -1)
        ts_parameters: Temporal scaling configuration using a :-separated list of key=value parameters
        auto_alt_ref: Enable use of alternate reference frames (2-pass only) (from -1 to 2) (default -1)
        cpu_used: Quality/Speed ratio modifier (from -16 to 16) (default 1)
        screen_content_mode: Encoder screen content mode (from -1 to 2) (default -1)
        speed: (from -16 to 16) (default 1)
        quality: (from INT_MIN to INT_MAX) (default good)
        vp8flags: (default 0)
        arnr_max_frames: altref noise reduction max frame count (from 0 to 15) (default 0)
        rc_lookahead: Number of frames to look ahead for alternate reference frame selection (from 0 to 25) (default 25)
        sharpness: Increase sharpness at the expense of lower PSNR (from -1 to 7) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "lag-in-frames": lag_in_frames,

        "arnr-maxframes": arnr_maxframes,

        "arnr-strength": arnr_strength,

        "arnr-type": arnr_type,

        "tune": tune,

        "deadline": deadline,

        "error-resilient": error_resilient,

        "max-intra-rate": max_intra_rate,

        "crf": crf,

        "static-thresh": static_thresh,

        "drop-threshold": drop_threshold,

        "noise-sensitivity": noise_sensitivity,

        "undershoot-pct": undershoot_pct,

        "overshoot-pct": overshoot_pct,

        "ts-parameters": ts_parameters,

        "auto-alt-ref": auto_alt_ref,

        "cpu-used": cpu_used,

        "screen-content-mode": screen_content_mode,

        "speed": speed,

        "quality": quality,

        "vp8flags": vp8flags,

        "arnr_max_frames": arnr_max_frames,

        "rc_lookahead": rc_lookahead,

        "sharpness": sharpness,

    }))



def wbmp(

) -> FFMpegEncoderOption:
    """
    WBMP (Wireless Application Protocol Bitmap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def wmv1(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    Windows Media Video 7

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def wmv2(

    mpv_flags: str | None = None,

    luma_elim_threshold: int | None = None,

    chroma_elim_threshold: int | None = None,

    quantizer_noise_shaping: int | None = None,

    error_rate: int | None = None,

    qsquish: float | None = None,

    rc_qmod_amp: float | None = None,

    rc_qmod_freq: int | None = None,

    rc_eq: str | None = None,

    rc_init_cplx: float | None = None,

    rc_buf_aggressivity: float | None = None,

    border_mask: float | None = None,

    lmin: int | None = None,

    lmax: int | None = None,

    skip_threshold: int | None = None,

    skip_factor: int | None = None,

    skip_exp: int | None = None,

    skip_cmp: int | None| Literal["sad", "sse", "satd", "dct", "psnr", "bit", "rd", "zero", "vsad", "vsse", "nsse", "dct264", "dctmax", "chroma", "msad"] = None,

    noise_reduction: int | None = None,

    ps: int | None = None,

    motion_est: int | None| Literal["zero", "epzs", "xone"] = None,

    mepc: int | None = None,

    mepre: int | None = None,

    intra_penalty: int | None = None,

    sc_threshold: int | None = None,

) -> FFMpegEncoderOption:
    """
    Windows Media Video 8

    Args:
        mpv_flags: Flags common for all mpegvideo-based encoders. (default 0)
        luma_elim_threshold: single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        chroma_elim_threshold: single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
        quantizer_noise_shaping: (from 0 to INT_MAX) (default 0)
        error_rate: Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)
        qsquish: how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)
        rc_qmod_amp: experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)
        rc_qmod_freq: experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.
        rc_init_cplx: initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)
        rc_buf_aggressivity: currently useless (from -FLT_MAX to FLT_MAX) (default 1)
        border_mask: increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)
        lmin: minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)
        lmax: maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)
        skip_threshold: Frame skip threshold (from INT_MIN to INT_MAX) (default 0)
        skip_factor: Frame skip factor (from INT_MIN to INT_MAX) (default 0)
        skip_exp: Frame skip exponent (from INT_MIN to INT_MAX) (default 0)
        skip_cmp: Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mpv_flags": mpv_flags,

        "luma_elim_threshold": luma_elim_threshold,

        "chroma_elim_threshold": chroma_elim_threshold,

        "quantizer_noise_shaping": quantizer_noise_shaping,

        "error_rate": error_rate,

        "qsquish": qsquish,

        "rc_qmod_amp": rc_qmod_amp,

        "rc_qmod_freq": rc_qmod_freq,

        "rc_eq": rc_eq,

        "rc_init_cplx": rc_init_cplx,

        "rc_buf_aggressivity": rc_buf_aggressivity,

        "border_mask": border_mask,

        "lmin": lmin,

        "lmax": lmax,

        "skip_threshold": skip_threshold,

        "skip_factor": skip_factor,

        "skip_exp": skip_exp,

        "skip_cmp": skip_cmp,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

        "sc_threshold": sc_threshold,

    }))



def wrapped_avframe(

) -> FFMpegEncoderOption:
    """
    AVFrame to AVPacket passthrough


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def xbm(

) -> FFMpegEncoderOption:
    """
    XBM (X BitMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def xface(

) -> FFMpegEncoderOption:
    """
    X-face image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def xwd(

) -> FFMpegEncoderOption:
    """
    XWD (X Window Dump) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def y41p(

) -> FFMpegEncoderOption:
    """
    Uncompressed YUV 4:1:1 12-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def yuv4(

) -> FFMpegEncoderOption:
    """
    Uncompressed packed 4:2:0


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def zlib(

) -> FFMpegEncoderOption:
    """
    LCL (LossLess Codec Library) ZLIB


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def zmbv(

) -> FFMpegEncoderOption:
    """
    Zip Motion Blocks Video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def aac(

    aac_coder: int | None| Literal["twoloop", "fast"] = None,

    aac_ms: bool | None = None,

    aac_is: bool | None = None,

    aac_pns: bool | None = None,

    aac_tns: bool | None = None,

    aac_pce: bool | None = None,

) -> FFMpegEncoderOption:
    """
    AAC (Advanced Audio Coding)

    Args:
        aac_coder: Coding algorithm (from 0 to 1) (default twoloop)
        aac_ms: Force M/S stereo coding (default auto)
        aac_is: Intensity stereo coding (default true)
        aac_pns: Perceptual noise substitution (default true)
        aac_tns: Temporal noise shaping (default true)
        aac_pce: Forces the use of PCEs (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "aac_coder": aac_coder,

        "aac_ms": aac_ms,

        "aac_is": aac_is,

        "aac_pns": aac_pns,

        "aac_tns": aac_tns,

        "aac_pce": aac_pce,

    }))



def aac_at(

    aac_at_mode: int | None| Literal["auto", "cbr", "abr", "cvbr", "vbr"] = None,

    aac_at_quality: int | None = None,

) -> FFMpegEncoderOption:
    """
    aac (AudioToolbox) (codec aac)

    Args:
        aac_at_mode: ratecontrol mode (from -1 to 3) (default auto)
        aac_at_quality: quality vs speed control (from 0 to 2) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "aac_at_mode": aac_at_mode,

        "aac_at_quality": aac_at_quality,

    }))



def ac3(

    center_mixlev: float | None = None,

    surround_mixlev: float | None = None,

    mixing_level: int | None = None,

    room_type: int | None| Literal["notindicated", "large", "small"] = None,

    per_frame_metadata: bool | None = None,

    copyright: int | None = None,

    dialnorm: int | None = None,

    dsur_mode: int | None| Literal["notindicated", "on", "off"] = None,

    original: int | None = None,

    dmix_mode: int | None| Literal["notindicated", "ltrt", "loro", "dplii"] = None,

    ltrt_cmixlev: float | None = None,

    ltrt_surmixlev: float | None = None,

    loro_cmixlev: float | None = None,

    loro_surmixlev: float | None = None,

    dsurex_mode: int | None| Literal["notindicated", "on", "off", "dpliiz"] = None,

    dheadphone_mode: int | None| Literal["notindicated", "on", "off"] = None,

    ad_conv_type: int | None| Literal["standard", "hdcd"] = None,

    stereo_rematrixing: bool | None = None,

    channel_coupling: int | None| Literal["auto"] = None,

    cpl_start_band: int | None| Literal["auto"] = None,

) -> FFMpegEncoderOption:
    """
    ATSC A/52A (AC-3)

    Args:
        center_mixlev: Center Mix Level (from 0 to 1) (default 0.594604)
        surround_mixlev: Surround Mix Level (from 0 to 1) (default 0.5)
        mixing_level: Mixing Level (from -1 to 111) (default -1)
        room_type: Room Type (from -1 to 2) (default -1)
        per_frame_metadata: Allow Changing Metadata Per-Frame (default false)
        copyright: Copyright Bit (from -1 to 1) (default -1)
        dialnorm: Dialogue Level (dB) (from -31 to -1) (default -31)
        dsur_mode: Dolby Surround Mode (from -1 to 2) (default -1)
        original: Original Bit Stream (from -1 to 1) (default -1)
        dmix_mode: Preferred Stereo Downmix Mode (from -1 to 3) (default -1)
        ltrt_cmixlev: Lt/Rt Center Mix Level (from -1 to 2) (default -1)
        ltrt_surmixlev: Lt/Rt Surround Mix Level (from -1 to 2) (default -1)
        loro_cmixlev: Lo/Ro Center Mix Level (from -1 to 2) (default -1)
        loro_surmixlev: Lo/Ro Surround Mix Level (from -1 to 2) (default -1)
        dsurex_mode: Dolby Surround EX Mode (from -1 to 3) (default -1)
        dheadphone_mode: Dolby Headphone Mode (from -1 to 2) (default -1)
        ad_conv_type: A/D Converter Type (from -1 to 1) (default -1)
        stereo_rematrixing: Stereo Rematrixing (default true)
        channel_coupling: Channel Coupling (from -1 to 1) (default auto)
        cpl_start_band: Coupling Start Band (from -1 to 15) (default auto)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "center_mixlev": center_mixlev,

        "surround_mixlev": surround_mixlev,

        "mixing_level": mixing_level,

        "room_type": room_type,

        "per_frame_metadata": per_frame_metadata,

        "copyright": copyright,

        "dialnorm": dialnorm,

        "dsur_mode": dsur_mode,

        "original": original,

        "dmix_mode": dmix_mode,

        "ltrt_cmixlev": ltrt_cmixlev,

        "ltrt_surmixlev": ltrt_surmixlev,

        "loro_cmixlev": loro_cmixlev,

        "loro_surmixlev": loro_surmixlev,

        "dsurex_mode": dsurex_mode,

        "dheadphone_mode": dheadphone_mode,

        "ad_conv_type": ad_conv_type,

        "stereo_rematrixing": stereo_rematrixing,

        "channel_coupling": channel_coupling,

        "cpl_start_band": cpl_start_band,

    }))



def ac3_fixed(

    center_mixlev: float | None = None,

    surround_mixlev: float | None = None,

    mixing_level: int | None = None,

    room_type: int | None| Literal["notindicated", "large", "small"] = None,

    per_frame_metadata: bool | None = None,

    copyright: int | None = None,

    dialnorm: int | None = None,

    dsur_mode: int | None| Literal["notindicated", "on", "off"] = None,

    original: int | None = None,

    dmix_mode: int | None| Literal["notindicated", "ltrt", "loro", "dplii"] = None,

    ltrt_cmixlev: float | None = None,

    ltrt_surmixlev: float | None = None,

    loro_cmixlev: float | None = None,

    loro_surmixlev: float | None = None,

    dsurex_mode: int | None| Literal["notindicated", "on", "off", "dpliiz"] = None,

    dheadphone_mode: int | None| Literal["notindicated", "on", "off"] = None,

    ad_conv_type: int | None| Literal["standard", "hdcd"] = None,

    stereo_rematrixing: bool | None = None,

    channel_coupling: int | None| Literal["auto"] = None,

    cpl_start_band: int | None| Literal["auto"] = None,

) -> FFMpegEncoderOption:
    """
    ATSC A/52A (AC-3) (codec ac3)

    Args:
        center_mixlev: Center Mix Level (from 0 to 1) (default 0.594604)
        surround_mixlev: Surround Mix Level (from 0 to 1) (default 0.5)
        mixing_level: Mixing Level (from -1 to 111) (default -1)
        room_type: Room Type (from -1 to 2) (default -1)
        per_frame_metadata: Allow Changing Metadata Per-Frame (default false)
        copyright: Copyright Bit (from -1 to 1) (default -1)
        dialnorm: Dialogue Level (dB) (from -31 to -1) (default -31)
        dsur_mode: Dolby Surround Mode (from -1 to 2) (default -1)
        original: Original Bit Stream (from -1 to 1) (default -1)
        dmix_mode: Preferred Stereo Downmix Mode (from -1 to 3) (default -1)
        ltrt_cmixlev: Lt/Rt Center Mix Level (from -1 to 2) (default -1)
        ltrt_surmixlev: Lt/Rt Surround Mix Level (from -1 to 2) (default -1)
        loro_cmixlev: Lo/Ro Center Mix Level (from -1 to 2) (default -1)
        loro_surmixlev: Lo/Ro Surround Mix Level (from -1 to 2) (default -1)
        dsurex_mode: Dolby Surround EX Mode (from -1 to 3) (default -1)
        dheadphone_mode: Dolby Headphone Mode (from -1 to 2) (default -1)
        ad_conv_type: A/D Converter Type (from -1 to 1) (default -1)
        stereo_rematrixing: Stereo Rematrixing (default true)
        channel_coupling: Channel Coupling (from -1 to 1) (default auto)
        cpl_start_band: Coupling Start Band (from -1 to 15) (default auto)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "center_mixlev": center_mixlev,

        "surround_mixlev": surround_mixlev,

        "mixing_level": mixing_level,

        "room_type": room_type,

        "per_frame_metadata": per_frame_metadata,

        "copyright": copyright,

        "dialnorm": dialnorm,

        "dsur_mode": dsur_mode,

        "original": original,

        "dmix_mode": dmix_mode,

        "ltrt_cmixlev": ltrt_cmixlev,

        "ltrt_surmixlev": ltrt_surmixlev,

        "loro_cmixlev": loro_cmixlev,

        "loro_surmixlev": loro_surmixlev,

        "dsurex_mode": dsurex_mode,

        "dheadphone_mode": dheadphone_mode,

        "ad_conv_type": ad_conv_type,

        "stereo_rematrixing": stereo_rematrixing,

        "channel_coupling": channel_coupling,

        "cpl_start_band": cpl_start_band,

    }))



def adpcm_adx(

) -> FFMpegEncoderOption:
    """
    SEGA CRI ADX ADPCM


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def adpcm_argo(

) -> FFMpegEncoderOption:
    """
    ADPCM Argonaut Games


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def g722(

) -> FFMpegEncoderOption:
    """
    G.722 ADPCM (codec adpcm_g722)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def g726(

    code_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    G.726 ADPCM (codec adpcm_g726)

    Args:
        code_size: Bits per code (from 2 to 5) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "code_size": code_size,

    }))



def g726le(

    code_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    G.726 little endian ADPCM ("right-justified") (codec adpcm_g726le)

    Args:
        code_size: Bits per code (from 2 to 5) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "code_size": code_size,

    }))



def adpcm_ima_alp(

    block_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA High Voltage Software ALP

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "block_size": block_size,

    }))



def adpcm_ima_amv(

    block_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA AMV

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "block_size": block_size,

    }))



def adpcm_ima_apm(

    block_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA Ubisoft APM

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "block_size": block_size,

    }))



def adpcm_ima_qt(

) -> FFMpegEncoderOption:
    """
    ADPCM IMA QuickTime


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def adpcm_ima_ssi(

    block_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA Simon & Schuster Interactive

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "block_size": block_size,

    }))



def adpcm_ima_wav(

    block_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA WAV

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "block_size": block_size,

    }))



def adpcm_ima_ws(

    block_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA Westwood

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "block_size": block_size,

    }))



def adpcm_ms(

    block_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    ADPCM Microsoft

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "block_size": block_size,

    }))



def adpcm_swf(

) -> FFMpegEncoderOption:
    """
    ADPCM Shockwave Flash


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def adpcm_yamaha(

    block_size: int | None = None,

) -> FFMpegEncoderOption:
    """
    ADPCM Yamaha

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "block_size": block_size,

    }))



def alac(

    min_prediction_order: int | None = None,

    max_prediction_order: int | None = None,

) -> FFMpegEncoderOption:
    """
    ALAC (Apple Lossless Audio Codec)

    Args:
        min_prediction_order: (from 1 to 30) (default 4)
        max_prediction_order: (from 1 to 30) (default 6)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "min_prediction_order": min_prediction_order,

        "max_prediction_order": max_prediction_order,

    }))



def alac_at(

    aac_at_mode: int | None| Literal["auto", "cbr", "abr", "cvbr", "vbr"] = None,

    aac_at_quality: int | None = None,

) -> FFMpegEncoderOption:
    """
    alac (AudioToolbox) (codec alac)

    Args:
        aac_at_mode: ratecontrol mode (from -1 to 3) (default auto)
        aac_at_quality: quality vs speed control (from 0 to 2) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "aac_at_mode": aac_at_mode,

        "aac_at_quality": aac_at_quality,

    }))



def anull(

) -> FFMpegEncoderOption:
    """
    null audio


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def aptx(

) -> FFMpegEncoderOption:
    """
    aptX (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def aptx_hd(

) -> FFMpegEncoderOption:
    """
    aptX HD (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def comfortnoise(

) -> FFMpegEncoderOption:
    """
    RFC 3389 comfort noise generator


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def dfpwm(

) -> FFMpegEncoderOption:
    """
    DFPWM1a audio


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def dca(

    dca_adpcm: bool | None = None,

) -> FFMpegEncoderOption:
    """
    DCA (DTS Coherent Acoustics) (codec dts)

    Args:
        dca_adpcm: Use ADPCM encoding (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "dca_adpcm": dca_adpcm,

    }))



def eac3(

    mixing_level: int | None = None,

    room_type: int | None| Literal["notindicated", "large", "small"] = None,

    per_frame_metadata: bool | None = None,

    copyright: int | None = None,

    dialnorm: int | None = None,

    dsur_mode: int | None| Literal["notindicated", "on", "off"] = None,

    original: int | None = None,

    dmix_mode: int | None| Literal["notindicated", "ltrt", "loro", "dplii"] = None,

    ltrt_cmixlev: float | None = None,

    ltrt_surmixlev: float | None = None,

    loro_cmixlev: float | None = None,

    loro_surmixlev: float | None = None,

    dsurex_mode: int | None| Literal["notindicated", "on", "off", "dpliiz"] = None,

    dheadphone_mode: int | None| Literal["notindicated", "on", "off"] = None,

    ad_conv_type: int | None| Literal["standard", "hdcd"] = None,

    stereo_rematrixing: bool | None = None,

    channel_coupling: int | None| Literal["auto"] = None,

    cpl_start_band: int | None| Literal["auto"] = None,

) -> FFMpegEncoderOption:
    """
    ATSC A/52 E-AC-3

    Args:
        mixing_level: Mixing Level (from -1 to 111) (default -1)
        room_type: Room Type (from -1 to 2) (default -1)
        per_frame_metadata: Allow Changing Metadata Per-Frame (default false)
        copyright: Copyright Bit (from -1 to 1) (default -1)
        dialnorm: Dialogue Level (dB) (from -31 to -1) (default -31)
        dsur_mode: Dolby Surround Mode (from -1 to 2) (default -1)
        original: Original Bit Stream (from -1 to 1) (default -1)
        dmix_mode: Preferred Stereo Downmix Mode (from -1 to 3) (default -1)
        ltrt_cmixlev: Lt/Rt Center Mix Level (from -1 to 2) (default -1)
        ltrt_surmixlev: Lt/Rt Surround Mix Level (from -1 to 2) (default -1)
        loro_cmixlev: Lo/Ro Center Mix Level (from -1 to 2) (default -1)
        loro_surmixlev: Lo/Ro Surround Mix Level (from -1 to 2) (default -1)
        dsurex_mode: Dolby Surround EX Mode (from -1 to 3) (default -1)
        dheadphone_mode: Dolby Headphone Mode (from -1 to 2) (default -1)
        ad_conv_type: A/D Converter Type (from -1 to 1) (default -1)
        stereo_rematrixing: Stereo Rematrixing (default true)
        channel_coupling: Channel Coupling (from -1 to 1) (default auto)
        cpl_start_band: Coupling Start Band (from -1 to 15) (default auto)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "mixing_level": mixing_level,

        "room_type": room_type,

        "per_frame_metadata": per_frame_metadata,

        "copyright": copyright,

        "dialnorm": dialnorm,

        "dsur_mode": dsur_mode,

        "original": original,

        "dmix_mode": dmix_mode,

        "ltrt_cmixlev": ltrt_cmixlev,

        "ltrt_surmixlev": ltrt_surmixlev,

        "loro_cmixlev": loro_cmixlev,

        "loro_surmixlev": loro_surmixlev,

        "dsurex_mode": dsurex_mode,

        "dheadphone_mode": dheadphone_mode,

        "ad_conv_type": ad_conv_type,

        "stereo_rematrixing": stereo_rematrixing,

        "channel_coupling": channel_coupling,

        "cpl_start_band": cpl_start_band,

    }))



def flac(

    lpc_coeff_precision: int | None = None,

    lpc_type: int | None| Literal["none", "fixed", "levinson", "cholesky"] = None,

    lpc_passes: int | None = None,

    min_partition_order: int | None = None,

    prediction_order_method: int | None| Literal["estimation", "2level", "4level", "8level", "search", "log"] = None,

    ch_mode: int | None| Literal["auto", "indep", "left_side", "right_side", "mid_side"] = None,

    exact_rice_parameters: bool | None = None,

    multi_dim_quant: bool | None = None,

    min_prediction_order: int | None = None,

) -> FFMpegEncoderOption:
    """
    FLAC (Free Lossless Audio Codec)

    Args:
        lpc_coeff_precision: LPC coefficient precision (from 0 to 15) (default 15)
        lpc_type: LPC algorithm (from -1 to 3) (default -1)
        lpc_passes: Number of passes to use for Cholesky factorization during LPC analysis (from 1 to INT_MAX) (default 2)
        min_partition_order: (from -1 to 8) (default -1)
        prediction_order_method: Search method for selecting prediction order (from -1 to 5) (default -1)
        ch_mode: Stereo decorrelation mode (from -1 to 3) (default auto)
        exact_rice_parameters: Calculate rice parameters exactly (default false)
        multi_dim_quant: Multi-dimensional quantization (default false)
        min_prediction_order: (from -1 to 32) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "lpc_coeff_precision": lpc_coeff_precision,

        "lpc_type": lpc_type,

        "lpc_passes": lpc_passes,

        "min_partition_order": min_partition_order,

        "prediction_order_method": prediction_order_method,

        "ch_mode": ch_mode,

        "exact_rice_parameters": exact_rice_parameters,

        "multi_dim_quant": multi_dim_quant,

        "min_prediction_order": min_prediction_order,

    }))



def g723_1(

) -> FFMpegEncoderOption:
    """
    G.723.1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def ilbc_at(

    aac_at_mode: int | None| Literal["auto", "cbr", "abr", "cvbr", "vbr"] = None,

    aac_at_quality: int | None = None,

) -> FFMpegEncoderOption:
    """
    ilbc (AudioToolbox) (codec ilbc)

    Args:
        aac_at_mode: ratecontrol mode (from -1 to 3) (default auto)
        aac_at_quality: quality vs speed control (from 0 to 2) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "aac_at_mode": aac_at_mode,

        "aac_at_quality": aac_at_quality,

    }))



def mlp(

    max_interval: int | None = None,

    lpc_coeff_precision: int | None = None,

    lpc_type: int | None| Literal["levinson", "cholesky"] = None,

    lpc_passes: int | None = None,

    codebook_search: int | None = None,

    prediction_order: int | None| Literal["estimation", "search"] = None,

    rematrix_precision: int | None = None,

) -> FFMpegEncoderOption:
    """
    MLP (Meridian Lossless Packing)

    Args:
        max_interval: Max number of frames between each new header (from 8 to 128) (default 16)
        lpc_coeff_precision: LPC coefficient precision (from 0 to 15) (default 15)
        lpc_type: LPC algorithm (from 2 to 3) (default levinson)
        lpc_passes: Number of passes to use for Cholesky factorization during LPC analysis (from 1 to INT_MAX) (default 2)
        codebook_search: Max number of codebook searches (from 1 to 100) (default 3)
        prediction_order: Search method for selecting prediction order (from 0 to 4) (default estimation)
        rematrix_precision: Rematrix coefficient precision (from 0 to 14) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "max_interval": max_interval,

        "lpc_coeff_precision": lpc_coeff_precision,

        "lpc_type": lpc_type,

        "lpc_passes": lpc_passes,

        "codebook_search": codebook_search,

        "prediction_order": prediction_order,

        "rematrix_precision": rematrix_precision,

    }))



def mp2(

) -> FFMpegEncoderOption:
    """
    MP2 (MPEG audio layer 2)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def mp2fixed(

) -> FFMpegEncoderOption:
    """
    MP2 fixed point (MPEG audio layer 2) (codec mp2)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def libmp3lame(

    reservoir: bool | None = None,

    joint_stereo: bool | None = None,

    abr: bool | None = None,

    copyright: bool | None = None,

    original: bool | None = None,

) -> FFMpegEncoderOption:
    """
    libmp3lame MP3 (MPEG audio layer 3) (codec mp3)

    Args:
        reservoir: use bit reservoir (default true)
        joint_stereo: use joint stereo (default true)
        abr: use ABR (default false)
        copyright: set copyright flag (default false)
        original: set original flag (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "reservoir": reservoir,

        "joint_stereo": joint_stereo,

        "abr": abr,

        "copyright": copyright,

        "original": original,

    }))



def nellymoser(

) -> FFMpegEncoderOption:
    """
    Nellymoser Asao


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def opus(

    opus_delay: float | None = None,

    apply_phase_inv: bool | None = None,

) -> FFMpegEncoderOption:
    """
    Opus

    Args:
        opus_delay: Maximum delay in milliseconds (from 2.5 to 360) (default 360)
        apply_phase_inv: Apply intensity stereo phase inversion (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "opus_delay": opus_delay,

        "apply_phase_inv": apply_phase_inv,

    }))



def libopus(

    application: int | None| Literal["voip", "audio", "lowdelay"] = None,

    frame_duration: float | None = None,

    packet_loss: int | None = None,

    fec: bool | None = None,

    vbr: int | None| Literal["off", "on", "constrained"] = None,

    mapping_family: int | None = None,

    apply_phase_inv: bool | None = None,

) -> FFMpegEncoderOption:
    """
    libopus Opus (codec opus)

    Args:
        application: Intended application type (from 2048 to 2051) (default audio)
        frame_duration: Duration of a frame in milliseconds (from 2.5 to 120) (default 20)
        packet_loss: Expected packet loss percentage (from 0 to 100) (default 0)
        fec: Enable inband FEC. Expected packet loss must be non-zero (default false)
        vbr: Variable bit rate mode (from 0 to 2) (default on)
        mapping_family: Channel Mapping Family (from -1 to 255) (default -1)
        apply_phase_inv: Apply intensity stereo phase inversion (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "application": application,

        "frame_duration": frame_duration,

        "packet_loss": packet_loss,

        "fec": fec,

        "vbr": vbr,

        "mapping_family": mapping_family,

        "apply_phase_inv": apply_phase_inv,

    }))



def pcm_alaw(

) -> FFMpegEncoderOption:
    """
    PCM A-law / G.711 A-law


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_alaw_at(

    aac_at_mode: int | None| Literal["auto", "cbr", "abr", "cvbr", "vbr"] = None,

    aac_at_quality: int | None = None,

) -> FFMpegEncoderOption:
    """
    pcm_alaw (AudioToolbox) (codec pcm_alaw)

    Args:
        aac_at_mode: ratecontrol mode (from -1 to 3) (default auto)
        aac_at_quality: quality vs speed control (from 0 to 2) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "aac_at_mode": aac_at_mode,

        "aac_at_quality": aac_at_quality,

    }))



def pcm_bluray(

) -> FFMpegEncoderOption:
    """
    PCM signed 16|20|24-bit big-endian for Blu-ray media


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_dvd(

) -> FFMpegEncoderOption:
    """
    PCM signed 16|20|24-bit big-endian for DVD media


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_f32be(

) -> FFMpegEncoderOption:
    """
    PCM 32-bit floating point big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_f32le(

) -> FFMpegEncoderOption:
    """
    PCM 32-bit floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_f64be(

) -> FFMpegEncoderOption:
    """
    PCM 64-bit floating point big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_f64le(

) -> FFMpegEncoderOption:
    """
    PCM 64-bit floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_mulaw(

) -> FFMpegEncoderOption:
    """
    PCM mu-law / G.711 mu-law


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_mulaw_at(

    aac_at_mode: int | None| Literal["auto", "cbr", "abr", "cvbr", "vbr"] = None,

    aac_at_quality: int | None = None,

) -> FFMpegEncoderOption:
    """
    pcm_mulaw (AudioToolbox) (codec pcm_mulaw)

    Args:
        aac_at_mode: ratecontrol mode (from -1 to 3) (default auto)
        aac_at_quality: quality vs speed control (from 0 to 2) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "aac_at_mode": aac_at_mode,

        "aac_at_quality": aac_at_quality,

    }))



def pcm_s16be(

) -> FFMpegEncoderOption:
    """
    PCM signed 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s16be_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 16-bit big-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s16le(

) -> FFMpegEncoderOption:
    """
    PCM signed 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s16le_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 16-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s24be(

) -> FFMpegEncoderOption:
    """
    PCM signed 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s24daud(

) -> FFMpegEncoderOption:
    """
    PCM D-Cinema audio signed 24-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s24le(

) -> FFMpegEncoderOption:
    """
    PCM signed 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s24le_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 24-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s32be(

) -> FFMpegEncoderOption:
    """
    PCM signed 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s32le(

) -> FFMpegEncoderOption:
    """
    PCM signed 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s32le_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 32-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s64be(

) -> FFMpegEncoderOption:
    """
    PCM signed 64-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s64le(

) -> FFMpegEncoderOption:
    """
    PCM signed 64-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s8(

) -> FFMpegEncoderOption:
    """
    PCM signed 8-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_s8_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 8-bit planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_u16be(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_u16le(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_u24be(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_u24le(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_u32be(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_u32le(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_u8(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 8-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def pcm_vidc(

) -> FFMpegEncoderOption:
    """
    PCM Archimedes VIDC


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def real_144(

) -> FFMpegEncoderOption:
    """
    RealAudio 1.0 (14.4K) (codec ra_144)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def roq_dpcm(

) -> FFMpegEncoderOption:
    """
    id RoQ DPCM


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def s302m(

) -> FFMpegEncoderOption:
    """
    SMPTE 302M


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def sbc(

    sbc_delay: str | None = None,

    msbc: bool | None = None,

) -> FFMpegEncoderOption:
    """
    SBC (low-complexity subband codec)

    Args:
        sbc_delay: set maximum algorithmic latency (default 0.013)
        msbc: use mSBC mode (wideband speech mono SBC) (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "sbc_delay": sbc_delay,

        "msbc": msbc,

    }))



def truehd(

    max_interval: int | None = None,

    lpc_coeff_precision: int | None = None,

    lpc_type: int | None| Literal["levinson", "cholesky"] = None,

    lpc_passes: int | None = None,

    codebook_search: int | None = None,

    prediction_order: int | None| Literal["estimation", "search"] = None,

    rematrix_precision: int | None = None,

) -> FFMpegEncoderOption:
    """
    TrueHD

    Args:
        max_interval: Max number of frames between each new header (from 8 to 128) (default 16)
        lpc_coeff_precision: LPC coefficient precision (from 0 to 15) (default 15)
        lpc_type: LPC algorithm (from 2 to 3) (default levinson)
        lpc_passes: Number of passes to use for Cholesky factorization during LPC analysis (from 1 to INT_MAX) (default 2)
        codebook_search: Max number of codebook searches (from 1 to 100) (default 3)
        prediction_order: Search method for selecting prediction order (from 0 to 4) (default estimation)
        rematrix_precision: Rematrix coefficient precision (from 0 to 14) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "max_interval": max_interval,

        "lpc_coeff_precision": lpc_coeff_precision,

        "lpc_type": lpc_type,

        "lpc_passes": lpc_passes,

        "codebook_search": codebook_search,

        "prediction_order": prediction_order,

        "rematrix_precision": rematrix_precision,

    }))



def tta(

) -> FFMpegEncoderOption:
    """
    TTA (True Audio)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def vorbis(

) -> FFMpegEncoderOption:
    """
    Vorbis


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def wavpack(

    joint_stereo: bool | None = None,

    optimize_mono: bool | None = None,

) -> FFMpegEncoderOption:
    """
    WavPack

    Args:
        joint_stereo: (default auto)
        optimize_mono: (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "joint_stereo": joint_stereo,

        "optimize_mono": optimize_mono,

    }))



def wmav1(

) -> FFMpegEncoderOption:
    """
    Windows Media Audio 1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def wmav2(

) -> FFMpegEncoderOption:
    """
    Windows Media Audio 2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def ssa(

) -> FFMpegEncoderOption:
    """
    ASS (Advanced SubStation Alpha) subtitle (codec ass)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def ass(

) -> FFMpegEncoderOption:
    """
    ASS (Advanced SubStation Alpha) subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def dvbsub(

    min_bpp: int | None = None,

) -> FFMpegEncoderOption:
    """
    DVB subtitles (codec dvb_subtitle)

    Args:
        min_bpp: minimum bits-per-pixel for subtitle colors (2, 4 or 8) (from 2 to 8) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "min_bpp": min_bpp,

    }))



def dvdsub(

    palette: str | None = None,

    even_rows_fix: bool | None = None,

) -> FFMpegEncoderOption:
    """
    DVD subtitles (codec dvd_subtitle)

    Args:
        palette: set the global palette
        even_rows_fix: Make number of rows even (workaround for some players) (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "palette": palette,

        "even_rows_fix": even_rows_fix,

    }))



def mov_text(

    height: int | None = None,

) -> FFMpegEncoderOption:
    """
    3GPP Timed Text subtitle

    Args:
        height: Frame height, usually video height (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

        "height": height,

    }))



def srt(

) -> FFMpegEncoderOption:
    """
    SubRip subtitle (codec subrip)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def subrip(

) -> FFMpegEncoderOption:
    """
    SubRip subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def text(

) -> FFMpegEncoderOption:
    """
    Raw text subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def ttml(

) -> FFMpegEncoderOption:
    """
    TTML subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def webvtt(

) -> FFMpegEncoderOption:
    """
    WebVTT subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))



def xsub(

) -> FFMpegEncoderOption:
    """
    DivX subtitles (XSUB)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(merge({

    }))
