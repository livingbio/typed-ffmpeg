# NOTE: this file is auto-generated, do not modify
from typing import Literal
from .schema import FFMpegEncoderOption
from ..utils.frozendict import FrozenDict, merge



def a64multi(

) -> FFMpegEncoderOption:
    """
    Multicolor charset for Commodore 64 (codec a64_multi)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def a64multi5(

) -> FFMpegEncoderOption:
    """
    Multicolor charset for Commodore 64, extended with 5th color (colram) (codec a64_multi5)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def alias_pix(

) -> FFMpegEncoderOption:
    """
    Alias/Wavefront PIX image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def amv(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    huffman: str = None,

    force_duplicated_matrix: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        huffman: Huffman table strategy (from 0 to 1) (default optimal)
        force_duplicated_matrix: Always write luma and chroma matrix for mjpeg, useful for rtp streaming. (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "huffman": huffman,

        "force_duplicated_matrix": force_duplicated_matrix,

    }))



def apng(

    dpi: str = None,

    dpm: str = None,

    pred: str = None,

) -> FFMpegEncoderOption:
    """
    APNG (Animated Portable Network Graphics) image

    Args:
        dpi: Set image resolution (in dots per inch) (from 0 to 65536) (default 0)
        dpm: Set image resolution (in dots per meter) (from 0 to 65536) (default 0)
        pred: Prediction method (from 0 to 5) (default none)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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
    return FFMpegEncoderOption(kwargs=merge({

    }))



def asv2(

) -> FFMpegEncoderOption:
    """
    ASUS V2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def librav1e(

    qp: str = None,

    speed: str = None,

    tiles: str = None,

    tile_rows: str = None,

    tile_columns: str = None,

    rav1e_params: str = None,

) -> FFMpegEncoderOption:
    """
    librav1e AV1 (codec av1)

    Args:
        qp: use constant quantizer mode (from -1 to 255) (default -1)
        speed: what speed preset to use (from -1 to 10) (default -1)
        tiles: number of tiles encode with (from -1 to I64_MAX) (default 0)
        tile_rows: number of tiles rows to encode with (from -1 to I64_MAX) (default 0)
        tile_columns: number of tiles columns to encode with (from -1 to I64_MAX) (default 0)
        rav1e_params: set the rav1e configuration using a :-separated list of key=value parameters

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "qp": qp,

        "speed": speed,

        "tiles": tiles,

        "tile-rows": tile_rows,

        "tile-columns": tile_columns,

        "rav1e-params": rav1e_params,

    }))



def libsvtav1(

    hielevel: str = None,

    la_depth: str = None,

    tier: str = None,

    preset: str = None,

    crf: str = None,

    qp: str = None,

    sc_detection: str = None,

    tile_columns: str = None,

    tile_rows: str = None,

    svtav1_params: str = None,

) -> FFMpegEncoderOption:
    """
    SVT-AV1(Scalable Video Technology for AV1) encoder (codec av1)

    Args:
        hielevel: Hierarchical prediction levels setting (Deprecated, use svtav1-params) (from -1 to 4) (default -1)
        la_depth: Look ahead distance [0, 120] (Deprecated, use svtav1-params) (from -1 to 120) (default -1)
        tier: Set operating point tier (Deprecated, use svtav1-params) (from -1 to 1) (default -1)
        preset: Encoding preset (from -2 to 13) (default -2)
        crf: Constant Rate Factor value (from 0 to 63) (default 0)
        qp: Initial Quantizer level value (from 0 to 63) (default 0)
        sc_detection: Scene change detection (Deprecated, use svtav1-params) (default auto)
        tile_columns: Log2 of number of tile columns to use (Deprecated, use svtav1-params) (from -1 to 4) (default -1)
        tile_rows: Log2 of number of tile rows to use (Deprecated, use svtav1-params) (from -1 to 6) (default -1)
        svtav1_params: Set the SVT-AV1 configuration using a :-separated list of key=value parameters

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "hielevel": hielevel,

        "la_depth": la_depth,

        "tier": tier,

        "preset": preset,

        "crf": crf,

        "qp": qp,

        "sc_detection": sc_detection,

        "tile_columns": tile_columns,

        "tile_rows": tile_rows,

        "svtav1-params": svtav1_params,

    }))



def av1_nvenc(

    preset: str = None,

    tune: str = None,

    level: str = None,

    tier: str = None,

    rc: str = None,

    multipass: str = None,

    highbitdepth: str = None,

    tile_rows: str = None,

    tile_columns: str = None,

    surfaces: str = None,

    gpu: str = None,

    rgb_mode: str = None,

    delay: str = None,

    rc_lookahead: str = None,

    cq: str = None,

    init_qpP: str = None,

    init_qpB: str = None,

    init_qpI: str = None,

    qp: str = None,

    qp_cb_offset: str = None,

    qp_cr_offset: str = None,

    no_scenecut: str = None,

    forced_idr: str = None,

    b_adapt: str = None,

    spatial_aq: str = None,

    temporal_aq: str = None,

    zerolatency: str = None,

    nonref_p: str = None,

    strict_gop: str = None,

    aq_strength: str = None,

    weighted_pred: str = None,

    b_ref_mode: str = None,

    dpb_size: str = None,

    ldkfs: str = None,

    intra_refresh: str = None,

    timing_info: str = None,

    extra_sei: str = None,

    a53cc: str = None,

    s12m_tc: str = None,

) -> FFMpegEncoderOption:
    """
    NVIDIA NVENC av1 encoder (codec av1)

    Args:
        preset: Set the encoding preset (from 0 to 18) (default p4)
        tune: Set the encoding tuning info (from 1 to 4) (default hq)
        level: Set the encoding level restriction (from 0 to 24) (default auto)
        tier: Set the encoding tier (from 0 to 1) (default 0)
        rc: Override the preset rate-control (from -1 to INT_MAX) (default -1)
        multipass: Set the multipass encoding (from 0 to 2) (default disabled)
        highbitdepth: Enable 10 bit encode for 8 bit input (default false)
        tile_rows: Number of tile rows to encode with (from -1 to 64) (default -1)
        tile_columns: Number of tile columns to encode with (from -1 to 64) (default -1)
        surfaces: Number of concurrent surfaces (from 0 to 64) (default 0)
        gpu: Selects which NVENC capable GPU to use. First GPU is 0, second is 1, and so on. (from -2 to INT_MAX) (default any)
        rgb_mode: Configure how nvenc handles packed RGB input. (from 0 to INT_MAX) (default yuv420)
        delay: Delay frame output by the given amount of frames (from 0 to INT_MAX) (default INT_MAX)
        rc_lookahead: Number of frames to look ahead for rate-control (from 0 to INT_MAX) (default 0)
        cq: Set target quality level (0 to 51, 0 means automatic) for constant quality mode in VBR rate control (from 0 to 51) (default 0)
        init_qpP: Initial QP value for P frame (from -1 to 255) (default -1)
        init_qpB: Initial QP value for B frame (from -1 to 255) (default -1)
        init_qpI: Initial QP value for I frame (from -1 to 255) (default -1)
        qp: Constant quantization parameter rate control method (from -1 to 255) (default -1)
        qp_cb_offset: Quantization parameter offset for cb channel (from -12 to 12) (default 0)
        qp_cr_offset: Quantization parameter offset for cr channel (from -12 to 12) (default 0)
        no_scenecut: When lookahead is enabled, set this to 1 to disable adaptive I-frame insertion at scene cuts (default false)
        forced_idr: If forcing keyframes, force them as IDR frames. (default false)
        b_adapt: When lookahead is enabled, set this to 0 to disable adaptive B-frame decision (default true)
        spatial_aq: set to 1 to enable Spatial AQ (default false)
        temporal_aq: set to 1 to enable Temporal AQ (default false)
        zerolatency: Set 1 to indicate zero latency operation (no reordering delay) (default false)
        nonref_p: Set this to 1 to enable automatic insertion of non-reference P-frames (default false)
        strict_gop: Set 1 to minimize GOP-to-GOP rate fluctuations (default false)
        aq_strength: When Spatial AQ is enabled, this field is used to specify AQ strength. AQ strength scale is from 1 (low) - 15 (aggressive) (from 1 to 15) (default 8)
        weighted_pred: Enable weighted prediction (default false)
        b_ref_mode: Use B frames as references (from -1 to 2) (default -1)
        dpb_size: Specifies the DPB size used for encoding (0 means automatic) (from 0 to INT_MAX) (default 0)
        ldkfs: Low delay key frame scale; Specifies the Scene Change frame size increase allowed in case of single frame VBV and CBR (from 0 to 255) (default 0)
        intra_refresh: Use Periodic Intra Refresh instead of IDR frames (default false)
        timing_info: Include timing info in sequence/frame headers (default false)
        extra_sei: Pass on extra SEI data (e.g. a53 cc) to be included in the bitstream (default true)
        a53cc: Use A53 Closed Captions (if available) (default true)
        s12m_tc: Use timecode (if available) (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "preset": preset,

        "tune": tune,

        "level": level,

        "tier": tier,

        "rc": rc,

        "multipass": multipass,

        "highbitdepth": highbitdepth,

        "tile-rows": tile_rows,

        "tile-columns": tile_columns,

        "surfaces": surfaces,

        "gpu": gpu,

        "rgb_mode": rgb_mode,

        "delay": delay,

        "rc-lookahead": rc_lookahead,

        "cq": cq,

        "init_qpP": init_qpP,

        "init_qpB": init_qpB,

        "init_qpI": init_qpI,

        "qp": qp,

        "qp_cb_offset": qp_cb_offset,

        "qp_cr_offset": qp_cr_offset,

        "no-scenecut": no_scenecut,

        "forced-idr": forced_idr,

        "b_adapt": b_adapt,

        "spatial-aq": spatial_aq,

        "temporal-aq": temporal_aq,

        "zerolatency": zerolatency,

        "nonref_p": nonref_p,

        "strict_gop": strict_gop,

        "aq-strength": aq_strength,

        "weighted_pred": weighted_pred,

        "b_ref_mode": b_ref_mode,

        "dpb_size": dpb_size,

        "ldkfs": ldkfs,

        "intra-refresh": intra_refresh,

        "timing-info": timing_info,

        "extra_sei": extra_sei,

        "a53cc": a53cc,

        "s12m_tc": s12m_tc,

    }))



def av1_vaapi(

    low_power: str = None,

    idr_interval: str = None,

    b_depth: str = None,

    async_depth: str = None,

    max_frame_size: str = None,

    rc_mode: str = None,

    profile: str = None,

    tier: str = None,

    level: str = None,

    tiles: str = None,

    tile_groups: str = None,

) -> FFMpegEncoderOption:
    """
    AV1 (VAAPI) (codec av1)

    Args:
        low_power: Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)
        idr_interval: Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)
        b_depth: Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)
        async_depth: Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)
        max_frame_size: Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)
        rc_mode: Set rate control mode (from 0 to 6) (default auto)
        profile: Set profile (seq_profile) (from -99 to 255) (default -99)
        tier: Set tier (seq_tier) (from 0 to 1) (default main)
        level: Set level (seq_level_idx) (from -99 to 31) (default -99)
        tiles: Tile columns x rows (Use minimal tile column/row number automatically by default)
        tile_groups: Number of tile groups for encoding (from 1 to 4096) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "low_power": low_power,

        "idr_interval": idr_interval,

        "b_depth": b_depth,

        "async_depth": async_depth,

        "max_frame_size": max_frame_size,

        "rc_mode": rc_mode,

        "profile": profile,

        "tier": tier,

        "level": level,

        "tiles": tiles,

        "tile_groups": tile_groups,

    }))



def avrp(

) -> FFMpegEncoderOption:
    """
    Avid 1:1 10-bit RGB Packer


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def avui(

) -> FFMpegEncoderOption:
    """
    Avid Meridien Uncompressed


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def ayuv(

) -> FFMpegEncoderOption:
    """
    Uncompressed packed MS 4:4:4:4


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def bitpacked(

) -> FFMpegEncoderOption:
    """
    Bitpacked


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def bmp(

) -> FFMpegEncoderOption:
    """
    BMP (Windows and OS/2 bitmap)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def cfhd(

    quality: str = None,

) -> FFMpegEncoderOption:
    """
    GoPro CineForm HD

    Args:
        quality: set quality (from 0 to 12) (default film3+)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "quality": quality,

    }))



def cinepak(

    max_extra_cb_iterations: str = None,

    skip_empty_cb: str = None,

    max_strips: str = None,

    min_strips: str = None,

    strip_number_adaptivity: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

        "max_extra_cb_iterations": max_extra_cb_iterations,

        "skip_empty_cb": skip_empty_cb,

        "max_strips": max_strips,

        "min_strips": min_strips,

        "strip_number_adaptivity": strip_number_adaptivity,

    }))



def cljr(

    dither_type: str = None,

) -> FFMpegEncoderOption:
    """
    Cirrus Logic AccuPak

    Args:
        dither_type: Dither type (from 0 to 2) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "dither_type": dither_type,

    }))



def vc2(

    tolerance: str = None,

    slice_width: str = None,

    slice_height: str = None,

    wavelet_depth: str = None,

    wavelet_type: str = None,

    qm: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

        "tolerance": tolerance,

        "slice_width": slice_width,

        "slice_height": slice_height,

        "wavelet_depth": wavelet_depth,

        "wavelet_type": wavelet_type,

        "qm": qm,

    }))



def dnxhd(

    nitris_compat: str = None,

    ibias: str = None,

    profile: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

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
    return FFMpegEncoderOption(kwargs=merge({

    }))



def dvvideo(

    quant_deadzone: str = None,

) -> FFMpegEncoderOption:
    """
    DV (Digital Video)

    Args:
        quant_deadzone: Quantizer dead zone (from 0 to 1024) (default 7)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "quant_deadzone": quant_deadzone,

    }))



def exr(

    compression: str = None,

    format: str = None,

    gamma: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

        "compression": compression,

        "format": format,

        "gamma": gamma,

    }))



def ffv1(

    slicecrc: str = None,

    coder: str = None,

    context: str = None,

) -> FFMpegEncoderOption:
    """
    FFmpeg video codec #1

    Args:
        slicecrc: Protect slices with CRCs (default auto)
        coder: Coder type (from -2 to 2) (default rice)
        context: Context model (from 0 to 1) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "slicecrc": slicecrc,

        "coder": coder,

        "context": context,

    }))



def ffvhuff(

    non_deterministic: str = None,

    pred: str = None,

    context: str = None,

) -> FFMpegEncoderOption:
    """
    Huffyuv FFmpeg variant

    Args:
        non_deterministic: Allow multithreading for e.g. context=1 at the expense of determinism (default false)
        pred: Prediction method (from 0 to 2) (default left)
        context: Set per-frame huffman tables (from 0 to 1) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "non_deterministic": non_deterministic,

        "pred": pred,

        "context": context,

    }))



def fits(

) -> FFMpegEncoderOption:
    """
    Flexible Image Transport System


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def flashsv(

) -> FFMpegEncoderOption:
    """
    Flash Screen Video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def flashsv2(

) -> FFMpegEncoderOption:
    """
    Flash Screen Video Version 2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def flv(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def gif(

    gifflags: str = None,

    gifimage: str = None,

    global_palette: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

        "gifflags": gifflags,

        "gifimage": gifimage,

        "global_palette": global_palette,

    }))



def h261(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def h263(

    obmc: str = None,

    mb_info: str = None,

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def h263_v4l2m2m(

    num_output_buffers: str = None,

    num_capture_buffers: str = None,

) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem H.263 encoder wrapper (codec h263)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "num_output_buffers": num_output_buffers,

        "num_capture_buffers": num_capture_buffers,

    }))



def h263p(

    umv: str = None,

    aiv: str = None,

    obmc: str = None,

    structured_slices: str = None,

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def libx264(

    preset: str = None,

    tune: str = None,

    profile: str = None,

    fastfirstpass: str = None,

    level: str = None,

    passlogfile: str = None,

    wpredp: str = None,

    a53cc: str = None,

    x264opts: str = None,

    crf: str = None,

    crf_max: str = None,

    qp: str = None,

    aq_mode: str = None,

    aq_strength: str = None,

    psy: str = None,

    psy_rd: str = None,

    rc_lookahead: str = None,

    weightb: str = None,

    weightp: str = None,

    ssim: str = None,

    intra_refresh: str = None,

    bluray_compat: str = None,

    b_bias: str = None,

    b_pyramid: str = None,

    mixed_refs: str = None,

    _8x8dct: str = None,

    fast_pskip: str = None,

    aud: str = None,

    mbtree: str = None,

    deblock: str = None,

    cplxblur: str = None,

    partitions: str = None,

    direct_pred: str = None,

    slice_max_size: str = None,

    stats: str = None,

    nal_hrd: str = None,

    avcintra_class: str = None,

    me_method: str = None,

    motion_est: str = None,

    forced_idr: str = None,

    coder: str = None,

    b_strategy: str = None,

    chromaoffset: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    udu_sei: str = None,

    x264_params: str = None,

    mb_info: str = None,

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
        motion_est: Set motion estimation method (from -1 to 4) (default -1)
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
    return FFMpegEncoderOption(kwargs=merge({

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

        "motion-est": motion_est,

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

    preset: str = None,

    tune: str = None,

    profile: str = None,

    fastfirstpass: str = None,

    level: str = None,

    passlogfile: str = None,

    wpredp: str = None,

    a53cc: str = None,

    x264opts: str = None,

    crf: str = None,

    crf_max: str = None,

    qp: str = None,

    aq_mode: str = None,

    aq_strength: str = None,

    psy: str = None,

    psy_rd: str = None,

    rc_lookahead: str = None,

    weightb: str = None,

    weightp: str = None,

    ssim: str = None,

    intra_refresh: str = None,

    bluray_compat: str = None,

    b_bias: str = None,

    b_pyramid: str = None,

    mixed_refs: str = None,

    _8x8dct: str = None,

    fast_pskip: str = None,

    aud: str = None,

    mbtree: str = None,

    deblock: str = None,

    cplxblur: str = None,

    partitions: str = None,

    direct_pred: str = None,

    slice_max_size: str = None,

    stats: str = None,

    nal_hrd: str = None,

    avcintra_class: str = None,

    me_method: str = None,

    motion_est: str = None,

    forced_idr: str = None,

    coder: str = None,

    b_strategy: str = None,

    chromaoffset: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    udu_sei: str = None,

    x264_params: str = None,

    mb_info: str = None,

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
        motion_est: Set motion estimation method (from -1 to 4) (default -1)
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
    return FFMpegEncoderOption(kwargs=merge({

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

        "motion-est": motion_est,

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



def h264_nvenc(

    preset: str = None,

    tune: str = None,

    profile: str = None,

    level: str = None,

    rc: str = None,

    rc_lookahead: str = None,

    surfaces: str = None,

    cbr: str = None,

    _2pass: str = None,

    gpu: str = None,

    rgb_mode: str = None,

    delay: str = None,

    no_scenecut: str = None,

    forced_idr: str = None,

    b_adapt: str = None,

    spatial_aq: str = None,

    spatial_aq: str = None,

    temporal_aq: str = None,

    temporal_aq: str = None,

    zerolatency: str = None,

    nonref_p: str = None,

    strict_gop: str = None,

    aq_strength: str = None,

    cq: str = None,

    aud: str = None,

    bluray_compat: str = None,

    init_qpP: str = None,

    init_qpB: str = None,

    init_qpI: str = None,

    qp: str = None,

    qp_cb_offset: str = None,

    qp_cr_offset: str = None,

    weighted_pred: str = None,

    coder: str = None,

    b_ref_mode: str = None,

    a53cc: str = None,

    dpb_size: str = None,

    multipass: str = None,

    ldkfs: str = None,

    extra_sei: str = None,

    udu_sei: str = None,

    intra_refresh: str = None,

    single_slice_intra_refresh: str = None,

    max_slice_size: str = None,

    constrained_encoding: str = None,

) -> FFMpegEncoderOption:
    """
    NVIDIA NVENC H.264 encoder (codec h264)

    Args:
        preset: Set the encoding preset (from 0 to 18) (default p4)
        tune: Set the encoding tuning info (from 1 to 4) (default hq)
        profile: Set the encoding profile (from 0 to 3) (default main)
        level: Set the encoding level restriction (from 0 to 62) (default auto)
        rc: Override the preset rate-control (from -1 to INT_MAX) (default -1)
        rc_lookahead: Number of frames to look ahead for rate-control (from 0 to INT_MAX) (default 0)
        surfaces: Number of concurrent surfaces (from 0 to 64) (default 0)
        cbr: Use cbr encoding mode (default false)
        _2pass: Use 2pass encoding mode (default auto)
        gpu: Selects which NVENC capable GPU to use. First GPU is 0, second is 1, and so on. (from -2 to INT_MAX) (default any)
        rgb_mode: Configure how nvenc handles packed RGB input. (from 0 to INT_MAX) (default yuv420)
        delay: Delay frame output by the given amount of frames (from 0 to INT_MAX) (default INT_MAX)
        no_scenecut: When lookahead is enabled, set this to 1 to disable adaptive I-frame insertion at scene cuts (default false)
        forced_idr: If forcing keyframes, force them as IDR frames. (default false)
        b_adapt: When lookahead is enabled, set this to 0 to disable adaptive B-frame decision (default true)
        spatial_aq: set to 1 to enable Spatial AQ (default false)
        spatial_aq: set to 1 to enable Spatial AQ (default false)
        temporal_aq: set to 1 to enable Temporal AQ (default false)
        temporal_aq: set to 1 to enable Temporal AQ (default false)
        zerolatency: Set 1 to indicate zero latency operation (no reordering delay) (default false)
        nonref_p: Set this to 1 to enable automatic insertion of non-reference P-frames (default false)
        strict_gop: Set 1 to minimize GOP-to-GOP rate fluctuations (default false)
        aq_strength: When Spatial AQ is enabled, this field is used to specify AQ strength. AQ strength scale is from 1 (low) - 15 (aggressive) (from 1 to 15) (default 8)
        cq: Set target quality level (0 to 51, 0 means automatic) for constant quality mode in VBR rate control (from 0 to 51) (default 0)
        aud: Use access unit delimiters (default false)
        bluray_compat: Bluray compatibility workarounds (default false)
        init_qpP: Initial QP value for P frame (from -1 to 51) (default -1)
        init_qpB: Initial QP value for B frame (from -1 to 51) (default -1)
        init_qpI: Initial QP value for I frame (from -1 to 51) (default -1)
        qp: Constant quantization parameter rate control method (from -1 to 51) (default -1)
        qp_cb_offset: Quantization parameter offset for cb channel (from -12 to 12) (default 0)
        qp_cr_offset: Quantization parameter offset for cr channel (from -12 to 12) (default 0)
        weighted_pred: Set 1 to enable weighted prediction (from 0 to 1) (default 0)
        coder: Coder type (from -1 to 2) (default default)
        b_ref_mode: Use B frames as references (from -1 to 2) (default -1)
        a53cc: Use A53 Closed Captions (if available) (default true)
        dpb_size: Specifies the DPB size used for encoding (0 means automatic) (from 0 to INT_MAX) (default 0)
        multipass: Set the multipass encoding (from 0 to 2) (default disabled)
        ldkfs: Low delay key frame scale; Specifies the Scene Change frame size increase allowed in case of single frame VBV and CBR (from 0 to 255) (default 0)
        extra_sei: Pass on extra SEI data (e.g. a53 cc) to be included in the bitstream (default true)
        udu_sei: Pass on user data unregistered SEI if available (default false)
        intra_refresh: Use Periodic Intra Refresh instead of IDR frames (default false)
        single_slice_intra_refresh: Use single slice intra refresh (default false)
        max_slice_size: Maximum encoded slice size in bytes (from 0 to INT_MAX) (default 0)
        constrained_encoding: Enable constrainedFrame encoding where each slice in the constrained picture is independent of other slices (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "preset": preset,

        "tune": tune,

        "profile": profile,

        "level": level,

        "rc": rc,

        "rc-lookahead": rc_lookahead,

        "surfaces": surfaces,

        "cbr": cbr,

        "2pass": _2pass,

        "gpu": gpu,

        "rgb_mode": rgb_mode,

        "delay": delay,

        "no-scenecut": no_scenecut,

        "forced-idr": forced_idr,

        "b_adapt": b_adapt,

        "spatial-aq": spatial_aq,

        "spatial_aq": spatial_aq,

        "temporal-aq": temporal_aq,

        "temporal_aq": temporal_aq,

        "zerolatency": zerolatency,

        "nonref_p": nonref_p,

        "strict_gop": strict_gop,

        "aq-strength": aq_strength,

        "cq": cq,

        "aud": aud,

        "bluray-compat": bluray_compat,

        "init_qpP": init_qpP,

        "init_qpB": init_qpB,

        "init_qpI": init_qpI,

        "qp": qp,

        "qp_cb_offset": qp_cb_offset,

        "qp_cr_offset": qp_cr_offset,

        "weighted_pred": weighted_pred,

        "coder": coder,

        "b_ref_mode": b_ref_mode,

        "a53cc": a53cc,

        "dpb_size": dpb_size,

        "multipass": multipass,

        "ldkfs": ldkfs,

        "extra_sei": extra_sei,

        "udu_sei": udu_sei,

        "intra-refresh": intra_refresh,

        "single-slice-intra-refresh": single_slice_intra_refresh,

        "max_slice_size": max_slice_size,

        "constrained-encoding": constrained_encoding,

    }))



def h264_v4l2m2m(

    num_output_buffers: str = None,

    num_capture_buffers: str = None,

) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem H.264 encoder wrapper (codec h264)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "num_output_buffers": num_output_buffers,

        "num_capture_buffers": num_capture_buffers,

    }))



def h264_vaapi(

    low_power: str = None,

    idr_interval: str = None,

    b_depth: str = None,

    async_depth: str = None,

    max_frame_size: str = None,

    rc_mode: str = None,

    qp: str = None,

    quality: str = None,

    coder: str = None,

    aud: str = None,

    sei: str = None,

    profile: str = None,

    level: str = None,

) -> FFMpegEncoderOption:
    """
    H.264/AVC (VAAPI) (codec h264)

    Args:
        low_power: Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)
        idr_interval: Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)
        b_depth: Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)
        async_depth: Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)
        max_frame_size: Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)
        rc_mode: Set rate control mode (from 0 to 6) (default auto)
        qp: Constant QP (for P-frames; scaled by qfactor/qoffset for I/B) (from 0 to 52) (default 0)
        quality: Set encode quality (trades off against speed, higher is faster) (from -1 to INT_MAX) (default -1)
        coder: Entropy coder type (from 0 to 1) (default cabac)
        aud: Include AUD (default false)
        sei: Set SEI to include (default identifier+timing+recovery_point+a53_cc)
        profile: Set profile (profile_idc and constraint_set*_flag) (from -99 to 65535) (default -99)
        level: Set level (level_idc) (from -99 to 255) (default -99)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "low_power": low_power,

        "idr_interval": idr_interval,

        "b_depth": b_depth,

        "async_depth": async_depth,

        "max_frame_size": max_frame_size,

        "rc_mode": rc_mode,

        "qp": qp,

        "quality": quality,

        "coder": coder,

        "aud": aud,

        "sei": sei,

        "profile": profile,

        "level": level,

    }))



def hap(

    format: str = None,

    chunks: str = None,

    compressor: str = None,

) -> FFMpegEncoderOption:
    """
    Vidvox Hap

    Args:
        format: (from 11 to 15) (default hap)
        chunks: chunk count (from 1 to 64) (default 1)
        compressor: second-stage compressor (from 160 to 176) (default snappy)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "format": format,

        "chunks": chunks,

        "compressor": compressor,

    }))



def hdr(

) -> FFMpegEncoderOption:
    """
    HDR (Radiance RGBE format) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libx265(

    crf: str = None,

    qp: str = None,

    forced_idr: str = None,

    preset: str = None,

    tune: str = None,

    profile: str = None,

    udu_sei: str = None,

    a53cc: str = None,

    x265_params: str = None,

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
        udu_sei: Use user data unregistered SEI if available (default false)
        a53cc: Use A53 Closed Captions (if available) (default true)
        x265_params: set the x265 configuration using a :-separated list of key=value parameters

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "crf": crf,

        "qp": qp,

        "forced-idr": forced_idr,

        "preset": preset,

        "tune": tune,

        "profile": profile,

        "udu_sei": udu_sei,

        "a53cc": a53cc,

        "x265-params": x265_params,

    }))



def hevc_nvenc(

    preset: str = None,

    tune: str = None,

    profile: str = None,

    level: str = None,

    tier: str = None,

    rc: str = None,

    rc_lookahead: str = None,

    surfaces: str = None,

    cbr: str = None,

    _2pass: str = None,

    gpu: str = None,

    rgb_mode: str = None,

    delay: str = None,

    no_scenecut: str = None,

    forced_idr: str = None,

    spatial_aq: str = None,

    spatial_aq: str = None,

    temporal_aq: str = None,

    temporal_aq: str = None,

    zerolatency: str = None,

    nonref_p: str = None,

    strict_gop: str = None,

    aq_strength: str = None,

    cq: str = None,

    aud: str = None,

    bluray_compat: str = None,

    init_qpP: str = None,

    init_qpB: str = None,

    init_qpI: str = None,

    qp: str = None,

    qp_cb_offset: str = None,

    qp_cr_offset: str = None,

    weighted_pred: str = None,

    b_ref_mode: str = None,

    a53cc: str = None,

    s12m_tc: str = None,

    dpb_size: str = None,

    multipass: str = None,

    ldkfs: str = None,

    extra_sei: str = None,

    udu_sei: str = None,

    intra_refresh: str = None,

    single_slice_intra_refresh: str = None,

    max_slice_size: str = None,

    constrained_encoding: str = None,

) -> FFMpegEncoderOption:
    """
    NVIDIA NVENC hevc encoder (codec hevc)

    Args:
        preset: Set the encoding preset (from 0 to 18) (default p4)
        tune: Set the encoding tuning info (from 1 to 4) (default hq)
        profile: Set the encoding profile (from 0 to 4) (default main)
        level: Set the encoding level restriction (from 0 to 186) (default auto)
        tier: Set the encoding tier (from 0 to 1) (default main)
        rc: Override the preset rate-control (from -1 to INT_MAX) (default -1)
        rc_lookahead: Number of frames to look ahead for rate-control (from 0 to INT_MAX) (default 0)
        surfaces: Number of concurrent surfaces (from 0 to 64) (default 0)
        cbr: Use cbr encoding mode (default false)
        _2pass: Use 2pass encoding mode (default auto)
        gpu: Selects which NVENC capable GPU to use. First GPU is 0, second is 1, and so on. (from -2 to INT_MAX) (default any)
        rgb_mode: Configure how nvenc handles packed RGB input. (from 0 to INT_MAX) (default yuv420)
        delay: Delay frame output by the given amount of frames (from 0 to INT_MAX) (default INT_MAX)
        no_scenecut: When lookahead is enabled, set this to 1 to disable adaptive I-frame insertion at scene cuts (default false)
        forced_idr: If forcing keyframes, force them as IDR frames. (default false)
        spatial_aq: set to 1 to enable Spatial AQ (default false)
        spatial_aq: set to 1 to enable Spatial AQ (default false)
        temporal_aq: set to 1 to enable Temporal AQ (default false)
        temporal_aq: set to 1 to enable Temporal AQ (default false)
        zerolatency: Set 1 to indicate zero latency operation (no reordering delay) (default false)
        nonref_p: Set this to 1 to enable automatic insertion of non-reference P-frames (default false)
        strict_gop: Set 1 to minimize GOP-to-GOP rate fluctuations (default false)
        aq_strength: When Spatial AQ is enabled, this field is used to specify AQ strength. AQ strength scale is from 1 (low) - 15 (aggressive) (from 1 to 15) (default 8)
        cq: Set target quality level (0 to 51, 0 means automatic) for constant quality mode in VBR rate control (from 0 to 51) (default 0)
        aud: Use access unit delimiters (default false)
        bluray_compat: Bluray compatibility workarounds (default false)
        init_qpP: Initial QP value for P frame (from -1 to 51) (default -1)
        init_qpB: Initial QP value for B frame (from -1 to 51) (default -1)
        init_qpI: Initial QP value for I frame (from -1 to 51) (default -1)
        qp: Constant quantization parameter rate control method (from -1 to 51) (default -1)
        qp_cb_offset: Quantization parameter offset for cb channel (from -12 to 12) (default 0)
        qp_cr_offset: Quantization parameter offset for cr channel (from -12 to 12) (default 0)
        weighted_pred: Set 1 to enable weighted prediction (from 0 to 1) (default 0)
        b_ref_mode: Use B frames as references (from -1 to 2) (default -1)
        a53cc: Use A53 Closed Captions (if available) (default true)
        s12m_tc: Use timecode (if available) (default true)
        dpb_size: Specifies the DPB size used for encoding (0 means automatic) (from 0 to INT_MAX) (default 0)
        multipass: Set the multipass encoding (from 0 to 2) (default disabled)
        ldkfs: Low delay key frame scale; Specifies the Scene Change frame size increase allowed in case of single frame VBV and CBR (from 0 to 255) (default 0)
        extra_sei: Pass on extra SEI data (e.g. a53 cc) to be included in the bitstream (default true)
        udu_sei: Pass on user data unregistered SEI if available (default false)
        intra_refresh: Use Periodic Intra Refresh instead of IDR frames (default false)
        single_slice_intra_refresh: Use single slice intra refresh (default false)
        max_slice_size: Maximum encoded slice size in bytes (from 0 to INT_MAX) (default 0)
        constrained_encoding: Enable constrainedFrame encoding where each slice in the constrained picture is independent of other slices (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "preset": preset,

        "tune": tune,

        "profile": profile,

        "level": level,

        "tier": tier,

        "rc": rc,

        "rc-lookahead": rc_lookahead,

        "surfaces": surfaces,

        "cbr": cbr,

        "2pass": _2pass,

        "gpu": gpu,

        "rgb_mode": rgb_mode,

        "delay": delay,

        "no-scenecut": no_scenecut,

        "forced-idr": forced_idr,

        "spatial_aq": spatial_aq,

        "spatial-aq": spatial_aq,

        "temporal_aq": temporal_aq,

        "temporal-aq": temporal_aq,

        "zerolatency": zerolatency,

        "nonref_p": nonref_p,

        "strict_gop": strict_gop,

        "aq-strength": aq_strength,

        "cq": cq,

        "aud": aud,

        "bluray-compat": bluray_compat,

        "init_qpP": init_qpP,

        "init_qpB": init_qpB,

        "init_qpI": init_qpI,

        "qp": qp,

        "qp_cb_offset": qp_cb_offset,

        "qp_cr_offset": qp_cr_offset,

        "weighted_pred": weighted_pred,

        "b_ref_mode": b_ref_mode,

        "a53cc": a53cc,

        "s12m_tc": s12m_tc,

        "dpb_size": dpb_size,

        "multipass": multipass,

        "ldkfs": ldkfs,

        "extra_sei": extra_sei,

        "udu_sei": udu_sei,

        "intra-refresh": intra_refresh,

        "single-slice-intra-refresh": single_slice_intra_refresh,

        "max_slice_size": max_slice_size,

        "constrained-encoding": constrained_encoding,

    }))



def hevc_v4l2m2m(

    num_output_buffers: str = None,

    num_capture_buffers: str = None,

) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem HEVC encoder wrapper (codec hevc)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "num_output_buffers": num_output_buffers,

        "num_capture_buffers": num_capture_buffers,

    }))



def hevc_vaapi(

    low_power: str = None,

    idr_interval: str = None,

    b_depth: str = None,

    async_depth: str = None,

    max_frame_size: str = None,

    rc_mode: str = None,

    qp: str = None,

    aud: str = None,

    profile: str = None,

    tier: str = None,

    level: str = None,

    sei: str = None,

    tiles: str = None,

) -> FFMpegEncoderOption:
    """
    H.265/HEVC (VAAPI) (codec hevc)

    Args:
        low_power: Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)
        idr_interval: Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)
        b_depth: Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)
        async_depth: Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)
        max_frame_size: Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)
        rc_mode: Set rate control mode (from 0 to 6) (default auto)
        qp: Constant QP (for P-frames; scaled by qfactor/qoffset for I/B) (from 0 to 52) (default 0)
        aud: Include AUD (default false)
        profile: Set profile (general_profile_idc) (from -99 to 255) (default -99)
        tier: Set tier (general_tier_flag) (from 0 to 1) (default main)
        level: Set level (general_level_idc) (from -99 to 255) (default -99)
        sei: Set SEI to include (default hdr+a53_cc)
        tiles: Tile columns x rows

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "low_power": low_power,

        "idr_interval": idr_interval,

        "b_depth": b_depth,

        "async_depth": async_depth,

        "max_frame_size": max_frame_size,

        "rc_mode": rc_mode,

        "qp": qp,

        "aud": aud,

        "profile": profile,

        "tier": tier,

        "level": level,

        "sei": sei,

        "tiles": tiles,

    }))



def huffyuv(

    non_deterministic: str = None,

    pred: str = None,

) -> FFMpegEncoderOption:
    """
    Huffyuv / HuffYUV

    Args:
        non_deterministic: Allow multithreading for e.g. context=1 at the expense of determinism (default false)
        pred: Prediction method (from 0 to 2) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "non_deterministic": non_deterministic,

        "pred": pred,

    }))



def jpeg2000(

    format: str = None,

    tile_width: str = None,

    tile_height: str = None,

    pred: str = None,

    sop: str = None,

    eph: str = None,

    prog: str = None,

    layer_rates: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

        "format": format,

        "tile_width": tile_width,

        "tile_height": tile_height,

        "pred": pred,

        "sop": sop,

        "eph": eph,

        "prog": prog,

        "layer_rates": layer_rates,

    }))



def libopenjpeg(

    format: str = None,

    profile: str = None,

    cinema_mode: str = None,

    prog_order: str = None,

    numresolution: str = None,

    irreversible: str = None,

    disto_alloc: str = None,

    fixed_quality: str = None,

) -> FFMpegEncoderOption:
    """
    OpenJPEG JPEG 2000 (codec jpeg2000)

    Args:
        format: Codec Format (from 0 to 2) (default jp2)
        profile: (from 0 to 4) (default jpeg2000)
        cinema_mode: Digital Cinema (from 0 to 3) (default off)
        prog_order: Progression Order (from 0 to 4) (default lrcp)
        numresolution: (from 0 to 33) (default 6)
        irreversible: (from 0 to 1) (default 0)
        disto_alloc: (from 0 to 1) (default 1)
        fixed_quality: (from 0 to 1) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "format": format,

        "profile": profile,

        "cinema_mode": cinema_mode,

        "prog_order": prog_order,

        "numresolution": numresolution,

        "irreversible": irreversible,

        "disto_alloc": disto_alloc,

        "fixed_quality": fixed_quality,

    }))



def jpegls(

    pred: str = None,

) -> FFMpegEncoderOption:
    """
    JPEG-LS

    Args:
        pred: Prediction method (from 0 to 2) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "pred": pred,

    }))



def libjxl(

    effort: str = None,

    distance: str = None,

    modular: str = None,

) -> FFMpegEncoderOption:
    """
    libjxl JPEG XL (codec jpegxl)

    Args:
        effort: Encoding effort (from 1 to 9) (default 7)
        distance: Maximum Butteraugli distance (quality setting, lower = better, zero = lossless, default 1.0) (from -1 to 15) (default -1)
        modular: Force modular mode (from 0 to 1) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "effort": effort,

        "distance": distance,

        "modular": modular,

    }))



def ljpeg(

    pred: str = None,

) -> FFMpegEncoderOption:
    """
    Lossless JPEG

    Args:
        pred: Prediction method (from 1 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "pred": pred,

    }))



def magicyuv(

    pred: str = None,

) -> FFMpegEncoderOption:
    """
    MagicYUV video

    Args:
        pred: Prediction method (from 1 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "pred": pred,

    }))



def mjpeg(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    huffman: str = None,

    force_duplicated_matrix: str = None,

) -> FFMpegEncoderOption:
    """
    MJPEG (Motion JPEG)

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        huffman: Huffman table strategy (from 0 to 1) (default optimal)
        force_duplicated_matrix: Always write luma and chroma matrix for mjpeg, useful for rtp streaming. (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "huffman": huffman,

        "force_duplicated_matrix": force_duplicated_matrix,

    }))



def mjpeg_vaapi(

    low_power: str = None,

    idr_interval: str = None,

    b_depth: str = None,

    async_depth: str = None,

    max_frame_size: str = None,

    jfif: str = None,

    huffman: str = None,

) -> FFMpegEncoderOption:
    """
    MJPEG (VAAPI) (codec mjpeg)

    Args:
        low_power: Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)
        idr_interval: Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)
        b_depth: Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)
        async_depth: Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)
        max_frame_size: Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)
        jfif: Include JFIF header (default false)
        huffman: Include huffman tables (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "low_power": low_power,

        "idr_interval": idr_interval,

        "b_depth": b_depth,

        "async_depth": async_depth,

        "max_frame_size": max_frame_size,

        "jfif": jfif,

        "huffman": huffman,

    }))



def mpeg1video(

    gop_timecode: str = None,

    drop_frame_timecode: str = None,

    scan_offset: str = None,

    timecode_frame_start: str = None,

    b_strategy: str = None,

    b_sensitivity: str = None,

    brd_scale: str = None,

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def mpeg2video(

    gop_timecode: str = None,

    drop_frame_timecode: str = None,

    scan_offset: str = None,

    timecode_frame_start: str = None,

    b_strategy: str = None,

    b_sensitivity: str = None,

    brd_scale: str = None,

    intra_vlc: str = None,

    non_linear_quant: str = None,

    alternate_scan: str = None,

    a53cc: str = None,

    seq_disp_ext: str = None,

    video_format: str = None,

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "gop_timecode": gop_timecode,

        "drop_frame_timecode": drop_frame_timecode,

        "scan_offset": scan_offset,

        "timecode_frame_start": timecode_frame_start,

        "b_strategy": b_strategy,

        "b_sensitivity": b_sensitivity,

        "brd_scale": brd_scale,

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def mpeg2_vaapi(

    low_power: str = None,

    idr_interval: str = None,

    b_depth: str = None,

    async_depth: str = None,

    max_frame_size: str = None,

    rc_mode: str = None,

    profile: str = None,

    level: str = None,

) -> FFMpegEncoderOption:
    """
    MPEG-2 (VAAPI) (codec mpeg2video)

    Args:
        low_power: Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)
        idr_interval: Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)
        b_depth: Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)
        async_depth: Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)
        max_frame_size: Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)
        rc_mode: Set rate control mode (from 0 to 6) (default auto)
        profile: Set profile (in profile_and_level_indication) (from -99 to 7) (default -99)
        level: Set level (in profile_and_level_indication) (from 0 to 15) (default high)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "low_power": low_power,

        "idr_interval": idr_interval,

        "b_depth": b_depth,

        "async_depth": async_depth,

        "max_frame_size": max_frame_size,

        "rc_mode": rc_mode,

        "profile": profile,

        "level": level,

    }))



def mpeg4(

    data_partitioning: str = None,

    alternate_scan: str = None,

    mpeg_quant: str = None,

    b_strategy: str = None,

    b_sensitivity: str = None,

    brd_scale: str = None,

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def libxvid(

    lumi_aq: str = None,

    variance_aq: str = None,

    ssim: str = None,

    ssim_acc: str = None,

    gmc: str = None,

    me_quality: str = None,

    mpeg_quant: str = None,

) -> FFMpegEncoderOption:
    """
    libxvidcore MPEG-4 part 2 (codec mpeg4)

    Args:
        lumi_aq: Luminance masking AQ (from 0 to 1) (default 0)
        variance_aq: Variance AQ (from 0 to 1) (default 0)
        ssim: Show SSIM information to stdout (from 0 to 2) (default off)
        ssim_acc: SSIM accuracy (from 0 to 4) (default 2)
        gmc: use GMC (from 0 to 1) (default 0)
        me_quality: Motion estimation quality (from 0 to 6) (default 4)
        mpeg_quant: Use MPEG quantizers instead of H.263 (from 0 to 1) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "lumi_aq": lumi_aq,

        "variance_aq": variance_aq,

        "ssim": ssim,

        "ssim_acc": ssim_acc,

        "gmc": gmc,

        "me_quality": me_quality,

        "mpeg_quant": mpeg_quant,

    }))



def mpeg4_v4l2m2m(

    num_output_buffers: str = None,

    num_capture_buffers: str = None,

) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem MPEG4 encoder wrapper (codec mpeg4)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "num_output_buffers": num_output_buffers,

        "num_capture_buffers": num_capture_buffers,

    }))



def msmpeg4v2(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def msmpeg4(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def msrle(

) -> FFMpegEncoderOption:
    """
    Microsoft RLE


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def msvideo1(

) -> FFMpegEncoderOption:
    """
    Microsoft Video-1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pam(

) -> FFMpegEncoderOption:
    """
    PAM (Portable AnyMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pbm(

) -> FFMpegEncoderOption:
    """
    PBM (Portable BitMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcx(

) -> FFMpegEncoderOption:
    """
    PC Paintbrush PCX image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pfm(

) -> FFMpegEncoderOption:
    """
    PFM (Portable FloatMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pgm(

) -> FFMpegEncoderOption:
    """
    PGM (Portable GrayMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pgmyuv(

) -> FFMpegEncoderOption:
    """
    PGMYUV (Portable GrayMap YUV) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def phm(

) -> FFMpegEncoderOption:
    """
    PHM (Portable HalfFloatMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def png(

    dpi: str = None,

    dpm: str = None,

    pred: str = None,

) -> FFMpegEncoderOption:
    """
    PNG (Portable Network Graphics) image

    Args:
        dpi: Set image resolution (in dots per inch) (from 0 to 65536) (default 0)
        dpm: Set image resolution (in dots per meter) (from 0 to 65536) (default 0)
        pred: Prediction method (from 0 to 5) (default none)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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
    return FFMpegEncoderOption(kwargs=merge({

    }))



def prores(

    vendor: str = None,

) -> FFMpegEncoderOption:
    """
    Apple ProRes

    Args:
        vendor: vendor ID (default "fmpg")

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "vendor": vendor,

    }))



def prores_aw(

    vendor: str = None,

) -> FFMpegEncoderOption:
    """
    Apple ProRes (codec prores)

    Args:
        vendor: vendor ID (default "fmpg")

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "vendor": vendor,

    }))



def prores_ks(

    mbs_per_slice: str = None,

    profile: str = None,

    vendor: str = None,

    bits_per_mb: str = None,

    quant_mat: str = None,

    alpha_bits: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

        "mbs_per_slice": mbs_per_slice,

        "profile": profile,

        "vendor": vendor,

        "bits_per_mb": bits_per_mb,

        "quant_mat": quant_mat,

        "alpha_bits": alpha_bits,

    }))



def qoi(

) -> FFMpegEncoderOption:
    """
    QOI (Quite OK Image format) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def qtrle(

) -> FFMpegEncoderOption:
    """
    QuickTime Animation (RLE) video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def r10k(

) -> FFMpegEncoderOption:
    """
    AJA Kona 10-bit RGB Codec


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def r210(

) -> FFMpegEncoderOption:
    """
    Uncompressed RGB 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def rawvideo(

) -> FFMpegEncoderOption:
    """
    raw video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def roqvideo(

    quake3_compat: str = None,

) -> FFMpegEncoderOption:
    """
    id RoQ video (codec roq)

    Args:
        quake3_compat: Whether to respect known limitations in Quake 3 decoder (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "quake3_compat": quake3_compat,

    }))



def rpza(

    skip_frame_thresh: str = None,

    start_one_color_thresh: str = None,

    continue_one_color_thresh: str = None,

    sixteen_color_thresh: str = None,

) -> FFMpegEncoderOption:
    """
    QuickTime video (RPZA)

    Args:
        skip_frame_thresh: (from 0 to 24) (default 1)
        start_one_color_thresh: (from 0 to 24) (default 1)
        continue_one_color_thresh: (from 0 to 24) (default 0)
        sixteen_color_thresh: (from 0 to 24) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "skip_frame_thresh": skip_frame_thresh,

        "start_one_color_thresh": start_one_color_thresh,

        "continue_one_color_thresh": continue_one_color_thresh,

        "sixteen_color_thresh": sixteen_color_thresh,

    }))



def rv10(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def rv20(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def sgi(

    rle: str = None,

) -> FFMpegEncoderOption:
    """
    SGI image

    Args:
        rle: Use run-length compression (from 0 to 1) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "rle": rle,

    }))



def smc(

) -> FFMpegEncoderOption:
    """
    QuickTime Graphics (SMC)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def snow(

    motion_est: str = None,

    memc_only: str = None,

    no_bitstream: str = None,

    intra_penalty: str = None,

    iterative_dia_size: str = None,

    sc_threshold: str = None,

    pred: str = None,

    rc_eq: str = None,

) -> FFMpegEncoderOption:
    """
    Snow

    Args:
        motion_est: motion estimation algorithm (from 0 to 3) (default epzs)
        memc_only: Only do ME/MC (I frames -> ref, P frame -> ME+MC). (default false)
        no_bitstream: Skip final bitstream writeout. (default false)
        intra_penalty: Penalty for intra blocks in block decission (from 0 to INT_MAX) (default 0)
        iterative_dia_size: Dia size for the iterative ME (from 0 to INT_MAX) (default 0)
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        pred: Spatial decomposition type (from 0 to 1) (default dwt97)
        rc_eq: Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex.

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def sunrast(

    rle: str = None,

) -> FFMpegEncoderOption:
    """
    Sun Rasterfile image

    Args:
        rle: Use run-length compression (from 0 to 1) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "rle": rle,

    }))



def svq1(

    motion_est: str = None,

) -> FFMpegEncoderOption:
    """
    Sorenson Vector Quantizer 1 / Sorenson Video 1 / SVQ1

    Args:
        motion_est: Motion estimation algorithm (from 0 to 2) (default epzs)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "motion-est": motion_est,

    }))



def targa(

    rle: str = None,

) -> FFMpegEncoderOption:
    """
    Truevision Targa image

    Args:
        rle: Use run-length compression (from 0 to 1) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "rle": rle,

    }))



def libtheora(

) -> FFMpegEncoderOption:
    """
    libtheora Theora (codec theora)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def tiff(

    dpi: str = None,

    compression_algo: str = None,

) -> FFMpegEncoderOption:
    """
    TIFF image

    Args:
        dpi: set the image resolution (in dpi) (from 1 to 65536) (default 72)
        compression_algo: (from 1 to 32946) (default packbits)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "dpi": dpi,

        "compression_algo": compression_algo,

    }))



def utvideo(

    pred: str = None,

) -> FFMpegEncoderOption:
    """
    Ut Video

    Args:
        pred: Prediction method (from 0 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "pred": pred,

    }))



def v210(

) -> FFMpegEncoderOption:
    """
    Uncompressed 4:2:2 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def v308(

) -> FFMpegEncoderOption:
    """
    Uncompressed packed 4:4:4


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def v408(

) -> FFMpegEncoderOption:
    """
    Uncompressed packed QT 4:4:4:4


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def v410(

) -> FFMpegEncoderOption:
    """
    Uncompressed 4:4:4 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def vbn(

    format: str = None,

) -> FFMpegEncoderOption:
    """
    Vizrt Binary Image

    Args:
        format: Texture format (from 0 to 3) (default dxt5)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "format": format,

    }))



def vnull(

) -> FFMpegEncoderOption:
    """
    null video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libvpx(

    lag_in_frames: str = None,

    arnr_maxframes: str = None,

    arnr_strength: str = None,

    arnr_type: str = None,

    tune: str = None,

    deadline: str = None,

    error_resilient: str = None,

    max_intra_rate: str = None,

    crf: str = None,

    static_thresh: str = None,

    drop_threshold: str = None,

    noise_sensitivity: str = None,

    undershoot_pct: str = None,

    overshoot_pct: str = None,

    ts_parameters: str = None,

    auto_alt_ref: str = None,

    cpu_used: str = None,

    speed: str = None,

    quality: str = None,

    vp8flags: str = None,

    arnr_max_frames: str = None,

    arnr_strength: str = None,

    arnr_type: str = None,

    rc_lookahead: str = None,

    sharpness: str = None,

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
        speed: (from -16 to 16) (default 1)
        quality: (from INT_MIN to INT_MAX) (default good)
        vp8flags: (default 0)
        arnr_max_frames: altref noise reduction max frame count (from 0 to 15) (default 0)
        arnr_strength: altref noise reduction filter strength (from 0 to 6) (default 3)
        arnr_type: altref noise reduction filter type (from 1 to 3) (default 3)
        rc_lookahead: Number of frames to look ahead for alternate reference frame selection (from 0 to 25) (default 25)
        sharpness: Increase sharpness at the expense of lower PSNR (from -1 to 7) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "speed": speed,

        "quality": quality,

        "vp8flags": vp8flags,

        "arnr_max_frames": arnr_max_frames,

        "arnr_strength": arnr_strength,

        "arnr_type": arnr_type,

        "rc_lookahead": rc_lookahead,

        "sharpness": sharpness,

    }))



def vp8_v4l2m2m(

    num_output_buffers: str = None,

    num_capture_buffers: str = None,

) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem VP8 encoder wrapper (codec vp8)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "num_output_buffers": num_output_buffers,

        "num_capture_buffers": num_capture_buffers,

    }))



def vp8_vaapi(

    low_power: str = None,

    idr_interval: str = None,

    b_depth: str = None,

    async_depth: str = None,

    max_frame_size: str = None,

    rc_mode: str = None,

    loop_filter_level: str = None,

    loop_filter_sharpness: str = None,

) -> FFMpegEncoderOption:
    """
    VP8 (VAAPI) (codec vp8)

    Args:
        low_power: Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)
        idr_interval: Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)
        b_depth: Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)
        async_depth: Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)
        max_frame_size: Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)
        rc_mode: Set rate control mode (from 0 to 6) (default auto)
        loop_filter_level: Loop filter level (from 0 to 63) (default 16)
        loop_filter_sharpness: Loop filter sharpness (from 0 to 15) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "low_power": low_power,

        "idr_interval": idr_interval,

        "b_depth": b_depth,

        "async_depth": async_depth,

        "max_frame_size": max_frame_size,

        "rc_mode": rc_mode,

        "loop_filter_level": loop_filter_level,

        "loop_filter_sharpness": loop_filter_sharpness,

    }))



def vp9_vaapi(

    low_power: str = None,

    idr_interval: str = None,

    b_depth: str = None,

    async_depth: str = None,

    max_frame_size: str = None,

    rc_mode: str = None,

    loop_filter_level: str = None,

    loop_filter_sharpness: str = None,

) -> FFMpegEncoderOption:
    """
    VP9 (VAAPI) (codec vp9)

    Args:
        low_power: Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)
        idr_interval: Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)
        b_depth: Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)
        async_depth: Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)
        max_frame_size: Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)
        rc_mode: Set rate control mode (from 0 to 6) (default auto)
        loop_filter_level: Loop filter level (from 0 to 63) (default 16)
        loop_filter_sharpness: Loop filter sharpness (from 0 to 15) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "low_power": low_power,

        "idr_interval": idr_interval,

        "b_depth": b_depth,

        "async_depth": async_depth,

        "max_frame_size": max_frame_size,

        "rc_mode": rc_mode,

        "loop_filter_level": loop_filter_level,

        "loop_filter_sharpness": loop_filter_sharpness,

    }))



def wbmp(

) -> FFMpegEncoderOption:
    """
    WBMP (Wireless Application Protocol Bitmap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libwebp_anim(

    lossless: str = None,

    preset: str = None,

    cr_threshold: str = None,

    cr_size: str = None,

    quality: str = None,

) -> FFMpegEncoderOption:
    """
    libwebp WebP image (codec webp)

    Args:
        lossless: Use lossless mode (from 0 to 1) (default 0)
        preset: Configuration preset (from -1 to 5) (default none)
        cr_threshold: Conditional replenishment threshold (from 0 to INT_MAX) (default 0)
        cr_size: Conditional replenishment block size (from 0 to 256) (default 16)
        quality: Quality (from 0 to 100) (default 75)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "lossless": lossless,

        "preset": preset,

        "cr_threshold": cr_threshold,

        "cr_size": cr_size,

        "quality": quality,

    }))



def libwebp(

    lossless: str = None,

    preset: str = None,

    cr_threshold: str = None,

    cr_size: str = None,

    quality: str = None,

) -> FFMpegEncoderOption:
    """
    libwebp WebP image (codec webp)

    Args:
        lossless: Use lossless mode (from 0 to 1) (default 0)
        preset: Configuration preset (from -1 to 5) (default none)
        cr_threshold: Conditional replenishment threshold (from 0 to INT_MAX) (default 0)
        cr_size: Conditional replenishment block size (from 0 to 256) (default 16)
        quality: Quality (from 0 to 100) (default 75)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "lossless": lossless,

        "preset": preset,

        "cr_threshold": cr_threshold,

        "cr_size": cr_size,

        "quality": quality,

    }))



def wmv1(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def wmv2(

    mpv_flags: str = None,

    luma_elim_threshold: str = None,

    chroma_elim_threshold: str = None,

    quantizer_noise_shaping: str = None,

    error_rate: str = None,

    qsquish: str = None,

    rc_qmod_amp: str = None,

    rc_qmod_freq: str = None,

    rc_eq: str = None,

    rc_init_cplx: str = None,

    rc_buf_aggressivity: str = None,

    border_mask: str = None,

    lmin: str = None,

    lmax: str = None,

    skip_threshold: str = None,

    skip_factor: str = None,

    skip_exp: str = None,

    skip_cmp: str = None,

    sc_threshold: str = None,

    noise_reduction: str = None,

    ps: str = None,

    motion_est: str = None,

    mepc: str = None,

    mepre: str = None,

    intra_penalty: str = None,

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
        sc_threshold: Scene change threshold (from INT_MIN to INT_MAX) (default 0)
        noise_reduction: Noise reduction (from INT_MIN to INT_MAX) (default 0)
        ps: RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)
        motion_est: motion estimation algorithm (from 0 to 2) (default epzs)
        mepc: Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)
        mepre: pre motion estimation (from INT_MIN to INT_MAX) (default 0)
        intra_penalty: Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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

        "sc_threshold": sc_threshold,

        "noise_reduction": noise_reduction,

        "ps": ps,

        "motion_est": motion_est,

        "mepc": mepc,

        "mepre": mepre,

        "intra_penalty": intra_penalty,

    }))



def wrapped_avframe(

) -> FFMpegEncoderOption:
    """
    AVFrame to AVPacket passthrough


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def xbm(

) -> FFMpegEncoderOption:
    """
    XBM (X BitMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def xface(

) -> FFMpegEncoderOption:
    """
    X-face image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def xwd(

) -> FFMpegEncoderOption:
    """
    XWD (X Window Dump) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def y41p(

) -> FFMpegEncoderOption:
    """
    Uncompressed YUV 4:1:1 12-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def yuv4(

) -> FFMpegEncoderOption:
    """
    Uncompressed packed 4:2:0


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def zlib(

) -> FFMpegEncoderOption:
    """
    LCL (LossLess Codec Library) ZLIB


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def zmbv(

) -> FFMpegEncoderOption:
    """
    Zip Motion Blocks Video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def aac(

    aac_coder: str = None,

    aac_ms: str = None,

    aac_is: str = None,

    aac_pns: str = None,

    aac_tns: str = None,

    aac_ltp: str = None,

    aac_pred: str = None,

    aac_pce: str = None,

) -> FFMpegEncoderOption:
    """
    AAC (Advanced Audio Coding)

    Args:
        aac_coder: Coding algorithm (from 0 to 2) (default twoloop)
        aac_ms: Force M/S stereo coding (default auto)
        aac_is: Intensity stereo coding (default true)
        aac_pns: Perceptual noise substitution (default true)
        aac_tns: Temporal noise shaping (default true)
        aac_ltp: Long term prediction (default false)
        aac_pred: AAC-Main prediction (default false)
        aac_pce: Forces the use of PCEs (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "aac_coder": aac_coder,

        "aac_ms": aac_ms,

        "aac_is": aac_is,

        "aac_pns": aac_pns,

        "aac_tns": aac_tns,

        "aac_ltp": aac_ltp,

        "aac_pred": aac_pred,

        "aac_pce": aac_pce,

    }))



def ac3(

    center_mixlev: str = None,

    surround_mixlev: str = None,

    mixing_level: str = None,

    room_type: str = None,

    per_frame_metadata: str = None,

    copyright: str = None,

    dialnorm: str = None,

    dsur_mode: str = None,

    original: str = None,

    dmix_mode: str = None,

    ltrt_cmixlev: str = None,

    ltrt_surmixlev: str = None,

    loro_cmixlev: str = None,

    loro_surmixlev: str = None,

    dsurex_mode: str = None,

    dheadphone_mode: str = None,

    ad_conv_type: str = None,

    stereo_rematrixing: str = None,

    channel_coupling: str = None,

    cpl_start_band: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

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

    center_mixlev: str = None,

    surround_mixlev: str = None,

    mixing_level: str = None,

    room_type: str = None,

    per_frame_metadata: str = None,

    copyright: str = None,

    dialnorm: str = None,

    dsur_mode: str = None,

    original: str = None,

    dmix_mode: str = None,

    ltrt_cmixlev: str = None,

    ltrt_surmixlev: str = None,

    loro_cmixlev: str = None,

    loro_surmixlev: str = None,

    dsurex_mode: str = None,

    dheadphone_mode: str = None,

    ad_conv_type: str = None,

    stereo_rematrixing: str = None,

    channel_coupling: str = None,

    cpl_start_band: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

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
    return FFMpegEncoderOption(kwargs=merge({

    }))



def adpcm_argo(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM Argonaut Games

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def g722(

) -> FFMpegEncoderOption:
    """
    G.722 ADPCM (codec adpcm_g722)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def g726(

    code_size: str = None,

) -> FFMpegEncoderOption:
    """
    G.726 ADPCM (codec adpcm_g726)

    Args:
        code_size: Bits per code (from 2 to 5) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "code_size": code_size,

    }))



def g726le(

    code_size: str = None,

) -> FFMpegEncoderOption:
    """
    G.726 little endian ADPCM ("right-justified") (codec adpcm_g726le)

    Args:
        code_size: Bits per code (from 2 to 5) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "code_size": code_size,

    }))



def adpcm_ima_alp(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA High Voltage Software ALP

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_ima_amv(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA AMV

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_ima_apm(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA Ubisoft APM

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_ima_qt(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA QuickTime

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_ima_ssi(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA Simon & Schuster Interactive

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_ima_wav(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA WAV

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_ima_ws(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM IMA Westwood

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_ms(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM Microsoft

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_swf(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM Shockwave Flash

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def adpcm_yamaha(

    block_size: str = None,

) -> FFMpegEncoderOption:
    """
    ADPCM Yamaha

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "block_size": block_size,

    }))



def alac(

    min_prediction_order: str = None,

    max_prediction_order: str = None,

) -> FFMpegEncoderOption:
    """
    ALAC (Apple Lossless Audio Codec)

    Args:
        min_prediction_order: (from 1 to 30) (default 4)
        max_prediction_order: (from 1 to 30) (default 6)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "min_prediction_order": min_prediction_order,

        "max_prediction_order": max_prediction_order,

    }))



def anull(

) -> FFMpegEncoderOption:
    """
    null audio


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def aptx(

) -> FFMpegEncoderOption:
    """
    aptX (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def aptx_hd(

) -> FFMpegEncoderOption:
    """
    aptX HD (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libcodec2(

    mode: str = None,

) -> FFMpegEncoderOption:
    """
    codec2 encoder using libcodec2 (codec codec2)

    Args:
        mode: codec2 mode (from 0 to 8) (default 1300)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "mode": mode,

    }))



def comfortnoise(

) -> FFMpegEncoderOption:
    """
    RFC 3389 comfort noise generator


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def dfpwm(

) -> FFMpegEncoderOption:
    """
    DFPWM1a audio


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def dca(

    dca_adpcm: str = None,

) -> FFMpegEncoderOption:
    """
    DCA (DTS Coherent Acoustics) (codec dts)

    Args:
        dca_adpcm: Use ADPCM encoding (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "dca_adpcm": dca_adpcm,

    }))



def eac3(

    mixing_level: str = None,

    room_type: str = None,

    per_frame_metadata: str = None,

    copyright: str = None,

    dialnorm: str = None,

    dsur_mode: str = None,

    original: str = None,

    dmix_mode: str = None,

    ltrt_cmixlev: str = None,

    ltrt_surmixlev: str = None,

    loro_cmixlev: str = None,

    loro_surmixlev: str = None,

    dsurex_mode: str = None,

    dheadphone_mode: str = None,

    ad_conv_type: str = None,

    stereo_rematrixing: str = None,

    channel_coupling: str = None,

    cpl_start_band: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

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

    lpc_coeff_precision: str = None,

    lpc_type: str = None,

    lpc_passes: str = None,

    min_partition_order: str = None,

    max_partition_order: str = None,

    prediction_order_method: str = None,

    ch_mode: str = None,

    exact_rice_parameters: str = None,

    multi_dim_quant: str = None,

    min_prediction_order: str = None,

    max_prediction_order: str = None,

) -> FFMpegEncoderOption:
    """
    FLAC (Free Lossless Audio Codec)

    Args:
        lpc_coeff_precision: LPC coefficient precision (from 0 to 15) (default 15)
        lpc_type: LPC algorithm (from -1 to 3) (default -1)
        lpc_passes: Number of passes to use for Cholesky factorization during LPC analysis (from 1 to INT_MAX) (default 2)
        min_partition_order: (from -1 to 8) (default -1)
        max_partition_order: (from -1 to 8) (default -1)
        prediction_order_method: Search method for selecting prediction order (from -1 to 5) (default -1)
        ch_mode: Stereo decorrelation mode (from -1 to 3) (default auto)
        exact_rice_parameters: Calculate rice parameters exactly (default false)
        multi_dim_quant: Multi-dimensional quantization (default false)
        min_prediction_order: (from -1 to 32) (default -1)
        max_prediction_order: (from -1 to 32) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "lpc_coeff_precision": lpc_coeff_precision,

        "lpc_type": lpc_type,

        "lpc_passes": lpc_passes,

        "min_partition_order": min_partition_order,

        "max_partition_order": max_partition_order,

        "prediction_order_method": prediction_order_method,

        "ch_mode": ch_mode,

        "exact_rice_parameters": exact_rice_parameters,

        "multi_dim_quant": multi_dim_quant,

        "min_prediction_order": min_prediction_order,

        "max_prediction_order": max_prediction_order,

    }))



def g723_1(

) -> FFMpegEncoderOption:
    """
    G.723.1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libgsm(

) -> FFMpegEncoderOption:
    """
    libgsm GSM (codec gsm)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libgsm_ms(

) -> FFMpegEncoderOption:
    """
    libgsm GSM Microsoft variant (codec gsm_ms)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def mlp(

    max_interval: str = None,

    lpc_coeff_precision: str = None,

    lpc_type: str = None,

    lpc_passes: str = None,

    codebook_search: str = None,

    prediction_order: str = None,

    rematrix_precision: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

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
    return FFMpegEncoderOption(kwargs=merge({

    }))



def mp2fixed(

) -> FFMpegEncoderOption:
    """
    MP2 fixed point (MPEG audio layer 2) (codec mp2)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libtwolame(

    mode: str = None,

    psymodel: str = None,

    energy_levels: str = None,

    error_protection: str = None,

    copyright: str = None,

    original: str = None,

    verbosity: str = None,

) -> FFMpegEncoderOption:
    """
    libtwolame MP2 (MPEG audio layer 2) (codec mp2)

    Args:
        mode: Mpeg Mode (from -1 to 3) (default auto)
        psymodel: Psychoacoustic Model (from -1 to 4) (default 3)
        energy_levels: enable energy levels (from 0 to 1) (default 0)
        error_protection: enable CRC error protection (from 0 to 1) (default 0)
        copyright: set MPEG Audio Copyright flag (from 0 to 1) (default 0)
        original: set MPEG Audio Original flag (from 0 to 1) (default 0)
        verbosity: set library optput level (0-10) (from 0 to 10) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "mode": mode,

        "psymodel": psymodel,

        "energy_levels": energy_levels,

        "error_protection": error_protection,

        "copyright": copyright,

        "original": original,

        "verbosity": verbosity,

    }))



def libmp3lame(

    reservoir: str = None,

    joint_stereo: str = None,

    abr: str = None,

    copyright: str = None,

    original: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

        "reservoir": reservoir,

        "joint_stereo": joint_stereo,

        "abr": abr,

        "copyright": copyright,

        "original": original,

    }))



def libshine(

) -> FFMpegEncoderOption:
    """
    libshine MP3 (MPEG audio layer 3) (codec mp3)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def nellymoser(

) -> FFMpegEncoderOption:
    """
    Nellymoser Asao


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def opus(

    opus_delay: str = None,

    apply_phase_inv: str = None,

) -> FFMpegEncoderOption:
    """
    Opus

    Args:
        opus_delay: Maximum delay in milliseconds (from 2.5 to 360) (default 360)
        apply_phase_inv: Apply intensity stereo phase inversion (default true)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "opus_delay": opus_delay,

        "apply_phase_inv": apply_phase_inv,

    }))



def libopus(

    application: str = None,

    frame_duration: str = None,

    packet_loss: str = None,

    fec: str = None,

    vbr: str = None,

    mapping_family: str = None,

    apply_phase_inv: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

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
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_bluray(

) -> FFMpegEncoderOption:
    """
    PCM signed 16|20|24-bit big-endian for Blu-ray media


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_dvd(

) -> FFMpegEncoderOption:
    """
    PCM signed 16|20|24-bit big-endian for DVD media


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_f32be(

) -> FFMpegEncoderOption:
    """
    PCM 32-bit floating point big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_f32le(

) -> FFMpegEncoderOption:
    """
    PCM 32-bit floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_f64be(

) -> FFMpegEncoderOption:
    """
    PCM 64-bit floating point big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_f64le(

) -> FFMpegEncoderOption:
    """
    PCM 64-bit floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_mulaw(

) -> FFMpegEncoderOption:
    """
    PCM mu-law / G.711 mu-law


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s16be(

) -> FFMpegEncoderOption:
    """
    PCM signed 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s16be_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 16-bit big-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s16le(

) -> FFMpegEncoderOption:
    """
    PCM signed 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s16le_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 16-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s24be(

) -> FFMpegEncoderOption:
    """
    PCM signed 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s24daud(

) -> FFMpegEncoderOption:
    """
    PCM D-Cinema audio signed 24-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s24le(

) -> FFMpegEncoderOption:
    """
    PCM signed 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s24le_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 24-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s32be(

) -> FFMpegEncoderOption:
    """
    PCM signed 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s32le(

) -> FFMpegEncoderOption:
    """
    PCM signed 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s32le_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 32-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s64be(

) -> FFMpegEncoderOption:
    """
    PCM signed 64-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s64le(

) -> FFMpegEncoderOption:
    """
    PCM signed 64-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s8(

) -> FFMpegEncoderOption:
    """
    PCM signed 8-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_s8_planar(

) -> FFMpegEncoderOption:
    """
    PCM signed 8-bit planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_u16be(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_u16le(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_u24be(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_u24le(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_u32be(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_u32le(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_u8(

) -> FFMpegEncoderOption:
    """
    PCM unsigned 8-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def pcm_vidc(

) -> FFMpegEncoderOption:
    """
    PCM Archimedes VIDC


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def real_144(

) -> FFMpegEncoderOption:
    """
    RealAudio 1.0 (14.4K) (codec ra_144)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def roq_dpcm(

) -> FFMpegEncoderOption:
    """
    id RoQ DPCM


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def s302m(

) -> FFMpegEncoderOption:
    """
    SMPTE 302M


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def sbc(

    sbc_delay: str = None,

    msbc: str = None,

) -> FFMpegEncoderOption:
    """
    SBC (low-complexity subband codec)

    Args:
        sbc_delay: set maximum algorithmic latency (default 0.013)
        msbc: use mSBC mode (wideband speech mono SBC) (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "sbc_delay": sbc_delay,

        "msbc": msbc,

    }))



def sonic(

) -> FFMpegEncoderOption:
    """
    Sonic


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def sonicls(

) -> FFMpegEncoderOption:
    """
    Sonic lossless


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libspeex(

    abr: str = None,

    cbr_quality: str = None,

    frames_per_packet: str = None,

    vad: str = None,

    dtx: str = None,

) -> FFMpegEncoderOption:
    """
    libspeex Speex (codec speex)

    Args:
        abr: Use average bit rate (from 0 to 1) (default 0)
        cbr_quality: Set quality value (0 to 10) for CBR (from 0 to 10) (default 8)
        frames_per_packet: Number of frames to encode in each packet (from 1 to 8) (default 1)
        vad: Voice Activity Detection (from 0 to 1) (default 0)
        dtx: Discontinuous Transmission (from 0 to 1) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "abr": abr,

        "cbr_quality": cbr_quality,

        "frames_per_packet": frames_per_packet,

        "vad": vad,

        "dtx": dtx,

    }))



def truehd(

    max_interval: str = None,

    lpc_coeff_precision: str = None,

    lpc_type: str = None,

    lpc_passes: str = None,

    codebook_search: str = None,

    prediction_order: str = None,

    rematrix_precision: str = None,

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
    return FFMpegEncoderOption(kwargs=merge({

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
    return FFMpegEncoderOption(kwargs=merge({

    }))



def vorbis(

) -> FFMpegEncoderOption:
    """
    Vorbis


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def libvorbis(

    iblock: str = None,

) -> FFMpegEncoderOption:
    """
    libvorbis (codec vorbis)

    Args:
        iblock: Sets the impulse block bias (from -15 to 0) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "iblock": iblock,

    }))



def wavpack(

    joint_stereo: str = None,

    optimize_mono: str = None,

) -> FFMpegEncoderOption:
    """
    WavPack

    Args:
        joint_stereo: (default auto)
        optimize_mono: (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

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
    return FFMpegEncoderOption(kwargs=merge({

    }))



def wmav2(

) -> FFMpegEncoderOption:
    """
    Windows Media Audio 2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def ssa(

) -> FFMpegEncoderOption:
    """
    ASS (Advanced SubStation Alpha) subtitle (codec ass)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def ass(

) -> FFMpegEncoderOption:
    """
    ASS (Advanced SubStation Alpha) subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def dvbsub(

) -> FFMpegEncoderOption:
    """
    DVB subtitles (codec dvb_subtitle)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def dvdsub(

    palette: str = None,

    even_rows_fix: str = None,

) -> FFMpegEncoderOption:
    """
    DVD subtitles (codec dvd_subtitle)

    Args:
        palette: set the global palette
        even_rows_fix: Make number of rows even (workaround for some players) (default false)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "palette": palette,

        "even_rows_fix": even_rows_fix,

    }))



def mov_text(

    height: str = None,

) -> FFMpegEncoderOption:
    """
    3GPP Timed Text subtitle

    Args:
        height: Frame height, usually video height (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

        "height": height,

    }))



def srt(

) -> FFMpegEncoderOption:
    """
    SubRip subtitle (codec subrip)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def subrip(

) -> FFMpegEncoderOption:
    """
    SubRip subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def text(

) -> FFMpegEncoderOption:
    """
    Raw text subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def ttml(

) -> FFMpegEncoderOption:
    """
    TTML subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def webvtt(

) -> FFMpegEncoderOption:
    """
    WebVTT subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))



def xsub(

) -> FFMpegEncoderOption:
    """
    DivX subtitles (XSUB)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=merge({

    }))
