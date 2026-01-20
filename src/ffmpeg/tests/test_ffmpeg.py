from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension
from ffmpeg.info import parse_codec_flags, CodecFlags
from ffmpeg.info import parse_coder_flags, CoderFlags
import ffmpeg


def test_typed_ffmpeg(snapshot: SnapshotAssertion) -> None:
    assert dir(ffmpeg) == snapshot(extension_class=JSONSnapshotExtension)

def parse_codec_flags():
    flags="DEVASDTILS"
    resuult=parse_codec_flags(flags)
    assert result & CodecFlags.decoding
    assert result & CodecFlags.encoding
    assert result & CodecFlags.video
    assert result & CodecFlags.audio

def parse_coder_flags():
    flags="VFSXBD"
    
    resuult=parse_coder_flags(flags)
    assert result & CoderFlags.video
    assert result & CoderFlags.experimental

