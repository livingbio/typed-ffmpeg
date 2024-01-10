from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..input_node import InputNode


def test_input_node(snapshot: SnapshotAssertion) -> None:
    assert (
        snapshot(extension_class=JSONSnapshotExtension)
        == InputNode(filename="test.mp4", kwargs={"f": "mp4"}).get_args()
    )
