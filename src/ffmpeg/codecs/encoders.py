# NOTE: this file is auto-generated, do not modify
from ..utils.frozendict import FrozenDict
from .schema import FFMpegEncoderOption


def a64multi() -> FFMpegEncoderOption:
    """
    Multicolor charset for Commodore 64 (codec a64_multi)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def a64multi5() -> FFMpegEncoderOption:
    """
    Multicolor charset for Commodore 64, extended with 5th color (colram) (codec a64_multi5)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def alias_pix() -> FFMpegEncoderOption:
    """
    Alias/Wavefront PIX image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    huffman: int | None = None,
    force_duplicated_matrix: bool | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def apng() -> FFMpegEncoderOption:
    """
    APNG (Animated Portable Network Graphics) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def asv1() -> FFMpegEncoderOption:
    """
    ASUS V1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def asv2() -> FFMpegEncoderOption:
    """
    ASUS V2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def librav1e(
    qp: int | None = None,
    speed: int | None = None,
    tiles: int | None = None,
    tile_rows: int | None = None,
    tile_columns: int | None = None,
    rav1e_params: str | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libsvtav1(
    hielevel: int | None = None,
    la_depth: int | None = None,
    tier: int | None = None,
    preset: int | None = None,
    crf: int | None = None,
    qp: int | None = None,
    sc_detection: bool | None = None,
    tile_columns: int | None = None,
    tile_rows: int | None = None,
    svtav1_params: str | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def av1_nvenc(
    preset: int | None = None,
    tune: int | None = None,
    level: int | None = None,
    tier: int | None = None,
    rc: int | None = None,
    multipass: int | None = None,
    highbitdepth: bool | None = None,
    tile_rows: int | None = None,
    tile_columns: int | None = None,
    surfaces: int | None = None,
    gpu: int | None = None,
    rgb_mode: int | None = None,
    delay: int | None = None,
    rc_lookahead: int | None = None,
    cq: float | None = None,
    init_qpP: int | None = None,
    init_qpB: int | None = None,
    init_qpI: int | None = None,
    qp: int | None = None,
    qp_cb_offset: int | None = None,
    qp_cr_offset: int | None = None,
    no_scenecut: bool | None = None,
    forced_idr: bool | None = None,
    b_adapt: bool | None = None,
    spatial_aq: bool | None = None,
    temporal_aq: bool | None = None,
    zerolatency: bool | None = None,
    nonref_p: bool | None = None,
    strict_gop: bool | None = None,
    aq_strength: int | None = None,
    weighted_pred: bool | None = None,
    b_ref_mode: int | None = None,
    dpb_size: int | None = None,
    ldkfs: int | None = None,
    intra_refresh: bool | None = None,
    timing_info: bool | None = None,
    extra_sei: bool | None = None,
    a53cc: bool | None = None,
    s12m_tc: bool | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def av1_vaapi(
    low_power: bool | None = None,
    idr_interval: int | None = None,
    b_depth: int | None = None,
    async_depth: int | None = None,
    max_frame_size: int | None = None,
    rc_mode: int | None = None,
    profile: int | None = None,
    tier: int | None = None,
    level: int | None = None,
    tiles: str | None = None,
    tile_groups: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def avrp() -> FFMpegEncoderOption:
    """
    Avid 1:1 10-bit RGB Packer


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def avui() -> FFMpegEncoderOption:
    """
    Avid Meridien Uncompressed


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ayuv() -> FFMpegEncoderOption:
    """
    Uncompressed packed MS 4:4:4:4


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def bitpacked() -> FFMpegEncoderOption:
    """
    Bitpacked


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def bmp() -> FFMpegEncoderOption:
    """
    BMP (Windows and OS/2 bitmap)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def cfhd(
    quality: int | None = None,
) -> FFMpegEncoderOption:
    """
    GoPro CineForm HD

    Args:
        quality: set quality (from 0 to 12) (default film3+)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def vc2() -> FFMpegEncoderOption:
    """
    SMPTE VC-2 (codec dirac)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def dnxhd(
    nitris_compat: bool | None = None,
    ibias: int | None = None,
    profile: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def dpx() -> FFMpegEncoderOption:
    """
    DPX (Digital Picture Exchange) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def exr(
    compression: int | None = None,
    format: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ffv1(
    slicecrc: bool | None = None,
    coder: int | None = None,
    context: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ffvhuff(
    non_deterministic: bool | None = None,
    pred: int | None = None,
    context: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def fits() -> FFMpegEncoderOption:
    """
    Flexible Image Transport System


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def flashsv() -> FFMpegEncoderOption:
    """
    Flash Screen Video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def flashsv2() -> FFMpegEncoderOption:
    """
    Flash Screen Video Version 2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def h263_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem H.263 encoder wrapper (codec h263)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    aq_mode: int | None = None,
    aq_strength: float | None = None,
    psy: bool | None = None,
    psy_rd: str | None = None,
    rc_lookahead: int | None = None,
    weightb: bool | None = None,
    weightp: int | None = None,
    ssim: bool | None = None,
    intra_refresh: bool | None = None,
    bluray_compat: bool | None = None,
    b_bias: int | None = None,
    b_pyramid: int | None = None,
    mixed_refs: bool | None = None,
    _8x8dct: bool | None = None,
    fast_pskip: bool | None = None,
    aud: bool | None = None,
    mbtree: bool | None = None,
    deblock: str | None = None,
    cplxblur: float | None = None,
    partitions: str | None = None,
    direct_pred: int | None = None,
    slice_max_size: int | None = None,
    stats: str | None = None,
    nal_hrd: int | None = None,
    avcintra_class: int | None = None,
    me_method: int | None = None,
    motion_est: int | None = None,
    forced_idr: bool | None = None,
    coder: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    aq_mode: int | None = None,
    aq_strength: float | None = None,
    psy: bool | None = None,
    psy_rd: str | None = None,
    rc_lookahead: int | None = None,
    weightb: bool | None = None,
    weightp: int | None = None,
    ssim: bool | None = None,
    intra_refresh: bool | None = None,
    bluray_compat: bool | None = None,
    b_bias: int | None = None,
    b_pyramid: int | None = None,
    mixed_refs: bool | None = None,
    _8x8dct: bool | None = None,
    fast_pskip: bool | None = None,
    aud: bool | None = None,
    mbtree: bool | None = None,
    deblock: str | None = None,
    cplxblur: float | None = None,
    partitions: str | None = None,
    direct_pred: int | None = None,
    slice_max_size: int | None = None,
    stats: str | None = None,
    nal_hrd: int | None = None,
    avcintra_class: int | None = None,
    me_method: int | None = None,
    motion_est: int | None = None,
    forced_idr: bool | None = None,
    coder: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def h264_nvenc(
    preset: int | None = None,
    tune: int | None = None,
    profile: int | None = None,
    level: int | None = None,
    rc: int | None = None,
    rc_lookahead: int | None = None,
    surfaces: int | None = None,
    cbr: bool | None = None,
    _2pass: bool | None = None,
    gpu: int | None = None,
    rgb_mode: int | None = None,
    delay: int | None = None,
    no_scenecut: bool | None = None,
    forced_idr: bool | None = None,
    b_adapt: bool | None = None,
    spatial_aq: bool | None = None,
    temporal_aq: bool | None = None,
    zerolatency: bool | None = None,
    nonref_p: bool | None = None,
    strict_gop: bool | None = None,
    aq_strength: int | None = None,
    cq: float | None = None,
    aud: bool | None = None,
    bluray_compat: bool | None = None,
    init_qpP: int | None = None,
    init_qpB: int | None = None,
    init_qpI: int | None = None,
    qp: int | None = None,
    qp_cb_offset: int | None = None,
    qp_cr_offset: int | None = None,
    weighted_pred: int | None = None,
    coder: int | None = None,
    b_ref_mode: int | None = None,
    a53cc: bool | None = None,
    dpb_size: int | None = None,
    multipass: int | None = None,
    ldkfs: int | None = None,
    extra_sei: bool | None = None,
    udu_sei: bool | None = None,
    intra_refresh: bool | None = None,
    single_slice_intra_refresh: bool | None = None,
    max_slice_size: int | None = None,
    constrained_encoding: bool | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def h264_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem H.264 encoder wrapper (codec h264)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def h264_vaapi(
    low_power: bool | None = None,
    idr_interval: int | None = None,
    b_depth: int | None = None,
    async_depth: int | None = None,
    max_frame_size: int | None = None,
    rc_mode: int | None = None,
    qp: int | None = None,
    quality: int | None = None,
    coder: int | None = None,
    aud: bool | None = None,
    sei: str | None = None,
    profile: int | None = None,
    level: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def hap(
    format: int | None = None,
    chunks: int | None = None,
    compressor: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def hdr() -> FFMpegEncoderOption:
    """
    HDR (Radiance RGBE format) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libx265(
    crf: float | None = None,
    qp: int | None = None,
    forced_idr: bool | None = None,
    preset: str | None = None,
    tune: str | None = None,
    profile: str | None = None,
    udu_sei: bool | None = None,
    a53cc: bool | None = None,
    x265_params: str | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def hevc_nvenc(
    preset: int | None = None,
    tune: int | None = None,
    profile: int | None = None,
    level: int | None = None,
    tier: int | None = None,
    rc: int | None = None,
    rc_lookahead: int | None = None,
    surfaces: int | None = None,
    cbr: bool | None = None,
    _2pass: bool | None = None,
    gpu: int | None = None,
    rgb_mode: int | None = None,
    delay: int | None = None,
    no_scenecut: bool | None = None,
    forced_idr: bool | None = None,
    spatial_aq: bool | None = None,
    temporal_aq: bool | None = None,
    zerolatency: bool | None = None,
    nonref_p: bool | None = None,
    strict_gop: bool | None = None,
    aq_strength: int | None = None,
    cq: float | None = None,
    aud: bool | None = None,
    bluray_compat: bool | None = None,
    init_qpP: int | None = None,
    init_qpB: int | None = None,
    init_qpI: int | None = None,
    qp: int | None = None,
    qp_cb_offset: int | None = None,
    qp_cr_offset: int | None = None,
    weighted_pred: int | None = None,
    b_ref_mode: int | None = None,
    a53cc: bool | None = None,
    s12m_tc: bool | None = None,
    dpb_size: int | None = None,
    multipass: int | None = None,
    ldkfs: int | None = None,
    extra_sei: bool | None = None,
    udu_sei: bool | None = None,
    intra_refresh: bool | None = None,
    single_slice_intra_refresh: bool | None = None,
    max_slice_size: int | None = None,
    constrained_encoding: bool | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def hevc_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem HEVC encoder wrapper (codec hevc)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def hevc_vaapi(
    low_power: bool | None = None,
    idr_interval: int | None = None,
    b_depth: int | None = None,
    async_depth: int | None = None,
    max_frame_size: int | None = None,
    rc_mode: int | None = None,
    qp: int | None = None,
    aud: bool | None = None,
    profile: int | None = None,
    tier: int | None = None,
    level: int | None = None,
    sei: str | None = None,
    tiles: str | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def huffyuv(
    non_deterministic: bool | None = None,
    pred: int | None = None,
) -> FFMpegEncoderOption:
    """
    Huffyuv / HuffYUV

    Args:
        non_deterministic: Allow multithreading for e.g. context=1 at the expense of determinism (default false)
        pred: Prediction method (from 0 to 2) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def jpeg2000(
    format: int | None = None,
    tile_width: int | None = None,
    tile_height: int | None = None,
    pred: int | None = None,
    sop: int | None = None,
    eph: int | None = None,
    prog: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libopenjpeg(
    format: int | None = None,
    profile: int | None = None,
    cinema_mode: int | None = None,
    prog_order: int | None = None,
    numresolution: int | None = None,
    irreversible: int | None = None,
    disto_alloc: int | None = None,
    fixed_quality: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def jpegls(
    pred: int | None = None,
) -> FFMpegEncoderOption:
    """
    JPEG-LS

    Args:
        pred: Prediction method (from 0 to 2) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libjxl(
    effort: int | None = None,
    distance: float | None = None,
    modular: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ljpeg(
    pred: int | None = None,
) -> FFMpegEncoderOption:
    """
    Lossless JPEG

    Args:
        pred: Prediction method (from 1 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def magicyuv(
    pred: int | None = None,
) -> FFMpegEncoderOption:
    """
    MagicYUV video

    Args:
        pred: Prediction method (from 1 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def mjpeg(
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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    huffman: int | None = None,
    force_duplicated_matrix: bool | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def mjpeg_vaapi(
    low_power: bool | None = None,
    idr_interval: int | None = None,
    b_depth: int | None = None,
    async_depth: int | None = None,
    max_frame_size: int | None = None,
    jfif: bool | None = None,
    huffman: bool | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def mpeg2video(
    gop_timecode: str | None = None,
    drop_frame_timecode: bool | None = None,
    scan_offset: bool | None = None,
    timecode_frame_start: int | None = None,
    b_strategy: int | None = None,
    b_sensitivity: int | None = None,
    brd_scale: int | None = None,
    intra_vlc: bool | None = None,
    non_linear_quant: bool | None = None,
    alternate_scan: bool | None = None,
    a53cc: bool | None = None,
    seq_disp_ext: int | None = None,
    video_format: int | None = None,
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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def mpeg2_vaapi(
    low_power: bool | None = None,
    idr_interval: int | None = None,
    b_depth: int | None = None,
    async_depth: int | None = None,
    max_frame_size: int | None = None,
    rc_mode: int | None = None,
    profile: int | None = None,
    level: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libxvid(
    lumi_aq: int | None = None,
    variance_aq: int | None = None,
    ssim: int | None = None,
    ssim_acc: int | None = None,
    gmc: int | None = None,
    me_quality: int | None = None,
    mpeg_quant: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def mpeg4_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem MPEG4 encoder wrapper (codec mpeg4)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def msrle() -> FFMpegEncoderOption:
    """
    Microsoft RLE


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def msvideo1() -> FFMpegEncoderOption:
    """
    Microsoft Video-1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pam() -> FFMpegEncoderOption:
    """
    PAM (Portable AnyMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pbm() -> FFMpegEncoderOption:
    """
    PBM (Portable BitMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcx() -> FFMpegEncoderOption:
    """
    PC Paintbrush PCX image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pfm() -> FFMpegEncoderOption:
    """
    PFM (Portable FloatMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pgm() -> FFMpegEncoderOption:
    """
    PGM (Portable GrayMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pgmyuv() -> FFMpegEncoderOption:
    """
    PGMYUV (Portable GrayMap YUV) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def phm() -> FFMpegEncoderOption:
    """
    PHM (Portable HalfFloatMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def png() -> FFMpegEncoderOption:
    """
    PNG (Portable Network Graphics) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ppm() -> FFMpegEncoderOption:
    """
    PPM (Portable PixelMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def prores_ks(
    mbs_per_slice: int | None = None,
    profile: int | None = None,
    vendor: str | None = None,
    bits_per_mb: int | None = None,
    quant_mat: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def qoi() -> FFMpegEncoderOption:
    """
    QOI (Quite OK Image format) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def qtrle() -> FFMpegEncoderOption:
    """
    QuickTime Animation (RLE) video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def r10k() -> FFMpegEncoderOption:
    """
    AJA Kona 10-bit RGB Codec


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def r210() -> FFMpegEncoderOption:
    """
    Uncompressed RGB 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def rawvideo() -> FFMpegEncoderOption:
    """
    raw video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def rpza(
    skip_frame_thresh: int | None = None,
    start_one_color_thresh: int | None = None,
    continue_one_color_thresh: int | None = None,
    sixteen_color_thresh: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def smc() -> FFMpegEncoderOption:
    """
    QuickTime Graphics (SMC)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def snow(
    motion_est: int | None = None,
    memc_only: bool | None = None,
    no_bitstream: bool | None = None,
    intra_penalty: int | None = None,
    iterative_dia_size: int | None = None,
    sc_threshold: int | None = None,
    pred: int | None = None,
    rc_eq: str | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def svq1(
    motion_est: int | None = None,
) -> FFMpegEncoderOption:
    """
    Sorenson Vector Quantizer 1 / Sorenson Video 1 / SVQ1

    Args:
        motion_est: Motion estimation algorithm (from 0 to 2) (default epzs)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libtheora() -> FFMpegEncoderOption:
    """
    libtheora Theora (codec theora)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def tiff(
    dpi: int | None = None,
    compression_algo: int | None = None,
) -> FFMpegEncoderOption:
    """
    TIFF image

    Args:
        dpi: set the image resolution (in dpi) (from 1 to 65536) (default 72)
        compression_algo: (from 1 to 32946) (default packbits)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def utvideo(
    pred: int | None = None,
) -> FFMpegEncoderOption:
    """
    Ut Video

    Args:
        pred: Prediction method (from 0 to 3) (default left)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def v210() -> FFMpegEncoderOption:
    """
    Uncompressed 4:2:2 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def v308() -> FFMpegEncoderOption:
    """
    Uncompressed packed 4:4:4


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def v408() -> FFMpegEncoderOption:
    """
    Uncompressed packed QT 4:4:4:4


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def v410() -> FFMpegEncoderOption:
    """
    Uncompressed 4:4:4 10-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def vbn(
    format: int | None = None,
) -> FFMpegEncoderOption:
    """
    Vizrt Binary Image

    Args:
        format: Texture format (from 0 to 3) (default dxt5)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def vnull() -> FFMpegEncoderOption:
    """
    null video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libvpx() -> FFMpegEncoderOption:
    """
    libvpx VP8 (codec vp8)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def vp8_v4l2m2m(
    num_output_buffers: int | None = None,
    num_capture_buffers: int | None = None,
) -> FFMpegEncoderOption:
    """
    V4L2 mem2mem VP8 encoder wrapper (codec vp8)

    Args:
        num_output_buffers: Number of buffers in the output context (from 2 to INT_MAX) (default 16)
        num_capture_buffers: Number of buffers in the capture context (from 4 to INT_MAX) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def vp8_vaapi(
    low_power: bool | None = None,
    idr_interval: int | None = None,
    b_depth: int | None = None,
    async_depth: int | None = None,
    max_frame_size: int | None = None,
    rc_mode: int | None = None,
    loop_filter_level: int | None = None,
    loop_filter_sharpness: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def vp9_vaapi(
    low_power: bool | None = None,
    idr_interval: int | None = None,
    b_depth: int | None = None,
    async_depth: int | None = None,
    max_frame_size: int | None = None,
    rc_mode: int | None = None,
    loop_filter_level: int | None = None,
    loop_filter_sharpness: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def wbmp() -> FFMpegEncoderOption:
    """
    WBMP (Wireless Application Protocol Bitmap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libwebp_anim(
    lossless: int | None = None,
    preset: int | None = None,
    cr_threshold: int | None = None,
    cr_size: int | None = None,
    quality: float | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libwebp(
    lossless: int | None = None,
    preset: int | None = None,
    cr_threshold: int | None = None,
    cr_size: int | None = None,
    quality: float | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    skip_cmp: int | None = None,
    sc_threshold: int | None = None,
    noise_reduction: int | None = None,
    ps: int | None = None,
    motion_est: int | None = None,
    mepc: int | None = None,
    mepre: int | None = None,
    intra_penalty: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def wrapped_avframe() -> FFMpegEncoderOption:
    """
    AVFrame to AVPacket passthrough


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def xbm() -> FFMpegEncoderOption:
    """
    XBM (X BitMap) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def xface() -> FFMpegEncoderOption:
    """
    X-face image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def xwd() -> FFMpegEncoderOption:
    """
    XWD (X Window Dump) image


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def y41p() -> FFMpegEncoderOption:
    """
    Uncompressed YUV 4:1:1 12-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def yuv4() -> FFMpegEncoderOption:
    """
    Uncompressed packed 4:2:0


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def zlib() -> FFMpegEncoderOption:
    """
    LCL (LossLess Codec Library) ZLIB


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def zmbv() -> FFMpegEncoderOption:
    """
    Zip Motion Blocks Video


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def aac(
    aac_coder: int | None = None,
    aac_ms: bool | None = None,
    aac_is: bool | None = None,
    aac_pns: bool | None = None,
    aac_tns: bool | None = None,
    aac_ltp: bool | None = None,
    aac_pred: bool | None = None,
    aac_pce: bool | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ac3() -> FFMpegEncoderOption:
    """
    ATSC A/52A (AC-3)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ac3_fixed() -> FFMpegEncoderOption:
    """
    ATSC A/52A (AC-3) (codec ac3)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def adpcm_adx() -> FFMpegEncoderOption:
    """
    SEGA CRI ADX ADPCM


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def adpcm_argo(
    block_size: int | None = None,
) -> FFMpegEncoderOption:
    """
    ADPCM Argonaut Games

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def g722() -> FFMpegEncoderOption:
    """
    G.722 ADPCM (codec adpcm_g722)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def adpcm_ima_qt(
    block_size: int | None = None,
) -> FFMpegEncoderOption:
    """
    ADPCM IMA QuickTime

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def adpcm_swf(
    block_size: int | None = None,
) -> FFMpegEncoderOption:
    """
    ADPCM Shockwave Flash

    Args:
        block_size: set the block size (from 32 to 8192) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def anull() -> FFMpegEncoderOption:
    """
    null audio


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def aptx() -> FFMpegEncoderOption:
    """
    aptX (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def aptx_hd() -> FFMpegEncoderOption:
    """
    aptX HD (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libcodec2(
    mode: int | None = None,
) -> FFMpegEncoderOption:
    """
    codec2 encoder using libcodec2 (codec codec2)

    Args:
        mode: codec2 mode (from 0 to 8) (default 1300)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def comfortnoise() -> FFMpegEncoderOption:
    """
    RFC 3389 comfort noise generator


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def dfpwm() -> FFMpegEncoderOption:
    """
    DFPWM1a audio


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def dca() -> FFMpegEncoderOption:
    """
    DCA (DTS Coherent Acoustics) (codec dts)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def eac3() -> FFMpegEncoderOption:
    """
    ATSC A/52 E-AC-3


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def flac(
    lpc_coeff_precision: int | None = None,
    lpc_type: int | None = None,
    lpc_passes: int | None = None,
    min_partition_order: int | None = None,
    max_partition_order: int | None = None,
    prediction_order_method: int | None = None,
    ch_mode: int | None = None,
    exact_rice_parameters: bool | None = None,
    multi_dim_quant: bool | None = None,
    min_prediction_order: int | None = None,
    max_prediction_order: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def g723_1() -> FFMpegEncoderOption:
    """
    G.723.1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libgsm() -> FFMpegEncoderOption:
    """
    libgsm GSM (codec gsm)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libgsm_ms() -> FFMpegEncoderOption:
    """
    libgsm GSM Microsoft variant (codec gsm_ms)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def mlp(
    max_interval: int | None = None,
    lpc_coeff_precision: int | None = None,
    lpc_type: int | None = None,
    lpc_passes: int | None = None,
    codebook_search: int | None = None,
    prediction_order: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def mp2() -> FFMpegEncoderOption:
    """
    MP2 (MPEG audio layer 2)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def mp2fixed() -> FFMpegEncoderOption:
    """
    MP2 fixed point (MPEG audio layer 2) (codec mp2)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libtwolame(
    mode: int | None = None,
    psymodel: int | None = None,
    energy_levels: int | None = None,
    error_protection: int | None = None,
    copyright: int | None = None,
    original: int | None = None,
    verbosity: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libshine() -> FFMpegEncoderOption:
    """
    libshine MP3 (MPEG audio layer 3) (codec mp3)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def nellymoser() -> FFMpegEncoderOption:
    """
    Nellymoser Asao


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libopus(
    application: int | None = None,
    frame_duration: float | None = None,
    packet_loss: int | None = None,
    fec: bool | None = None,
    vbr: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_alaw() -> FFMpegEncoderOption:
    """
    PCM A-law / G.711 A-law


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_bluray() -> FFMpegEncoderOption:
    """
    PCM signed 16|20|24-bit big-endian for Blu-ray media


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_dvd() -> FFMpegEncoderOption:
    """
    PCM signed 16|20|24-bit big-endian for DVD media


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_f32be() -> FFMpegEncoderOption:
    """
    PCM 32-bit floating point big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_f32le() -> FFMpegEncoderOption:
    """
    PCM 32-bit floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_f64be() -> FFMpegEncoderOption:
    """
    PCM 64-bit floating point big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_f64le() -> FFMpegEncoderOption:
    """
    PCM 64-bit floating point little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_mulaw() -> FFMpegEncoderOption:
    """
    PCM mu-law / G.711 mu-law


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s16be() -> FFMpegEncoderOption:
    """
    PCM signed 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s16be_planar() -> FFMpegEncoderOption:
    """
    PCM signed 16-bit big-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s16le() -> FFMpegEncoderOption:
    """
    PCM signed 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s16le_planar() -> FFMpegEncoderOption:
    """
    PCM signed 16-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s24be() -> FFMpegEncoderOption:
    """
    PCM signed 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s24daud() -> FFMpegEncoderOption:
    """
    PCM D-Cinema audio signed 24-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s24le() -> FFMpegEncoderOption:
    """
    PCM signed 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s24le_planar() -> FFMpegEncoderOption:
    """
    PCM signed 24-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s32be() -> FFMpegEncoderOption:
    """
    PCM signed 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s32le() -> FFMpegEncoderOption:
    """
    PCM signed 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s32le_planar() -> FFMpegEncoderOption:
    """
    PCM signed 32-bit little-endian planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s64be() -> FFMpegEncoderOption:
    """
    PCM signed 64-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s64le() -> FFMpegEncoderOption:
    """
    PCM signed 64-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s8() -> FFMpegEncoderOption:
    """
    PCM signed 8-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_s8_planar() -> FFMpegEncoderOption:
    """
    PCM signed 8-bit planar


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_u16be() -> FFMpegEncoderOption:
    """
    PCM unsigned 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_u16le() -> FFMpegEncoderOption:
    """
    PCM unsigned 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_u24be() -> FFMpegEncoderOption:
    """
    PCM unsigned 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_u24le() -> FFMpegEncoderOption:
    """
    PCM unsigned 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_u32be() -> FFMpegEncoderOption:
    """
    PCM unsigned 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_u32le() -> FFMpegEncoderOption:
    """
    PCM unsigned 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_u8() -> FFMpegEncoderOption:
    """
    PCM unsigned 8-bit


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def pcm_vidc() -> FFMpegEncoderOption:
    """
    PCM Archimedes VIDC


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def real_144() -> FFMpegEncoderOption:
    """
    RealAudio 1.0 (14.4K) (codec ra_144)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def roq_dpcm() -> FFMpegEncoderOption:
    """
    id RoQ DPCM


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def s302m() -> FFMpegEncoderOption:
    """
    SMPTE 302M


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def sonic() -> FFMpegEncoderOption:
    """
    Sonic


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def sonicls() -> FFMpegEncoderOption:
    """
    Sonic lossless


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libspeex(
    abr: int | None = None,
    cbr_quality: int | None = None,
    frames_per_packet: int | None = None,
    vad: int | None = None,
    dtx: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def truehd(
    max_interval: int | None = None,
    lpc_coeff_precision: int | None = None,
    lpc_type: int | None = None,
    lpc_passes: int | None = None,
    codebook_search: int | None = None,
    prediction_order: int | None = None,
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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def tta() -> FFMpegEncoderOption:
    """
    TTA (True Audio)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def vorbis() -> FFMpegEncoderOption:
    """
    Vorbis


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def libvorbis(
    iblock: float | None = None,
) -> FFMpegEncoderOption:
    """
    libvorbis (codec vorbis)

    Args:
        iblock: Sets the impulse block bias (from -15 to 0) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def wmav1() -> FFMpegEncoderOption:
    """
    Windows Media Audio 1


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def wmav2() -> FFMpegEncoderOption:
    """
    Windows Media Audio 2


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ssa() -> FFMpegEncoderOption:
    """
    ASS (Advanced SubStation Alpha) subtitle (codec ass)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ass() -> FFMpegEncoderOption:
    """
    ASS (Advanced SubStation Alpha) subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def dvbsub() -> FFMpegEncoderOption:
    """
    DVB subtitles (codec dvb_subtitle)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


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
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def srt() -> FFMpegEncoderOption:
    """
    SubRip subtitle (codec subrip)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def subrip() -> FFMpegEncoderOption:
    """
    SubRip subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def text() -> FFMpegEncoderOption:
    """
    Raw text subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def ttml() -> FFMpegEncoderOption:
    """
    TTML subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def webvtt() -> FFMpegEncoderOption:
    """
    WebVTT subtitle


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))


def xsub() -> FFMpegEncoderOption:
    """
    DivX subtitles (XSUB)


    Returns:
        the set codec options
    """
    return FFMpegEncoderOption(kwargs=FrozenDict(locals()))
