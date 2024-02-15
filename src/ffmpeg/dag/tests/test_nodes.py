import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...base import input
from ...filters import concat
from ...schema import StreamType
from ..context import DAGContext
from ..nodes import FilterNode, InputNode, OutputNode
from ..schema import Node


@pytest.mark.parametrize(
    "node",
    [
        pytest.param(FilterNode(name="scale", kwargs=(("w", "1920"), ("h", "1080"))), id="filter-node"),
        pytest.param(InputNode(filename="test.mp4", kwargs=(("f", "mp4"),)), id="input-node"),
        pytest.param(OutputNode(filename="test.mp4", kwargs=(("bufsize", "64k"),), inputs=()), id="output-node"),
        pytest.param(
            input("tmp.mp4").output(filename="temp").global_args(y=True, no=False, speed=1).node, id="global-node"
        ),
    ],
)
def test_node_prop(node: Node, snapshot: SnapshotAssertion) -> None:
    assert snapshot(name="f.repr") == node.repr()
    assert snapshot(name="__repr__") == repr(node)
    assert snapshot(name="get_args") == node.get_args()


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


def test_input_selector(snapshot: SnapshotAssertion) -> None:
    node = InputNode(filename="test.mp4", kwargs=(("f", "mp4"),))

    assert snapshot(extension_class=JSONSnapshotExtension) == node.audio.areverse().node.get_args()
    assert snapshot(extension_class=JSONSnapshotExtension) == node.video.reverse().node.get_args()


def test_filterable_stream(snapshot: SnapshotAssertion) -> None:
    input1 = input("tmp1.mp4")
    input2 = input("tmp2.mp4")

    out = concat(input1, input2).video(0).output(filename="output.mp4")

    assert snapshot == input2.label(DAGContext.build(out.node))
    assert snapshot == input2.label()
