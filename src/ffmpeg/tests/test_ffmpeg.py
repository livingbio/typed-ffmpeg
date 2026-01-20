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


def test_parse_coder_flags() -> None:
    flags = "VFSXBD"
    result = parse_coder_flags(flags)
    assert result & CoderFlags.video
    assert result & CoderFlags.experimental
