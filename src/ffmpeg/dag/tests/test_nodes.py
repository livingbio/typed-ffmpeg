from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..nodes import InputNode, OutputNode


def test_input_node(snapshot: SnapshotAssertion) -> None:
    assert (
        snapshot(extension_class=JSONSnapshotExtension)
        == InputNode(filename="test.mp4", kwargs=(("f", "mp4"),)).get_args()
    )


def test_output_node(snapshot: SnapshotAssertion) -> None:
    assert (
        snapshot(extension_class=JSONSnapshotExtension)
        == OutputNode(filename="test.mp4", kwargs=(("bufsize", "64k"),), inputs=()).get_args()
    )
