from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from .._input import input
from .._output import output


def test_output(snapshot: SnapshotAssertion) -> None:
    assert (
        snapshot(extension_class=JSONSnapshotExtension)
        == output(
            input("input.mp4"),
            filename="output.mp4",
            c="copy",
            shortest=True,
            force_fps=False,
            ar=44100,
        ).compile()
    )
