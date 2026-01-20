from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

import ffmpeg
from ffmpeg.info import CodecFlags, CoderFlags, parse_codec_flags, parse_coder_flags


def test_typed_ffmpeg(snapshot: SnapshotAssertion) -> None:
    assert dir(ffmpeg) == snapshot(extension_class=JSONSnapshotExtension)


def test_parse_codec_flags() -> None:
    flags = "DEVASDTILS"
    result = parse_codec_flags(flags)
    assert result & CodecFlags.decoding
    assert result & CodecFlags.encoding
    assert result & CodecFlags.video
    assert result & CodecFlags.audio
    assert result & CodecFlags.subtitle
    assert result & CodecFlags.data
    assert result & CodecFlags.attachment
    assert result & CodecFlags.intraframe_only
    assert result & CodecFlags.lossy
    assert result & CodecFlags.lossless


def test_parse_coder_flags() -> None:
    flags = "VASFSXBD"
    result = parse_coder_flags(flags)
    assert result & CoderFlags.video
    assert result & CoderFlags.audio
    assert result & CoderFlags.subtitle
    assert result & CoderFlags.frame_level_multithreading
    assert result & CoderFlags.slice_level_multithreading
    assert result & CoderFlags.experimental
    assert result & CoderFlags.draw_horiz_band
    assert result & CoderFlags.direct_rendering_method_1


def test_parse_codec_flags_multiple() -> None:
    result = parse_codec_flags("")
    assert result == CodecFlags(0)


def test_parse_coder_flags_multiple() -> None:
    result = parse_coder_flags("")
    assert result == CoderFlags(0)
