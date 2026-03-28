from ..conftest import requires_ffmpeg
from ..info import (
    Codec,
    CodecFlags,
    Coder,
    CoderFlags,
    get_codecs,
    get_coders,
    get_decoders,
    get_encoders,
    parse_codec_flags,
    parse_coder_flags,
)


def test_parse_codec_flags_full() -> None:
    flags = parse_codec_flags("DEV.S.....")
    assert CodecFlags.decoding in flags
    assert CodecFlags.encoding in flags
    assert CodecFlags.video in flags
    assert CodecFlags.subtitle in flags


def test_parse_codec_flags_audio() -> None:
    # Position: D E V A S D T I L S
    flags = parse_codec_flags("D..A......")
    assert CodecFlags.decoding in flags
    assert CodecFlags.audio in flags
    assert CodecFlags.encoding not in flags


def test_parse_codec_flags_all_set() -> None:
    flags = parse_codec_flags("DEVASDTILS")
    assert CodecFlags.decoding in flags
    assert CodecFlags.encoding in flags
    assert CodecFlags.video in flags
    assert CodecFlags.audio in flags
    assert CodecFlags.subtitle in flags
    assert CodecFlags.data in flags
    assert CodecFlags.attachment in flags
    assert CodecFlags.intraframe_only in flags
    assert CodecFlags.lossy in flags
    assert CodecFlags.lossless in flags


def test_parse_codec_flags_empty() -> None:
    flags = parse_codec_flags("")
    assert flags == CodecFlags(0)


def test_parse_coder_flags_full() -> None:
    flags = parse_coder_flags("V.....BD")
    assert CoderFlags.video in flags
    assert CoderFlags.draw_horiz_band in flags
    assert CoderFlags.direct_rendering_method_1 in flags


def test_parse_coder_flags_audio() -> None:
    flags = parse_coder_flags(".A......")
    assert CoderFlags.audio in flags
    assert CoderFlags.video not in flags


def test_parse_coder_flags_all_set() -> None:
    flags = parse_coder_flags("VASFSXBD")
    assert CoderFlags.video in flags
    assert CoderFlags.audio in flags
    assert CoderFlags.subtitle in flags
    assert CoderFlags.frame_level_multithreading in flags
    assert CoderFlags.slice_level_multithreading in flags
    assert CoderFlags.experimental in flags
    assert CoderFlags.draw_horiz_band in flags
    assert CoderFlags.direct_rendering_method_1 in flags


def test_parse_coder_flags_empty() -> None:
    flags = parse_coder_flags("")
    assert flags == CoderFlags(0)


def test_get_coders_parses_output() -> None:
    # Coder flags: V A S F S X B D
    sample_output = """\
Encoders:
 ------
 V..... libx264              libx264 H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 (codec h264)
 .A.... aac                  AAC (Advanced Audio Coding) (codec aac)
"""
    coders = get_coders(sample_output)
    assert len(coders) == 2
    assert coders[0].name == "libx264"
    assert CoderFlags.video in coders[0].flags
    assert coders[1].name == "aac"
    assert CoderFlags.audio in coders[1].flags


@requires_ffmpeg
def test_get_codecs() -> None:
    codecs = get_codecs()
    assert len(codecs) > 0
    assert isinstance(codecs[0], Codec)


@requires_ffmpeg
def test_get_decoders() -> None:
    decoders = get_decoders()
    assert len(decoders) > 0
    assert isinstance(decoders[0], Coder)


@requires_ffmpeg
def test_get_encoders() -> None:
    encoders = get_encoders()
    assert len(encoders) > 0
    assert isinstance(encoders[0], Coder)
