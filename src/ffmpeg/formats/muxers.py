# NOTE: this file is auto-generated, do not modify
from ..utils.frozendict import merge
from .schema import FFMpegMuxerOption


def _3g2(
    movflags: str = None,
    moov_size: str = None,
    rtpflags: str = None,
    skip_iods: str = None,
    iods_audio_profile: str = None,
    iods_video_profile: str = None,
    frag_duration: str = None,
    min_frag_duration: str = None,
    frag_size: str = None,
    ism_lookahead: str = None,
    video_track_timescale: str = None,
    brand: str = None,
    use_editlist: str = None,
    fragment_index: str = None,
    mov_gamma: str = None,
    frag_interleave: str = None,
    encryption_scheme: str = None,
    encryption_key: str = None,
    encryption_kid: str = None,
    use_stream_ids_as_track_ids: str = None,
    write_btrt: str = None,
    write_tmcd: str = None,
    write_prft: str = None,
    empty_hdlr_name: str = None,
    movie_timescale: str = None,
) -> FFMpegMuxerOption:
    """
    3GP2 (3GPP2 file format)

    Args:
        movflags: MOV muxer flags (default 0)
        moov_size: maximum moov size so it can be placed at the begin (from 0 to INT_MAX) (default 0)
        rtpflags: RTP muxer flags (default 0)
        skip_iods: Skip writing iods atom. (default true)
        iods_audio_profile: iods audio profile atom. (from -1 to 255) (default -1)
        iods_video_profile: iods video profile atom. (from -1 to 255) (default -1)
        frag_duration: Maximum fragment duration (from 0 to INT_MAX) (default 0)
        min_frag_duration: Minimum fragment duration (from 0 to INT_MAX) (default 0)
        frag_size: Maximum fragment size (from 0 to INT_MAX) (default 0)
        ism_lookahead: Number of lookahead entries for ISM files (from 0 to 255) (default 0)
        video_track_timescale: set timescale of all video tracks (from 0 to INT_MAX) (default 0)
        brand: Override major brand
        use_editlist: use edit list (default auto)
        fragment_index: Fragment number of the next fragment (from 1 to INT_MAX) (default 1)
        mov_gamma: gamma value for gama atom (from 0 to 10) (default 0)
        frag_interleave: Interleave samples within fragments (max number of consecutive samples, lower is tighter interleaving, but with more overhead) (from 0 to INT_MAX) (default 0)
        encryption_scheme: Configures the encryption scheme, allowed values are none, cenc-aes-ctr
        encryption_key: The media encryption key (hex)
        encryption_kid: The media encryption key identifier (hex)
        use_stream_ids_as_track_ids: use stream ids as track ids (default false)
        write_btrt: force or disable writing btrt (default auto)
        write_tmcd: force or disable writing tmcd (default auto)
        write_prft: Write producer reference time box with specified time source (from 0 to 2) (default 0)
        empty_hdlr_name: write zero-length name string in hdlr atoms within mdia and minf atoms (default false)
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movflags": movflags,
                "moov_size": moov_size,
                "rtpflags": rtpflags,
                "skip_iods": skip_iods,
                "iods_audio_profile": iods_audio_profile,
                "iods_video_profile": iods_video_profile,
                "frag_duration": frag_duration,
                "min_frag_duration": min_frag_duration,
                "frag_size": frag_size,
                "ism_lookahead": ism_lookahead,
                "video_track_timescale": video_track_timescale,
                "brand": brand,
                "use_editlist": use_editlist,
                "fragment_index": fragment_index,
                "mov_gamma": mov_gamma,
                "frag_interleave": frag_interleave,
                "encryption_scheme": encryption_scheme,
                "encryption_key": encryption_key,
                "encryption_kid": encryption_kid,
                "use_stream_ids_as_track_ids": use_stream_ids_as_track_ids,
                "write_btrt": write_btrt,
                "write_tmcd": write_tmcd,
                "write_prft": write_prft,
                "empty_hdlr_name": empty_hdlr_name,
                "movie_timescale": movie_timescale,
            }
        )
    )


def _3gp(
    movflags: str = None,
    moov_size: str = None,
    rtpflags: str = None,
    skip_iods: str = None,
    iods_audio_profile: str = None,
    iods_video_profile: str = None,
    frag_duration: str = None,
    min_frag_duration: str = None,
    frag_size: str = None,
    ism_lookahead: str = None,
    video_track_timescale: str = None,
    brand: str = None,
    use_editlist: str = None,
    fragment_index: str = None,
    mov_gamma: str = None,
    frag_interleave: str = None,
    encryption_scheme: str = None,
    encryption_key: str = None,
    encryption_kid: str = None,
    use_stream_ids_as_track_ids: str = None,
    write_btrt: str = None,
    write_tmcd: str = None,
    write_prft: str = None,
    empty_hdlr_name: str = None,
    movie_timescale: str = None,
) -> FFMpegMuxerOption:
    """
    3GP (3GPP file format)

    Args:
        movflags: MOV muxer flags (default 0)
        moov_size: maximum moov size so it can be placed at the begin (from 0 to INT_MAX) (default 0)
        rtpflags: RTP muxer flags (default 0)
        skip_iods: Skip writing iods atom. (default true)
        iods_audio_profile: iods audio profile atom. (from -1 to 255) (default -1)
        iods_video_profile: iods video profile atom. (from -1 to 255) (default -1)
        frag_duration: Maximum fragment duration (from 0 to INT_MAX) (default 0)
        min_frag_duration: Minimum fragment duration (from 0 to INT_MAX) (default 0)
        frag_size: Maximum fragment size (from 0 to INT_MAX) (default 0)
        ism_lookahead: Number of lookahead entries for ISM files (from 0 to 255) (default 0)
        video_track_timescale: set timescale of all video tracks (from 0 to INT_MAX) (default 0)
        brand: Override major brand
        use_editlist: use edit list (default auto)
        fragment_index: Fragment number of the next fragment (from 1 to INT_MAX) (default 1)
        mov_gamma: gamma value for gama atom (from 0 to 10) (default 0)
        frag_interleave: Interleave samples within fragments (max number of consecutive samples, lower is tighter interleaving, but with more overhead) (from 0 to INT_MAX) (default 0)
        encryption_scheme: Configures the encryption scheme, allowed values are none, cenc-aes-ctr
        encryption_key: The media encryption key (hex)
        encryption_kid: The media encryption key identifier (hex)
        use_stream_ids_as_track_ids: use stream ids as track ids (default false)
        write_btrt: force or disable writing btrt (default auto)
        write_tmcd: force or disable writing tmcd (default auto)
        write_prft: Write producer reference time box with specified time source (from 0 to 2) (default 0)
        empty_hdlr_name: write zero-length name string in hdlr atoms within mdia and minf atoms (default false)
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movflags": movflags,
                "moov_size": moov_size,
                "rtpflags": rtpflags,
                "skip_iods": skip_iods,
                "iods_audio_profile": iods_audio_profile,
                "iods_video_profile": iods_video_profile,
                "frag_duration": frag_duration,
                "min_frag_duration": min_frag_duration,
                "frag_size": frag_size,
                "ism_lookahead": ism_lookahead,
                "video_track_timescale": video_track_timescale,
                "brand": brand,
                "use_editlist": use_editlist,
                "fragment_index": fragment_index,
                "mov_gamma": mov_gamma,
                "frag_interleave": frag_interleave,
                "encryption_scheme": encryption_scheme,
                "encryption_key": encryption_key,
                "encryption_kid": encryption_kid,
                "use_stream_ids_as_track_ids": use_stream_ids_as_track_ids,
                "write_btrt": write_btrt,
                "write_tmcd": write_tmcd,
                "write_prft": write_prft,
                "empty_hdlr_name": empty_hdlr_name,
                "movie_timescale": movie_timescale,
            }
        )
    )


def a64() -> FFMpegMuxerOption:
    """
    a64 - video for Commodore 64


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def ac3() -> FFMpegMuxerOption:
    """
    raw AC-3


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def ac4(
    write_crc: str = None,
) -> FFMpegMuxerOption:
    """
    raw AC-4

    Args:
        write_crc: enable checksum (default false)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "write_crc": write_crc,
            }
        )
    )


def adts(
    write_id3v2: str = None,
    write_apetag: str = None,
    write_mpeg2: str = None,
) -> FFMpegMuxerOption:
    """
    ADTS AAC (Advanced Audio Coding)

    Args:
        write_id3v2: Enable ID3v2 tag writing (default false)
        write_apetag: Enable APE tag writing (default false)
        write_mpeg2: Set MPEG version to MPEG-2 (default false)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "write_id3v2": write_id3v2,
                "write_apetag": write_apetag,
                "write_mpeg2": write_mpeg2,
            }
        )
    )


def adx() -> FFMpegMuxerOption:
    """
    CRI ADX


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def aiff(
    write_id3v2: str = None,
    id3v2_version: str = None,
) -> FFMpegMuxerOption:
    """
    Audio IFF

    Args:
        write_id3v2: Enable ID3 tags writing. (default false)
        id3v2_version: Select ID3v2 version to write. Currently 3 and 4 are supported. (from 3 to 4) (default 4)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "write_id3v2": write_id3v2,
                "id3v2_version": id3v2_version,
            }
        )
    )


def alaw() -> FFMpegMuxerOption:
    """
    PCM A-law


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def alp(
    type: str = None,
) -> FFMpegMuxerOption:
    """
    LEGO Racers ALP

    Args:
        type: set file type (from 0 to 2) (default auto)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "type": type,
            }
        )
    )


def alsa() -> FFMpegMuxerOption:
    """
    ALSA audio output


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def amr() -> FFMpegMuxerOption:
    """
    3GPP AMR


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def amv() -> FFMpegMuxerOption:
    """
    AMV


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def apm() -> FFMpegMuxerOption:
    """
    Ubisoft Rayman 2 APM


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def apng(
    plays: str = None,
    final_delay: str = None,
) -> FFMpegMuxerOption:
    """
    Animated Portable Network Graphics

    Args:
        plays: Number of times to play the output: 0 - infinite loop, 1 - no loop (from 0 to 65535) (default 1)
        final_delay: Force delay after the last frame (from 0 to 65535) (default 0/1)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "plays": plays,
                "final_delay": final_delay,
            }
        )
    )


def aptx() -> FFMpegMuxerOption:
    """
    raw aptX (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def aptx_hd() -> FFMpegMuxerOption:
    """
    raw aptX HD (Audio Processing Technology for Bluetooth)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def argo_asf(
    version_major: str = None,
    version_minor: str = None,
    name: str = None,
) -> FFMpegMuxerOption:
    """
    Argonaut Games ASF

    Args:
        version_major: override file major version (from 0 to 65535) (default 2)
        version_minor: override file minor version (from 0 to 65535) (default 1)
        name: embedded file name (max 8 characters)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "version_major": version_major,
                "version_minor": version_minor,
                "name": name,
            }
        )
    )


def argo_cvg(
    skip_rate_check: str = None,
    loop: str = None,
    reverb: str = None,
) -> FFMpegMuxerOption:
    """
    Argonaut Games CVG

    Args:
        skip_rate_check: skip sample rate check (default false)
        loop: set loop flag (default false)
        reverb: set reverb flag (default true)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "skip_rate_check": skip_rate_check,
                "loop": loop,
                "reverb": reverb,
            }
        )
    )


def asf(
    packet_size: str = None,
) -> FFMpegMuxerOption:
    """
    ASF (Advanced / Active Streaming Format)

    Args:
        packet_size: Packet size (from 100 to 65536) (default 3200)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "packet_size": packet_size,
            }
        )
    )


def asf_stream(
    packet_size: str = None,
) -> FFMpegMuxerOption:
    """
    ASF (Advanced / Active Streaming Format)

    Args:
        packet_size: Packet size (from 100 to 65536) (default 3200)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "packet_size": packet_size,
            }
        )
    )


def ass(
    ignore_readorder: str = None,
) -> FFMpegMuxerOption:
    """
    SSA (SubStation Alpha) subtitle

    Args:
        ignore_readorder: write events immediately, even if they're out-of-order (default false)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "ignore_readorder": ignore_readorder,
            }
        )
    )


def ast(
    loopstart: str = None,
    loopend: str = None,
) -> FFMpegMuxerOption:
    """
    AST (Audio Stream)

    Args:
        loopstart: Loopstart position in milliseconds. (from -1 to INT_MAX) (default -1)
        loopend: Loopend position in milliseconds. (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "loopstart": loopstart,
                "loopend": loopend,
            }
        )
    )


def au() -> FFMpegMuxerOption:
    """
    Sun AU


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def avi(
    reserve_index_space: str = None,
    write_channel_mask: str = None,
    flipped_raw_rgb: str = None,
) -> FFMpegMuxerOption:
    """
    AVI (Audio Video Interleaved)

    Args:
        reserve_index_space: reserve space (in bytes) at the beginning of the file for each stream index (from 0 to INT_MAX) (default 0)
        write_channel_mask: write channel mask into wave format header (default true)
        flipped_raw_rgb: Raw RGB bitmaps are stored bottom-up (default false)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "reserve_index_space": reserve_index_space,
                "write_channel_mask": write_channel_mask,
                "flipped_raw_rgb": flipped_raw_rgb,
            }
        )
    )


def avif(
    movie_timescale: str = None,
    loop: str = None,
) -> FFMpegMuxerOption:
    """
    AVIF

    Args:
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)
        loop: Number of times to loop animated AVIF: 0 - infinite loop (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movie_timescale": movie_timescale,
                "loop": loop,
            }
        )
    )


def avm2() -> FFMpegMuxerOption:
    """
    SWF (ShockWave Flash) (AVM2)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def avs2() -> FFMpegMuxerOption:
    """
    raw AVS2-P2/IEEE1857.4 video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def avs3() -> FFMpegMuxerOption:
    """
    AVS3-P2/IEEE1857.10


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def bit() -> FFMpegMuxerOption:
    """
    G.729 BIT file format


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def caca(
    window_size: str = None,
    window_title: str = None,
    driver: str = None,
    algorithm: str = None,
    antialias: str = None,
    charset: str = None,
    color: str = None,
    list_drivers: str = None,
    list_dither: str = None,
) -> FFMpegMuxerOption:
    """
    caca (color ASCII art) output device

    Args:
        window_size: set window forced size
        window_title: set window title
        driver: set display driver
        algorithm: set dithering algorithm (default "default")
        antialias: set antialias method (default "default")
        charset: set charset used to render output (default "default")
        color: set color used to render output (default "default")
        list_drivers: list available drivers (default false)
        list_dither: list available dither options

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "window_size": window_size,
                "window_title": window_title,
                "driver": driver,
                "algorithm": algorithm,
                "antialias": antialias,
                "charset": charset,
                "color": color,
                "list_drivers": list_drivers,
                "list_dither": list_dither,
            }
        )
    )


def caf() -> FFMpegMuxerOption:
    """
    Apple CAF (Core Audio Format)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def cavsvideo() -> FFMpegMuxerOption:
    """
    raw Chinese AVS (Audio Video Standard) video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def chromaprint(
    silence_threshold: str = None,
    algorithm: str = None,
    fp_format: str = None,
) -> FFMpegMuxerOption:
    """
    Chromaprint

    Args:
        silence_threshold: threshold for detecting silence (from -1 to 32767) (default -1)
        algorithm: version of the fingerprint algorithm (from 0 to INT_MAX) (default 1)
        fp_format: fingerprint format to write (from 0 to 2) (default base64)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "silence_threshold": silence_threshold,
                "algorithm": algorithm,
                "fp_format": fp_format,
            }
        )
    )


def codec2() -> FFMpegMuxerOption:
    """
    codec2 .c2 muxer


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def codec2raw() -> FFMpegMuxerOption:
    """
    raw codec2 muxer


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def crc() -> FFMpegMuxerOption:
    """
    CRC testing


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def dash(
    adaptation_sets: str = None,
    window_size: str = None,
    extra_window_size: str = None,
    seg_duration: str = None,
    frag_duration: str = None,
    frag_type: str = None,
    remove_at_exit: str = None,
    use_template: str = None,
    use_timeline: str = None,
    single_file: str = None,
    single_file_name: str = None,
    init_seg_name: str = None,
    media_seg_name: str = None,
    utc_timing_url: str = None,
    method: str = None,
    http_user_agent: str = None,
    http_persistent: str = None,
    hls_playlist: str = None,
    hls_master_name: str = None,
    streaming: str = None,
    timeout: str = None,
    index_correction: str = None,
    format_options: str = None,
    global_sidx: str = None,
    dash_segment_type: str = None,
    ignore_io_errors: str = None,
    lhls: str = None,
    ldash: str = None,
    master_m3u8_publish_rate: str = None,
    write_prft: str = None,
    mpd_profile: str = None,
    http_opts: str = None,
    target_latency: str = None,
    min_playback_rate: str = None,
    max_playback_rate: str = None,
    update_period: str = None,
) -> FFMpegMuxerOption:
    """
    DASH Muxer

    Args:
        adaptation_sets: Adaptation sets. Syntax: id=0,streams=0,1,2 id=1,streams=3,4 and so on
        window_size: number of segments kept in the manifest (from 0 to INT_MAX) (default 0)
        extra_window_size: number of segments kept outside of the manifest before removing from disk (from 0 to INT_MAX) (default 5)
        seg_duration: segment duration (in seconds, fractional value can be set) (default 5)
        frag_duration: fragment duration (in seconds, fractional value can be set) (default 0)
        frag_type: set type of interval for fragments (from 0 to 3) (default none)
        remove_at_exit: remove all segments when finished (default false)
        use_template: Use SegmentTemplate instead of SegmentList (default true)
        use_timeline: Use SegmentTimeline in SegmentTemplate (default true)
        single_file: Store all segments in one file, accessed using byte ranges (default false)
        single_file_name: DASH-templated name to be used for baseURL. Implies storing all segments in one file, accessed using byte ranges
        init_seg_name: DASH-templated name to used for the initialization segment (default "init-stream$RepresentationID$.$ext$")
        media_seg_name: DASH-templated name to used for the media segments (default "chunk-stream$RepresentationID$-$Number%05d$.$ext$")
        utc_timing_url: URL of the page that will return the UTC timestamp in ISO format
        method: set the HTTP method
        http_user_agent: override User-Agent field in HTTP header
        http_persistent: Use persistent HTTP connections (default false)
        hls_playlist: Generate HLS playlist files(master.m3u8, media_%d.m3u8) (default false)
        hls_master_name: HLS master playlist name (default "master.m3u8")
        streaming: Enable/Disable streaming mode of output. Each frame will be moof fragment (default false)
        timeout: set timeout for socket I/O operations (default -0.000001)
        index_correction: Enable/Disable segment index correction logic (default false)
        format_options: set list of options for the container format (mp4/webm) used for dash
        global_sidx: Write global SIDX atom. Applicable only for single file, mp4 output, non-streaming mode (default false)
        dash_segment_type: set dash segment files type (from 0 to 2) (default auto)
        ignore_io_errors: Ignore IO errors during open and write. Useful for long-duration runs with network output (default false)
        lhls: Enable Low-latency HLS(Experimental). Adds #EXT-X-PREFETCH tag with current segment's URI (default false)
        ldash: Enable Low-latency dash. Constrains the value of a few elements (default false)
        master_m3u8_publish_rate: Publish master playlist every after this many segment intervals (from 0 to UINT32_MAX) (default 0)
        write_prft: Write producer reference time element (default auto)
        mpd_profile: Set profiles. Elements and values used in the manifest may be constrained by them (default dash)
        http_opts: HTTP protocol options
        target_latency: Set desired target latency for Low-latency dash (default 0)
        min_playback_rate: Set desired minimum playback rate (from 0.5 to 1.5) (default 1/1)
        max_playback_rate: Set desired maximum playback rate (from 0.5 to 1.5) (default 1/1)
        update_period: Set the mpd update interval (from 0 to I64_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "adaptation_sets": adaptation_sets,
                "window_size": window_size,
                "extra_window_size": extra_window_size,
                "seg_duration": seg_duration,
                "frag_duration": frag_duration,
                "frag_type": frag_type,
                "remove_at_exit": remove_at_exit,
                "use_template": use_template,
                "use_timeline": use_timeline,
                "single_file": single_file,
                "single_file_name": single_file_name,
                "init_seg_name": init_seg_name,
                "media_seg_name": media_seg_name,
                "utc_timing_url": utc_timing_url,
                "method": method,
                "http_user_agent": http_user_agent,
                "http_persistent": http_persistent,
                "hls_playlist": hls_playlist,
                "hls_master_name": hls_master_name,
                "streaming": streaming,
                "timeout": timeout,
                "index_correction": index_correction,
                "format_options": format_options,
                "global_sidx": global_sidx,
                "dash_segment_type": dash_segment_type,
                "ignore_io_errors": ignore_io_errors,
                "lhls": lhls,
                "ldash": ldash,
                "master_m3u8_publish_rate": master_m3u8_publish_rate,
                "write_prft": write_prft,
                "mpd_profile": mpd_profile,
                "http_opts": http_opts,
                "target_latency": target_latency,
                "min_playback_rate": min_playback_rate,
                "max_playback_rate": max_playback_rate,
                "update_period": update_period,
            }
        )
    )


def data() -> FFMpegMuxerOption:
    """
    raw data


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def daud() -> FFMpegMuxerOption:
    """
    D-Cinema audio


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def dfpwm() -> FFMpegMuxerOption:
    """
    raw DFPWM1a


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def dirac() -> FFMpegMuxerOption:
    """
    raw Dirac


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def dnxhd() -> FFMpegMuxerOption:
    """
    raw DNxHD (SMPTE VC-3)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def dts() -> FFMpegMuxerOption:
    """
    raw DTS


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def dv() -> FFMpegMuxerOption:
    """
    DV (Digital Video)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def dvd(
    muxrate: str = None,
    preload: str = None,
) -> FFMpegMuxerOption:
    """
    MPEG-2 PS (DVD VOB)

    Args:
        muxrate: (from 0 to 1.67772e+09) (default 0)
        preload: Initial demux-decode delay in microseconds. (from 0 to INT_MAX) (default 500000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "muxrate": muxrate,
                "preload": preload,
            }
        )
    )


def eac3() -> FFMpegMuxerOption:
    """
    raw E-AC-3


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def evc() -> FFMpegMuxerOption:
    """
    raw EVC video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def f32be() -> FFMpegMuxerOption:
    """
    PCM 32-bit floating-point big-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def f32le() -> FFMpegMuxerOption:
    """
    PCM 32-bit floating-point little-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def f4v(
    movflags: str = None,
    moov_size: str = None,
    rtpflags: str = None,
    skip_iods: str = None,
    iods_audio_profile: str = None,
    iods_video_profile: str = None,
    frag_duration: str = None,
    min_frag_duration: str = None,
    frag_size: str = None,
    ism_lookahead: str = None,
    video_track_timescale: str = None,
    brand: str = None,
    use_editlist: str = None,
    fragment_index: str = None,
    mov_gamma: str = None,
    frag_interleave: str = None,
    encryption_scheme: str = None,
    encryption_key: str = None,
    encryption_kid: str = None,
    use_stream_ids_as_track_ids: str = None,
    write_btrt: str = None,
    write_tmcd: str = None,
    write_prft: str = None,
    empty_hdlr_name: str = None,
    movie_timescale: str = None,
) -> FFMpegMuxerOption:
    """
    F4V Adobe Flash Video

    Args:
        movflags: MOV muxer flags (default 0)
        moov_size: maximum moov size so it can be placed at the begin (from 0 to INT_MAX) (default 0)
        rtpflags: RTP muxer flags (default 0)
        skip_iods: Skip writing iods atom. (default true)
        iods_audio_profile: iods audio profile atom. (from -1 to 255) (default -1)
        iods_video_profile: iods video profile atom. (from -1 to 255) (default -1)
        frag_duration: Maximum fragment duration (from 0 to INT_MAX) (default 0)
        min_frag_duration: Minimum fragment duration (from 0 to INT_MAX) (default 0)
        frag_size: Maximum fragment size (from 0 to INT_MAX) (default 0)
        ism_lookahead: Number of lookahead entries for ISM files (from 0 to 255) (default 0)
        video_track_timescale: set timescale of all video tracks (from 0 to INT_MAX) (default 0)
        brand: Override major brand
        use_editlist: use edit list (default auto)
        fragment_index: Fragment number of the next fragment (from 1 to INT_MAX) (default 1)
        mov_gamma: gamma value for gama atom (from 0 to 10) (default 0)
        frag_interleave: Interleave samples within fragments (max number of consecutive samples, lower is tighter interleaving, but with more overhead) (from 0 to INT_MAX) (default 0)
        encryption_scheme: Configures the encryption scheme, allowed values are none, cenc-aes-ctr
        encryption_key: The media encryption key (hex)
        encryption_kid: The media encryption key identifier (hex)
        use_stream_ids_as_track_ids: use stream ids as track ids (default false)
        write_btrt: force or disable writing btrt (default auto)
        write_tmcd: force or disable writing tmcd (default auto)
        write_prft: Write producer reference time box with specified time source (from 0 to 2) (default 0)
        empty_hdlr_name: write zero-length name string in hdlr atoms within mdia and minf atoms (default false)
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movflags": movflags,
                "moov_size": moov_size,
                "rtpflags": rtpflags,
                "skip_iods": skip_iods,
                "iods_audio_profile": iods_audio_profile,
                "iods_video_profile": iods_video_profile,
                "frag_duration": frag_duration,
                "min_frag_duration": min_frag_duration,
                "frag_size": frag_size,
                "ism_lookahead": ism_lookahead,
                "video_track_timescale": video_track_timescale,
                "brand": brand,
                "use_editlist": use_editlist,
                "fragment_index": fragment_index,
                "mov_gamma": mov_gamma,
                "frag_interleave": frag_interleave,
                "encryption_scheme": encryption_scheme,
                "encryption_key": encryption_key,
                "encryption_kid": encryption_kid,
                "use_stream_ids_as_track_ids": use_stream_ids_as_track_ids,
                "write_btrt": write_btrt,
                "write_tmcd": write_tmcd,
                "write_prft": write_prft,
                "empty_hdlr_name": empty_hdlr_name,
                "movie_timescale": movie_timescale,
            }
        )
    )


def f64be() -> FFMpegMuxerOption:
    """
    PCM 64-bit floating-point big-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def f64le() -> FFMpegMuxerOption:
    """
    PCM 64-bit floating-point little-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def fbdev(
    xoffset: str = None,
    yoffset: str = None,
) -> FFMpegMuxerOption:
    """
    Linux framebuffer

    Args:
        xoffset: set x coordinate of top left corner (from INT_MIN to INT_MAX) (default 0)
        yoffset: set y coordinate of top left corner (from INT_MIN to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "xoffset": xoffset,
                "yoffset": yoffset,
            }
        )
    )


def ffmetadata() -> FFMpegMuxerOption:
    """
    FFmpeg metadata in text


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def fifo(
    fifo_format: str = None,
    queue_size: str = None,
    format_opts: str = None,
    drop_pkts_on_overflow: str = None,
    restart_with_keyframe: str = None,
    attempt_recovery: str = None,
    max_recovery_attempts: str = None,
    recovery_wait_time: str = None,
    recovery_wait_streamtime: str = None,
    recover_any_error: str = None,
    timeshift: str = None,
) -> FFMpegMuxerOption:
    """
    FIFO queue pseudo-muxer

    Args:
        fifo_format: Target muxer
        queue_size: Size of fifo queue (from 1 to INT_MAX) (default 60)
        format_opts: Options to be passed to underlying muxer
        drop_pkts_on_overflow: Drop packets on fifo queue overflow not to block encoder (default false)
        restart_with_keyframe: Wait for keyframe when restarting output (default false)
        attempt_recovery: Attempt recovery in case of failure (default false)
        max_recovery_attempts: Maximal number of recovery attempts (from 0 to INT_MAX) (default 0)
        recovery_wait_time: Waiting time between recovery attempts (default 5)
        recovery_wait_streamtime: Use stream time instead of real time while waiting for recovery (default false)
        recover_any_error: Attempt recovery regardless of type of the error (default false)
        timeshift: Delay fifo output (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "fifo_format": fifo_format,
                "queue_size": queue_size,
                "format_opts": format_opts,
                "drop_pkts_on_overflow": drop_pkts_on_overflow,
                "restart_with_keyframe": restart_with_keyframe,
                "attempt_recovery": attempt_recovery,
                "max_recovery_attempts": max_recovery_attempts,
                "recovery_wait_time": recovery_wait_time,
                "recovery_wait_streamtime": recovery_wait_streamtime,
                "recover_any_error": recover_any_error,
                "timeshift": timeshift,
            }
        )
    )


def fifo_test(
    write_header_ret: str = None,
    write_trailer_ret: str = None,
    print_deinit_summary: str = None,
) -> FFMpegMuxerOption:
    """
    Fifo test muxer

    Args:
        write_header_ret: write_header() return value (from INT_MIN to INT_MAX) (default 0)
        write_trailer_ret: write_trailer() return value (from INT_MIN to INT_MAX) (default 0)
        print_deinit_summary: print summary when deinitializing muxer (default true)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "write_header_ret": write_header_ret,
                "write_trailer_ret": write_trailer_ret,
                "print_deinit_summary": print_deinit_summary,
            }
        )
    )


def film_cpk() -> FFMpegMuxerOption:
    """
    Sega FILM / CPK


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def filmstrip() -> FFMpegMuxerOption:
    """
    Adobe Filmstrip


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def fits() -> FFMpegMuxerOption:
    """
    Flexible Image Transport System


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def flac(
    write_header: str = None,
) -> FFMpegMuxerOption:
    """
    raw FLAC

    Args:
        write_header: Write the file header (default true)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "write_header": write_header,
            }
        )
    )


def flv(
    flvflags: str = None,
) -> FFMpegMuxerOption:
    """
    FLV (Flash Video)

    Args:
        flvflags: FLV muxer flags (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "flvflags": flvflags,
            }
        )
    )


def framecrc() -> FFMpegMuxerOption:
    """
    framecrc testing


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def framehash(
    hash: str = None,
    format_version: str = None,
) -> FFMpegMuxerOption:
    """
    Per-frame hash testing

    Args:
        hash: set hash to use (default "sha256")
        format_version: file format version (from 1 to 2) (default 2)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "hash": hash,
                "format_version": format_version,
            }
        )
    )


def framemd5(
    hash: str = None,
    format_version: str = None,
) -> FFMpegMuxerOption:
    """
    Per-frame MD5 testing

    Args:
        hash: set hash to use (default "md5")
        format_version: file format version (from 1 to 2) (default 2)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "hash": hash,
                "format_version": format_version,
            }
        )
    )


def g722() -> FFMpegMuxerOption:
    """
    raw G.722


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def g723_1() -> FFMpegMuxerOption:
    """
    raw G.723.1


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def g726() -> FFMpegMuxerOption:
    """
    raw big-endian G.726 ("left-justified")


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def g726le() -> FFMpegMuxerOption:
    """
    raw little-endian G.726 ("right-justified")


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def gif(
    loop: str = None,
    final_delay: str = None,
) -> FFMpegMuxerOption:
    """
    CompuServe Graphics Interchange Format (GIF)

    Args:
        loop: Number of times to loop the output: -1 - no loop, 0 - infinite loop (from -1 to 65535) (default 0)
        final_delay: Force delay (in centiseconds) after the last frame (from -1 to 65535) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "loop": loop,
                "final_delay": final_delay,
            }
        )
    )


def gsm() -> FFMpegMuxerOption:
    """
    raw GSM


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def gxf() -> FFMpegMuxerOption:
    """
    GXF (General eXchange Format)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def h261() -> FFMpegMuxerOption:
    """
    raw H.261


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def h263() -> FFMpegMuxerOption:
    """
    raw H.263


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def h264() -> FFMpegMuxerOption:
    """
    raw H.264 video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def hash(
    hash: str = None,
) -> FFMpegMuxerOption:
    """
    Hash testing

    Args:
        hash: set hash to use (default "sha256")

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "hash": hash,
            }
        )
    )


def hds(
    window_size: str = None,
    extra_window_size: str = None,
    min_frag_duration: str = None,
    remove_at_exit: str = None,
) -> FFMpegMuxerOption:
    """
    HDS Muxer

    Args:
        window_size: number of fragments kept in the manifest (from 0 to INT_MAX) (default 0)
        extra_window_size: number of fragments kept outside of the manifest before removing from disk (from 0 to INT_MAX) (default 5)
        min_frag_duration: minimum fragment duration (in microseconds) (from 0 to INT_MAX) (default 10000000)
        remove_at_exit: remove all fragments when finished (default false)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "window_size": window_size,
                "extra_window_size": extra_window_size,
                "min_frag_duration": min_frag_duration,
                "remove_at_exit": remove_at_exit,
            }
        )
    )


def hevc() -> FFMpegMuxerOption:
    """
    raw HEVC video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def hls(
    start_number: str = None,
    hls_time: str = None,
    hls_init_time: str = None,
    hls_list_size: str = None,
    hls_delete_threshold: str = None,
    hls_vtt_options: str = None,
    hls_allow_cache: str = None,
    hls_base_url: str = None,
    hls_segment_filename: str = None,
    hls_segment_options: str = None,
    hls_segment_size: str = None,
    hls_key_info_file: str = None,
    hls_enc: str = None,
    hls_enc_key: str = None,
    hls_enc_key_url: str = None,
    hls_enc_iv: str = None,
    hls_subtitle_path: str = None,
    hls_segment_type: str = None,
    hls_fmp4_init_filename: str = None,
    hls_fmp4_init_resend: str = None,
    hls_flags: str = None,
    strftime: str = None,
    strftime_mkdir: str = None,
    hls_playlist_type: str = None,
    method: str = None,
    hls_start_number_source: str = None,
    http_user_agent: str = None,
    var_stream_map: str = None,
    cc_stream_map: str = None,
    master_pl_name: str = None,
    master_pl_publish_rate: str = None,
    http_persistent: str = None,
    timeout: str = None,
    ignore_io_errors: str = None,
    headers: str = None,
) -> FFMpegMuxerOption:
    """
    Apple HTTP Live Streaming

    Args:
        start_number: set first number in the sequence (from 0 to I64_MAX) (default 0)
        hls_time: set segment length (default 2)
        hls_init_time: set segment length at init list (default 0)
        hls_list_size: set maximum number of playlist entries (from 0 to INT_MAX) (default 5)
        hls_delete_threshold: set number of unreferenced segments to keep before deleting (from 1 to INT_MAX) (default 1)
        hls_vtt_options: set hls vtt list of options for the container format used for hls
        hls_allow_cache: explicitly set whether the client MAY (1) or MUST NOT (0) cache media segments (from INT_MIN to INT_MAX) (default -1)
        hls_base_url: url to prepend to each playlist entry
        hls_segment_filename: filename template for segment files
        hls_segment_options: set segments files format options of hls
        hls_segment_size: maximum size per segment file, (in bytes) (from 0 to INT_MAX) (default 0)
        hls_key_info_file: file with key URI and key file path
        hls_enc: enable AES128 encryption support (default false)
        hls_enc_key: hex-coded 16 byte key to encrypt the segments
        hls_enc_key_url: url to access the key to decrypt the segments
        hls_enc_iv: hex-coded 16 byte initialization vector
        hls_subtitle_path: set path of hls subtitles
        hls_segment_type: set hls segment files type (from 0 to 1) (default mpegts)
        hls_fmp4_init_filename: set fragment mp4 file init filename (default "init.mp4")
        hls_fmp4_init_resend: resend fragment mp4 init file after refresh m3u8 every time (default false)
        hls_flags: set flags affecting HLS playlist and media file generation (default 0)
        strftime: set filename expansion with strftime at segment creation (default false)
        strftime_mkdir: create last directory component in strftime-generated filename (default false)
        hls_playlist_type: set the HLS playlist type (from 0 to 2) (default 0)
        method: set the HTTP method(default: PUT)
        hls_start_number_source: set source of first number in sequence (from 0 to 3) (default generic)
        http_user_agent: override User-Agent field in HTTP header
        var_stream_map: Variant stream map string
        cc_stream_map: Closed captions stream map string
        master_pl_name: Create HLS master playlist with this name
        master_pl_publish_rate: Publish master play list every after this many segment intervals (from 0 to UINT32_MAX) (default 0)
        http_persistent: Use persistent HTTP connections (default false)
        timeout: set timeout for socket I/O operations (default -0.000001)
        ignore_io_errors: Ignore IO errors for stable long-duration runs with network output (default false)
        headers: set custom HTTP headers, can override built in default headers

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "start_number": start_number,
                "hls_time": hls_time,
                "hls_init_time": hls_init_time,
                "hls_list_size": hls_list_size,
                "hls_delete_threshold": hls_delete_threshold,
                "hls_vtt_options": hls_vtt_options,
                "hls_allow_cache": hls_allow_cache,
                "hls_base_url": hls_base_url,
                "hls_segment_filename": hls_segment_filename,
                "hls_segment_options": hls_segment_options,
                "hls_segment_size": hls_segment_size,
                "hls_key_info_file": hls_key_info_file,
                "hls_enc": hls_enc,
                "hls_enc_key": hls_enc_key,
                "hls_enc_key_url": hls_enc_key_url,
                "hls_enc_iv": hls_enc_iv,
                "hls_subtitle_path": hls_subtitle_path,
                "hls_segment_type": hls_segment_type,
                "hls_fmp4_init_filename": hls_fmp4_init_filename,
                "hls_fmp4_init_resend": hls_fmp4_init_resend,
                "hls_flags": hls_flags,
                "strftime": strftime,
                "strftime_mkdir": strftime_mkdir,
                "hls_playlist_type": hls_playlist_type,
                "method": method,
                "hls_start_number_source": hls_start_number_source,
                "http_user_agent": http_user_agent,
                "var_stream_map": var_stream_map,
                "cc_stream_map": cc_stream_map,
                "master_pl_name": master_pl_name,
                "master_pl_publish_rate": master_pl_publish_rate,
                "http_persistent": http_persistent,
                "timeout": timeout,
                "ignore_io_errors": ignore_io_errors,
                "headers": headers,
            }
        )
    )


def ico() -> FFMpegMuxerOption:
    """
    Microsoft Windows ICO


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def ilbc() -> FFMpegMuxerOption:
    """
    iLBC storage


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def image2(
    update: str = None,
    start_number: str = None,
    strftime: str = None,
    frame_pts: str = None,
    atomic_writing: str = None,
    protocol_opts: str = None,
) -> FFMpegMuxerOption:
    """
    image2 sequence

    Args:
        update: continuously overwrite one file (default false)
        start_number: set first number in the sequence (from 0 to INT_MAX) (default 1)
        strftime: use strftime for filename (default false)
        frame_pts: use current frame pts for filename (default false)
        atomic_writing: write files atomically (using temporary files and renames) (default false)
        protocol_opts: specify protocol options for the opened files

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "update": update,
                "start_number": start_number,
                "strftime": strftime,
                "frame_pts": frame_pts,
                "atomic_writing": atomic_writing,
                "protocol_opts": protocol_opts,
            }
        )
    )


def image2pipe() -> FFMpegMuxerOption:
    """
    piped image2 sequence


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def ipod(
    movflags: str = None,
    moov_size: str = None,
    rtpflags: str = None,
    skip_iods: str = None,
    iods_audio_profile: str = None,
    iods_video_profile: str = None,
    frag_duration: str = None,
    min_frag_duration: str = None,
    frag_size: str = None,
    ism_lookahead: str = None,
    video_track_timescale: str = None,
    brand: str = None,
    use_editlist: str = None,
    fragment_index: str = None,
    mov_gamma: str = None,
    frag_interleave: str = None,
    encryption_scheme: str = None,
    encryption_key: str = None,
    encryption_kid: str = None,
    use_stream_ids_as_track_ids: str = None,
    write_btrt: str = None,
    write_tmcd: str = None,
    write_prft: str = None,
    empty_hdlr_name: str = None,
    movie_timescale: str = None,
) -> FFMpegMuxerOption:
    """
    iPod H.264 MP4 (MPEG-4 Part 14)

    Args:
        movflags: MOV muxer flags (default 0)
        moov_size: maximum moov size so it can be placed at the begin (from 0 to INT_MAX) (default 0)
        rtpflags: RTP muxer flags (default 0)
        skip_iods: Skip writing iods atom. (default true)
        iods_audio_profile: iods audio profile atom. (from -1 to 255) (default -1)
        iods_video_profile: iods video profile atom. (from -1 to 255) (default -1)
        frag_duration: Maximum fragment duration (from 0 to INT_MAX) (default 0)
        min_frag_duration: Minimum fragment duration (from 0 to INT_MAX) (default 0)
        frag_size: Maximum fragment size (from 0 to INT_MAX) (default 0)
        ism_lookahead: Number of lookahead entries for ISM files (from 0 to 255) (default 0)
        video_track_timescale: set timescale of all video tracks (from 0 to INT_MAX) (default 0)
        brand: Override major brand
        use_editlist: use edit list (default auto)
        fragment_index: Fragment number of the next fragment (from 1 to INT_MAX) (default 1)
        mov_gamma: gamma value for gama atom (from 0 to 10) (default 0)
        frag_interleave: Interleave samples within fragments (max number of consecutive samples, lower is tighter interleaving, but with more overhead) (from 0 to INT_MAX) (default 0)
        encryption_scheme: Configures the encryption scheme, allowed values are none, cenc-aes-ctr
        encryption_key: The media encryption key (hex)
        encryption_kid: The media encryption key identifier (hex)
        use_stream_ids_as_track_ids: use stream ids as track ids (default false)
        write_btrt: force or disable writing btrt (default auto)
        write_tmcd: force or disable writing tmcd (default auto)
        write_prft: Write producer reference time box with specified time source (from 0 to 2) (default 0)
        empty_hdlr_name: write zero-length name string in hdlr atoms within mdia and minf atoms (default false)
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movflags": movflags,
                "moov_size": moov_size,
                "rtpflags": rtpflags,
                "skip_iods": skip_iods,
                "iods_audio_profile": iods_audio_profile,
                "iods_video_profile": iods_video_profile,
                "frag_duration": frag_duration,
                "min_frag_duration": min_frag_duration,
                "frag_size": frag_size,
                "ism_lookahead": ism_lookahead,
                "video_track_timescale": video_track_timescale,
                "brand": brand,
                "use_editlist": use_editlist,
                "fragment_index": fragment_index,
                "mov_gamma": mov_gamma,
                "frag_interleave": frag_interleave,
                "encryption_scheme": encryption_scheme,
                "encryption_key": encryption_key,
                "encryption_kid": encryption_kid,
                "use_stream_ids_as_track_ids": use_stream_ids_as_track_ids,
                "write_btrt": write_btrt,
                "write_tmcd": write_tmcd,
                "write_prft": write_prft,
                "empty_hdlr_name": empty_hdlr_name,
                "movie_timescale": movie_timescale,
            }
        )
    )


def ircam() -> FFMpegMuxerOption:
    """
    Berkeley/IRCAM/CARL Sound Format


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def ismv(
    movflags: str = None,
    moov_size: str = None,
    rtpflags: str = None,
    skip_iods: str = None,
    iods_audio_profile: str = None,
    iods_video_profile: str = None,
    frag_duration: str = None,
    min_frag_duration: str = None,
    frag_size: str = None,
    ism_lookahead: str = None,
    video_track_timescale: str = None,
    brand: str = None,
    use_editlist: str = None,
    fragment_index: str = None,
    mov_gamma: str = None,
    frag_interleave: str = None,
    encryption_scheme: str = None,
    encryption_key: str = None,
    encryption_kid: str = None,
    use_stream_ids_as_track_ids: str = None,
    write_btrt: str = None,
    write_tmcd: str = None,
    write_prft: str = None,
    empty_hdlr_name: str = None,
    movie_timescale: str = None,
) -> FFMpegMuxerOption:
    """
    ISMV/ISMA (Smooth Streaming)

    Args:
        movflags: MOV muxer flags (default 0)
        moov_size: maximum moov size so it can be placed at the begin (from 0 to INT_MAX) (default 0)
        rtpflags: RTP muxer flags (default 0)
        skip_iods: Skip writing iods atom. (default true)
        iods_audio_profile: iods audio profile atom. (from -1 to 255) (default -1)
        iods_video_profile: iods video profile atom. (from -1 to 255) (default -1)
        frag_duration: Maximum fragment duration (from 0 to INT_MAX) (default 0)
        min_frag_duration: Minimum fragment duration (from 0 to INT_MAX) (default 0)
        frag_size: Maximum fragment size (from 0 to INT_MAX) (default 0)
        ism_lookahead: Number of lookahead entries for ISM files (from 0 to 255) (default 0)
        video_track_timescale: set timescale of all video tracks (from 0 to INT_MAX) (default 0)
        brand: Override major brand
        use_editlist: use edit list (default auto)
        fragment_index: Fragment number of the next fragment (from 1 to INT_MAX) (default 1)
        mov_gamma: gamma value for gama atom (from 0 to 10) (default 0)
        frag_interleave: Interleave samples within fragments (max number of consecutive samples, lower is tighter interleaving, but with more overhead) (from 0 to INT_MAX) (default 0)
        encryption_scheme: Configures the encryption scheme, allowed values are none, cenc-aes-ctr
        encryption_key: The media encryption key (hex)
        encryption_kid: The media encryption key identifier (hex)
        use_stream_ids_as_track_ids: use stream ids as track ids (default false)
        write_btrt: force or disable writing btrt (default auto)
        write_tmcd: force or disable writing tmcd (default auto)
        write_prft: Write producer reference time box with specified time source (from 0 to 2) (default 0)
        empty_hdlr_name: write zero-length name string in hdlr atoms within mdia and minf atoms (default false)
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movflags": movflags,
                "moov_size": moov_size,
                "rtpflags": rtpflags,
                "skip_iods": skip_iods,
                "iods_audio_profile": iods_audio_profile,
                "iods_video_profile": iods_video_profile,
                "frag_duration": frag_duration,
                "min_frag_duration": min_frag_duration,
                "frag_size": frag_size,
                "ism_lookahead": ism_lookahead,
                "video_track_timescale": video_track_timescale,
                "brand": brand,
                "use_editlist": use_editlist,
                "fragment_index": fragment_index,
                "mov_gamma": mov_gamma,
                "frag_interleave": frag_interleave,
                "encryption_scheme": encryption_scheme,
                "encryption_key": encryption_key,
                "encryption_kid": encryption_kid,
                "use_stream_ids_as_track_ids": use_stream_ids_as_track_ids,
                "write_btrt": write_btrt,
                "write_tmcd": write_tmcd,
                "write_prft": write_prft,
                "empty_hdlr_name": empty_hdlr_name,
                "movie_timescale": movie_timescale,
            }
        )
    )


def ivf() -> FFMpegMuxerOption:
    """
    On2 IVF


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def jacosub() -> FFMpegMuxerOption:
    """
    JACOsub subtitle format


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def kvag() -> FFMpegMuxerOption:
    """
    Simon & Schuster Interactive VAG


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def latm(
    smc_interval: str = None,
) -> FFMpegMuxerOption:
    """
    LOAS/LATM

    Args:
        smc_interval: StreamMuxConfig interval. (from 1 to 65535) (default 20)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "smc-interval": smc_interval,
            }
        )
    )


def lrc() -> FFMpegMuxerOption:
    """
    LRC lyrics


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def m4v() -> FFMpegMuxerOption:
    """
    raw MPEG-4 video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def matroska(
    reserve_index_space: str = None,
    cues_to_front: str = None,
    cluster_size_limit: str = None,
    cluster_time_limit: str = None,
    dash: str = None,
    dash_track_number: str = None,
    live: str = None,
    allow_raw_vfw: str = None,
    flipped_raw_rgb: str = None,
    write_crc32: str = None,
    default_mode: str = None,
) -> FFMpegMuxerOption:
    """
    Matroska

    Args:
        reserve_index_space: Reserve a given amount of space (in bytes) at the beginning of the file for the index (cues). (from 0 to INT_MAX) (default 0)
        cues_to_front: Move Cues (the index) to the front by shifting data if necessary (default false)
        cluster_size_limit: Store at most the provided amount of bytes in a cluster.  (from -1 to INT_MAX) (default -1)
        cluster_time_limit: Store at most the provided number of milliseconds in a cluster. (from -1 to I64_MAX) (default -1)
        dash: Create a WebM file conforming to WebM DASH specification (default false)
        dash_track_number: Track number for the DASH stream (from 1 to INT_MAX) (default 1)
        live: Write files assuming it is a live stream. (default false)
        allow_raw_vfw: allow RAW VFW mode (default false)
        flipped_raw_rgb: Raw RGB bitmaps in VFW mode are stored bottom-up (default false)
        write_crc32: write a CRC32 element inside every Level 1 element (default true)
        default_mode: Controls how a track's FlagDefault is inferred (from 0 to 2) (default passthrough)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "reserve_index_space": reserve_index_space,
                "cues_to_front": cues_to_front,
                "cluster_size_limit": cluster_size_limit,
                "cluster_time_limit": cluster_time_limit,
                "dash": dash,
                "dash_track_number": dash_track_number,
                "live": live,
                "allow_raw_vfw": allow_raw_vfw,
                "flipped_raw_rgb": flipped_raw_rgb,
                "write_crc32": write_crc32,
                "default_mode": default_mode,
            }
        )
    )


def md5(
    hash: str = None,
) -> FFMpegMuxerOption:
    """
    MD5 testing

    Args:
        hash: set hash to use (default "md5")

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "hash": hash,
            }
        )
    )


def microdvd() -> FFMpegMuxerOption:
    """
    MicroDVD subtitle format


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mjpeg() -> FFMpegMuxerOption:
    """
    raw MJPEG video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mkvtimestamp_v2() -> FFMpegMuxerOption:
    """
    extract pts as timecode v2 format, as defined by mkvtoolnix


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mlp() -> FFMpegMuxerOption:
    """
    raw MLP


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mmf() -> FFMpegMuxerOption:
    """
    Yamaha SMAF


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mov(
    movflags: str = None,
    moov_size: str = None,
    rtpflags: str = None,
    skip_iods: str = None,
    iods_audio_profile: str = None,
    iods_video_profile: str = None,
    frag_duration: str = None,
    min_frag_duration: str = None,
    frag_size: str = None,
    ism_lookahead: str = None,
    video_track_timescale: str = None,
    brand: str = None,
    use_editlist: str = None,
    fragment_index: str = None,
    mov_gamma: str = None,
    frag_interleave: str = None,
    encryption_scheme: str = None,
    encryption_key: str = None,
    encryption_kid: str = None,
    use_stream_ids_as_track_ids: str = None,
    write_btrt: str = None,
    write_tmcd: str = None,
    write_prft: str = None,
    empty_hdlr_name: str = None,
    movie_timescale: str = None,
) -> FFMpegMuxerOption:
    """
    QuickTime / MOV

    Args:
        movflags: MOV muxer flags (default 0)
        moov_size: maximum moov size so it can be placed at the begin (from 0 to INT_MAX) (default 0)
        rtpflags: RTP muxer flags (default 0)
        skip_iods: Skip writing iods atom. (default true)
        iods_audio_profile: iods audio profile atom. (from -1 to 255) (default -1)
        iods_video_profile: iods video profile atom. (from -1 to 255) (default -1)
        frag_duration: Maximum fragment duration (from 0 to INT_MAX) (default 0)
        min_frag_duration: Minimum fragment duration (from 0 to INT_MAX) (default 0)
        frag_size: Maximum fragment size (from 0 to INT_MAX) (default 0)
        ism_lookahead: Number of lookahead entries for ISM files (from 0 to 255) (default 0)
        video_track_timescale: set timescale of all video tracks (from 0 to INT_MAX) (default 0)
        brand: Override major brand
        use_editlist: use edit list (default auto)
        fragment_index: Fragment number of the next fragment (from 1 to INT_MAX) (default 1)
        mov_gamma: gamma value for gama atom (from 0 to 10) (default 0)
        frag_interleave: Interleave samples within fragments (max number of consecutive samples, lower is tighter interleaving, but with more overhead) (from 0 to INT_MAX) (default 0)
        encryption_scheme: Configures the encryption scheme, allowed values are none, cenc-aes-ctr
        encryption_key: The media encryption key (hex)
        encryption_kid: The media encryption key identifier (hex)
        use_stream_ids_as_track_ids: use stream ids as track ids (default false)
        write_btrt: force or disable writing btrt (default auto)
        write_tmcd: force or disable writing tmcd (default auto)
        write_prft: Write producer reference time box with specified time source (from 0 to 2) (default 0)
        empty_hdlr_name: write zero-length name string in hdlr atoms within mdia and minf atoms (default false)
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movflags": movflags,
                "moov_size": moov_size,
                "rtpflags": rtpflags,
                "skip_iods": skip_iods,
                "iods_audio_profile": iods_audio_profile,
                "iods_video_profile": iods_video_profile,
                "frag_duration": frag_duration,
                "min_frag_duration": min_frag_duration,
                "frag_size": frag_size,
                "ism_lookahead": ism_lookahead,
                "video_track_timescale": video_track_timescale,
                "brand": brand,
                "use_editlist": use_editlist,
                "fragment_index": fragment_index,
                "mov_gamma": mov_gamma,
                "frag_interleave": frag_interleave,
                "encryption_scheme": encryption_scheme,
                "encryption_key": encryption_key,
                "encryption_kid": encryption_kid,
                "use_stream_ids_as_track_ids": use_stream_ids_as_track_ids,
                "write_btrt": write_btrt,
                "write_tmcd": write_tmcd,
                "write_prft": write_prft,
                "empty_hdlr_name": empty_hdlr_name,
                "movie_timescale": movie_timescale,
            }
        )
    )


def mp2() -> FFMpegMuxerOption:
    """
    MP2 (MPEG audio layer 2)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mp3(
    id3v2_version: str = None,
    write_id3v1: str = None,
    write_xing: str = None,
) -> FFMpegMuxerOption:
    """
    MP3 (MPEG audio layer 3)

    Args:
        id3v2_version: Select ID3v2 version to write. Currently 3 and 4 are supported. (from 0 to 4) (default 4)
        write_id3v1: Enable ID3v1 writing. ID3v1 tags are written in UTF-8 which may not be supported by most software. (default false)
        write_xing: Write the Xing header containing file duration. (default true)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "id3v2_version": id3v2_version,
                "write_id3v1": write_id3v1,
                "write_xing": write_xing,
            }
        )
    )


def mp4(
    movflags: str = None,
    moov_size: str = None,
    rtpflags: str = None,
    skip_iods: str = None,
    iods_audio_profile: str = None,
    iods_video_profile: str = None,
    frag_duration: str = None,
    min_frag_duration: str = None,
    frag_size: str = None,
    ism_lookahead: str = None,
    video_track_timescale: str = None,
    brand: str = None,
    use_editlist: str = None,
    fragment_index: str = None,
    mov_gamma: str = None,
    frag_interleave: str = None,
    encryption_scheme: str = None,
    encryption_key: str = None,
    encryption_kid: str = None,
    use_stream_ids_as_track_ids: str = None,
    write_btrt: str = None,
    write_tmcd: str = None,
    write_prft: str = None,
    empty_hdlr_name: str = None,
    movie_timescale: str = None,
) -> FFMpegMuxerOption:
    """
    MP4 (MPEG-4 Part 14)

    Args:
        movflags: MOV muxer flags (default 0)
        moov_size: maximum moov size so it can be placed at the begin (from 0 to INT_MAX) (default 0)
        rtpflags: RTP muxer flags (default 0)
        skip_iods: Skip writing iods atom. (default true)
        iods_audio_profile: iods audio profile atom. (from -1 to 255) (default -1)
        iods_video_profile: iods video profile atom. (from -1 to 255) (default -1)
        frag_duration: Maximum fragment duration (from 0 to INT_MAX) (default 0)
        min_frag_duration: Minimum fragment duration (from 0 to INT_MAX) (default 0)
        frag_size: Maximum fragment size (from 0 to INT_MAX) (default 0)
        ism_lookahead: Number of lookahead entries for ISM files (from 0 to 255) (default 0)
        video_track_timescale: set timescale of all video tracks (from 0 to INT_MAX) (default 0)
        brand: Override major brand
        use_editlist: use edit list (default auto)
        fragment_index: Fragment number of the next fragment (from 1 to INT_MAX) (default 1)
        mov_gamma: gamma value for gama atom (from 0 to 10) (default 0)
        frag_interleave: Interleave samples within fragments (max number of consecutive samples, lower is tighter interleaving, but with more overhead) (from 0 to INT_MAX) (default 0)
        encryption_scheme: Configures the encryption scheme, allowed values are none, cenc-aes-ctr
        encryption_key: The media encryption key (hex)
        encryption_kid: The media encryption key identifier (hex)
        use_stream_ids_as_track_ids: use stream ids as track ids (default false)
        write_btrt: force or disable writing btrt (default auto)
        write_tmcd: force or disable writing tmcd (default auto)
        write_prft: Write producer reference time box with specified time source (from 0 to 2) (default 0)
        empty_hdlr_name: write zero-length name string in hdlr atoms within mdia and minf atoms (default false)
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movflags": movflags,
                "moov_size": moov_size,
                "rtpflags": rtpflags,
                "skip_iods": skip_iods,
                "iods_audio_profile": iods_audio_profile,
                "iods_video_profile": iods_video_profile,
                "frag_duration": frag_duration,
                "min_frag_duration": min_frag_duration,
                "frag_size": frag_size,
                "ism_lookahead": ism_lookahead,
                "video_track_timescale": video_track_timescale,
                "brand": brand,
                "use_editlist": use_editlist,
                "fragment_index": fragment_index,
                "mov_gamma": mov_gamma,
                "frag_interleave": frag_interleave,
                "encryption_scheme": encryption_scheme,
                "encryption_key": encryption_key,
                "encryption_kid": encryption_kid,
                "use_stream_ids_as_track_ids": use_stream_ids_as_track_ids,
                "write_btrt": write_btrt,
                "write_tmcd": write_tmcd,
                "write_prft": write_prft,
                "empty_hdlr_name": empty_hdlr_name,
                "movie_timescale": movie_timescale,
            }
        )
    )


def mpeg(
    muxrate: str = None,
    preload: str = None,
) -> FFMpegMuxerOption:
    """
    MPEG-1 Systems / MPEG program stream

    Args:
        muxrate: (from 0 to 1.67772e+09) (default 0)
        preload: Initial demux-decode delay in microseconds. (from 0 to INT_MAX) (default 500000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "muxrate": muxrate,
                "preload": preload,
            }
        )
    )


def mpeg1video() -> FFMpegMuxerOption:
    """
    raw MPEG-1 video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mpeg2video() -> FFMpegMuxerOption:
    """
    raw MPEG-2 video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mpegts(
    mpegts_transport_stream_id: str = None,
    mpegts_original_network_id: str = None,
    mpegts_service_id: str = None,
    mpegts_service_type: str = None,
    mpegts_pmt_start_pid: str = None,
    mpegts_start_pid: str = None,
    mpegts_m2ts_mode: str = None,
    muxrate: str = None,
    pes_payload_size: str = None,
    mpegts_flags: str = None,
    mpegts_copyts: str = None,
    tables_version: str = None,
    omit_video_pes_length: str = None,
    pcr_period: str = None,
    pat_period: str = None,
    sdt_period: str = None,
    nit_period: str = None,
) -> FFMpegMuxerOption:
    """
    MPEG-TS (MPEG-2 Transport Stream)

    Args:
        mpegts_transport_stream_id: Set transport_stream_id field. (from 1 to 65535) (default 1)
        mpegts_original_network_id: Set original_network_id field. (from 1 to 65535) (default 65281)
        mpegts_service_id: Set service_id field. (from 1 to 65535) (default 1)
        mpegts_service_type: Set service_type field. (from 1 to 255) (default digital_tv)
        mpegts_pmt_start_pid: Set the first pid of the PMT. (from 32 to 8186) (default 4096)
        mpegts_start_pid: Set the first pid. (from 32 to 8186) (default 256)
        mpegts_m2ts_mode: Enable m2ts mode. (default auto)
        muxrate: (from 0 to INT_MAX) (default 1)
        pes_payload_size: Minimum PES packet payload in bytes (from 0 to INT_MAX) (default 2930)
        mpegts_flags: MPEG-TS muxing flags (default 0)
        mpegts_copyts: don't offset dts/pts (default auto)
        tables_version: set PAT, PMT, SDT and NIT version (from 0 to 31) (default 0)
        omit_video_pes_length: Omit the PES packet length for video packets (default true)
        pcr_period: PCR retransmission time in milliseconds (from -1 to INT_MAX) (default -1)
        pat_period: PAT/PMT retransmission time limit in seconds (default 0.1)
        sdt_period: SDT retransmission time limit in seconds (default 0.5)
        nit_period: NIT retransmission time limit in seconds (default 0.5)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "mpegts_transport_stream_id": mpegts_transport_stream_id,
                "mpegts_original_network_id": mpegts_original_network_id,
                "mpegts_service_id": mpegts_service_id,
                "mpegts_service_type": mpegts_service_type,
                "mpegts_pmt_start_pid": mpegts_pmt_start_pid,
                "mpegts_start_pid": mpegts_start_pid,
                "mpegts_m2ts_mode": mpegts_m2ts_mode,
                "muxrate": muxrate,
                "pes_payload_size": pes_payload_size,
                "mpegts_flags": mpegts_flags,
                "mpegts_copyts": mpegts_copyts,
                "tables_version": tables_version,
                "omit_video_pes_length": omit_video_pes_length,
                "pcr_period": pcr_period,
                "pat_period": pat_period,
                "sdt_period": sdt_period,
                "nit_period": nit_period,
            }
        )
    )


def mpjpeg(
    boundary_tag: str = None,
) -> FFMpegMuxerOption:
    """
    MIME multipart JPEG

    Args:
        boundary_tag: Boundary tag (default "ffmpeg")

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "boundary_tag": boundary_tag,
            }
        )
    )


def mulaw() -> FFMpegMuxerOption:
    """
    PCM mu-law


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def mxf(
    signal_standard: str = None,
    store_user_comments: str = None,
) -> FFMpegMuxerOption:
    """
    MXF (Material eXchange Format)

    Args:
        signal_standard: Force/set Signal Standard (from -1 to 7) (default -1)
        store_user_comments: (default true)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "signal_standard": signal_standard,
                "store_user_comments": store_user_comments,
            }
        )
    )


def mxf_d10(
    d10_channelcount: str = None,
    signal_standard: str = None,
    store_user_comments: str = None,
) -> FFMpegMuxerOption:
    """
    MXF (Material eXchange Format) D-10 Mapping

    Args:
        d10_channelcount: Force/set channelcount in generic sound essence descriptor (from -1 to 8) (default -1)
        signal_standard: Force/set Signal Standard (from -1 to 7) (default -1)
        store_user_comments: (default false)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "d10_channelcount": d10_channelcount,
                "signal_standard": signal_standard,
                "store_user_comments": store_user_comments,
            }
        )
    )


def mxf_opatom(
    mxf_audio_edit_rate: str = None,
    signal_standard: str = None,
    store_user_comments: str = None,
) -> FFMpegMuxerOption:
    """
    MXF (Material eXchange Format) Operational Pattern Atom

    Args:
        mxf_audio_edit_rate: Audio edit rate for timecode (from 0 to INT_MAX) (default 25/1)
        signal_standard: Force/set Signal Standard (from -1 to 7) (default -1)
        store_user_comments: (default true)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "mxf_audio_edit_rate": mxf_audio_edit_rate,
                "signal_standard": signal_standard,
                "store_user_comments": store_user_comments,
            }
        )
    )


def null() -> FFMpegMuxerOption:
    """
    raw null video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def nut(
    syncpoints: str = None,
    write_index: str = None,
) -> FFMpegMuxerOption:
    """
    NUT

    Args:
        syncpoints: NUT syncpoint behaviour (default 0)
        write_index: Write index (default true)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "syncpoints": syncpoints,
                "write_index": write_index,
            }
        )
    )


def obu() -> FFMpegMuxerOption:
    """
    AV1 low overhead OBU


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def oga(
    serial_offset: str = None,
    oggpagesize: str = None,
    pagesize: str = None,
    page_duration: str = None,
) -> FFMpegMuxerOption:
    """
    Ogg Audio

    Args:
        serial_offset: serial number offset (from 0 to INT_MAX) (default 0)
        oggpagesize: Set preferred Ogg page size. (from 0 to 65025) (default 0)
        pagesize: preferred page size in bytes (deprecated) (from 0 to 65025) (default 0)
        page_duration: preferred page duration, in microseconds (from 0 to I64_MAX) (default 1000000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "serial_offset": serial_offset,
                "oggpagesize": oggpagesize,
                "pagesize": pagesize,
                "page_duration": page_duration,
            }
        )
    )


def ogg(
    serial_offset: str = None,
    oggpagesize: str = None,
    pagesize: str = None,
    page_duration: str = None,
) -> FFMpegMuxerOption:
    """
    Ogg

    Args:
        serial_offset: serial number offset (from 0 to INT_MAX) (default 0)
        oggpagesize: Set preferred Ogg page size. (from 0 to 65025) (default 0)
        pagesize: preferred page size in bytes (deprecated) (from 0 to 65025) (default 0)
        page_duration: preferred page duration, in microseconds (from 0 to I64_MAX) (default 1000000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "serial_offset": serial_offset,
                "oggpagesize": oggpagesize,
                "pagesize": pagesize,
                "page_duration": page_duration,
            }
        )
    )


def ogv(
    serial_offset: str = None,
    oggpagesize: str = None,
    pagesize: str = None,
    page_duration: str = None,
) -> FFMpegMuxerOption:
    """
    Ogg Video

    Args:
        serial_offset: serial number offset (from 0 to INT_MAX) (default 0)
        oggpagesize: Set preferred Ogg page size. (from 0 to 65025) (default 0)
        pagesize: preferred page size in bytes (deprecated) (from 0 to 65025) (default 0)
        page_duration: preferred page duration, in microseconds (from 0 to I64_MAX) (default 1000000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "serial_offset": serial_offset,
                "oggpagesize": oggpagesize,
                "pagesize": pagesize,
                "page_duration": page_duration,
            }
        )
    )


def oma() -> FFMpegMuxerOption:
    """
    Sony OpenMG audio


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def opengl(
    background: str = None,
    no_window: str = None,
    window_title: str = None,
    window_size: str = None,
) -> FFMpegMuxerOption:
    """
    OpenGL output

    Args:
        background: set background color (default "black")
        no_window: disable default window (from INT_MIN to INT_MAX) (default 0)
        window_title: set window title
        window_size: set window size

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "background": background,
                "no_window": no_window,
                "window_title": window_title,
                "window_size": window_size,
            }
        )
    )


def opus(
    serial_offset: str = None,
    oggpagesize: str = None,
    pagesize: str = None,
    page_duration: str = None,
) -> FFMpegMuxerOption:
    """
    Ogg Opus

    Args:
        serial_offset: serial number offset (from 0 to INT_MAX) (default 0)
        oggpagesize: Set preferred Ogg page size. (from 0 to 65025) (default 0)
        pagesize: preferred page size in bytes (deprecated) (from 0 to 65025) (default 0)
        page_duration: preferred page duration, in microseconds (from 0 to I64_MAX) (default 1000000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "serial_offset": serial_offset,
                "oggpagesize": oggpagesize,
                "pagesize": pagesize,
                "page_duration": page_duration,
            }
        )
    )


def oss() -> FFMpegMuxerOption:
    """
    OSS (Open Sound System) playback


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def psp(
    movflags: str = None,
    moov_size: str = None,
    rtpflags: str = None,
    skip_iods: str = None,
    iods_audio_profile: str = None,
    iods_video_profile: str = None,
    frag_duration: str = None,
    min_frag_duration: str = None,
    frag_size: str = None,
    ism_lookahead: str = None,
    video_track_timescale: str = None,
    brand: str = None,
    use_editlist: str = None,
    fragment_index: str = None,
    mov_gamma: str = None,
    frag_interleave: str = None,
    encryption_scheme: str = None,
    encryption_key: str = None,
    encryption_kid: str = None,
    use_stream_ids_as_track_ids: str = None,
    write_btrt: str = None,
    write_tmcd: str = None,
    write_prft: str = None,
    empty_hdlr_name: str = None,
    movie_timescale: str = None,
) -> FFMpegMuxerOption:
    """
    PSP MP4 (MPEG-4 Part 14)

    Args:
        movflags: MOV muxer flags (default 0)
        moov_size: maximum moov size so it can be placed at the begin (from 0 to INT_MAX) (default 0)
        rtpflags: RTP muxer flags (default 0)
        skip_iods: Skip writing iods atom. (default true)
        iods_audio_profile: iods audio profile atom. (from -1 to 255) (default -1)
        iods_video_profile: iods video profile atom. (from -1 to 255) (default -1)
        frag_duration: Maximum fragment duration (from 0 to INT_MAX) (default 0)
        min_frag_duration: Minimum fragment duration (from 0 to INT_MAX) (default 0)
        frag_size: Maximum fragment size (from 0 to INT_MAX) (default 0)
        ism_lookahead: Number of lookahead entries for ISM files (from 0 to 255) (default 0)
        video_track_timescale: set timescale of all video tracks (from 0 to INT_MAX) (default 0)
        brand: Override major brand
        use_editlist: use edit list (default auto)
        fragment_index: Fragment number of the next fragment (from 1 to INT_MAX) (default 1)
        mov_gamma: gamma value for gama atom (from 0 to 10) (default 0)
        frag_interleave: Interleave samples within fragments (max number of consecutive samples, lower is tighter interleaving, but with more overhead) (from 0 to INT_MAX) (default 0)
        encryption_scheme: Configures the encryption scheme, allowed values are none, cenc-aes-ctr
        encryption_key: The media encryption key (hex)
        encryption_kid: The media encryption key identifier (hex)
        use_stream_ids_as_track_ids: use stream ids as track ids (default false)
        write_btrt: force or disable writing btrt (default auto)
        write_tmcd: force or disable writing tmcd (default auto)
        write_prft: Write producer reference time box with specified time source (from 0 to 2) (default 0)
        empty_hdlr_name: write zero-length name string in hdlr atoms within mdia and minf atoms (default false)
        movie_timescale: set movie timescale (from 1 to INT_MAX) (default 1000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "movflags": movflags,
                "moov_size": moov_size,
                "rtpflags": rtpflags,
                "skip_iods": skip_iods,
                "iods_audio_profile": iods_audio_profile,
                "iods_video_profile": iods_video_profile,
                "frag_duration": frag_duration,
                "min_frag_duration": min_frag_duration,
                "frag_size": frag_size,
                "ism_lookahead": ism_lookahead,
                "video_track_timescale": video_track_timescale,
                "brand": brand,
                "use_editlist": use_editlist,
                "fragment_index": fragment_index,
                "mov_gamma": mov_gamma,
                "frag_interleave": frag_interleave,
                "encryption_scheme": encryption_scheme,
                "encryption_key": encryption_key,
                "encryption_kid": encryption_kid,
                "use_stream_ids_as_track_ids": use_stream_ids_as_track_ids,
                "write_btrt": write_btrt,
                "write_tmcd": write_tmcd,
                "write_prft": write_prft,
                "empty_hdlr_name": empty_hdlr_name,
                "movie_timescale": movie_timescale,
            }
        )
    )


def pulse(
    server: str = None,
    name: str = None,
    stream_name: str = None,
    device: str = None,
    buffer_size: str = None,
    buffer_duration: str = None,
    prebuf: str = None,
    minreq: str = None,
) -> FFMpegMuxerOption:
    """
    Pulse audio output

    Args:
        server: set PulseAudio server
        name: set application name (default "Lavf60.16.100")
        stream_name: set stream description
        device: set device name
        buffer_size: set buffer size in bytes (from 0 to INT_MAX) (default 0)
        buffer_duration: set buffer duration in millisecs (from 0 to INT_MAX) (default 0)
        prebuf: set pre-buffering size (from 0 to INT_MAX) (default 0)
        minreq: set minimum request size (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "server": server,
                "name": name,
                "stream_name": stream_name,
                "device": device,
                "buffer_size": buffer_size,
                "buffer_duration": buffer_duration,
                "prebuf": prebuf,
                "minreq": minreq,
            }
        )
    )


def rawvideo() -> FFMpegMuxerOption:
    """
    raw video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def rm() -> FFMpegMuxerOption:
    """
    RealMedia


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def roq() -> FFMpegMuxerOption:
    """
    raw id RoQ


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def rso() -> FFMpegMuxerOption:
    """
    Lego Mindstorms RSO


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def rtp(
    rtpflags: str = None,
    payload_type: str = None,
    ssrc: str = None,
    cname: str = None,
    seq: str = None,
) -> FFMpegMuxerOption:
    """
    RTP output

    Args:
        rtpflags: RTP muxer flags (default 0)
        payload_type: Specify RTP payload type (from -1 to 127) (default -1)
        ssrc: Stream identifier (from INT_MIN to INT_MAX) (default 0)
        cname: CNAME to include in RTCP SR packets
        seq: Starting sequence number (from -1 to 65535) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "rtpflags": rtpflags,
                "payload_type": payload_type,
                "ssrc": ssrc,
                "cname": cname,
                "seq": seq,
            }
        )
    )


def rtp_mpegts(
    mpegts_muxer_options: str = None,
    rtp_muxer_options: str = None,
) -> FFMpegMuxerOption:
    """
    RTP/mpegts output format

    Args:
        mpegts_muxer_options: set list of options for the MPEG-TS muxer
        rtp_muxer_options: set list of options for the RTP muxer

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "mpegts_muxer_options": mpegts_muxer_options,
                "rtp_muxer_options": rtp_muxer_options,
            }
        )
    )


def rtsp(
    rtpflags: str = None,
    rtsp_transport: str = None,
    min_port: str = None,
    max_port: str = None,
    buffer_size: str = None,
    pkt_size: str = None,
) -> FFMpegMuxerOption:
    """
    RTSP output

    Args:
        rtpflags: RTP muxer flags (default 0)
        rtsp_transport: set RTSP transport protocols (default 0)
        min_port: set minimum local UDP port (from 0 to 65535) (default 5000)
        max_port: set maximum local UDP port (from 0 to 65535) (default 65000)
        buffer_size: Underlying protocol send/receive buffer size (from -1 to INT_MAX) (default -1)
        pkt_size: Underlying protocol send packet size (from -1 to INT_MAX) (default 1472)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "rtpflags": rtpflags,
                "rtsp_transport": rtsp_transport,
                "min_port": min_port,
                "max_port": max_port,
                "buffer_size": buffer_size,
                "pkt_size": pkt_size,
            }
        )
    )


def s16be() -> FFMpegMuxerOption:
    """
    PCM signed 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def s16le() -> FFMpegMuxerOption:
    """
    PCM signed 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def s24be() -> FFMpegMuxerOption:
    """
    PCM signed 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def s24le() -> FFMpegMuxerOption:
    """
    PCM signed 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def s32be() -> FFMpegMuxerOption:
    """
    PCM signed 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def s32le() -> FFMpegMuxerOption:
    """
    PCM signed 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def s8() -> FFMpegMuxerOption:
    """
    PCM signed 8-bit


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def sap() -> FFMpegMuxerOption:
    """
    SAP output


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def sbc() -> FFMpegMuxerOption:
    """
    raw SBC


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def scc() -> FFMpegMuxerOption:
    """
    Scenarist Closed Captions


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def segment(
    reference_stream: str = None,
    segment_format: str = None,
    segment_format_options: str = None,
    segment_list: str = None,
    segment_header_filename: str = None,
    segment_list_flags: str = None,
    segment_list_size: str = None,
    segment_list_type: str = None,
    segment_atclocktime: str = None,
    segment_clocktime_offset: str = None,
    segment_clocktime_wrap_duration: str = None,
    segment_time: str = None,
    segment_time_delta: str = None,
    min_seg_duration: str = None,
    segment_times: str = None,
    segment_frames: str = None,
    segment_wrap: str = None,
    segment_list_entry_prefix: str = None,
    segment_start_number: str = None,
    segment_wrap_number: str = None,
    strftime: str = None,
    increment_tc: str = None,
    break_non_keyframes: str = None,
    individual_header_trailer: str = None,
    write_header_trailer: str = None,
    reset_timestamps: str = None,
    initial_offset: str = None,
    write_empty_segments: str = None,
) -> FFMpegMuxerOption:
    """
    segment

    Args:
        reference_stream: set reference stream (default "auto")
        segment_format: set container format used for the segments
        segment_format_options: set list of options for the container format used for the segments
        segment_list: set the segment list filename
        segment_header_filename: write a single file containing the header
        segment_list_flags: set flags affecting segment list generation (default cache)
        segment_list_size: set the maximum number of playlist entries (from 0 to INT_MAX) (default 0)
        segment_list_type: set the segment list type (from -1 to 4) (default -1)
        segment_atclocktime: set segment to be cut at clocktime (default false)
        segment_clocktime_offset: set segment clocktime offset (default 0)
        segment_clocktime_wrap_duration: set segment clocktime wrapping duration (default INT64_MAX)
        segment_time: set segment duration (default 2)
        segment_time_delta: set approximation value used for the segment times (default 0)
        min_seg_duration: set minimum segment duration (default 0)
        segment_times: set segment split time points
        segment_frames: set segment split frame numbers
        segment_wrap: set number after which the index wraps (from 0 to INT_MAX) (default 0)
        segment_list_entry_prefix: set base url prefix for segments
        segment_start_number: set the sequence number of the first segment (from 0 to INT_MAX) (default 0)
        segment_wrap_number: set the number of wrap before the first segment (from 0 to INT_MAX) (default 0)
        strftime: set filename expansion with strftime at segment creation (default false)
        increment_tc: increment timecode between each segment (default false)
        break_non_keyframes: allow breaking segments on non-keyframes (default false)
        individual_header_trailer: write header/trailer to each segment (default true)
        write_header_trailer: write a header to the first segment and a trailer to the last one (default true)
        reset_timestamps: reset timestamps at the beginning of each segment (default false)
        initial_offset: set initial timestamp offset (default 0)
        write_empty_segments: allow writing empty 'filler' segments (default false)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "reference_stream": reference_stream,
                "segment_format": segment_format,
                "segment_format_options": segment_format_options,
                "segment_list": segment_list,
                "segment_header_filename": segment_header_filename,
                "segment_list_flags": segment_list_flags,
                "segment_list_size": segment_list_size,
                "segment_list_type": segment_list_type,
                "segment_atclocktime": segment_atclocktime,
                "segment_clocktime_offset": segment_clocktime_offset,
                "segment_clocktime_wrap_duration": segment_clocktime_wrap_duration,
                "segment_time": segment_time,
                "segment_time_delta": segment_time_delta,
                "min_seg_duration": min_seg_duration,
                "segment_times": segment_times,
                "segment_frames": segment_frames,
                "segment_wrap": segment_wrap,
                "segment_list_entry_prefix": segment_list_entry_prefix,
                "segment_start_number": segment_start_number,
                "segment_wrap_number": segment_wrap_number,
                "strftime": strftime,
                "increment_tc": increment_tc,
                "break_non_keyframes": break_non_keyframes,
                "individual_header_trailer": individual_header_trailer,
                "write_header_trailer": write_header_trailer,
                "reset_timestamps": reset_timestamps,
                "initial_offset": initial_offset,
                "write_empty_segments": write_empty_segments,
            }
        )
    )


def smjpeg() -> FFMpegMuxerOption:
    """
    Loki SDL MJPEG


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def smoothstreaming(
    window_size: str = None,
    extra_window_size: str = None,
    lookahead_count: str = None,
    min_frag_duration: str = None,
    remove_at_exit: str = None,
) -> FFMpegMuxerOption:
    """
    Smooth Streaming Muxer

    Args:
        window_size: number of fragments kept in the manifest (from 0 to INT_MAX) (default 0)
        extra_window_size: number of fragments kept outside of the manifest before removing from disk (from 0 to INT_MAX) (default 5)
        lookahead_count: number of lookahead fragments (from 0 to INT_MAX) (default 2)
        min_frag_duration: minimum fragment duration (in microseconds) (from 0 to INT_MAX) (default 5000000)
        remove_at_exit: remove all fragments when finished (default false)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "window_size": window_size,
                "extra_window_size": extra_window_size,
                "lookahead_count": lookahead_count,
                "min_frag_duration": min_frag_duration,
                "remove_at_exit": remove_at_exit,
            }
        )
    )


def sox() -> FFMpegMuxerOption:
    """
    SoX (Sound eXchange) native


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def spdif(
    spdif_flags: str = None,
    dtshd_rate: str = None,
    dtshd_fallback_time: str = None,
) -> FFMpegMuxerOption:
    """
    IEC 61937 (used on S/PDIF - IEC958)

    Args:
        spdif_flags: IEC 61937 encapsulation flags (default 0)
        dtshd_rate: mux complete DTS frames in HD mode at the specified IEC958 rate (in Hz, default 0=disabled) (from 0 to 768000) (default 0)
        dtshd_fallback_time: min secs to strip HD for after an overflow (-1: till the end, default 60) (from -1 to INT_MAX) (default 60)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "spdif_flags": spdif_flags,
                "dtshd_rate": dtshd_rate,
                "dtshd_fallback_time": dtshd_fallback_time,
            }
        )
    )


def spx(
    serial_offset: str = None,
    oggpagesize: str = None,
    pagesize: str = None,
    page_duration: str = None,
) -> FFMpegMuxerOption:
    """
    Ogg Speex

    Args:
        serial_offset: serial number offset (from 0 to INT_MAX) (default 0)
        oggpagesize: Set preferred Ogg page size. (from 0 to 65025) (default 0)
        pagesize: preferred page size in bytes (deprecated) (from 0 to 65025) (default 0)
        page_duration: preferred page duration, in microseconds (from 0 to I64_MAX) (default 1000000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "serial_offset": serial_offset,
                "oggpagesize": oggpagesize,
                "pagesize": pagesize,
                "page_duration": page_duration,
            }
        )
    )


def srt() -> FFMpegMuxerOption:
    """
    SubRip subtitle


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def streamhash(
    hash: str = None,
) -> FFMpegMuxerOption:
    """
    Per-stream hash testing

    Args:
        hash: set hash to use (default "sha256")

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "hash": hash,
            }
        )
    )


def sup() -> FFMpegMuxerOption:
    """
    raw HDMV Presentation Graphic Stream subtitles


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def svcd(
    muxrate: str = None,
    preload: str = None,
) -> FFMpegMuxerOption:
    """
    MPEG-2 PS (SVCD)

    Args:
        muxrate: (from 0 to 1.67772e+09) (default 0)
        preload: Initial demux-decode delay in microseconds. (from 0 to INT_MAX) (default 500000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "muxrate": muxrate,
                "preload": preload,
            }
        )
    )


def swf() -> FFMpegMuxerOption:
    """
    SWF (ShockWave Flash)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def tee(
    use_fifo: str = None,
    fifo_options: str = None,
) -> FFMpegMuxerOption:
    """
    Multiple muxer tee

    Args:
        use_fifo: Use fifo pseudo-muxer to separate actual muxers from encoder (default false)
        fifo_options: fifo pseudo-muxer options

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "use_fifo": use_fifo,
                "fifo_options": fifo_options,
            }
        )
    )


def truehd() -> FFMpegMuxerOption:
    """
    raw TrueHD


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def tta() -> FFMpegMuxerOption:
    """
    TTA (True Audio)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def ttml() -> FFMpegMuxerOption:
    """
    TTML subtitle


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def u16be() -> FFMpegMuxerOption:
    """
    PCM unsigned 16-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def u16le() -> FFMpegMuxerOption:
    """
    PCM unsigned 16-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def u24be() -> FFMpegMuxerOption:
    """
    PCM unsigned 24-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def u24le() -> FFMpegMuxerOption:
    """
    PCM unsigned 24-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def u32be() -> FFMpegMuxerOption:
    """
    PCM unsigned 32-bit big-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def u32le() -> FFMpegMuxerOption:
    """
    PCM unsigned 32-bit little-endian


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def u8() -> FFMpegMuxerOption:
    """
    PCM unsigned 8-bit


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def uncodedframecrc() -> FFMpegMuxerOption:
    """
    uncoded framecrc testing


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def vc1() -> FFMpegMuxerOption:
    """
    raw VC-1 video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def vc1test() -> FFMpegMuxerOption:
    """
    VC-1 test bitstream


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def vcd(
    muxrate: str = None,
    preload: str = None,
) -> FFMpegMuxerOption:
    """
    MPEG-1 Systems / MPEG program stream (VCD)

    Args:
        muxrate: (from 0 to 1.67772e+09) (default 0)
        preload: Initial demux-decode delay in microseconds. (from 0 to INT_MAX) (default 500000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "muxrate": muxrate,
                "preload": preload,
            }
        )
    )


def vidc() -> FFMpegMuxerOption:
    """
    PCM Archimedes VIDC


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def vob(
    muxrate: str = None,
    preload: str = None,
) -> FFMpegMuxerOption:
    """
    MPEG-2 PS (VOB)

    Args:
        muxrate: (from 0 to 1.67772e+09) (default 0)
        preload: Initial demux-decode delay in microseconds. (from 0 to INT_MAX) (default 500000)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "muxrate": muxrate,
                "preload": preload,
            }
        )
    )


def voc() -> FFMpegMuxerOption:
    """
    Creative Voice


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def vvc() -> FFMpegMuxerOption:
    """
    raw H.266/VVC video


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def w64() -> FFMpegMuxerOption:
    """
    Sony Wave64


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def wav(
    write_bext: str = None,
    write_peak: str = None,
    rf64: str = None,
    peak_block_size: str = None,
    peak_format: str = None,
    peak_ppv: str = None,
) -> FFMpegMuxerOption:
    """
    WAV / WAVE (Waveform Audio)

    Args:
        write_bext: Write BEXT chunk. (default false)
        write_peak: Write Peak Envelope chunk. (from 0 to 2) (default off)
        rf64: Use RF64 header rather than RIFF for large files. (from -1 to 1) (default never)
        peak_block_size: Number of audio samples used to generate each peak frame. (from 0 to 65536) (default 256)
        peak_format: The format of the peak envelope data (1: uint8, 2: uint16). (from 1 to 2) (default 2)
        peak_ppv: Number of peak points per peak value (1 or 2). (from 1 to 2) (default 2)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "write_bext": write_bext,
                "write_peak": write_peak,
                "rf64": rf64,
                "peak_block_size": peak_block_size,
                "peak_format": peak_format,
                "peak_ppv": peak_ppv,
            }
        )
    )


def webm(
    reserve_index_space: str = None,
    cues_to_front: str = None,
    cluster_size_limit: str = None,
    cluster_time_limit: str = None,
    dash: str = None,
    dash_track_number: str = None,
    live: str = None,
    allow_raw_vfw: str = None,
    flipped_raw_rgb: str = None,
    write_crc32: str = None,
    default_mode: str = None,
) -> FFMpegMuxerOption:
    """
    WebM

    Args:
        reserve_index_space: Reserve a given amount of space (in bytes) at the beginning of the file for the index (cues). (from 0 to INT_MAX) (default 0)
        cues_to_front: Move Cues (the index) to the front by shifting data if necessary (default false)
        cluster_size_limit: Store at most the provided amount of bytes in a cluster.  (from -1 to INT_MAX) (default -1)
        cluster_time_limit: Store at most the provided number of milliseconds in a cluster. (from -1 to I64_MAX) (default -1)
        dash: Create a WebM file conforming to WebM DASH specification (default false)
        dash_track_number: Track number for the DASH stream (from 1 to INT_MAX) (default 1)
        live: Write files assuming it is a live stream. (default false)
        allow_raw_vfw: allow RAW VFW mode (default false)
        flipped_raw_rgb: Raw RGB bitmaps in VFW mode are stored bottom-up (default false)
        write_crc32: write a CRC32 element inside every Level 1 element (default true)
        default_mode: Controls how a track's FlagDefault is inferred (from 0 to 2) (default passthrough)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "reserve_index_space": reserve_index_space,
                "cues_to_front": cues_to_front,
                "cluster_size_limit": cluster_size_limit,
                "cluster_time_limit": cluster_time_limit,
                "dash": dash,
                "dash_track_number": dash_track_number,
                "live": live,
                "allow_raw_vfw": allow_raw_vfw,
                "flipped_raw_rgb": flipped_raw_rgb,
                "write_crc32": write_crc32,
                "default_mode": default_mode,
            }
        )
    )


def webm_chunk(
    chunk_start_index: str = None,
    header: str = None,
    audio_chunk_duration: str = None,
    method: str = None,
) -> FFMpegMuxerOption:
    """
    WebM Chunk Muxer

    Args:
        chunk_start_index: start index of the chunk (from 0 to INT_MAX) (default 0)
        header: filename of the header where the initialization data will be written
        audio_chunk_duration: duration of each chunk in milliseconds (from 0 to INT_MAX) (default 5000)
        method: set the HTTP method

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "chunk_start_index": chunk_start_index,
                "header": header,
                "audio_chunk_duration": audio_chunk_duration,
                "method": method,
            }
        )
    )


def webm_dash_manifest(
    adaptation_sets: str = None,
    live: str = None,
    chunk_start_index: str = None,
    chunk_duration_ms: str = None,
    utc_timing_url: str = None,
    time_shift_buffer_depth: str = None,
    minimum_update_period: str = None,
) -> FFMpegMuxerOption:
    """
    WebM DASH Manifest

    Args:
        adaptation_sets: Adaptation sets. Syntax: id=0,streams=0,1,2 id=1,streams=3,4 and so on
        live: create a live stream manifest (default false)
        chunk_start_index: start index of the chunk (from 0 to INT_MAX) (default 0)
        chunk_duration_ms: duration of each chunk (in milliseconds) (from 0 to INT_MAX) (default 1000)
        utc_timing_url: URL of the page that will return the UTC timestamp in ISO format
        time_shift_buffer_depth: Smallest time (in seconds) shifting buffer for which any Representation is guaranteed to be available. (from 1 to DBL_MAX) (default 60)
        minimum_update_period: Minimum Update Period (in seconds) of the manifest. (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "adaptation_sets": adaptation_sets,
                "live": live,
                "chunk_start_index": chunk_start_index,
                "chunk_duration_ms": chunk_duration_ms,
                "utc_timing_url": utc_timing_url,
                "time_shift_buffer_depth": time_shift_buffer_depth,
                "minimum_update_period": minimum_update_period,
            }
        )
    )


def webp(
    loop: str = None,
) -> FFMpegMuxerOption:
    """
    WebP

    Args:
        loop: Number of times to loop the output: 0 - infinite loop (from 0 to 65535) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "loop": loop,
            }
        )
    )


def webvtt() -> FFMpegMuxerOption:
    """
    WebVTT subtitle


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def wsaud() -> FFMpegMuxerOption:
    """
    Westwood Studios audio


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def wtv() -> FFMpegMuxerOption:
    """
    Windows Television (WTV)


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def wv() -> FFMpegMuxerOption:
    """
    raw WavPack


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))


def xv(
    display_name: str = None,
    window_id: str = None,
    window_size: str = None,
    window_title: str = None,
    window_x: str = None,
    window_y: str = None,
) -> FFMpegMuxerOption:
    """
    XV (XVideo) output device

    Args:
        display_name: set display name
        window_id: set existing window id (from 0 to I64_MAX) (default 0)
        window_size: set window forced size
        window_title: set window title
        window_x: set window x offset (from -2.14748e+09 to INT_MAX) (default 0)
        window_y: set window y offset (from -2.14748e+09 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(
        kwargs=merge(
            {
                "display_name": display_name,
                "window_id": window_id,
                "window_size": window_size,
                "window_title": window_title,
                "window_x": window_x,
                "window_y": window_y,
            }
        )
    )


def yuv4mpegpipe() -> FFMpegMuxerOption:
    """
    YUV4MPEG pipe


    Returns:
        the set codec options
    """
    return FFMpegMuxerOption(kwargs=merge({}))
