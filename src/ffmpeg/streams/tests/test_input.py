from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from .._input import input


def test_input(snapshot: SnapshotAssertion) -> None:
    assert (
        snapshot(extension_class=JSONSnapshotExtension)
        == input("input.mp4", c="copy", accurate_seek=True, display_vflip=False, ss=5, display_rotation=1.0)
        .output(filename="output.mp4")
        .compile()
    )
