# NOTE: this file is auto-generated, do not modify
from dataclasses import dataclass

from .schema import FFMpegEncoderOption


@dataclass(frozen=True, kw_only=True)
class a64multi(FFMpegEncoderOption):
    """Multicolor charset for Commodore 64 (codec a64_multi)"""


@dataclass(frozen=True, kw_only=True)
class a64multi5(FFMpegEncoderOption):
    """Multicolor charset for Commodore 64, extended with 5th color (colram) (codec a64_multi5)"""


@dataclass(frozen=True, kw_only=True)
class alias_pix(FFMpegEncoderOption):
    """Alias/Wavefront PIX image"""


@dataclass(frozen=True, kw_only=True)
class amv(FFMpegEncoderOption):
    """AMV Video"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    huffman: int | None = None
    """Huffman table strategy (from 0 to 1) (default optimal)"""

    force_duplicated_matrix: bool | None = None
    """Always write luma and chroma matrix for mjpeg, useful for rtp streaming. (default false)"""


@dataclass(frozen=True, kw_only=True)
class apng(FFMpegEncoderOption):
    """APNG (Animated Portable Network Graphics) image"""


@dataclass(frozen=True, kw_only=True)
class asv1(FFMpegEncoderOption):
    """ASUS V1"""


@dataclass(frozen=True, kw_only=True)
class asv2(FFMpegEncoderOption):
    """ASUS V2"""


@dataclass(frozen=True, kw_only=True)
class librav1e(FFMpegEncoderOption):
    """librav1e AV1 (codec av1)"""

    qp: int | None = None
    """use constant quantizer mode (from -1 to 255) (default -1)"""

    speed: int | None = None
    """what speed preset to use (from -1 to 10) (default -1)"""

    tiles: int | None = None
    """number of tiles encode with (from -1 to I64_MAX) (default 0)"""

    tile_rows: int | None = None
    """number of tiles rows to encode with (from -1 to I64_MAX) (default 0)"""

    tile_columns: int | None = None
    """number of tiles columns to encode with (from -1 to I64_MAX) (default 0)"""

    rav1e_params: str | None = None
    """set the rav1e configuration using a :-separated list of key=value parameters"""


@dataclass(frozen=True, kw_only=True)
class libsvtav1(FFMpegEncoderOption):
    """SVT-AV1(Scalable Video Technology for AV1) encoder (codec av1)"""

    hielevel: int | None = None
    """Hierarchical prediction levels setting (Deprecated, use svtav1-params) (from -1 to 4) (default -1)"""

    la_depth: int | None = None
    """Look ahead distance [0, 120] (Deprecated, use svtav1-params) (from -1 to 120) (default -1)"""

    tier: int | None = None
    """Set operating point tier (Deprecated, use svtav1-params) (from -1 to 1) (default -1)"""

    preset: int | None = None
    """Encoding preset (from -2 to 13) (default -2)"""

    crf: int | None = None
    """Constant Rate Factor value (from 0 to 63) (default 0)"""

    qp: int | None = None
    """Initial Quantizer level value (from 0 to 63) (default 0)"""

    sc_detection: bool | None = None
    """Scene change detection (Deprecated, use svtav1-params) (default auto)"""

    tile_columns: int | None = None
    """Log2 of number of tile columns to use (Deprecated, use svtav1-params) (from -1 to 4) (default -1)"""

    tile_rows: int | None = None
    """Log2 of number of tile rows to use (Deprecated, use svtav1-params) (from -1 to 6) (default -1)"""

    svtav1_params: str | None = None
    """Set the SVT-AV1 configuration using a :-separated list of key=value parameters"""


@dataclass(frozen=True, kw_only=True)
class av1_nvenc(FFMpegEncoderOption):
    """NVIDIA NVENC av1 encoder (codec av1)"""

    preset: int | None = None
    """Set the encoding preset (from 0 to 18) (default p4)"""

    tune: int | None = None
    """Set the encoding tuning info (from 1 to 4) (default hq)"""

    level: int | None = None
    """Set the encoding level restriction (from 0 to 24) (default auto)"""

    tier: int | None = None
    """Set the encoding tier (from 0 to 1) (default 0)"""

    rc: int | None = None
    """Override the preset rate-control (from -1 to INT_MAX) (default -1)"""

    multipass: int | None = None
    """Set the multipass encoding (from 0 to 2) (default disabled)"""

    highbitdepth: bool | None = None
    """Enable 10 bit encode for 8 bit input (default false)"""

    tile_rows: int | None = None
    """Number of tile rows to encode with (from -1 to 64) (default -1)"""

    tile_columns: int | None = None
    """Number of tile columns to encode with (from -1 to 64) (default -1)"""

    surfaces: int | None = None
    """Number of concurrent surfaces (from 0 to 64) (default 0)"""

    gpu: int | None = None
    """Selects which NVENC capable GPU to use. First GPU is 0, second is 1, and so on. (from -2 to INT_MAX) (default any)"""

    rgb_mode: int | None = None
    """Configure how nvenc handles packed RGB input. (from 0 to INT_MAX) (default yuv420)"""

    delay: int | None = None
    """Delay frame output by the given amount of frames (from 0 to INT_MAX) (default INT_MAX)"""

    rc_lookahead: int | None = None
    """Number of frames to look ahead for rate-control (from 0 to INT_MAX) (default 0)"""

    cq: float | None = None
    """Set target quality level (0 to 51, 0 means automatic) for constant quality mode in VBR rate control (from 0 to 51) (default 0)"""

    init_qpP: int | None = None
    """Initial QP value for P frame (from -1 to 255) (default -1)"""

    init_qpB: int | None = None
    """Initial QP value for B frame (from -1 to 255) (default -1)"""

    init_qpI: int | None = None
    """Initial QP value for I frame (from -1 to 255) (default -1)"""

    qp: int | None = None
    """Constant quantization parameter rate control method (from -1 to 255) (default -1)"""

    qp_cb_offset: int | None = None
    """Quantization parameter offset for cb channel (from -12 to 12) (default 0)"""

    qp_cr_offset: int | None = None
    """Quantization parameter offset for cr channel (from -12 to 12) (default 0)"""

    no_scenecut: bool | None = None
    """When lookahead is enabled, set this to 1 to disable adaptive I-frame insertion at scene cuts (default false)"""

    forced_idr: bool | None = None
    """If forcing keyframes, force them as IDR frames. (default false)"""

    b_adapt: bool | None = None
    """When lookahead is enabled, set this to 0 to disable adaptive B-frame decision (default true)"""

    spatial_aq: bool | None = None
    """set to 1 to enable Spatial AQ (default false)"""

    temporal_aq: bool | None = None
    """set to 1 to enable Temporal AQ (default false)"""

    zerolatency: bool | None = None
    """Set 1 to indicate zero latency operation (no reordering delay) (default false)"""

    nonref_p: bool | None = None
    """Set this to 1 to enable automatic insertion of non-reference P-frames (default false)"""

    strict_gop: bool | None = None
    """Set 1 to minimize GOP-to-GOP rate fluctuations (default false)"""

    aq_strength: int | None = None
    """When Spatial AQ is enabled, this field is used to specify AQ strength. AQ strength scale is from 1 (low) - 15 (aggressive) (from 1 to 15) (default 8)"""

    weighted_pred: bool | None = None
    """Enable weighted prediction (default false)"""

    b_ref_mode: int | None = None
    """Use B frames as references (from -1 to 2) (default -1)"""

    dpb_size: int | None = None
    """Specifies the DPB size used for encoding (0 means automatic) (from 0 to INT_MAX) (default 0)"""

    ldkfs: int | None = None
    """Low delay key frame scale; Specifies the Scene Change frame size increase allowed in case of single frame VBV and CBR (from 0 to 255) (default 0)"""

    intra_refresh: bool | None = None
    """Use Periodic Intra Refresh instead of IDR frames (default false)"""

    timing_info: bool | None = None
    """Include timing info in sequence/frame headers (default false)"""

    extra_sei: bool | None = None
    """Pass on extra SEI data (e.g. a53 cc) to be included in the bitstream (default true)"""

    a53cc: bool | None = None
    """Use A53 Closed Captions (if available) (default true)"""

    s12m_tc: bool | None = None
    """Use timecode (if available) (default true)"""


@dataclass(frozen=True, kw_only=True)
class av1_vaapi(FFMpegEncoderOption):
    """AV1 (VAAPI) (codec av1)"""

    low_power: bool | None = None
    """Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)"""

    idr_interval: int | None = None
    """Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)"""

    b_depth: int | None = None
    """Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)"""

    async_depth: int | None = None
    """Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)"""

    max_frame_size: int | None = None
    """Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)"""

    rc_mode: int | None = None
    """Set rate control mode (from 0 to 6) (default auto)"""

    profile: int | None = None
    """Set profile (seq_profile) (from -99 to 255) (default -99)"""

    tier: int | None = None
    """Set tier (seq_tier) (from 0 to 1) (default main)"""

    level: int | None = None
    """Set level (seq_level_idx) (from -99 to 31) (default -99)"""

    tiles: str | None = None
    """Tile columns x rows (Use minimal tile column/row number automatically by default)"""

    tile_groups: int | None = None
    """Number of tile groups for encoding (from 1 to 4096) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class avrp(FFMpegEncoderOption):
    """Avid 1:1 10-bit RGB Packer"""


@dataclass(frozen=True, kw_only=True)
class avui(FFMpegEncoderOption):
    """Avid Meridien Uncompressed"""


@dataclass(frozen=True, kw_only=True)
class ayuv(FFMpegEncoderOption):
    """Uncompressed packed MS 4:4:4:4"""


@dataclass(frozen=True, kw_only=True)
class bitpacked(FFMpegEncoderOption):
    """Bitpacked"""


@dataclass(frozen=True, kw_only=True)
class bmp(FFMpegEncoderOption):
    """BMP (Windows and OS/2 bitmap)"""


@dataclass(frozen=True, kw_only=True)
class cfhd(FFMpegEncoderOption):
    """GoPro CineForm HD"""

    quality: int | None = None
    """set quality (from 0 to 12) (default film3+)"""


@dataclass(frozen=True, kw_only=True)
class cinepak(FFMpegEncoderOption):
    """Cinepak"""

    max_extra_cb_iterations: int | None = None
    """Max extra codebook recalculation passes, more is better and slower (from 0 to INT_MAX) (default 2)"""

    skip_empty_cb: bool | None = None
    """Avoid wasting bytes, ignore vintage MacOS decoder (default false)"""

    max_strips: int | None = None
    """Limit strips/frame, vintage compatible is 1..3, otherwise the more the better (from 1 to 32) (default 3)"""

    min_strips: int | None = None
    """Enforce min strips/frame, more is worse and faster, must be <= max_strips (from 1 to 32) (default 1)"""

    strip_number_adaptivity: int | None = None
    """How fast the strip number adapts, more is slightly better, much slower (from 0 to 31) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class cljr(FFMpegEncoderOption):
    """Cirrus Logic AccuPak"""

    dither_type: int | None = None
    """Dither type (from 0 to 2) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class vc2(FFMpegEncoderOption):
    """SMPTE VC-2 (codec dirac)"""


@dataclass(frozen=True, kw_only=True)
class dnxhd(FFMpegEncoderOption):
    """VC3/DNxHD"""

    nitris_compat: bool | None = None
    """encode with Avid Nitris compatibility (default false)"""

    ibias: int | None = None
    """intra quant bias (from INT_MIN to INT_MAX) (default 0)"""

    profile: int | None = None
    """(from 0 to 5) (default dnxhd)"""


@dataclass(frozen=True, kw_only=True)
class dpx(FFMpegEncoderOption):
    """DPX (Digital Picture Exchange) image"""


@dataclass(frozen=True, kw_only=True)
class dvvideo(FFMpegEncoderOption):
    """DV (Digital Video)"""

    quant_deadzone: int | None = None
    """Quantizer dead zone (from 0 to 1024) (default 7)"""


@dataclass(frozen=True, kw_only=True)
class exr(FFMpegEncoderOption):
    """OpenEXR image"""

    compression: int | None = None
    """set compression type (from 0 to 3) (default none)"""

    format: int | None = None
    """set pixel type (from 1 to 2) (default float)"""

    gamma: float | None = None
    """set gamma (from 0.001 to FLT_MAX) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class ffv1(FFMpegEncoderOption):
    """FFmpeg video codec #1"""

    slicecrc: bool | None = None
    """Protect slices with CRCs (default auto)"""

    coder: int | None = None
    """Coder type (from -2 to 2) (default rice)"""

    context: int | None = None
    """Context model (from 0 to 1) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class ffvhuff(FFMpegEncoderOption):
    """Huffyuv FFmpeg variant"""

    non_deterministic: bool | None = None
    """Allow multithreading for e.g. context=1 at the expense of determinism (default false)"""

    pred: int | None = None
    """Prediction method (from 0 to 2) (default left)"""

    context: int | None = None
    """Set per-frame huffman tables (from 0 to 1) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class fits(FFMpegEncoderOption):
    """Flexible Image Transport System"""


@dataclass(frozen=True, kw_only=True)
class flashsv(FFMpegEncoderOption):
    """Flash Screen Video"""


@dataclass(frozen=True, kw_only=True)
class flashsv2(FFMpegEncoderOption):
    """Flash Screen Video Version 2"""


@dataclass(frozen=True, kw_only=True)
class flv(FFMpegEncoderOption):
    """FLV / Sorenson Spark / Sorenson H.263 (Flash Video) (codec flv1)"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class gif(FFMpegEncoderOption):
    """GIF (Graphics Interchange Format)"""

    gifflags: str | None = None
    """set GIF flags (default offsetting+transdiff)"""

    gifimage: bool | None = None
    """enable encoding only images per frame (default false)"""

    global_palette: bool | None = None
    """write a palette to the global gif header where feasible (default true)"""


@dataclass(frozen=True, kw_only=True)
class h261(FFMpegEncoderOption):
    """H.261"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class h263(FFMpegEncoderOption):
    """H.263 / H.263-1996"""

    obmc: bool | None = None
    """use overlapped block motion compensation. (default false)"""

    mb_info: int | None = None
    """emit macroblock info for RFC 2190 packetization, the parameter value is the maximum payload size (from 0 to INT_MAX) (default 0)"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class h263_v4l2m2m(FFMpegEncoderOption):
    """V4L2 mem2mem H.263 encoder wrapper (codec h263)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 4 to INT_MAX) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class h263p(FFMpegEncoderOption):
    """H.263+ / H.263-1998 / H.263 version 2"""

    umv: bool | None = None
    """Use unlimited motion vectors. (default false)"""

    aiv: bool | None = None
    """Use alternative inter VLC. (default false)"""

    obmc: bool | None = None
    """use overlapped block motion compensation. (default false)"""

    structured_slices: bool | None = None
    """Write slice start position at every GOB header instead of just GOB number. (default false)"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class libx264(FFMpegEncoderOption):
    """libx264 H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 (codec h264)"""

    preset: str | None = None
    """Set the encoding preset (cf. x264 --fullhelp) (default "medium")"""

    tune: str | None = None
    """Tune the encoding params (cf. x264 --fullhelp)"""

    profile: str | None = None
    """Set profile restrictions (cf. x264 --fullhelp)"""

    fastfirstpass: bool | None = None
    """Use fast settings when encoding first pass (default true)"""

    level: str | None = None
    """Specify level (as defined by Annex A)"""

    passlogfile: str | None = None
    """Filename for 2 pass stats"""

    wpredp: str | None = None
    """Weighted prediction for P-frames"""

    a53cc: bool | None = None
    """Use A53 Closed Captions (if available) (default true)"""

    x264opts: str | None = None
    """x264 options"""

    crf: float | None = None
    """Select the quality for constant quality mode (from -1 to FLT_MAX) (default -1)"""

    crf_max: float | None = None
    """In CRF mode, prevents VBV from lowering quality beyond this point. (from -1 to FLT_MAX) (default -1)"""

    qp: int | None = None
    """Constant quantization parameter rate control method (from -1 to INT_MAX) (default -1)"""

    aq_mode: int | None = None
    """AQ method (from -1 to INT_MAX) (default -1)"""

    aq_strength: float | None = None
    """AQ strength. Reduces blocking and blurring in flat and textured areas. (from -1 to FLT_MAX) (default -1)"""

    psy: bool | None = None
    """Use psychovisual optimizations. (default auto)"""

    psy_rd: str | None = None
    """Strength of psychovisual optimization, in <psy-rd>:<psy-trellis> format."""

    rc_lookahead: int | None = None
    """Number of frames to look ahead for frametype and ratecontrol (from -1 to INT_MAX) (default -1)"""

    weightb: bool | None = None
    """Weighted prediction for B-frames. (default auto)"""

    weightp: int | None = None
    """Weighted prediction analysis method. (from -1 to INT_MAX) (default -1)"""

    ssim: bool | None = None
    """Calculate and print SSIM stats. (default auto)"""

    intra_refresh: bool | None = None
    """Use Periodic Intra Refresh instead of IDR frames. (default auto)"""

    bluray_compat: bool | None = None
    """Bluray compatibility workarounds. (default auto)"""

    b_bias: int | None = None
    """Influences how often B-frames are used (from INT_MIN to INT_MAX) (default INT_MIN)"""

    b_pyramid: int | None = None
    """Keep some B-frames as references. (from -1 to INT_MAX) (default -1)"""

    mixed_refs: bool | None = None
    """One reference per partition, as opposed to one reference per macroblock (default auto)"""

    _8x8dct: bool | None = None
    """High profile 8x8 transform. (default auto)"""

    fast_pskip: bool | None = None
    """(default auto)"""

    aud: bool | None = None
    """Use access unit delimiters. (default auto)"""

    mbtree: bool | None = None
    """Use macroblock tree ratecontrol. (default auto)"""

    deblock: str | None = None
    """Loop filter parameters, in <alpha:beta> form."""

    cplxblur: float | None = None
    """Reduce fluctuations in QP (before curve compression) (from -1 to FLT_MAX) (default -1)"""

    partitions: str | None = None
    """A comma-separated list of partitions to consider. Possible values: p8x8, p4x4, b8x8, i8x8, i4x4, none, all"""

    direct_pred: int | None = None
    """Direct MV prediction mode (from -1 to INT_MAX) (default -1)"""

    slice_max_size: int | None = None
    """Limit the size of each slice in bytes (from -1 to INT_MAX) (default -1)"""

    stats: str | None = None
    """Filename for 2 pass stats"""

    nal_hrd: int | None = None
    """Signal HRD information (requires vbv-bufsize; cbr not allowed in .mp4) (from -1 to INT_MAX) (default -1)"""

    avcintra_class: int | None = None
    """AVC-Intra class 50/100/200/300/480 (from -1 to 480) (default -1)"""

    me_method: int | None = None
    """Set motion estimation method (from -1 to 4) (default -1)"""

    motion_est: int | None = None
    """Set motion estimation method (from -1 to 4) (default -1)"""

    forced_idr: bool | None = None
    """If forcing keyframes, force them as IDR frames. (default false)"""

    coder: int | None = None
    """Coder type (from -1 to 1) (default default)"""

    b_strategy: int | None = None
    """Strategy to choose between I/P/B-frames (from -1 to 2) (default -1)"""

    chromaoffset: int | None = None
    """QP difference between chroma and luma (from INT_MIN to INT_MAX) (default 0)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default -1)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default -1)"""

    udu_sei: bool | None = None
    """Use user data unregistered SEI if available (default false)"""

    x264_params: str | None = None
    """Override the x264 configuration using a :-separated list of key=value parameters"""

    mb_info: bool | None = None
    """Set mb_info data through AVSideData, only useful when used from the API (default false)"""


@dataclass(frozen=True, kw_only=True)
class libx264rgb(FFMpegEncoderOption):
    """libx264 H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 RGB (codec h264)"""

    preset: str | None = None
    """Set the encoding preset (cf. x264 --fullhelp) (default "medium")"""

    tune: str | None = None
    """Tune the encoding params (cf. x264 --fullhelp)"""

    profile: str | None = None
    """Set profile restrictions (cf. x264 --fullhelp)"""

    fastfirstpass: bool | None = None
    """Use fast settings when encoding first pass (default true)"""

    level: str | None = None
    """Specify level (as defined by Annex A)"""

    passlogfile: str | None = None
    """Filename for 2 pass stats"""

    wpredp: str | None = None
    """Weighted prediction for P-frames"""

    a53cc: bool | None = None
    """Use A53 Closed Captions (if available) (default true)"""

    x264opts: str | None = None
    """x264 options"""

    crf: float | None = None
    """Select the quality for constant quality mode (from -1 to FLT_MAX) (default -1)"""

    crf_max: float | None = None
    """In CRF mode, prevents VBV from lowering quality beyond this point. (from -1 to FLT_MAX) (default -1)"""

    qp: int | None = None
    """Constant quantization parameter rate control method (from -1 to INT_MAX) (default -1)"""

    aq_mode: int | None = None
    """AQ method (from -1 to INT_MAX) (default -1)"""

    aq_strength: float | None = None
    """AQ strength. Reduces blocking and blurring in flat and textured areas. (from -1 to FLT_MAX) (default -1)"""

    psy: bool | None = None
    """Use psychovisual optimizations. (default auto)"""

    psy_rd: str | None = None
    """Strength of psychovisual optimization, in <psy-rd>:<psy-trellis> format."""

    rc_lookahead: int | None = None
    """Number of frames to look ahead for frametype and ratecontrol (from -1 to INT_MAX) (default -1)"""

    weightb: bool | None = None
    """Weighted prediction for B-frames. (default auto)"""

    weightp: int | None = None
    """Weighted prediction analysis method. (from -1 to INT_MAX) (default -1)"""

    ssim: bool | None = None
    """Calculate and print SSIM stats. (default auto)"""

    intra_refresh: bool | None = None
    """Use Periodic Intra Refresh instead of IDR frames. (default auto)"""

    bluray_compat: bool | None = None
    """Bluray compatibility workarounds. (default auto)"""

    b_bias: int | None = None
    """Influences how often B-frames are used (from INT_MIN to INT_MAX) (default INT_MIN)"""

    b_pyramid: int | None = None
    """Keep some B-frames as references. (from -1 to INT_MAX) (default -1)"""

    mixed_refs: bool | None = None
    """One reference per partition, as opposed to one reference per macroblock (default auto)"""

    _8x8dct: bool | None = None
    """High profile 8x8 transform. (default auto)"""

    fast_pskip: bool | None = None
    """(default auto)"""

    aud: bool | None = None
    """Use access unit delimiters. (default auto)"""

    mbtree: bool | None = None
    """Use macroblock tree ratecontrol. (default auto)"""

    deblock: str | None = None
    """Loop filter parameters, in <alpha:beta> form."""

    cplxblur: float | None = None
    """Reduce fluctuations in QP (before curve compression) (from -1 to FLT_MAX) (default -1)"""

    partitions: str | None = None
    """A comma-separated list of partitions to consider. Possible values: p8x8, p4x4, b8x8, i8x8, i4x4, none, all"""

    direct_pred: int | None = None
    """Direct MV prediction mode (from -1 to INT_MAX) (default -1)"""

    slice_max_size: int | None = None
    """Limit the size of each slice in bytes (from -1 to INT_MAX) (default -1)"""

    stats: str | None = None
    """Filename for 2 pass stats"""

    nal_hrd: int | None = None
    """Signal HRD information (requires vbv-bufsize; cbr not allowed in .mp4) (from -1 to INT_MAX) (default -1)"""

    avcintra_class: int | None = None
    """AVC-Intra class 50/100/200/300/480 (from -1 to 480) (default -1)"""

    me_method: int | None = None
    """Set motion estimation method (from -1 to 4) (default -1)"""

    motion_est: int | None = None
    """Set motion estimation method (from -1 to 4) (default -1)"""

    forced_idr: bool | None = None
    """If forcing keyframes, force them as IDR frames. (default false)"""

    coder: int | None = None
    """Coder type (from -1 to 1) (default default)"""

    b_strategy: int | None = None
    """Strategy to choose between I/P/B-frames (from -1 to 2) (default -1)"""

    chromaoffset: int | None = None
    """QP difference between chroma and luma (from INT_MIN to INT_MAX) (default 0)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default -1)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default -1)"""

    udu_sei: bool | None = None
    """Use user data unregistered SEI if available (default false)"""

    x264_params: str | None = None
    """Override the x264 configuration using a :-separated list of key=value parameters"""

    mb_info: bool | None = None
    """Set mb_info data through AVSideData, only useful when used from the API (default false)"""


@dataclass(frozen=True, kw_only=True)
class h264_nvenc(FFMpegEncoderOption):
    """NVIDIA NVENC H.264 encoder (codec h264)"""

    preset: int | None = None
    """Set the encoding preset (from 0 to 18) (default p4)"""

    tune: int | None = None
    """Set the encoding tuning info (from 1 to 4) (default hq)"""

    profile: int | None = None
    """Set the encoding profile (from 0 to 3) (default main)"""

    level: int | None = None
    """Set the encoding level restriction (from 0 to 62) (default auto)"""

    rc: int | None = None
    """Override the preset rate-control (from -1 to INT_MAX) (default -1)"""

    rc_lookahead: int | None = None
    """Number of frames to look ahead for rate-control (from 0 to INT_MAX) (default 0)"""

    surfaces: int | None = None
    """Number of concurrent surfaces (from 0 to 64) (default 0)"""

    cbr: bool | None = None
    """Use cbr encoding mode (default false)"""

    _2pass: bool | None = None
    """Use 2pass encoding mode (default auto)"""

    gpu: int | None = None
    """Selects which NVENC capable GPU to use. First GPU is 0, second is 1, and so on. (from -2 to INT_MAX) (default any)"""

    rgb_mode: int | None = None
    """Configure how nvenc handles packed RGB input. (from 0 to INT_MAX) (default yuv420)"""

    delay: int | None = None
    """Delay frame output by the given amount of frames (from 0 to INT_MAX) (default INT_MAX)"""

    no_scenecut: bool | None = None
    """When lookahead is enabled, set this to 1 to disable adaptive I-frame insertion at scene cuts (default false)"""

    forced_idr: bool | None = None
    """If forcing keyframes, force them as IDR frames. (default false)"""

    b_adapt: bool | None = None
    """When lookahead is enabled, set this to 0 to disable adaptive B-frame decision (default true)"""

    spatial_aq: bool | None = None
    """set to 1 to enable Spatial AQ (default false)"""

    spatial_aq: bool | None = None
    """set to 1 to enable Spatial AQ (default false)"""

    temporal_aq: bool | None = None
    """set to 1 to enable Temporal AQ (default false)"""

    temporal_aq: bool | None = None
    """set to 1 to enable Temporal AQ (default false)"""

    zerolatency: bool | None = None
    """Set 1 to indicate zero latency operation (no reordering delay) (default false)"""

    nonref_p: bool | None = None
    """Set this to 1 to enable automatic insertion of non-reference P-frames (default false)"""

    strict_gop: bool | None = None
    """Set 1 to minimize GOP-to-GOP rate fluctuations (default false)"""

    aq_strength: int | None = None
    """When Spatial AQ is enabled, this field is used to specify AQ strength. AQ strength scale is from 1 (low) - 15 (aggressive) (from 1 to 15) (default 8)"""

    cq: float | None = None
    """Set target quality level (0 to 51, 0 means automatic) for constant quality mode in VBR rate control (from 0 to 51) (default 0)"""

    aud: bool | None = None
    """Use access unit delimiters (default false)"""

    bluray_compat: bool | None = None
    """Bluray compatibility workarounds (default false)"""

    init_qpP: int | None = None
    """Initial QP value for P frame (from -1 to 51) (default -1)"""

    init_qpB: int | None = None
    """Initial QP value for B frame (from -1 to 51) (default -1)"""

    init_qpI: int | None = None
    """Initial QP value for I frame (from -1 to 51) (default -1)"""

    qp: int | None = None
    """Constant quantization parameter rate control method (from -1 to 51) (default -1)"""

    qp_cb_offset: int | None = None
    """Quantization parameter offset for cb channel (from -12 to 12) (default 0)"""

    qp_cr_offset: int | None = None
    """Quantization parameter offset for cr channel (from -12 to 12) (default 0)"""

    weighted_pred: int | None = None
    """Set 1 to enable weighted prediction (from 0 to 1) (default 0)"""

    coder: int | None = None
    """Coder type (from -1 to 2) (default default)"""

    b_ref_mode: int | None = None
    """Use B frames as references (from -1 to 2) (default -1)"""

    a53cc: bool | None = None
    """Use A53 Closed Captions (if available) (default true)"""

    dpb_size: int | None = None
    """Specifies the DPB size used for encoding (0 means automatic) (from 0 to INT_MAX) (default 0)"""

    multipass: int | None = None
    """Set the multipass encoding (from 0 to 2) (default disabled)"""

    ldkfs: int | None = None
    """Low delay key frame scale; Specifies the Scene Change frame size increase allowed in case of single frame VBV and CBR (from 0 to 255) (default 0)"""

    extra_sei: bool | None = None
    """Pass on extra SEI data (e.g. a53 cc) to be included in the bitstream (default true)"""

    udu_sei: bool | None = None
    """Pass on user data unregistered SEI if available (default false)"""

    intra_refresh: bool | None = None
    """Use Periodic Intra Refresh instead of IDR frames (default false)"""

    single_slice_intra_refresh: bool | None = None
    """Use single slice intra refresh (default false)"""

    max_slice_size: int | None = None
    """Maximum encoded slice size in bytes (from 0 to INT_MAX) (default 0)"""

    constrained_encoding: bool | None = None
    """Enable constrainedFrame encoding where each slice in the constrained picture is independent of other slices (default false)"""


@dataclass(frozen=True, kw_only=True)
class h264_v4l2m2m(FFMpegEncoderOption):
    """V4L2 mem2mem H.264 encoder wrapper (codec h264)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 4 to INT_MAX) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class h264_vaapi(FFMpegEncoderOption):
    """H.264/AVC (VAAPI) (codec h264)"""

    low_power: bool | None = None
    """Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)"""

    idr_interval: int | None = None
    """Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)"""

    b_depth: int | None = None
    """Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)"""

    async_depth: int | None = None
    """Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)"""

    max_frame_size: int | None = None
    """Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)"""

    rc_mode: int | None = None
    """Set rate control mode (from 0 to 6) (default auto)"""

    qp: int | None = None
    """Constant QP (for P-frames; scaled by qfactor/qoffset for I/B) (from 0 to 52) (default 0)"""

    quality: int | None = None
    """Set encode quality (trades off against speed, higher is faster) (from -1 to INT_MAX) (default -1)"""

    coder: int | None = None
    """Entropy coder type (from 0 to 1) (default cabac)"""

    aud: bool | None = None
    """Include AUD (default false)"""

    sei: str | None = None
    """Set SEI to include (default identifier+timing+recovery_point+a53_cc)"""

    profile: int | None = None
    """Set profile (profile_idc and constraint_set*_flag) (from -99 to 65535) (default -99)"""

    level: int | None = None
    """Set level (level_idc) (from -99 to 255) (default -99)"""


@dataclass(frozen=True, kw_only=True)
class hap(FFMpegEncoderOption):
    """Vidvox Hap"""

    format: int | None = None
    """(from 11 to 15) (default hap)"""

    chunks: int | None = None
    """chunk count (from 1 to 64) (default 1)"""

    compressor: int | None = None
    """second-stage compressor (from 160 to 176) (default snappy)"""


@dataclass(frozen=True, kw_only=True)
class hdr(FFMpegEncoderOption):
    """HDR (Radiance RGBE format) image"""


@dataclass(frozen=True, kw_only=True)
class libx265(FFMpegEncoderOption):
    """libx265 H.265 / HEVC (codec hevc)"""

    crf: float | None = None
    """set the x265 crf (from -1 to FLT_MAX) (default -1)"""

    qp: int | None = None
    """set the x265 qp (from -1 to INT_MAX) (default -1)"""

    forced_idr: bool | None = None
    """if forcing keyframes, force them as IDR frames (default false)"""

    preset: str | None = None
    """set the x265 preset"""

    tune: str | None = None
    """set the x265 tune parameter"""

    profile: str | None = None
    """set the x265 profile"""

    udu_sei: bool | None = None
    """Use user data unregistered SEI if available (default false)"""

    a53cc: bool | None = None
    """Use A53 Closed Captions (if available) (default true)"""

    x265_params: str | None = None
    """set the x265 configuration using a :-separated list of key=value parameters"""


@dataclass(frozen=True, kw_only=True)
class hevc_nvenc(FFMpegEncoderOption):
    """NVIDIA NVENC hevc encoder (codec hevc)"""

    preset: int | None = None
    """Set the encoding preset (from 0 to 18) (default p4)"""

    tune: int | None = None
    """Set the encoding tuning info (from 1 to 4) (default hq)"""

    profile: int | None = None
    """Set the encoding profile (from 0 to 4) (default main)"""

    level: int | None = None
    """Set the encoding level restriction (from 0 to 186) (default auto)"""

    tier: int | None = None
    """Set the encoding tier (from 0 to 1) (default main)"""

    rc: int | None = None
    """Override the preset rate-control (from -1 to INT_MAX) (default -1)"""

    rc_lookahead: int | None = None
    """Number of frames to look ahead for rate-control (from 0 to INT_MAX) (default 0)"""

    surfaces: int | None = None
    """Number of concurrent surfaces (from 0 to 64) (default 0)"""

    cbr: bool | None = None
    """Use cbr encoding mode (default false)"""

    _2pass: bool | None = None
    """Use 2pass encoding mode (default auto)"""

    gpu: int | None = None
    """Selects which NVENC capable GPU to use. First GPU is 0, second is 1, and so on. (from -2 to INT_MAX) (default any)"""

    rgb_mode: int | None = None
    """Configure how nvenc handles packed RGB input. (from 0 to INT_MAX) (default yuv420)"""

    delay: int | None = None
    """Delay frame output by the given amount of frames (from 0 to INT_MAX) (default INT_MAX)"""

    no_scenecut: bool | None = None
    """When lookahead is enabled, set this to 1 to disable adaptive I-frame insertion at scene cuts (default false)"""

    forced_idr: bool | None = None
    """If forcing keyframes, force them as IDR frames. (default false)"""

    spatial_aq: bool | None = None
    """set to 1 to enable Spatial AQ (default false)"""

    spatial_aq: bool | None = None
    """set to 1 to enable Spatial AQ (default false)"""

    temporal_aq: bool | None = None
    """set to 1 to enable Temporal AQ (default false)"""

    temporal_aq: bool | None = None
    """set to 1 to enable Temporal AQ (default false)"""

    zerolatency: bool | None = None
    """Set 1 to indicate zero latency operation (no reordering delay) (default false)"""

    nonref_p: bool | None = None
    """Set this to 1 to enable automatic insertion of non-reference P-frames (default false)"""

    strict_gop: bool | None = None
    """Set 1 to minimize GOP-to-GOP rate fluctuations (default false)"""

    aq_strength: int | None = None
    """When Spatial AQ is enabled, this field is used to specify AQ strength. AQ strength scale is from 1 (low) - 15 (aggressive) (from 1 to 15) (default 8)"""

    cq: float | None = None
    """Set target quality level (0 to 51, 0 means automatic) for constant quality mode in VBR rate control (from 0 to 51) (default 0)"""

    aud: bool | None = None
    """Use access unit delimiters (default false)"""

    bluray_compat: bool | None = None
    """Bluray compatibility workarounds (default false)"""

    init_qpP: int | None = None
    """Initial QP value for P frame (from -1 to 51) (default -1)"""

    init_qpB: int | None = None
    """Initial QP value for B frame (from -1 to 51) (default -1)"""

    init_qpI: int | None = None
    """Initial QP value for I frame (from -1 to 51) (default -1)"""

    qp: int | None = None
    """Constant quantization parameter rate control method (from -1 to 51) (default -1)"""

    qp_cb_offset: int | None = None
    """Quantization parameter offset for cb channel (from -12 to 12) (default 0)"""

    qp_cr_offset: int | None = None
    """Quantization parameter offset for cr channel (from -12 to 12) (default 0)"""

    weighted_pred: int | None = None
    """Set 1 to enable weighted prediction (from 0 to 1) (default 0)"""

    b_ref_mode: int | None = None
    """Use B frames as references (from -1 to 2) (default -1)"""

    a53cc: bool | None = None
    """Use A53 Closed Captions (if available) (default true)"""

    s12m_tc: bool | None = None
    """Use timecode (if available) (default true)"""

    dpb_size: int | None = None
    """Specifies the DPB size used for encoding (0 means automatic) (from 0 to INT_MAX) (default 0)"""

    multipass: int | None = None
    """Set the multipass encoding (from 0 to 2) (default disabled)"""

    ldkfs: int | None = None
    """Low delay key frame scale; Specifies the Scene Change frame size increase allowed in case of single frame VBV and CBR (from 0 to 255) (default 0)"""

    extra_sei: bool | None = None
    """Pass on extra SEI data (e.g. a53 cc) to be included in the bitstream (default true)"""

    udu_sei: bool | None = None
    """Pass on user data unregistered SEI if available (default false)"""

    intra_refresh: bool | None = None
    """Use Periodic Intra Refresh instead of IDR frames (default false)"""

    single_slice_intra_refresh: bool | None = None
    """Use single slice intra refresh (default false)"""

    max_slice_size: int | None = None
    """Maximum encoded slice size in bytes (from 0 to INT_MAX) (default 0)"""

    constrained_encoding: bool | None = None
    """Enable constrainedFrame encoding where each slice in the constrained picture is independent of other slices (default false)"""


@dataclass(frozen=True, kw_only=True)
class hevc_v4l2m2m(FFMpegEncoderOption):
    """V4L2 mem2mem HEVC encoder wrapper (codec hevc)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 4 to INT_MAX) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class hevc_vaapi(FFMpegEncoderOption):
    """H.265/HEVC (VAAPI) (codec hevc)"""

    low_power: bool | None = None
    """Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)"""

    idr_interval: int | None = None
    """Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)"""

    b_depth: int | None = None
    """Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)"""

    async_depth: int | None = None
    """Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)"""

    max_frame_size: int | None = None
    """Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)"""

    rc_mode: int | None = None
    """Set rate control mode (from 0 to 6) (default auto)"""

    qp: int | None = None
    """Constant QP (for P-frames; scaled by qfactor/qoffset for I/B) (from 0 to 52) (default 0)"""

    aud: bool | None = None
    """Include AUD (default false)"""

    profile: int | None = None
    """Set profile (general_profile_idc) (from -99 to 255) (default -99)"""

    tier: int | None = None
    """Set tier (general_tier_flag) (from 0 to 1) (default main)"""

    level: int | None = None
    """Set level (general_level_idc) (from -99 to 255) (default -99)"""

    sei: str | None = None
    """Set SEI to include (default hdr+a53_cc)"""

    tiles: str | None = None
    """Tile columns x rows"""


@dataclass(frozen=True, kw_only=True)
class huffyuv(FFMpegEncoderOption):
    """Huffyuv / HuffYUV"""

    non_deterministic: bool | None = None
    """Allow multithreading for e.g. context=1 at the expense of determinism (default false)"""

    pred: int | None = None
    """Prediction method (from 0 to 2) (default left)"""


@dataclass(frozen=True, kw_only=True)
class jpeg2000(FFMpegEncoderOption):
    """JPEG 2000"""

    format: int | None = None
    """Codec Format (from 0 to 1) (default jp2)"""

    tile_width: int | None = None
    """Tile Width (from 1 to 1.07374e+09) (default 256)"""

    tile_height: int | None = None
    """Tile Height (from 1 to 1.07374e+09) (default 256)"""

    pred: int | None = None
    """DWT Type (from 0 to 1) (default dwt97int)"""

    sop: int | None = None
    """SOP marker (from 0 to 1) (default 0)"""

    eph: int | None = None
    """EPH marker (from 0 to 1) (default 0)"""

    prog: int | None = None
    """Progression Order (from 0 to 4) (default lrcp)"""

    layer_rates: str | None = None
    """Layer Rates"""


@dataclass(frozen=True, kw_only=True)
class libopenjpeg(FFMpegEncoderOption):
    """OpenJPEG JPEG 2000 (codec jpeg2000)"""

    format: int | None = None
    """Codec Format (from 0 to 2) (default jp2)"""

    profile: int | None = None
    """(from 0 to 4) (default jpeg2000)"""

    cinema_mode: int | None = None
    """Digital Cinema (from 0 to 3) (default off)"""

    prog_order: int | None = None
    """Progression Order (from 0 to 4) (default lrcp)"""

    numresolution: int | None = None
    """(from 0 to 33) (default 6)"""

    irreversible: int | None = None
    """(from 0 to 1) (default 0)"""

    disto_alloc: int | None = None
    """(from 0 to 1) (default 1)"""

    fixed_quality: int | None = None
    """(from 0 to 1) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class jpegls(FFMpegEncoderOption):
    """JPEG-LS"""

    pred: int | None = None
    """Prediction method (from 0 to 2) (default left)"""


@dataclass(frozen=True, kw_only=True)
class libjxl(FFMpegEncoderOption):
    """libjxl JPEG XL (codec jpegxl)"""

    effort: int | None = None
    """Encoding effort (from 1 to 9) (default 7)"""

    distance: float | None = None
    """Maximum Butteraugli distance (quality setting, lower = better, zero = lossless, default 1.0) (from -1 to 15) (default -1)"""

    modular: int | None = None
    """Force modular mode (from 0 to 1) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class ljpeg(FFMpegEncoderOption):
    """Lossless JPEG"""

    pred: int | None = None
    """Prediction method (from 1 to 3) (default left)"""


@dataclass(frozen=True, kw_only=True)
class magicyuv(FFMpegEncoderOption):
    """MagicYUV video"""

    pred: int | None = None
    """Prediction method (from 1 to 3) (default left)"""


@dataclass(frozen=True, kw_only=True)
class mjpeg(FFMpegEncoderOption):
    """MJPEG (Motion JPEG)"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    huffman: int | None = None
    """Huffman table strategy (from 0 to 1) (default optimal)"""

    force_duplicated_matrix: bool | None = None
    """Always write luma and chroma matrix for mjpeg, useful for rtp streaming. (default false)"""


@dataclass(frozen=True, kw_only=True)
class mjpeg_vaapi(FFMpegEncoderOption):
    """MJPEG (VAAPI) (codec mjpeg)"""

    low_power: bool | None = None
    """Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)"""

    idr_interval: int | None = None
    """Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)"""

    b_depth: int | None = None
    """Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)"""

    async_depth: int | None = None
    """Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)"""

    max_frame_size: int | None = None
    """Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)"""

    jfif: bool | None = None
    """Include JFIF header (default false)"""

    huffman: bool | None = None
    """Include huffman tables (default true)"""


@dataclass(frozen=True, kw_only=True)
class mpeg1video(FFMpegEncoderOption):
    """MPEG-1 video"""

    gop_timecode: str | None = None
    """MPEG GOP Timecode in hh:mm:ss[:;.]ff format. Overrides timecode_frame_start."""

    drop_frame_timecode: bool | None = None
    """Timecode is in drop frame format. (default false)"""

    scan_offset: bool | None = None
    """Reserve space for SVCD scan offset user data. (default false)"""

    timecode_frame_start: int | None = None
    """GOP timecode frame start number, in non-drop-frame format (from -1 to I64_MAX) (default -1)"""

    b_strategy: int | None = None
    """Strategy to choose between I/P/B-frames (from 0 to 2) (default 0)"""

    b_sensitivity: int | None = None
    """Adjust sensitivity of b_frame_strategy 1 (from 1 to INT_MAX) (default 40)"""

    brd_scale: int | None = None
    """Downscale frames for dynamic B-frame decision (from 0 to 3) (default 0)"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class mpeg2video(FFMpegEncoderOption):
    """MPEG-2 video"""

    gop_timecode: str | None = None
    """MPEG GOP Timecode in hh:mm:ss[:;.]ff format. Overrides timecode_frame_start."""

    drop_frame_timecode: bool | None = None
    """Timecode is in drop frame format. (default false)"""

    scan_offset: bool | None = None
    """Reserve space for SVCD scan offset user data. (default false)"""

    timecode_frame_start: int | None = None
    """GOP timecode frame start number, in non-drop-frame format (from -1 to I64_MAX) (default -1)"""

    b_strategy: int | None = None
    """Strategy to choose between I/P/B-frames (from 0 to 2) (default 0)"""

    b_sensitivity: int | None = None
    """Adjust sensitivity of b_frame_strategy 1 (from 1 to INT_MAX) (default 40)"""

    brd_scale: int | None = None
    """Downscale frames for dynamic B-frame decision (from 0 to 3) (default 0)"""

    intra_vlc: bool | None = None
    """Use MPEG-2 intra VLC table. (default false)"""

    non_linear_quant: bool | None = None
    """Use nonlinear quantizer. (default false)"""

    alternate_scan: bool | None = None
    """Enable alternate scantable. (default false)"""

    a53cc: bool | None = None
    """Use A53 Closed Captions (if available) (default true)"""

    seq_disp_ext: int | None = None
    """Write sequence_display_extension blocks. (from -1 to 1) (default auto)"""

    video_format: int | None = None
    """Video_format in the sequence_display_extension indicating the source of the video. (from 0 to 7) (default unspecified)"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class mpeg2_vaapi(FFMpegEncoderOption):
    """MPEG-2 (VAAPI) (codec mpeg2video)"""

    low_power: bool | None = None
    """Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)"""

    idr_interval: int | None = None
    """Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)"""

    b_depth: int | None = None
    """Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)"""

    async_depth: int | None = None
    """Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)"""

    max_frame_size: int | None = None
    """Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)"""

    rc_mode: int | None = None
    """Set rate control mode (from 0 to 6) (default auto)"""

    profile: int | None = None
    """Set profile (in profile_and_level_indication) (from -99 to 7) (default -99)"""

    level: int | None = None
    """Set level (in profile_and_level_indication) (from 0 to 15) (default high)"""


@dataclass(frozen=True, kw_only=True)
class mpeg4(FFMpegEncoderOption):
    """MPEG-4 part 2"""

    data_partitioning: bool | None = None
    """Use data partitioning. (default false)"""

    alternate_scan: bool | None = None
    """Enable alternate scantable. (default false)"""

    mpeg_quant: int | None = None
    """Use MPEG quantizers instead of H.263 (from 0 to 1) (default 0)"""

    b_strategy: int | None = None
    """Strategy to choose between I/P/B-frames (from 0 to 2) (default 0)"""

    b_sensitivity: int | None = None
    """Adjust sensitivity of b_frame_strategy 1 (from 1 to INT_MAX) (default 40)"""

    brd_scale: int | None = None
    """Downscale frames for dynamic B-frame decision (from 0 to 3) (default 0)"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class libxvid(FFMpegEncoderOption):
    """libxvidcore MPEG-4 part 2 (codec mpeg4)"""

    lumi_aq: int | None = None
    """Luminance masking AQ (from 0 to 1) (default 0)"""

    variance_aq: int | None = None
    """Variance AQ (from 0 to 1) (default 0)"""

    ssim: int | None = None
    """Show SSIM information to stdout (from 0 to 2) (default off)"""

    ssim_acc: int | None = None
    """SSIM accuracy (from 0 to 4) (default 2)"""

    gmc: int | None = None
    """use GMC (from 0 to 1) (default 0)"""

    me_quality: int | None = None
    """Motion estimation quality (from 0 to 6) (default 4)"""

    mpeg_quant: int | None = None
    """Use MPEG quantizers instead of H.263 (from 0 to 1) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class mpeg4_v4l2m2m(FFMpegEncoderOption):
    """V4L2 mem2mem MPEG4 encoder wrapper (codec mpeg4)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 4 to INT_MAX) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class msmpeg4v2(FFMpegEncoderOption):
    """MPEG-4 part 2 Microsoft variant version 2"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class msmpeg4(FFMpegEncoderOption):
    """MPEG-4 part 2 Microsoft variant version 3 (codec msmpeg4v3)"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class msrle(FFMpegEncoderOption):
    """Microsoft RLE"""


@dataclass(frozen=True, kw_only=True)
class msvideo1(FFMpegEncoderOption):
    """Microsoft Video-1"""


@dataclass(frozen=True, kw_only=True)
class pam(FFMpegEncoderOption):
    """PAM (Portable AnyMap) image"""


@dataclass(frozen=True, kw_only=True)
class pbm(FFMpegEncoderOption):
    """PBM (Portable BitMap) image"""


@dataclass(frozen=True, kw_only=True)
class pcx(FFMpegEncoderOption):
    """PC Paintbrush PCX image"""


@dataclass(frozen=True, kw_only=True)
class pfm(FFMpegEncoderOption):
    """PFM (Portable FloatMap) image"""


@dataclass(frozen=True, kw_only=True)
class pgm(FFMpegEncoderOption):
    """PGM (Portable GrayMap) image"""


@dataclass(frozen=True, kw_only=True)
class pgmyuv(FFMpegEncoderOption):
    """PGMYUV (Portable GrayMap YUV) image"""


@dataclass(frozen=True, kw_only=True)
class phm(FFMpegEncoderOption):
    """PHM (Portable HalfFloatMap) image"""


@dataclass(frozen=True, kw_only=True)
class png(FFMpegEncoderOption):
    """PNG (Portable Network Graphics) image"""


@dataclass(frozen=True, kw_only=True)
class ppm(FFMpegEncoderOption):
    """PPM (Portable PixelMap) image"""


@dataclass(frozen=True, kw_only=True)
class prores(FFMpegEncoderOption):
    """Apple ProRes"""

    vendor: str | None = None
    """vendor ID (default "fmpg")"""


@dataclass(frozen=True, kw_only=True)
class prores_aw(FFMpegEncoderOption):
    """Apple ProRes (codec prores)"""

    vendor: str | None = None
    """vendor ID (default "fmpg")"""


@dataclass(frozen=True, kw_only=True)
class prores_ks(FFMpegEncoderOption):
    """Apple ProRes (iCodec Pro) (codec prores)"""

    mbs_per_slice: int | None = None
    """macroblocks per slice (from 1 to 8) (default 8)"""

    profile: int | None = None
    """(from -1 to 5) (default auto)"""

    vendor: str | None = None
    """vendor ID (default "Lavc")"""

    bits_per_mb: int | None = None
    """desired bits per macroblock (from 0 to 8192) (default 0)"""

    quant_mat: int | None = None
    """quantiser matrix (from -1 to 6) (default auto)"""

    alpha_bits: int | None = None
    """bits for alpha plane (from 0 to 16) (default 16)"""


@dataclass(frozen=True, kw_only=True)
class qoi(FFMpegEncoderOption):
    """QOI (Quite OK Image format) image"""


@dataclass(frozen=True, kw_only=True)
class qtrle(FFMpegEncoderOption):
    """QuickTime Animation (RLE) video"""


@dataclass(frozen=True, kw_only=True)
class r10k(FFMpegEncoderOption):
    """AJA Kona 10-bit RGB Codec"""


@dataclass(frozen=True, kw_only=True)
class r210(FFMpegEncoderOption):
    """Uncompressed RGB 10-bit"""


@dataclass(frozen=True, kw_only=True)
class rawvideo(FFMpegEncoderOption):
    """raw video"""


@dataclass(frozen=True, kw_only=True)
class roqvideo(FFMpegEncoderOption):
    """id RoQ video (codec roq)"""

    quake3_compat: bool | None = None
    """Whether to respect known limitations in Quake 3 decoder (default true)"""


@dataclass(frozen=True, kw_only=True)
class rpza(FFMpegEncoderOption):
    """QuickTime video (RPZA)"""

    skip_frame_thresh: int | None = None
    """(from 0 to 24) (default 1)"""

    start_one_color_thresh: int | None = None
    """(from 0 to 24) (default 1)"""

    continue_one_color_thresh: int | None = None
    """(from 0 to 24) (default 0)"""

    sixteen_color_thresh: int | None = None
    """(from 0 to 24) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class rv10(FFMpegEncoderOption):
    """RealVideo 1.0"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class rv20(FFMpegEncoderOption):
    """RealVideo 2.0"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class sgi(FFMpegEncoderOption):
    """SGI image"""

    rle: int | None = None
    """Use run-length compression (from 0 to 1) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class smc(FFMpegEncoderOption):
    """QuickTime Graphics (SMC)"""


@dataclass(frozen=True, kw_only=True)
class snow(FFMpegEncoderOption):
    """Snow"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 3) (default epzs)"""

    memc_only: bool | None = None
    """Only do ME/MC (I frames -> ref, P frame -> ME+MC). (default false)"""

    no_bitstream: bool | None = None
    """Skip final bitstream writeout. (default false)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decission (from 0 to INT_MAX) (default 0)"""

    iterative_dia_size: int | None = None
    """Dia size for the iterative ME (from 0 to INT_MAX) (default 0)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    pred: int | None = None
    """Spatial decomposition type (from 0 to 1) (default dwt97)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""


@dataclass(frozen=True, kw_only=True)
class speedhq(FFMpegEncoderOption):
    """NewTek SpeedHQ"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class sunrast(FFMpegEncoderOption):
    """Sun Rasterfile image"""

    rle: int | None = None
    """Use run-length compression (from 0 to 1) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class svq1(FFMpegEncoderOption):
    """Sorenson Vector Quantizer 1 / Sorenson Video 1 / SVQ1"""

    motion_est: int | None = None
    """Motion estimation algorithm (from 0 to 2) (default epzs)"""


@dataclass(frozen=True, kw_only=True)
class targa(FFMpegEncoderOption):
    """Truevision Targa image"""

    rle: int | None = None
    """Use run-length compression (from 0 to 1) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class libtheora(FFMpegEncoderOption):
    """libtheora Theora (codec theora)"""


@dataclass(frozen=True, kw_only=True)
class tiff(FFMpegEncoderOption):
    """TIFF image"""

    dpi: int | None = None
    """set the image resolution (in dpi) (from 1 to 65536) (default 72)"""

    compression_algo: int | None = None
    """(from 1 to 32946) (default packbits)"""


@dataclass(frozen=True, kw_only=True)
class utvideo(FFMpegEncoderOption):
    """Ut Video"""

    pred: int | None = None
    """Prediction method (from 0 to 3) (default left)"""


@dataclass(frozen=True, kw_only=True)
class v210(FFMpegEncoderOption):
    """Uncompressed 4:2:2 10-bit"""


@dataclass(frozen=True, kw_only=True)
class v308(FFMpegEncoderOption):
    """Uncompressed packed 4:4:4"""


@dataclass(frozen=True, kw_only=True)
class v408(FFMpegEncoderOption):
    """Uncompressed packed QT 4:4:4:4"""


@dataclass(frozen=True, kw_only=True)
class v410(FFMpegEncoderOption):
    """Uncompressed 4:4:4 10-bit"""


@dataclass(frozen=True, kw_only=True)
class vbn(FFMpegEncoderOption):
    """Vizrt Binary Image"""

    format: int | None = None
    """Texture format (from 0 to 3) (default dxt5)"""


@dataclass(frozen=True, kw_only=True)
class vnull(FFMpegEncoderOption):
    """null video"""


@dataclass(frozen=True, kw_only=True)
class libvpx(FFMpegEncoderOption):
    """libvpx VP8 (codec vp8)"""


@dataclass(frozen=True, kw_only=True)
class vp8_v4l2m2m(FFMpegEncoderOption):
    """V4L2 mem2mem VP8 encoder wrapper (codec vp8)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 4 to INT_MAX) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class vp8_vaapi(FFMpegEncoderOption):
    """VP8 (VAAPI) (codec vp8)"""

    low_power: bool | None = None
    """Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)"""

    idr_interval: int | None = None
    """Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)"""

    b_depth: int | None = None
    """Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)"""

    async_depth: int | None = None
    """Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)"""

    max_frame_size: int | None = None
    """Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)"""

    rc_mode: int | None = None
    """Set rate control mode (from 0 to 6) (default auto)"""

    loop_filter_level: int | None = None
    """Loop filter level (from 0 to 63) (default 16)"""

    loop_filter_sharpness: int | None = None
    """Loop filter sharpness (from 0 to 15) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class vp9_vaapi(FFMpegEncoderOption):
    """VP9 (VAAPI) (codec vp9)"""

    low_power: bool | None = None
    """Use low-power encoding mode (only available on some platforms; may not support all encoding features) (default false)"""

    idr_interval: int | None = None
    """Distance (in I-frames) between IDR frames (from 0 to INT_MAX) (default 0)"""

    b_depth: int | None = None
    """Maximum B-frame reference depth (from 1 to INT_MAX) (default 1)"""

    async_depth: int | None = None
    """Maximum processing parallelism. Increase this to improve single channel performance. This option doesn't work if driver doesn't implement vaSyncBuffer function. (from 1 to 64) (default 2)"""

    max_frame_size: int | None = None
    """Maximum frame size (in bytes) (from 0 to INT_MAX) (default 0)"""

    rc_mode: int | None = None
    """Set rate control mode (from 0 to 6) (default auto)"""

    loop_filter_level: int | None = None
    """Loop filter level (from 0 to 63) (default 16)"""

    loop_filter_sharpness: int | None = None
    """Loop filter sharpness (from 0 to 15) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class wbmp(FFMpegEncoderOption):
    """WBMP (Wireless Application Protocol Bitmap) image"""


@dataclass(frozen=True, kw_only=True)
class libwebp_anim(FFMpegEncoderOption):
    """libwebp WebP image (codec webp)"""

    lossless: int | None = None
    """Use lossless mode (from 0 to 1) (default 0)"""

    preset: int | None = None
    """Configuration preset (from -1 to 5) (default none)"""

    cr_threshold: int | None = None
    """Conditional replenishment threshold (from 0 to INT_MAX) (default 0)"""

    cr_size: int | None = None
    """Conditional replenishment block size (from 0 to 256) (default 16)"""

    quality: float | None = None
    """Quality (from 0 to 100) (default 75)"""


@dataclass(frozen=True, kw_only=True)
class libwebp(FFMpegEncoderOption):
    """libwebp WebP image (codec webp)"""

    lossless: int | None = None
    """Use lossless mode (from 0 to 1) (default 0)"""

    preset: int | None = None
    """Configuration preset (from -1 to 5) (default none)"""

    cr_threshold: int | None = None
    """Conditional replenishment threshold (from 0 to INT_MAX) (default 0)"""

    cr_size: int | None = None
    """Conditional replenishment block size (from 0 to 256) (default 16)"""

    quality: float | None = None
    """Quality (from 0 to 100) (default 75)"""


@dataclass(frozen=True, kw_only=True)
class wmv1(FFMpegEncoderOption):
    """Windows Media Video 7"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class wmv2(FFMpegEncoderOption):
    """Windows Media Video 8"""

    mpv_flags: str | None = None
    """Flags common for all mpegvideo-based encoders. (default 0)"""

    luma_elim_threshold: int | None = None
    """single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    chroma_elim_threshold: int | None = None
    """single coefficient elimination threshold for chrominance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)"""

    quantizer_noise_shaping: int | None = None
    """(from 0 to INT_MAX) (default 0)"""

    error_rate: int | None = None
    """Simulate errors in the bitstream to test error concealment. (from 0 to INT_MAX) (default 0)"""

    qsquish: float | None = None
    """how to keep quantizer between qmin and qmax (0 = clip, 1 = use differentiable function) (from 0 to 99) (default 0)"""

    rc_qmod_amp: float | None = None
    """experimental quantizer modulation (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_qmod_freq: int | None = None
    """experimental quantizer modulation (from INT_MIN to INT_MAX) (default 0)"""

    rc_eq: str | None = None
    """Set rate control equation. When computing the expression, besides the standard functions defined in the section 'Expression Evaluation', the following functions are available: bits2qp(bits), qp2bits(qp). Also the following constants are available: iTex pTex tex mv fCode iCount mcVar var isI isP isB avgQP qComp avgIITex avgPITex avgPPTex avgBPTex avgTex."""

    rc_init_cplx: float | None = None
    """initial complexity for 1-pass encoding (from -FLT_MAX to FLT_MAX) (default 0)"""

    rc_buf_aggressivity: float | None = None
    """currently useless (from -FLT_MAX to FLT_MAX) (default 1)"""

    border_mask: float | None = None
    """increase the quantizer for macroblocks close to borders (from -FLT_MAX to FLT_MAX) (default 0)"""

    lmin: int | None = None
    """minimum Lagrange factor (VBR) (from 0 to INT_MAX) (default 236)"""

    lmax: int | None = None
    """maximum Lagrange factor (VBR) (from 0 to INT_MAX) (default 3658)"""

    skip_threshold: int | None = None
    """Frame skip threshold (from INT_MIN to INT_MAX) (default 0)"""

    skip_factor: int | None = None
    """Frame skip factor (from INT_MIN to INT_MAX) (default 0)"""

    skip_exp: int | None = None
    """Frame skip exponent (from INT_MIN to INT_MAX) (default 0)"""

    skip_cmp: int | None = None
    """Frame skip compare function (from INT_MIN to INT_MAX) (default dctmax)"""

    sc_threshold: int | None = None
    """Scene change threshold (from INT_MIN to INT_MAX) (default 0)"""

    noise_reduction: int | None = None
    """Noise reduction (from INT_MIN to INT_MAX) (default 0)"""

    ps: int | None = None
    """RTP payload size in bytes (from INT_MIN to INT_MAX) (default 0)"""

    motion_est: int | None = None
    """motion estimation algorithm (from 0 to 2) (default epzs)"""

    mepc: int | None = None
    """Motion estimation bitrate penalty compensation (1.0 = 256) (from INT_MIN to INT_MAX) (default 256)"""

    mepre: int | None = None
    """pre motion estimation (from INT_MIN to INT_MAX) (default 0)"""

    intra_penalty: int | None = None
    """Penalty for intra blocks in block decision (from 0 to 1.07374e+09) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class wrapped_avframe(FFMpegEncoderOption):
    """AVFrame to AVPacket passthrough"""


@dataclass(frozen=True, kw_only=True)
class xbm(FFMpegEncoderOption):
    """XBM (X BitMap) image"""


@dataclass(frozen=True, kw_only=True)
class xface(FFMpegEncoderOption):
    """X-face image"""


@dataclass(frozen=True, kw_only=True)
class xwd(FFMpegEncoderOption):
    """XWD (X Window Dump) image"""


@dataclass(frozen=True, kw_only=True)
class y41p(FFMpegEncoderOption):
    """Uncompressed YUV 4:1:1 12-bit"""


@dataclass(frozen=True, kw_only=True)
class yuv4(FFMpegEncoderOption):
    """Uncompressed packed 4:2:0"""


@dataclass(frozen=True, kw_only=True)
class zlib(FFMpegEncoderOption):
    """LCL (LossLess Codec Library) ZLIB"""


@dataclass(frozen=True, kw_only=True)
class zmbv(FFMpegEncoderOption):
    """Zip Motion Blocks Video"""


@dataclass(frozen=True, kw_only=True)
class aac(FFMpegEncoderOption):
    """AAC (Advanced Audio Coding)"""

    aac_coder: int | None = None
    """Coding algorithm (from 0 to 2) (default twoloop)"""

    aac_ms: bool | None = None
    """Force M/S stereo coding (default auto)"""

    aac_is: bool | None = None
    """Intensity stereo coding (default true)"""

    aac_pns: bool | None = None
    """Perceptual noise substitution (default true)"""

    aac_tns: bool | None = None
    """Temporal noise shaping (default true)"""

    aac_ltp: bool | None = None
    """Long term prediction (default false)"""

    aac_pred: bool | None = None
    """AAC-Main prediction (default false)"""

    aac_pce: bool | None = None
    """Forces the use of PCEs (default false)"""


@dataclass(frozen=True, kw_only=True)
class ac3(FFMpegEncoderOption):
    """ATSC A/52A (AC-3)"""


@dataclass(frozen=True, kw_only=True)
class ac3_fixed(FFMpegEncoderOption):
    """ATSC A/52A (AC-3) (codec ac3)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_adx(FFMpegEncoderOption):
    """SEGA CRI ADX ADPCM"""


@dataclass(frozen=True, kw_only=True)
class adpcm_argo(FFMpegEncoderOption):
    """ADPCM Argonaut Games"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class g722(FFMpegEncoderOption):
    """G.722 ADPCM (codec adpcm_g722)"""


@dataclass(frozen=True, kw_only=True)
class g726(FFMpegEncoderOption):
    """G.726 ADPCM (codec adpcm_g726)"""

    code_size: int | None = None
    """Bits per code (from 2 to 5) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class g726le(FFMpegEncoderOption):
    """G.726 little endian ADPCM ("right-justified") (codec adpcm_g726le)"""

    code_size: int | None = None
    """Bits per code (from 2 to 5) (default 4)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_alp(FFMpegEncoderOption):
    """ADPCM IMA High Voltage Software ALP"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_amv(FFMpegEncoderOption):
    """ADPCM IMA AMV"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_apm(FFMpegEncoderOption):
    """ADPCM IMA Ubisoft APM"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_qt(FFMpegEncoderOption):
    """ADPCM IMA QuickTime"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_ssi(FFMpegEncoderOption):
    """ADPCM IMA Simon & Schuster Interactive"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_wav(FFMpegEncoderOption):
    """ADPCM IMA WAV"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_ws(FFMpegEncoderOption):
    """ADPCM IMA Westwood"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ms(FFMpegEncoderOption):
    """ADPCM Microsoft"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_swf(FFMpegEncoderOption):
    """ADPCM Shockwave Flash"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_yamaha(FFMpegEncoderOption):
    """ADPCM Yamaha"""

    block_size: int | None = None
    """set the block size (from 32 to 8192) (default 1024)"""


@dataclass(frozen=True, kw_only=True)
class alac(FFMpegEncoderOption):
    """ALAC (Apple Lossless Audio Codec)"""

    min_prediction_order: int | None = None
    """(from 1 to 30) (default 4)"""

    max_prediction_order: int | None = None
    """(from 1 to 30) (default 6)"""


@dataclass(frozen=True, kw_only=True)
class anull(FFMpegEncoderOption):
    """null audio"""


@dataclass(frozen=True, kw_only=True)
class aptx(FFMpegEncoderOption):
    """aptX (Audio Processing Technology for Bluetooth)"""


@dataclass(frozen=True, kw_only=True)
class aptx_hd(FFMpegEncoderOption):
    """aptX HD (Audio Processing Technology for Bluetooth)"""


@dataclass(frozen=True, kw_only=True)
class libcodec2(FFMpegEncoderOption):
    """codec2 encoder using libcodec2 (codec codec2)"""

    mode: int | None = None
    """codec2 mode (from 0 to 8) (default 1300)"""


@dataclass(frozen=True, kw_only=True)
class comfortnoise(FFMpegEncoderOption):
    """RFC 3389 comfort noise generator"""


@dataclass(frozen=True, kw_only=True)
class dfpwm(FFMpegEncoderOption):
    """DFPWM1a audio"""


@dataclass(frozen=True, kw_only=True)
class dca(FFMpegEncoderOption):
    """DCA (DTS Coherent Acoustics) (codec dts)"""


@dataclass(frozen=True, kw_only=True)
class eac3(FFMpegEncoderOption):
    """ATSC A/52 E-AC-3"""


@dataclass(frozen=True, kw_only=True)
class flac(FFMpegEncoderOption):
    """FLAC (Free Lossless Audio Codec)"""

    lpc_coeff_precision: int | None = None
    """LPC coefficient precision (from 0 to 15) (default 15)"""

    lpc_type: int | None = None
    """LPC algorithm (from -1 to 3) (default -1)"""

    lpc_passes: int | None = None
    """Number of passes to use for Cholesky factorization during LPC analysis (from 1 to INT_MAX) (default 2)"""

    min_partition_order: int | None = None
    """(from -1 to 8) (default -1)"""

    max_partition_order: int | None = None
    """(from -1 to 8) (default -1)"""

    prediction_order_method: int | None = None
    """Search method for selecting prediction order (from -1 to 5) (default -1)"""

    ch_mode: int | None = None
    """Stereo decorrelation mode (from -1 to 3) (default auto)"""

    exact_rice_parameters: bool | None = None
    """Calculate rice parameters exactly (default false)"""

    multi_dim_quant: bool | None = None
    """Multi-dimensional quantization (default false)"""

    min_prediction_order: int | None = None
    """(from -1 to 32) (default -1)"""

    max_prediction_order: int | None = None
    """(from -1 to 32) (default -1)"""


@dataclass(frozen=True, kw_only=True)
class g723_1(FFMpegEncoderOption):
    """G.723.1"""


@dataclass(frozen=True, kw_only=True)
class libgsm(FFMpegEncoderOption):
    """libgsm GSM (codec gsm)"""


@dataclass(frozen=True, kw_only=True)
class libgsm_ms(FFMpegEncoderOption):
    """libgsm GSM Microsoft variant (codec gsm_ms)"""


@dataclass(frozen=True, kw_only=True)
class mlp(FFMpegEncoderOption):
    """MLP (Meridian Lossless Packing)"""

    max_interval: int | None = None
    """Max number of frames between each new header (from 8 to 128) (default 16)"""

    lpc_coeff_precision: int | None = None
    """LPC coefficient precision (from 0 to 15) (default 15)"""

    lpc_type: int | None = None
    """LPC algorithm (from 2 to 3) (default levinson)"""

    lpc_passes: int | None = None
    """Number of passes to use for Cholesky factorization during LPC analysis (from 1 to INT_MAX) (default 2)"""

    codebook_search: int | None = None
    """Max number of codebook searches (from 1 to 100) (default 3)"""

    prediction_order: int | None = None
    """Search method for selecting prediction order (from 0 to 4) (default estimation)"""

    rematrix_precision: int | None = None
    """Rematrix coefficient precision (from 0 to 14) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class mp2(FFMpegEncoderOption):
    """MP2 (MPEG audio layer 2)"""


@dataclass(frozen=True, kw_only=True)
class mp2fixed(FFMpegEncoderOption):
    """MP2 fixed point (MPEG audio layer 2) (codec mp2)"""


@dataclass(frozen=True, kw_only=True)
class libtwolame(FFMpegEncoderOption):
    """libtwolame MP2 (MPEG audio layer 2) (codec mp2)"""

    mode: int | None = None
    """Mpeg Mode (from -1 to 3) (default auto)"""

    psymodel: int | None = None
    """Psychoacoustic Model (from -1 to 4) (default 3)"""

    energy_levels: int | None = None
    """enable energy levels (from 0 to 1) (default 0)"""

    error_protection: int | None = None
    """enable CRC error protection (from 0 to 1) (default 0)"""

    copyright: int | None = None
    """set MPEG Audio Copyright flag (from 0 to 1) (default 0)"""

    original: int | None = None
    """set MPEG Audio Original flag (from 0 to 1) (default 0)"""

    verbosity: int | None = None
    """set library optput level (0-10) (from 0 to 10) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class libmp3lame(FFMpegEncoderOption):
    """libmp3lame MP3 (MPEG audio layer 3) (codec mp3)"""

    reservoir: bool | None = None
    """use bit reservoir (default true)"""

    joint_stereo: bool | None = None
    """use joint stereo (default true)"""

    abr: bool | None = None
    """use ABR (default false)"""

    copyright: bool | None = None
    """set copyright flag (default false)"""

    original: bool | None = None
    """set original flag (default true)"""


@dataclass(frozen=True, kw_only=True)
class libshine(FFMpegEncoderOption):
    """libshine MP3 (MPEG audio layer 3) (codec mp3)"""


@dataclass(frozen=True, kw_only=True)
class nellymoser(FFMpegEncoderOption):
    """Nellymoser Asao"""


@dataclass(frozen=True, kw_only=True)
class opus(FFMpegEncoderOption):
    """Opus"""

    opus_delay: float | None = None
    """Maximum delay in milliseconds (from 2.5 to 360) (default 360)"""

    apply_phase_inv: bool | None = None
    """Apply intensity stereo phase inversion (default true)"""


@dataclass(frozen=True, kw_only=True)
class libopus(FFMpegEncoderOption):
    """libopus Opus (codec opus)"""

    application: int | None = None
    """Intended application type (from 2048 to 2051) (default audio)"""

    frame_duration: float | None = None
    """Duration of a frame in milliseconds (from 2.5 to 120) (default 20)"""

    packet_loss: int | None = None
    """Expected packet loss percentage (from 0 to 100) (default 0)"""

    fec: bool | None = None
    """Enable inband FEC. Expected packet loss must be non-zero (default false)"""

    vbr: int | None = None
    """Variable bit rate mode (from 0 to 2) (default on)"""

    mapping_family: int | None = None
    """Channel Mapping Family (from -1 to 255) (default -1)"""

    apply_phase_inv: bool | None = None
    """Apply intensity stereo phase inversion (default true)"""


@dataclass(frozen=True, kw_only=True)
class pcm_alaw(FFMpegEncoderOption):
    """PCM A-law / G.711 A-law"""


@dataclass(frozen=True, kw_only=True)
class pcm_bluray(FFMpegEncoderOption):
    """PCM signed 16|20|24-bit big-endian for Blu-ray media"""


@dataclass(frozen=True, kw_only=True)
class pcm_dvd(FFMpegEncoderOption):
    """PCM signed 16|20|24-bit big-endian for DVD media"""


@dataclass(frozen=True, kw_only=True)
class pcm_f32be(FFMpegEncoderOption):
    """PCM 32-bit floating point big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_f32le(FFMpegEncoderOption):
    """PCM 32-bit floating point little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_f64be(FFMpegEncoderOption):
    """PCM 64-bit floating point big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_f64le(FFMpegEncoderOption):
    """PCM 64-bit floating point little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_mulaw(FFMpegEncoderOption):
    """PCM mu-law / G.711 mu-law"""


@dataclass(frozen=True, kw_only=True)
class pcm_s16be(FFMpegEncoderOption):
    """PCM signed 16-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s16be_planar(FFMpegEncoderOption):
    """PCM signed 16-bit big-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_s16le(FFMpegEncoderOption):
    """PCM signed 16-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s16le_planar(FFMpegEncoderOption):
    """PCM signed 16-bit little-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_s24be(FFMpegEncoderOption):
    """PCM signed 24-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s24daud(FFMpegEncoderOption):
    """PCM D-Cinema audio signed 24-bit"""


@dataclass(frozen=True, kw_only=True)
class pcm_s24le(FFMpegEncoderOption):
    """PCM signed 24-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s24le_planar(FFMpegEncoderOption):
    """PCM signed 24-bit little-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_s32be(FFMpegEncoderOption):
    """PCM signed 32-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s32le(FFMpegEncoderOption):
    """PCM signed 32-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s32le_planar(FFMpegEncoderOption):
    """PCM signed 32-bit little-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_s64be(FFMpegEncoderOption):
    """PCM signed 64-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s64le(FFMpegEncoderOption):
    """PCM signed 64-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s8(FFMpegEncoderOption):
    """PCM signed 8-bit"""


@dataclass(frozen=True, kw_only=True)
class pcm_s8_planar(FFMpegEncoderOption):
    """PCM signed 8-bit planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_u16be(FFMpegEncoderOption):
    """PCM unsigned 16-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u16le(FFMpegEncoderOption):
    """PCM unsigned 16-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u24be(FFMpegEncoderOption):
    """PCM unsigned 24-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u24le(FFMpegEncoderOption):
    """PCM unsigned 24-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u32be(FFMpegEncoderOption):
    """PCM unsigned 32-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u32le(FFMpegEncoderOption):
    """PCM unsigned 32-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u8(FFMpegEncoderOption):
    """PCM unsigned 8-bit"""


@dataclass(frozen=True, kw_only=True)
class pcm_vidc(FFMpegEncoderOption):
    """PCM Archimedes VIDC"""


@dataclass(frozen=True, kw_only=True)
class real_144(FFMpegEncoderOption):
    """RealAudio 1.0 (14.4K) (codec ra_144)"""


@dataclass(frozen=True, kw_only=True)
class roq_dpcm(FFMpegEncoderOption):
    """id RoQ DPCM"""


@dataclass(frozen=True, kw_only=True)
class s302m(FFMpegEncoderOption):
    """SMPTE 302M"""


@dataclass(frozen=True, kw_only=True)
class sbc(FFMpegEncoderOption):
    """SBC (low-complexity subband codec)"""

    sbc_delay: str | None = None
    """set maximum algorithmic latency (default 0.013)"""

    msbc: bool | None = None
    """use mSBC mode (wideband speech mono SBC) (default false)"""


@dataclass(frozen=True, kw_only=True)
class sonic(FFMpegEncoderOption):
    """Sonic"""


@dataclass(frozen=True, kw_only=True)
class sonicls(FFMpegEncoderOption):
    """Sonic lossless"""


@dataclass(frozen=True, kw_only=True)
class libspeex(FFMpegEncoderOption):
    """libspeex Speex (codec speex)"""

    abr: int | None = None
    """Use average bit rate (from 0 to 1) (default 0)"""

    cbr_quality: int | None = None
    """Set quality value (0 to 10) for CBR (from 0 to 10) (default 8)"""

    frames_per_packet: int | None = None
    """Number of frames to encode in each packet (from 1 to 8) (default 1)"""

    vad: int | None = None
    """Voice Activity Detection (from 0 to 1) (default 0)"""

    dtx: int | None = None
    """Discontinuous Transmission (from 0 to 1) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class truehd(FFMpegEncoderOption):
    """TrueHD"""

    max_interval: int | None = None
    """Max number of frames between each new header (from 8 to 128) (default 16)"""

    lpc_coeff_precision: int | None = None
    """LPC coefficient precision (from 0 to 15) (default 15)"""

    lpc_type: int | None = None
    """LPC algorithm (from 2 to 3) (default levinson)"""

    lpc_passes: int | None = None
    """Number of passes to use for Cholesky factorization during LPC analysis (from 1 to INT_MAX) (default 2)"""

    codebook_search: int | None = None
    """Max number of codebook searches (from 1 to 100) (default 3)"""

    prediction_order: int | None = None
    """Search method for selecting prediction order (from 0 to 4) (default estimation)"""

    rematrix_precision: int | None = None
    """Rematrix coefficient precision (from 0 to 14) (default 1)"""


@dataclass(frozen=True, kw_only=True)
class tta(FFMpegEncoderOption):
    """TTA (True Audio)"""


@dataclass(frozen=True, kw_only=True)
class vorbis(FFMpegEncoderOption):
    """Vorbis"""


@dataclass(frozen=True, kw_only=True)
class libvorbis(FFMpegEncoderOption):
    """libvorbis (codec vorbis)"""

    iblock: float | None = None
    """Sets the impulse block bias (from -15 to 0) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class wavpack(FFMpegEncoderOption):
    """WavPack"""

    joint_stereo: bool | None = None
    """(default auto)"""

    optimize_mono: bool | None = None
    """(default false)"""


@dataclass(frozen=True, kw_only=True)
class wmav1(FFMpegEncoderOption):
    """Windows Media Audio 1"""


@dataclass(frozen=True, kw_only=True)
class wmav2(FFMpegEncoderOption):
    """Windows Media Audio 2"""


@dataclass(frozen=True, kw_only=True)
class ssa(FFMpegEncoderOption):
    """ASS (Advanced SubStation Alpha) subtitle (codec ass)"""


@dataclass(frozen=True, kw_only=True)
class ass(FFMpegEncoderOption):
    """ASS (Advanced SubStation Alpha) subtitle"""


@dataclass(frozen=True, kw_only=True)
class dvbsub(FFMpegEncoderOption):
    """DVB subtitles (codec dvb_subtitle)"""


@dataclass(frozen=True, kw_only=True)
class dvdsub(FFMpegEncoderOption):
    """DVD subtitles (codec dvd_subtitle)"""

    palette: str | None = None
    """set the global palette"""

    even_rows_fix: bool | None = None
    """Make number of rows even (workaround for some players) (default false)"""


@dataclass(frozen=True, kw_only=True)
class mov_text(FFMpegEncoderOption):
    """3GPP Timed Text subtitle"""

    height: int | None = None
    """Frame height, usually video height (from 0 to INT_MAX) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class srt(FFMpegEncoderOption):
    """SubRip subtitle (codec subrip)"""


@dataclass(frozen=True, kw_only=True)
class subrip(FFMpegEncoderOption):
    """SubRip subtitle"""


@dataclass(frozen=True, kw_only=True)
class text(FFMpegEncoderOption):
    """Raw text subtitle"""


@dataclass(frozen=True, kw_only=True)
class ttml(FFMpegEncoderOption):
    """TTML subtitle"""


@dataclass(frozen=True, kw_only=True)
class webvtt(FFMpegEncoderOption):
    """WebVTT subtitle"""


@dataclass(frozen=True, kw_only=True)
class xsub(FFMpegEncoderOption):
    """DivX subtitles (XSUB)"""
