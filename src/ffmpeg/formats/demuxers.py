# NOTE: this file is auto-generated, do not modify
from typing import Literal

from ..utils.frozendict import merge
from .schema import FFMpegDemuxerOption


def _3dostr() -> FFMpegDemuxerOption:
    """
    3DO STR


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def _4xm() -> FFMpegDemuxerOption:
    """
    4X Technologies


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def aa(
    aa_fixed_key: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Audible AA format files

    Args:
        aa_fixed_key: Fixed key used for handling Audible AA files

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "aa_fixed_key": aa_fixed_key,
            }
        )
    )


def aac() -> FFMpegDemuxerOption:
    """
    raw ADTS AAC (Advanced Audio Coding)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def aax() -> FFMpegDemuxerOption:
    """
    CRI AAX


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ac3(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw AC-3

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def ac4() -> FFMpegDemuxerOption:
    """
    raw AC-4


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ace() -> FFMpegDemuxerOption:
    """
    tri-Ace Audio Container


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def acm(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    Interplay ACM

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def act() -> FFMpegDemuxerOption:
    """
    ACT Voice file format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def adf(
    linespeed: int | None = None,
    video_size: str | None = None,
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Artworx Data Format

    Args:
        linespeed: set simulated line speed (bytes per second) (from 1 to INT_MAX) (default 6000)
        video_size: set video size, such as 640x480 or hd720.
        framerate: set framerate (frames per second) (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "linespeed": linespeed,
                "video_size": video_size,
                "framerate": framerate,
            }
        )
    )


def adp() -> FFMpegDemuxerOption:
    """
    ADP


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ads() -> FFMpegDemuxerOption:
    """
    Sony PS2 ADS


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def adx() -> FFMpegDemuxerOption:
    """
    CRI ADX


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def aea() -> FFMpegDemuxerOption:
    """
    MD STUDIO audio


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def afc() -> FFMpegDemuxerOption:
    """
    AFC


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def aiff() -> FFMpegDemuxerOption:
    """
    Audio IFF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def aix() -> FFMpegDemuxerOption:
    """
    CRI AIX


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def alaw(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM A-law

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def alias_pix(
    pattern_type: int
    | None
    | Literal["glob_sequence", "glob", "sequence", "none"] = None,
    start_number: int | None = None,
    start_number_range: int | None = None,
    ts_from_file: int | None | Literal["none", "sec", "ns"] = None,
    export_path_metadata: bool | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    Alias/Wavefront PIX image

    Args:
        pattern_type: set pattern type (from 0 to INT_MAX) (default 4)
        start_number: set first number in the sequence (from INT_MIN to INT_MAX) (default 0)
        start_number_range: set range for looking at the first sequence number (from 1 to INT_MAX) (default 5)
        ts_from_file: set frame timestamp from file's one (from 0 to 2) (default none)
        export_path_metadata: enable metadata containing input path information (default false)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "pattern_type": pattern_type,
                "start_number": start_number,
                "start_number_range": start_number_range,
                "ts_from_file": ts_from_file,
                "export_path_metadata": export_path_metadata,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def alp() -> FFMpegDemuxerOption:
    """
    LEGO Racers ALP


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def alsa(
    sample_rate: int | None = None,
    channels: int | None = None,
) -> FFMpegDemuxerOption:
    """
    ALSA audio input

    Args:
        sample_rate: (from 1 to INT_MAX) (default 48000)
        channels: (from 1 to INT_MAX) (default 2)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
            }
        )
    )


def amr(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    3GPP AMR

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def amrnb(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw AMR-NB

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def amrwb(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw AMR-WB

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def anm() -> FFMpegDemuxerOption:
    """
    Deluxe Paint Animation


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def apac(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw APAC

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def apc() -> FFMpegDemuxerOption:
    """
    CRYO APC


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ape() -> FFMpegDemuxerOption:
    """
    Monkey's Audio


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def apm() -> FFMpegDemuxerOption:
    """
    Ubisoft Rayman 2 APM


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def apng(
    ignore_loop: bool | None = None,
    max_fps: int | None = None,
    default_fps: int | None = None,
) -> FFMpegDemuxerOption:
    """
    Animated Portable Network Graphics

    Args:
        ignore_loop: ignore loop setting (default true)
        max_fps: maximum framerate (0 is no limit) (from 0 to INT_MAX) (default 0)
        default_fps: default framerate (0 is as fast as possible) (from 0 to INT_MAX) (default 15)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "ignore_loop": ignore_loop,
                "max_fps": max_fps,
                "default_fps": default_fps,
            }
        )
    )


def aptx() -> FFMpegDemuxerOption:
    """
    raw aptX


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def aptx_hd() -> FFMpegDemuxerOption:
    """
    raw aptX HD


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def aqtitle(
    subfps: str | None = None,
) -> FFMpegDemuxerOption:
    """
    AQTitle subtitles

    Args:
        subfps: set the movie frame rate (from 0 to INT_MAX) (default 25/1)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "subfps": subfps,
            }
        )
    )


def argo_asf() -> FFMpegDemuxerOption:
    """
    Argonaut Games ASF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def argo_brp() -> FFMpegDemuxerOption:
    """
    Argonaut Games BRP


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def argo_cvg() -> FFMpegDemuxerOption:
    """
    Argonaut Games CVG


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def asf(
    no_resync_search: bool | None = None,
    export_xmp: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    ASF (Advanced / Active Streaming Format)

    Args:
        no_resync_search: Don't try to resynchronize by looking for a certain optional start code (default false)
        export_xmp: Export full XMP metadata (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "no_resync_search": no_resync_search,
                "export_xmp": export_xmp,
            }
        )
    )


def asf_o() -> FFMpegDemuxerOption:
    """
    ASF (Advanced / Active Streaming Format)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ass() -> FFMpegDemuxerOption:
    """
    SSA (SubStation Alpha) subtitle


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ast() -> FFMpegDemuxerOption:
    """
    AST (Audio Stream)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def au() -> FFMpegDemuxerOption:
    """
    Sun AU


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def av1(
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    AV1 Annex B

    Args:
        framerate: (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
            }
        )
    )


def avi(
    use_odml: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    AVI (Audio Video Interleaved)

    Args:
        use_odml: use odml index (default true)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "use_odml": use_odml,
            }
        )
    )


def avr() -> FFMpegDemuxerOption:
    """
    AVR (Audio Visual Research)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def avs() -> FFMpegDemuxerOption:
    """
    Argonaut Games Creature Shock


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def avs2(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw AVS2-P2/IEEE1857.4

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def avs3(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw AVS3-P2/IEEE1857.10

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def bethsoftvid() -> FFMpegDemuxerOption:
    """
    Bethesda Softworks VID


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def bfi() -> FFMpegDemuxerOption:
    """
    Brute Force & Ignorance


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def bfstm() -> FFMpegDemuxerOption:
    """
    BFSTM (Binary Cafe Stream)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def bin(
    linespeed: int | None = None,
    video_size: str | None = None,
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Binary text

    Args:
        linespeed: set simulated line speed (bytes per second) (from 1 to INT_MAX) (default 6000)
        video_size: set video size, such as 640x480 or hd720.
        framerate: set framerate (frames per second) (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "linespeed": linespeed,
                "video_size": video_size,
                "framerate": framerate,
            }
        )
    )


def bink() -> FFMpegDemuxerOption:
    """
    Bink


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def binka() -> FFMpegDemuxerOption:
    """
    Bink Audio


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def bit() -> FFMpegDemuxerOption:
    """
    G.729 BIT file format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def bitpacked(
    pixel_format: str | None = None,
    video_size: str | None = None,
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Bitpacked

    Args:
        pixel_format: set pixel format (default "yuv420p")
        video_size: set frame size
        framerate: set frame rate (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "pixel_format": pixel_format,
                "video_size": video_size,
                "framerate": framerate,
            }
        )
    )


def bmp_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped bmp sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def bmv() -> FFMpegDemuxerOption:
    """
    Discworld II BMV


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def boa() -> FFMpegDemuxerOption:
    """
    Black Ops Audio


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def bonk(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw Bonk

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def brender_pix(
    pattern_type: int
    | None
    | Literal["glob_sequence", "glob", "sequence", "none"] = None,
    start_number: int | None = None,
    start_number_range: int | None = None,
    ts_from_file: int | None | Literal["none", "sec", "ns"] = None,
    export_path_metadata: bool | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    BRender PIX image

    Args:
        pattern_type: set pattern type (from 0 to INT_MAX) (default 4)
        start_number: set first number in the sequence (from INT_MIN to INT_MAX) (default 0)
        start_number_range: set range for looking at the first sequence number (from 1 to INT_MAX) (default 5)
        ts_from_file: set frame timestamp from file's one (from 0 to 2) (default none)
        export_path_metadata: enable metadata containing input path information (default false)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "pattern_type": pattern_type,
                "start_number": start_number,
                "start_number_range": start_number_range,
                "ts_from_file": ts_from_file,
                "export_path_metadata": export_path_metadata,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def brstm() -> FFMpegDemuxerOption:
    """
    BRSTM (Binary Revolution Stream)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def c93() -> FFMpegDemuxerOption:
    """
    Interplay C93


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def caf() -> FFMpegDemuxerOption:
    """
    Apple CAF (Core Audio Format)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def cavsvideo(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw Chinese AVS (Audio Video Standard)

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def cdg() -> FFMpegDemuxerOption:
    """
    CD Graphics


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def cdxl(
    sample_rate: int | None = None,
    frame_rate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Commodore CDXL video

    Args:
        sample_rate: (from 8000 to INT_MAX) (default 11025)
        frame_rate: (default "15")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "frame_rate": frame_rate,
            }
        )
    )


def cine() -> FFMpegDemuxerOption:
    """
    Phantom Cine


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def codec2(
    frames_per_packet: int | None = None,
) -> FFMpegDemuxerOption:
    """
    codec2 .c2 demuxer

    Args:
        frames_per_packet: Number of frames to read at a time. Higher = faster decoding, lower granularity (from 1 to INT_MAX) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frames_per_packet": frames_per_packet,
            }
        )
    )


def codec2raw(
    mode: int
    | None
    | Literal[
        "3200", "2400", "1600", "1400", "1300", "1200", "700", "700B", "700C"
    ] = None,
    frames_per_packet: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw codec2 demuxer

    Args:
        mode: codec2 mode [mandatory] (from -1 to 8) (default -1)
        frames_per_packet: Number of frames to read at a time. Higher = faster decoding, lower granularity (from 1 to INT_MAX) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "mode": mode,
                "frames_per_packet": frames_per_packet,
            }
        )
    )


def concat(
    safe: bool | None = None,
    auto_convert: bool | None = None,
    segment_time_metadata: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    Virtual concatenation script

    Args:
        safe: enable safe mode (default true)
        auto_convert: automatically convert bitstream format (default true)
        segment_time_metadata: output file segment start time and duration as packet metadata (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "safe": safe,
                "auto_convert": auto_convert,
                "segment_time_metadata": segment_time_metadata,
            }
        )
    )


def cri_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped cri sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def dash(
    allowed_extensions: str | None = None,
    cenc_decryption_key: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Dynamic Adaptive Streaming over HTTP

    Args:
        allowed_extensions: List of file extensions that dash is allowed to access (default "aac,m4a,m4s,m4v,mov,mp4,webm,ts")
        cenc_decryption_key: Media decryption key (hex)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "allowed_extensions": allowed_extensions,
                "cenc_decryption_key": cenc_decryption_key,
            }
        )
    )


def data(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw data

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def daud() -> FFMpegDemuxerOption:
    """
    D-Cinema audio


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dcstr() -> FFMpegDemuxerOption:
    """
    Sega DC STR


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dds_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped dds sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def derf() -> FFMpegDemuxerOption:
    """
    Xilam DERF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dfa() -> FFMpegDemuxerOption:
    """
    Chronomaster DFA


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dfpwm(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    raw DFPWM1a

    Args:
        sample_rate: (from 0 to INT_MAX) (default 48000)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def dhav() -> FFMpegDemuxerOption:
    """
    Video DAV


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dirac(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw Dirac

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def dnxhd(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw DNxHD (SMPTE VC-3)

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def dpx_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped dpx sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def dsf() -> FFMpegDemuxerOption:
    """
    DSD Stream File (DSF)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dsicin() -> FFMpegDemuxerOption:
    """
    Delphine Software International CIN


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dss() -> FFMpegDemuxerOption:
    """
    Digital Speech Standard (DSS)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dts(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw DTS

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def dtshd() -> FFMpegDemuxerOption:
    """
    raw DTS-HD


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dv() -> FFMpegDemuxerOption:
    """
    DV (Digital Video)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def dvbsub(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw dvbsub

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def dvbtxt(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    dvbtxt

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def dxa() -> FFMpegDemuxerOption:
    """
    DXA


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ea(
    merge_alpha: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    Electronic Arts Multimedia

    Args:
        merge_alpha: return VP6 alpha in the main video stream (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "merge_alpha": merge_alpha,
            }
        )
    )


def ea_cdata() -> FFMpegDemuxerOption:
    """
    Electronic Arts cdata


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def eac3(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw E-AC-3

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def epaf() -> FFMpegDemuxerOption:
    """
    Ensoniq Paris Audio File


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def evc(
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    EVC Annex B

    Args:
        framerate: (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
            }
        )
    )


def exr_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped exr sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def f32be(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM 32-bit floating-point big-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def f32le(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM 32-bit floating-point little-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def f64be(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM 64-bit floating-point big-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def f64le(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM 64-bit floating-point little-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def fbdev(
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Linux framebuffer

    Args:
        framerate: (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
            }
        )
    )


def ffmetadata() -> FFMpegDemuxerOption:
    """
    FFmpeg metadata in text


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def film_cpk() -> FFMpegDemuxerOption:
    """
    Sega FILM / CPK


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def filmstrip() -> FFMpegDemuxerOption:
    """
    Adobe Filmstrip


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def fits(
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Flexible Image Transport System

    Args:
        framerate: set the framerate (default "1")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
            }
        )
    )


def flac(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw FLAC

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def flic() -> FFMpegDemuxerOption:
    """
    FLI/FLC/FLX animation


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def flv() -> FFMpegDemuxerOption:
    """
    FLV (Flash Video)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def frm() -> FFMpegDemuxerOption:
    """
    Megalux Frame


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def fsb() -> FFMpegDemuxerOption:
    """
    FMOD Sample Bank


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def fwse() -> FFMpegDemuxerOption:
    """
    Capcom's MT Framework sound


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def g722(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw G.722

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def g723_1() -> FFMpegDemuxerOption:
    """
    G.723.1


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def g726(
    code_size: int | None = None,
    sample_rate: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw big-endian G.726 ("left aligned")

    Args:
        code_size: Bits per G.726 code (from 2 to 5) (default 4)
        sample_rate: (from 0 to INT_MAX) (default 8000)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "code_size": code_size,
                "sample_rate": sample_rate,
            }
        )
    )


def g726le(
    code_size: int | None = None,
    sample_rate: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw little-endian G.726 ("right aligned")

    Args:
        code_size: Bits per G.726 code (from 2 to 5) (default 4)
        sample_rate: (from 0 to INT_MAX) (default 8000)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "code_size": code_size,
                "sample_rate": sample_rate,
            }
        )
    )


def g729(
    bit_rate: int | None = None,
) -> FFMpegDemuxerOption:
    """
    G.729 raw format demuxer

    Args:
        bit_rate: (from 0 to INT_MAX) (default 8000)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "bit_rate": bit_rate,
            }
        )
    )


def gdv() -> FFMpegDemuxerOption:
    """
    Gremlin Digital Video


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def gem_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped gem sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def genh() -> FFMpegDemuxerOption:
    """
    GENeric Header


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def gif(
    min_delay: int | None = None,
    max_gif_delay: int | None = None,
    default_delay: int | None = None,
    ignore_loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    CompuServe Graphics Interchange Format (GIF)

    Args:
        min_delay: minimum valid delay between frames (in hundredths of second) (from 0 to 6000) (default 2)
        max_gif_delay: maximum valid delay between frames (in hundredths of seconds) (from 0 to 65535) (default 65535)
        default_delay: default delay between frames (in hundredths of second) (from 0 to 6000) (default 10)
        ignore_loop: ignore loop setting (netscape extension) (default true)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "min_delay": min_delay,
                "max_gif_delay": max_gif_delay,
                "default_delay": default_delay,
                "ignore_loop": ignore_loop,
            }
        )
    )


def gif_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped gif sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def gsm(
    sample_rate: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw GSM

    Args:
        sample_rate: (from 1 to 6.50753e+07) (default 8000)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
            }
        )
    )


def gxf() -> FFMpegDemuxerOption:
    """
    GXF (General eXchange Format)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def h261(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw H.261

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def h263(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw H.263

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def h264(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw H.264 video

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def hca(
    hca_lowkey: int | None = None,
    hca_highkey: int | None = None,
    hca_subkey: int | None = None,
) -> FFMpegDemuxerOption:
    """
    CRI HCA

    Args:
        hca_lowkey: Low key used for handling CRI HCA files (from 0 to UINT32_MAX) (default 0)
        hca_highkey: High key used for handling CRI HCA files (from 0 to UINT32_MAX) (default 0)
        hca_subkey: Subkey used for handling CRI HCA files (from 0 to 65535) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "hca_lowkey": hca_lowkey,
                "hca_highkey": hca_highkey,
                "hca_subkey": hca_subkey,
            }
        )
    )


def hcom() -> FFMpegDemuxerOption:
    """
    Macintosh HCOM


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def hdr_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped hdr sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def hevc(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw HEVC video

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def hls(
    live_start_index: int | None = None,
    prefer_x_start: bool | None = None,
    allowed_extensions: str | None = None,
    max_reload: int | None = None,
    m3u8_hold_counters: int | None = None,
    http_persistent: bool | None = None,
    http_multiple: bool | None = None,
    http_seekable: bool | None = None,
    seg_format_options: str | None = None,
    seg_max_retry: int | None = None,
) -> FFMpegDemuxerOption:
    """
    Apple HTTP Live Streaming

    Args:
        live_start_index: segment index to start live streams at (negative values are from the end) (from INT_MIN to INT_MAX) (default -3)
        prefer_x_start: prefer to use #EXT-X-START if it's in playlist instead of live_start_index (default false)
        allowed_extensions: List of file extensions that hls is allowed to access (default "3gp,aac,avi,ac3,eac3,flac,mkv,m3u8,m4a,m4s,m4v,mpg,mov,mp2,mp3,mp4,mpeg,mpegts,ogg,ogv,oga,ts,vob,wav")
        max_reload: Maximum number of times a insufficient list is attempted to be reloaded (from 0 to INT_MAX) (default 3)
        m3u8_hold_counters: The maximum number of times to load m3u8 when it refreshes without new segments (from 0 to INT_MAX) (default 1000)
        http_persistent: Use persistent HTTP connections (default true)
        http_multiple: Use multiple HTTP connections for fetching segments (default auto)
        http_seekable: Use HTTP partial requests, 0 = disable, 1 = enable, -1 = auto (default auto)
        seg_format_options: Set options for segment demuxer
        seg_max_retry: Maximum number of times to reload a segment on error. (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "live_start_index": live_start_index,
                "prefer_x_start": prefer_x_start,
                "allowed_extensions": allowed_extensions,
                "max_reload": max_reload,
                "m3u8_hold_counters": m3u8_hold_counters,
                "http_persistent": http_persistent,
                "http_multiple": http_multiple,
                "http_seekable": http_seekable,
                "seg_format_options": seg_format_options,
                "seg_max_retry": seg_max_retry,
            }
        )
    )


def hnm() -> FFMpegDemuxerOption:
    """
    Cryo HNM v4


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ico() -> FFMpegDemuxerOption:
    """
    Microsoft Windows ICO


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def idcin() -> FFMpegDemuxerOption:
    """
    id Cinematic


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def idf(
    linespeed: int | None = None,
    video_size: str | None = None,
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    iCE Draw File

    Args:
        linespeed: set simulated line speed (bytes per second) (from 1 to INT_MAX) (default 6000)
        video_size: set video size, such as 640x480 or hd720.
        framerate: set framerate (frames per second) (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "linespeed": linespeed,
                "video_size": video_size,
                "framerate": framerate,
            }
        )
    )


def iec61883(
    dvtype: int | None | Literal["auto", "dv", "hdv"] = None,
    dvbuffer: int | None = None,
    dvguid: str | None = None,
) -> FFMpegDemuxerOption:
    """
    libiec61883 (new DV1394) A/V input device

    Args:
        dvtype: override autodetection of DV/HDV (from 0 to 2) (default auto)
        dvbuffer: set queue buffer size (in packets) (from 0 to INT_MAX) (default 0)
        dvguid: select one of multiple DV devices by its GUID

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "dvtype": dvtype,
                "dvbuffer": dvbuffer,
                "dvguid": dvguid,
            }
        )
    )


def iff() -> FFMpegDemuxerOption:
    """
    IFF (Interchange File Format)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ifv() -> FFMpegDemuxerOption:
    """
    IFV CCTV DVR


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ilbc() -> FFMpegDemuxerOption:
    """
    iLBC storage


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def image2(
    pattern_type: int
    | None
    | Literal["glob_sequence", "glob", "sequence", "none"] = None,
    start_number: int | None = None,
    start_number_range: int | None = None,
    ts_from_file: int | None | Literal["none", "sec", "ns"] = None,
    export_path_metadata: bool | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    image2 sequence

    Args:
        pattern_type: set pattern type (from 0 to INT_MAX) (default 4)
        start_number: set first number in the sequence (from INT_MIN to INT_MAX) (default 0)
        start_number_range: set range for looking at the first sequence number (from 1 to INT_MAX) (default 5)
        ts_from_file: set frame timestamp from file's one (from 0 to 2) (default none)
        export_path_metadata: enable metadata containing input path information (default false)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "pattern_type": pattern_type,
                "start_number": start_number,
                "start_number_range": start_number_range,
                "ts_from_file": ts_from_file,
                "export_path_metadata": export_path_metadata,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def image2pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped image2 sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def imf(
    assetmaps: str | None = None,
) -> FFMpegDemuxerOption:
    """
    IMF (Interoperable Master Format)

    Args:
        assetmaps: Comma-separated paths to ASSETMAP files.If not specified, the `ASSETMAP.xml` file in the same directory as the CPL is used.

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "assetmaps": assetmaps,
            }
        )
    )


def ingenient(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw Ingenient MJPEG

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def ipmovie() -> FFMpegDemuxerOption:
    """
    Interplay MVE


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ipu(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw IPU Video

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def ircam() -> FFMpegDemuxerOption:
    """
    Berkeley/IRCAM/CARL Sound Format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def iss() -> FFMpegDemuxerOption:
    """
    Funcom ISS


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def iv8() -> FFMpegDemuxerOption:
    """
    IndigoVision 8000 video


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ivf() -> FFMpegDemuxerOption:
    """
    On2 IVF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ivr() -> FFMpegDemuxerOption:
    """
    IVR (Internet Video Recording)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def j2k_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped j2k sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def jack(
    channels: int | None = None,
) -> FFMpegDemuxerOption:
    """
    JACK Audio Connection Kit

    Args:
        channels: Number of audio channels. (from 1 to INT_MAX) (default 2)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "channels": channels,
            }
        )
    )


def jacosub() -> FFMpegDemuxerOption:
    """
    JACOsub subtitle format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def jpeg_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped jpeg sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def jpegls_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped jpegls sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def jpegxl_anim() -> FFMpegDemuxerOption:
    """
    Animated JPEG XL


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def jpegxl_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped jpegxl sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def jv() -> FFMpegDemuxerOption:
    """
    Bitmap Brothers JV


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def kmsgrab(
    device: str | None = None,
    format: str | None = None,
    format_modifier: int | None = None,
    crtc_id: int | None = None,
    plane_id: int | None = None,
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    KMS screen capture

    Args:
        device: DRM device path (default "/dev/dri/card0")
        format: Pixel format for framebuffer (default none)
        format_modifier: DRM format modifier for framebuffer (from 0 to I64_MAX) (default 72057594037927935)
        crtc_id: CRTC ID to define capture source (from 0 to UINT32_MAX) (default 0)
        plane_id: Plane ID to define capture source (from 0 to UINT32_MAX) (default 0)
        framerate: Framerate to capture at (from 0 to 1000) (default 30/1)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "device": device,
                "format": format,
                "format_modifier": format_modifier,
                "crtc_id": crtc_id,
                "plane_id": plane_id,
                "framerate": framerate,
            }
        )
    )


def kux() -> FFMpegDemuxerOption:
    """
    KUX (YouKu)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def kvag() -> FFMpegDemuxerOption:
    """
    Simon & Schuster Interactive VAG


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def laf() -> FFMpegDemuxerOption:
    """
    LAF (Limitless Audio Format)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def lavfi(
    graph: str | None = None,
    graph_file: str | None = None,
    dumpgraph: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Libavfilter virtual input device

    Args:
        graph: set libavfilter graph
        graph_file: set libavfilter graph filename
        dumpgraph: dump graph to stderr

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "graph": graph,
                "graph_file": graph_file,
                "dumpgraph": dumpgraph,
            }
        )
    )


def libcdio(
    speed: int | None = None,
    paranoia_mode: str | None = None,
) -> FFMpegDemuxerOption:
    """


    Args:
        speed: set drive reading speed (from 0 to INT_MAX) (default 0)
        paranoia_mode: set error recovery mode (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "speed": speed,
                "paranoia_mode": paranoia_mode,
            }
        )
    )


def libdc1394(
    video_size: str | None = None,
    pixel_format: str | None = None,
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    dc1394 v.2 A/V grab

    Args:
        video_size: A string describing frame size, such as 640x480 or hd720. (default "qvga")
        pixel_format: (default "uyvy422")
        framerate: (default "ntsc")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "video_size": video_size,
                "pixel_format": pixel_format,
                "framerate": framerate,
            }
        )
    )


def libgme(
    track_index: int | None = None,
    sample_rate: int | None = None,
    max_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    Game Music Emu demuxer

    Args:
        track_index: set track that should be played (from 0 to INT_MAX) (default 0)
        sample_rate: set sample rate (from 1000 to 999999) (default 44100)
        max_size: set max file size supported (in bytes) (from 0 to 1.84467e+19) (default 52428800)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "track_index": track_index,
                "sample_rate": sample_rate,
                "max_size": max_size,
            }
        )
    )


def libopenmpt(
    sample_rate: int | None = None,
    layout: str | None = None,
    subsong: int | None | Literal["all", "auto"] = None,
) -> FFMpegDemuxerOption:
    """
    Tracker formats (libopenmpt)

    Args:
        sample_rate: set sample rate (from 1000 to INT_MAX) (default 48000)
        layout: set channel layout (default "stereo")
        subsong: set subsong (from -2 to INT_MAX) (default auto)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "layout": layout,
                "subsong": subsong,
            }
        )
    )


def live_flv() -> FFMpegDemuxerOption:
    """
    live RTMP FLV (Flash Video)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def lmlm4() -> FFMpegDemuxerOption:
    """
    raw lmlm4


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def loas(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    LOAS AudioSyncStream

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def lrc() -> FFMpegDemuxerOption:
    """
    LRC lyrics


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def luodat() -> FFMpegDemuxerOption:
    """
    Video CCTV DAT


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def lvf() -> FFMpegDemuxerOption:
    """
    LVF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def lxf() -> FFMpegDemuxerOption:
    """
    VR native stream (LXF)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def m4v(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw MPEG-4 video

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def mca() -> FFMpegDemuxerOption:
    """
    MCA Audio Format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mcc() -> FFMpegDemuxerOption:
    """
    MacCaption


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mgsts() -> FFMpegDemuxerOption:
    """
    Metal Gear Solid: The Twin Snakes


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def microdvd(
    subfps: str | None = None,
) -> FFMpegDemuxerOption:
    """
    MicroDVD subtitle format

    Args:
        subfps: set the movie frame rate fallback (from 0 to INT_MAX) (default 0/1)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "subfps": subfps,
            }
        )
    )


def mjpeg(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw MJPEG video

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def mjpeg_2000(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw MJPEG 2000 video

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def mlp(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw MLP

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def mlv() -> FFMpegDemuxerOption:
    """
    Magic Lantern Video (MLV)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mm() -> FFMpegDemuxerOption:
    """
    American Laser Games MM


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mmf() -> FFMpegDemuxerOption:
    """
    Yamaha SMAF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mods() -> FFMpegDemuxerOption:
    """
    MobiClip MODS


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def moflex() -> FFMpegDemuxerOption:
    """
    MobiClip MOFLEX


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mp3(
    usetoc: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    MP2/3 (MPEG audio layer 2/3)

    Args:
        usetoc: use table of contents (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "usetoc": usetoc,
            }
        )
    )


def mpc() -> FFMpegDemuxerOption:
    """
    Musepack


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mpc8() -> FFMpegDemuxerOption:
    """
    Musepack SV8


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mpeg() -> FFMpegDemuxerOption:
    """
    MPEG-PS (MPEG-2 Program Stream)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mpegts(
    resync_size: int | None = None,
    fix_teletext_pts: bool | None = None,
    ts_packetsize: int | None = None,
    scan_all_pmts: bool | None = None,
    skip_unknown_pmt: bool | None = None,
    merge_pmt_versions: bool | None = None,
    max_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    MPEG-TS (MPEG-2 Transport Stream)

    Args:
        resync_size: set size limit for looking up a new synchronization (from 0 to INT_MAX) (default 65536)
        fix_teletext_pts: try to fix pts values of dvb teletext streams (default true)
        ts_packetsize: output option carrying the raw packet size (from 0 to 0) (default 0)
        scan_all_pmts: scan and combine all PMTs (default auto)
        skip_unknown_pmt: skip PMTs for programs not advertised in the PAT (default false)
        merge_pmt_versions: re-use streams when PMT's version/pids change (default false)
        max_packet_size: maximum size of emitted packet (from 1 to 1.07374e+09) (default 204800)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "resync_size": resync_size,
                "fix_teletext_pts": fix_teletext_pts,
                "ts_packetsize": ts_packetsize,
                "scan_all_pmts": scan_all_pmts,
                "skip_unknown_pmt": skip_unknown_pmt,
                "merge_pmt_versions": merge_pmt_versions,
                "max_packet_size": max_packet_size,
            }
        )
    )


def mpegtsraw(
    resync_size: int | None = None,
    compute_pcr: bool | None = None,
    ts_packetsize: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw MPEG-TS (MPEG-2 Transport Stream)

    Args:
        resync_size: set size limit for looking up a new synchronization (from 0 to INT_MAX) (default 65536)
        compute_pcr: compute exact PCR for each transport stream packet (default false)
        ts_packetsize: output option carrying the raw packet size (from 0 to 0) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "resync_size": resync_size,
                "compute_pcr": compute_pcr,
                "ts_packetsize": ts_packetsize,
            }
        )
    )


def mpegvideo(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw MPEG video

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def mpjpeg(
    strict_mime_boundary: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    MIME multipart JPEG

    Args:
        strict_mime_boundary: require MIME boundaries match (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "strict_mime_boundary": strict_mime_boundary,
            }
        )
    )


def mpl2() -> FFMpegDemuxerOption:
    """
    MPL2 subtitles


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mpsub() -> FFMpegDemuxerOption:
    """
    MPlayer subtitles


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def msf() -> FFMpegDemuxerOption:
    """
    Sony PS3 MSF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def msnwctcp() -> FFMpegDemuxerOption:
    """
    MSN TCP Webcam stream


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def msp() -> FFMpegDemuxerOption:
    """
    Microsoft Paint (MSP))


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mtaf() -> FFMpegDemuxerOption:
    """
    Konami PS2 MTAF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mtv() -> FFMpegDemuxerOption:
    """
    MTV


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mulaw(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM mu-law

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def musx() -> FFMpegDemuxerOption:
    """
    Eurocom MUSX


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mv() -> FFMpegDemuxerOption:
    """
    Silicon Graphics Movie


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mvi() -> FFMpegDemuxerOption:
    """
    Motion Pixels MVI


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def mxf(
    eia608_extract: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    MXF (Material eXchange Format)

    Args:
        eia608_extract: extract eia 608 captions from s436m track (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "eia608_extract": eia608_extract,
            }
        )
    )


def mxg() -> FFMpegDemuxerOption:
    """
    MxPEG clip


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def nc() -> FFMpegDemuxerOption:
    """
    NC camera feed


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def nistsphere() -> FFMpegDemuxerOption:
    """
    NIST SPeech HEader REsources


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def nsp() -> FFMpegDemuxerOption:
    """
    Computerized Speech Lab NSP


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def nsv() -> FFMpegDemuxerOption:
    """
    Nullsoft Streaming Video


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def nut() -> FFMpegDemuxerOption:
    """
    NUT


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def nuv() -> FFMpegDemuxerOption:
    """
    NuppelVideo


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def obu(
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    AV1 low overhead OBU

    Args:
        framerate: (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
            }
        )
    )


def ogg() -> FFMpegDemuxerOption:
    """
    Ogg


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def oma() -> FFMpegDemuxerOption:
    """
    Sony OpenMG audio


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def openal(
    channels: int | None = None,
    sample_rate: int | None = None,
    sample_size: int | None = None,
    list_devices: int | None | Literal["true", "false"] = None,
) -> FFMpegDemuxerOption:
    """
    OpenAL audio capture device

    Args:
        channels: set number of channels (from 1 to 2) (default 2)
        sample_rate: set sample rate (from 1 to 192000) (default 44100)
        sample_size: set sample size (from 8 to 16) (default 16)
        list_devices: list available devices (from 0 to 1) (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "channels": channels,
                "sample_rate": sample_rate,
                "sample_size": sample_size,
                "list_devices": list_devices,
            }
        )
    )


def osq(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw OSQ

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def oss(
    sample_rate: int | None = None,
    channels: int | None = None,
) -> FFMpegDemuxerOption:
    """
    OSS (Open Sound System) capture

    Args:
        sample_rate: (from 1 to INT_MAX) (default 48000)
        channels: (from 1 to INT_MAX) (default 2)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
            }
        )
    )


def paf() -> FFMpegDemuxerOption:
    """
    Amazing Studio Packed Animation File


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def pam_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped pam sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pbm_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped pbm sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pcx_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped pcx sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pdv() -> FFMpegDemuxerOption:
    """
    PlayDate Video


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def pfm_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped pfm sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pgm_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped pgm sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pgmyuv_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped pgmyuv sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pgx_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped pgx sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def phm_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped phm sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def photocd_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped photocd sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pictor_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped pictor sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pjs() -> FFMpegDemuxerOption:
    """
    PJS (Phoenix Japanimation Society) subtitles


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def pmp() -> FFMpegDemuxerOption:
    """
    Playstation Portable PMP


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def png_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped png sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def pp_bnk() -> FFMpegDemuxerOption:
    """
    Pro Pinball Series Soundbank


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ppm_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped ppm sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def psd_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped psd sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def psxstr() -> FFMpegDemuxerOption:
    """
    Sony Playstation STR


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def pulse(
    server: str | None = None,
    name: str | None = None,
    stream_name: str | None = None,
    sample_rate: int | None = None,
    channels: int | None = None,
    frame_size: int | None = None,
    fragment_size: int | None = None,
    wallclock: int | None = None,
) -> FFMpegDemuxerOption:
    """
    Pulse audio input

    Args:
        server: set PulseAudio server
        name: set application name (default "Lavf60.16.100")
        stream_name: set stream description (default "record")
        sample_rate: set sample rate in Hz (from 1 to INT_MAX) (default 48000)
        channels: set number of audio channels (from 1 to INT_MAX) (default 2)
        frame_size: set number of bytes per frame (from 1 to INT_MAX) (default 1024)
        fragment_size: set buffering size, affects latency and cpu usage (from -1 to INT_MAX) (default -1)
        wallclock: set the initial pts using the current time (from -1 to 1) (default 1)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "server": server,
                "name": name,
                "stream_name": stream_name,
                "sample_rate": sample_rate,
                "channels": channels,
                "frame_size": frame_size,
                "fragment_size": fragment_size,
                "wallclock": wallclock,
            }
        )
    )


def pva() -> FFMpegDemuxerOption:
    """
    TechnoTrend PVA


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def pvf() -> FFMpegDemuxerOption:
    """
    PVF (Portable Voice Format)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def qcp() -> FFMpegDemuxerOption:
    """
    QCP


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def qdraw_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped qdraw sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def qoi_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped qoi sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def r3d() -> FFMpegDemuxerOption:
    """
    REDCODE R3D


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def rawvideo(
    pixel_format: str | None = None,
    video_size: str | None = None,
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    raw video

    Args:
        pixel_format: set pixel format (default "yuv420p")
        video_size: set frame size
        framerate: set frame rate (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "pixel_format": pixel_format,
                "video_size": video_size,
                "framerate": framerate,
            }
        )
    )


def realtext() -> FFMpegDemuxerOption:
    """
    RealText subtitle format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def redspark() -> FFMpegDemuxerOption:
    """
    RedSpark


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def rka() -> FFMpegDemuxerOption:
    """
    RKA (RK Audio)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def rl2() -> FFMpegDemuxerOption:
    """
    RL2


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def rm() -> FFMpegDemuxerOption:
    """
    RealMedia


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def roq() -> FFMpegDemuxerOption:
    """
    id RoQ


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def rpl() -> FFMpegDemuxerOption:
    """
    RPL / ARMovie


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def rsd() -> FFMpegDemuxerOption:
    """
    GameCube RSD


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def rso() -> FFMpegDemuxerOption:
    """
    Lego Mindstorms RSO


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def rtp(
    rtp_flags: str | None = None,
    listen_timeout: str | None = None,
    localaddr: str | None = None,
    allowed_media_types: str | None = None,
    reorder_queue_size: int | None = None,
    buffer_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    RTP input

    Args:
        rtp_flags: set RTP flags (default 0)
        listen_timeout: set maximum timeout (in seconds) to wait for incoming connections (default 10)
        localaddr: local address
        allowed_media_types: set media types to accept from the server (default video+audio+data+subtitle)
        reorder_queue_size: set number of packets to buffer for handling of reordered packets (from -1 to INT_MAX) (default -1)
        buffer_size: Underlying protocol send/receive buffer size (from -1 to INT_MAX) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "rtp_flags": rtp_flags,
                "listen_timeout": listen_timeout,
                "localaddr": localaddr,
                "allowed_media_types": allowed_media_types,
                "reorder_queue_size": reorder_queue_size,
                "buffer_size": buffer_size,
            }
        )
    )


def rtsp(
    initial_pause: bool | None = None,
    rtsp_transport: str | None = None,
    rtsp_flags: str | None = None,
    allowed_media_types: str | None = None,
    min_port: int | None = None,
    max_port: int | None = None,
    listen_timeout: int | None = None,
    timeout: int | None = None,
    reorder_queue_size: int | None = None,
    buffer_size: int | None = None,
    user_agent: str | None = None,
) -> FFMpegDemuxerOption:
    """
    RTSP input

    Args:
        initial_pause: do not start playing the stream immediately (default false)
        rtsp_transport: set RTSP transport protocols (default 0)
        rtsp_flags: set RTSP flags (default 0)
        allowed_media_types: set media types to accept from the server (default video+audio+data+subtitle)
        min_port: set minimum local UDP port (from 0 to 65535) (default 5000)
        max_port: set maximum local UDP port (from 0 to 65535) (default 65000)
        listen_timeout: set maximum timeout (in seconds) to wait for incoming connections (-1 is infinite, imply flag listen) (from INT_MIN to INT_MAX) (default -1)
        timeout: set timeout (in microseconds) of socket I/O operations (from INT_MIN to I64_MAX) (default 0)
        reorder_queue_size: set number of packets to buffer for handling of reordered packets (from -1 to INT_MAX) (default -1)
        buffer_size: Underlying protocol send/receive buffer size (from -1 to INT_MAX) (default -1)
        user_agent: override User-Agent header (default "Lavf60.16.100")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "initial_pause": initial_pause,
                "rtsp_transport": rtsp_transport,
                "rtsp_flags": rtsp_flags,
                "allowed_media_types": allowed_media_types,
                "min_port": min_port,
                "max_port": max_port,
                "listen_timeout": listen_timeout,
                "timeout": timeout,
                "reorder_queue_size": reorder_queue_size,
                "buffer_size": buffer_size,
                "user_agent": user_agent,
            }
        )
    )


def s16be(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM signed 16-bit big-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def s16le(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM signed 16-bit little-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def s24be(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM signed 24-bit big-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def s24le(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM signed 24-bit little-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def s32be(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM signed 32-bit big-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def s32le(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM signed 32-bit little-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def s337m() -> FFMpegDemuxerOption:
    """
    SMPTE 337M


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def s8(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM signed 8-bit

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def sami() -> FFMpegDemuxerOption:
    """
    SAMI subtitle format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sap() -> FFMpegDemuxerOption:
    """
    SAP input


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sbc(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw SBC (low-complexity subband codec)

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def sbg(
    sample_rate: int | None = None,
    frame_size: int | None = None,
    max_file_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    SBaGen binaural beats script

    Args:
        sample_rate: (from 0 to INT_MAX) (default 0)
        frame_size: (from 0 to INT_MAX) (default 0)
        max_file_size: (from 0 to INT_MAX) (default 5000000)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "frame_size": frame_size,
                "max_file_size": max_file_size,
            }
        )
    )


def scc() -> FFMpegDemuxerOption:
    """
    Scenarist Closed Captions


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def scd() -> FFMpegDemuxerOption:
    """
    Square Enix SCD


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sdns() -> FFMpegDemuxerOption:
    """
    Xbox SDNS


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sdp(
    sdp_flags: str | None = None,
    listen_timeout: str | None = None,
    localaddr: str | None = None,
    allowed_media_types: str | None = None,
    reorder_queue_size: int | None = None,
    buffer_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    SDP

    Args:
        sdp_flags: SDP flags (default 0)
        listen_timeout: set maximum timeout (in seconds) to wait for incoming connections (default 10)
        localaddr: local address
        allowed_media_types: set media types to accept from the server (default video+audio+data+subtitle)
        reorder_queue_size: set number of packets to buffer for handling of reordered packets (from -1 to INT_MAX) (default -1)
        buffer_size: Underlying protocol send/receive buffer size (from -1 to INT_MAX) (default -1)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sdp_flags": sdp_flags,
                "listen_timeout": listen_timeout,
                "localaddr": localaddr,
                "allowed_media_types": allowed_media_types,
                "reorder_queue_size": reorder_queue_size,
                "buffer_size": buffer_size,
            }
        )
    )


def sdr2() -> FFMpegDemuxerOption:
    """
    SDR2


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sds() -> FFMpegDemuxerOption:
    """
    MIDI Sample Dump Standard


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sdx() -> FFMpegDemuxerOption:
    """
    Sample Dump eXchange


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ser(
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    SER (Simple uncompressed video format for astronomical capturing)

    Args:
        framerate: set frame rate (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
            }
        )
    )


def sga() -> FFMpegDemuxerOption:
    """
    Digital Pictures SGA


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sgi_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped sgi sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def shn(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw Shorten

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def siff() -> FFMpegDemuxerOption:
    """
    Beam Software SIFF


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def simbiosis_imx() -> FFMpegDemuxerOption:
    """
    Simbiosis Interactive IMX


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sln(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Asterisk raw pcm

    Args:
        sample_rate: (from 0 to INT_MAX) (default 8000)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def smjpeg() -> FFMpegDemuxerOption:
    """
    Loki SDL MJPEG


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def smk() -> FFMpegDemuxerOption:
    """
    Smacker


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def smush() -> FFMpegDemuxerOption:
    """
    LucasArts Smush


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sol() -> FFMpegDemuxerOption:
    """
    Sierra SOL


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sox() -> FFMpegDemuxerOption:
    """
    SoX (Sound eXchange) native


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def spdif() -> FFMpegDemuxerOption:
    """
    IEC 61937 (compressed data in S/PDIF)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def srt() -> FFMpegDemuxerOption:
    """
    SubRip subtitle


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def stl() -> FFMpegDemuxerOption:
    """
    Spruce subtitle format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def subviewer() -> FFMpegDemuxerOption:
    """
    SubViewer subtitle format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def subviewer1() -> FFMpegDemuxerOption:
    """
    SubViewer v1 subtitle format


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def sunrast_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped sunrast sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def sup() -> FFMpegDemuxerOption:
    """
    raw HDMV Presentation Graphic Stream subtitles


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def svag() -> FFMpegDemuxerOption:
    """
    Konami PS2 SVAG


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def svg_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped svg sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def svs() -> FFMpegDemuxerOption:
    """
    Square SVS


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def swf() -> FFMpegDemuxerOption:
    """
    SWF (ShockWave Flash)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def tak(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw TAK

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def tedcaptions(
    start_time: int | None = None,
) -> FFMpegDemuxerOption:
    """
    TED Talks captions

    Args:
        start_time: set the start time (offset) of the subtitles, in ms (from I64_MIN to I64_MAX) (default 15000)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "start_time": start_time,
            }
        )
    )


def thp() -> FFMpegDemuxerOption:
    """
    THP


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def tiertexseq() -> FFMpegDemuxerOption:
    """
    Tiertex Limited SEQ


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def tiff_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped tiff sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def tmv() -> FFMpegDemuxerOption:
    """
    8088flex TMV


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def truehd(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw TrueHD

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def tta() -> FFMpegDemuxerOption:
    """
    TTA (True Audio)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def tty(
    chars_per_frame: int | None = None,
    video_size: str | None = None,
    framerate: str | None = None,
) -> FFMpegDemuxerOption:
    """
    Tele-typewriter

    Args:
        chars_per_frame: (from 1 to INT_MAX) (default 6000)
        video_size: A string describing frame size, such as 640x480 or hd720.
        framerate: (default "25")

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "chars_per_frame": chars_per_frame,
                "video_size": video_size,
                "framerate": framerate,
            }
        )
    )


def txd() -> FFMpegDemuxerOption:
    """
    Renderware TeXture Dictionary


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def ty() -> FFMpegDemuxerOption:
    """
    TiVo TY Stream


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def u16be(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM unsigned 16-bit big-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def u16le(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM unsigned 16-bit little-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def u24be(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM unsigned 24-bit big-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def u24le(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM unsigned 24-bit little-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def u32be(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM unsigned 32-bit big-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def u32le(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM unsigned 32-bit little-endian

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def u8(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM unsigned 8-bit

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def usm() -> FFMpegDemuxerOption:
    """
    CRI USM


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def v210() -> FFMpegDemuxerOption:
    """
    Uncompressed 4:2:2 10-bit


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def v210x() -> FFMpegDemuxerOption:
    """
    Uncompressed 4:2:2 10-bit


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vag() -> FFMpegDemuxerOption:
    """
    Sony PS2 VAG


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vbn_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped vbn sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def vc1(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw VC-1

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def vc1test() -> FFMpegDemuxerOption:
    """
    VC-1 test bitstream


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vidc(
    sample_rate: int | None = None,
    channels: int | None = None,
    ch_layout: str | None = None,
) -> FFMpegDemuxerOption:
    """
    PCM Archimedes VIDC

    Args:
        sample_rate: (from 0 to INT_MAX) (default 44100)
        channels: (from 0 to INT_MAX) (default 1)
        ch_layout:

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sample_rate": sample_rate,
                "channels": channels,
                "ch_layout": ch_layout,
            }
        )
    )


def vividas() -> FFMpegDemuxerOption:
    """
    Vividas VIV


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vivo() -> FFMpegDemuxerOption:
    """
    Vivo


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vmd() -> FFMpegDemuxerOption:
    """
    Sierra VMD


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vobsub(
    sub_name: str | None = None,
) -> FFMpegDemuxerOption:
    """
    VobSub subtitle format

    Args:
        sub_name: URI for .sub file

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "sub_name": sub_name,
            }
        )
    )


def voc() -> FFMpegDemuxerOption:
    """
    Creative Voice


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vpk() -> FFMpegDemuxerOption:
    """
    Sony PS2 VPK


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vplayer() -> FFMpegDemuxerOption:
    """
    VPlayer subtitles


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vqf() -> FFMpegDemuxerOption:
    """
    Nippon Telegraph and Telephone Corporation (NTT) TwinVQ


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def vvc(
    framerate: str | None = None,
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    raw H.266/VVC video

    Args:
        framerate: (default "25")
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "framerate": framerate,
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def w64(
    max_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    Sony Wave64

    Args:
        max_size: max size of single packet (from 1024 to 4.1943e+06) (default 4096)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "max_size": max_size,
            }
        )
    )


def wady() -> FFMpegDemuxerOption:
    """
    Marble WADY


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def wav(
    ignore_length: bool | None = None,
    max_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    WAV / WAVE (Waveform Audio)

    Args:
        ignore_length: Ignore length (default false)
        max_size: max size of single packet (from 1024 to 4.1943e+06) (default 4096)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "ignore_length": ignore_length,
                "max_size": max_size,
            }
        )
    )


def wavarc() -> FFMpegDemuxerOption:
    """
    Waveform Archiver


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def wc3movie() -> FFMpegDemuxerOption:
    """
    Wing Commander III movie


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def webm_dash_manifest(
    live: bool | None = None,
    bandwidth: int | None = None,
) -> FFMpegDemuxerOption:
    """
    WebM DASH Manifest

    Args:
        live: flag indicating that the input is a live file that only has the headers. (default false)
        bandwidth: bandwidth of this stream to be specified in the DASH manifest. (from 0 to INT_MAX) (default 0)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "live": live,
                "bandwidth": bandwidth,
            }
        )
    )


def webp_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped webp sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def webvtt(
    kind: int
    | None
    | Literal["subtitles", "captions", "descriptions", "metadata"] = None,
) -> FFMpegDemuxerOption:
    """
    WebVTT subtitle

    Args:
        kind: Set kind of WebVTT track (from 0 to INT_MAX) (default subtitles)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "kind": kind,
            }
        )
    )


def wsaud() -> FFMpegDemuxerOption:
    """
    Westwood Studios audio


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def wsd(
    raw_packet_size: int | None = None,
) -> FFMpegDemuxerOption:
    """
    Wideband Single-bit Data (WSD)

    Args:
        raw_packet_size: (from 1 to INT_MAX) (default 1024)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "raw_packet_size": raw_packet_size,
            }
        )
    )


def wsvqa() -> FFMpegDemuxerOption:
    """
    Westwood Studios VQA


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def wtv() -> FFMpegDemuxerOption:
    """
    Windows Television (WTV)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def wv() -> FFMpegDemuxerOption:
    """
    WavPack


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def wve() -> FFMpegDemuxerOption:
    """
    Psion 3 audio


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def x11grab(
    window_id: int | None = None,
    x: int | None = None,
    y: int | None = None,
    grab_x: int | None = None,
    grab_y: int | None = None,
    video_size: str | None = None,
    framerate: str | None = None,
    draw_mouse: int | None = None,
    follow_mouse: int | None | Literal["centered"] = None,
    show_region: int | None = None,
    region_border: int | None = None,
    select_region: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    X11 screen capture, using XCB

    Args:
        window_id: Window to capture. (from 0 to UINT32_MAX) (default 0)
        x: Initial x coordinate. (from 0 to INT_MAX) (default 0)
        y: Initial y coordinate. (from 0 to INT_MAX) (default 0)
        grab_x: Initial x coordinate. (from 0 to INT_MAX) (default 0)
        grab_y: Initial y coordinate. (from 0 to INT_MAX) (default 0)
        video_size: A string describing frame size, such as 640x480 or hd720.
        framerate: (default "ntsc")
        draw_mouse: Draw the mouse pointer. (from 0 to 1) (default 1)
        follow_mouse: Move the grabbing region when the mouse pointer reaches within specified amount of pixels to the edge of region. (from -1 to INT_MAX) (default 0)
        show_region: Show the grabbing region. (from 0 to 1) (default 0)
        region_border: Set the region border thickness. (from 1 to 128) (default 3)
        select_region: Select the grabbing region graphically using the pointer. (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "window_id": window_id,
                "x": x,
                "y": y,
                "grab_x": grab_x,
                "grab_y": grab_y,
                "video_size": video_size,
                "framerate": framerate,
                "draw_mouse": draw_mouse,
                "follow_mouse": follow_mouse,
                "show_region": show_region,
                "region_border": region_border,
                "select_region": select_region,
            }
        )
    )


def xa() -> FFMpegDemuxerOption:
    """
    Maxis XA


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def xbin() -> FFMpegDemuxerOption:
    """
    eXtended BINary text (XBIN)


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def xbm_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped xbm sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def xmd() -> FFMpegDemuxerOption:
    """
    Konami XMD


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def xmv() -> FFMpegDemuxerOption:
    """
    Microsoft XMV


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def xpm_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped xpm sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def xvag() -> FFMpegDemuxerOption:
    """
    Sony PS3 XVAG


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def xwd_pipe(
    frame_size: int | None = None,
    framerate: str | None = None,
    pixel_format: str | None = None,
    video_size: str | None = None,
    loop: bool | None = None,
) -> FFMpegDemuxerOption:
    """
    piped xwd sequence

    Args:
        frame_size: force frame size in bytes (from 0 to INT_MAX) (default 0)
        framerate: set the video framerate (default "25")
        pixel_format: set video pixel format
        video_size: set video size
        loop: force loop over input file sequence (default false)

    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(
        kwargs=merge(
            {
                "frame_size": frame_size,
                "framerate": framerate,
                "pixel_format": pixel_format,
                "video_size": video_size,
                "loop": loop,
            }
        )
    )


def xwma() -> FFMpegDemuxerOption:
    """
    Microsoft xWMA


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def yop() -> FFMpegDemuxerOption:
    """
    Psygnosis YOP


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))


def yuv4mpegpipe() -> FFMpegDemuxerOption:
    """
    YUV4MPEG pipe


    Returns:
        the set codec options
    """
    return FFMpegDemuxerOption(kwargs=merge({}))
