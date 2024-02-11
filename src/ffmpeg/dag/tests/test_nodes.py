import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...base import input
from ...schema import StreamType
from ..nodes import FilterNode, InputNode, OutputNode


def test_filter_node(snapshot: SnapshotAssertion) -> None:
    assert (
        snapshot(extension_class=JSONSnapshotExtension)
        == FilterNode(name="scale", kwargs=(("w", "1920"), ("h", "1080"))).get_args()
    )


def test_filter_node_with_outputs(snapshot: SnapshotAssertion) -> None:
    f = FilterNode(
        name="scale",
        kwargs=(("w", "1920"), ("h", "1080")),
        output_typings=(StreamType.video, StreamType.audio),
    )
    assert f.video(0).index == 0
    assert f.audio(0).index == 1

    f = FilterNode(
        name="scale",
        kwargs=(("w", "1920"), ("h", "1080")),
        output_typings=(StreamType.audio,),
    )

    with pytest.raises(ValueError) as e:
        f.video(0)

    with pytest.raises(ValueError) as e:
        f.audio(1)


def test_filter_node_with_inputs(snapshot: SnapshotAssertion) -> None:
    in_file = input("test.mp4")

    assert snapshot(extension_class=JSONSnapshotExtension) == FilterNode(
        name="scale",
        kwargs=(("w", "1920"), ("h", "1080")),
        inputs=(in_file.video, in_file.audio),
        input_typings=(StreamType.video, StreamType.audio),
    )

    with pytest.raises(ValueError) as e:
        FilterNode(
            name="scale",
            kwargs=(("w", "1920"), ("h", "1080")),
            inputs=(in_file.video,),
            input_typings=(StreamType.audio,),
        )

    assert snapshot == e

    with pytest.raises(ValueError) as e:
        FilterNode(
            name="scale",
            kwargs=(("w", "1920"), ("h", "1080")),
            inputs=(in_file.audio,),
            input_typings=(StreamType.video,),
        )

    assert snapshot == e


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


def test_global_node(snapshot: SnapshotAssertion) -> None:
    assert snapshot == input("tmp.mp4").output(filename="temp").global_args(y=True).node.get_args()
