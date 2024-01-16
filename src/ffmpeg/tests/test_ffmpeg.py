from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

import ffmpeg


def test_typed_ffmpeg(snapshot: SnapshotAssertion) -> None:
    assert dir(ffmpeg) == snapshot(extension_class=JSONSnapshotExtension)
