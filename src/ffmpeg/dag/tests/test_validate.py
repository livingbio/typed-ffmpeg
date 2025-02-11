from typing import Any, Protocol

import pytest
from syrupy.assertion import SnapshotAssertion

from ...base import input
from ...filters import amix, concat
from ...utils.snapshot import DAGSnapshotExtenstion
from ..context import DAGContext
from ..schema import Stream
from ..validate import add_split, remove_split


def not_utilize_split() -> Any:
    input1 = input("input1.mp4")

    return pytest.param(
        input1.reverse().split(outputs=2).video(0).output(filename="tmp.mp4"),
        id="not-utilize-split",
    )


def redundant_split_outputs_1() -> Any:
    input1 = input("input1.mp4")
    graph = input1.reverse().split(outputs=1).video(0).output(filename="tmp.mp4")
    return pytest.param(graph, id="reduntant-split-outputs-1")


def reduntant_split_duplicate() -> Any:
    input1 = input("input1.mp4")
    s = input1.reverse().split(outputs=2)
    s0 = s.video(0)
    s1 = s.video(1)

    s00 = s0.split(outputs=2).video(0)
    s01 = s0.split(outputs=2).video(1)

    graph = concat(s00, s01, s1, n=3).video(0).output(filename="tmp.mp4")
    return pytest.param(graph, id="reduntant-split-duplicate")


def reuse_input() -> Any:
    input_stream = input("input.mp4")
    graph = (
        concat(input_stream.video, input_stream.video)
        .video(0)
        .output(filename="tmp.mp4")
    )
    return pytest.param(graph, id="reuse-input")


def reuse_stream() -> Any:
    input_stream = input("input.mp4")
    stream = input_stream.reverse()
    graph = concat(stream, stream).video(0).output(filename="tmp.mp4")
    return pytest.param(graph, id="reuse-stream")


def complex_stream() -> Any:
    input1 = input("input1.mp4")
    input2 = input("input2.mp4")

    v = input1.video.reverse()
    a = input2.audio.areverse()

    f = concat(v, a, v, a, v=1, a=1)
    graph = f.video(0).output(f.audio(0), filename="tmp.mp4")
    return pytest.param(graph, id="complex-stream")


def amix_stream() -> Any:
    input1 = input("input1.mp4")

    graph = amix(
        input1.audio.areverse().areverse(), input1.audio.areverse(), duration="first"
    ).output(filename="tmp.mp4")
    return pytest.param(graph, id="amix-stream")


def amix_stream_2() -> Any:
    input1 = input("input1.mp4")

    graph = amix(
        input1.audio.areverse(), input1.audio.areverse().areverse(), duration="first"
    ).output(filename="tmp.mp4")
    return pytest.param(graph, id="amix-stream-2")


@pytest.mark.parametrize(
    "graph",
    [
        reduntant_split_duplicate(),
        redundant_split_outputs_1(),
        not_utilize_split(),
        reuse_input(),
        reuse_stream(),
        complex_stream(),
        amix_stream(),
        amix_stream_2(),
    ],
)
def test_rebuild_graph(graph: Stream, snapshot: SnapshotAssertion) -> None:
    context = DAGContext.build(graph.node)
    assert snapshot(name="all_nodes") == context.all_nodes
    assert snapshot(name="all_streams") == context.all_streams
    assert snapshot(name="node_labels") == context.node_labels
    assert snapshot(name="outgoing_streams") == context.outgoing_streams
    assert snapshot(name="outgoing_nodes") == context.outgoing_nodes

    assert snapshot(name="before", extension_class=DAGSnapshotExtenstion) == graph.node
    removed_split = remove_split(graph)
    assert (
        snapshot(name="remove-split", extension_class=DAGSnapshotExtenstion)
        == removed_split[0].node
    )

    added_split = add_split(removed_split[0])
    assert (
        snapshot(name="add-split", extension_class=DAGSnapshotExtenstion)
        == added_split[0].node
    )


class Validator(Protocol):
    def __call__(
        self, context: DAGContext = ..., auto_fix: bool = False
    ) -> DAGContext: ...
