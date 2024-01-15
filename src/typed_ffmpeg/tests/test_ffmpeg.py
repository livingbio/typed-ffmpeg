from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

import typed_ffmpeg


def test_typed_ffmpeg(snapshot: SnapshotAssertion) -> None:
    assert dir(typed_ffmpeg) == snapshot(extension_class=JSONSnapshotExtension)
