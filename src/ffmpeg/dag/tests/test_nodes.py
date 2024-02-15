import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...base import input
from ...filters import concat
from ...schema import StreamType
from ..context import DAGContext
from ..nodes import FilterNode, InputNode, OutputNode


def test_filter_node(snapshot: SnapshotAssertion) -> None:
    f = FilterNode(name="scale", kwargs=(("w", "1920"), ("h", "1080")))
    assert snapshot == f.repr()
    assert snapshot == repr(f)

    assert snapshot(extension_class=JSONSnapshotExtension) == f.get_args()


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


def test_custom_filter(snapshot: SnapshotAssertion) -> None:
    in_file = input("test.mp4")

    assert snapshot == in_file.audio.afilter(name="volume", v=0.5, a=0.3).node.get_args()
    assert snapshot == in_file.video.vfilter(name="rotate", angle=90, xx=30).node.get_args()


def test_input_node(snapshot: SnapshotAssertion) -> None:
    node = InputNode(filename="test.mp4", kwargs=(("f", "mp4"),))
    assert snapshot == node.repr()
    assert snapshot == repr(node)

    assert snapshot(extension_class=JSONSnapshotExtension) == node.get_args()

    assert snapshot(extension_class=JSONSnapshotExtension) == node.audio.areverse().node.get_args()
    assert snapshot(extension_class=JSONSnapshotExtension) == node.video.reverse().node.get_args()


def test_output_node(snapshot: SnapshotAssertion) -> None:
    node = OutputNode(filename="test.mp4", kwargs=(("bufsize", "64k"),), inputs=())
    assert snapshot == node.repr()
    assert snapshot == repr(node)

    assert snapshot(extension_class=JSONSnapshotExtension) == node.get_args()


def test_global_node(snapshot: SnapshotAssertion) -> None:
    node = input("tmp.mp4").output(filename="temp").global_args(y=True, no=False, speed=1).node
    assert snapshot == node.repr()
    assert snapshot == repr(node)

    assert snapshot == node.get_args()


def test_filterable_stream(snapshot: SnapshotAssertion) -> None:
    input1 = input("tmp1.mp4")
    input2 = input("tmp2.mp4")

    out = concat(input1, input2).video(0).output(filename="output.mp4")

    assert snapshot == input2.label(DAGContext.build(out.node))
    assert snapshot == input2.label()
