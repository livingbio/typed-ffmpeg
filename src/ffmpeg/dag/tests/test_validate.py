from dataclasses import asdict
from pathlib import Path
from typing import Any, Callable, Protocol

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...base import input
from ...filters import concat
from ..context import DAGContext
from ..schema import Node, Stream
from ..validate import _validate_reused_stream, remove_split


def not_utilize_split() -> Any:
    input1 = input("input1.mp4")

    return pytest.param(input1.split(outputs=2).video(0).output(filename="tmp.mp4"), id="not-utilize-split")


def redundant_split_outputs_1() -> Any:
    input1 = input("input1.mp4")
    graph = input1.split(outputs=1).video(0).output(filename="tmp.mp4")
    return pytest.param(graph, id="reduntant-split-outputs-1")


def reduntant_split_duplicate() -> Any:
    input1 = input("input1.mp4")
    s = input1.split(outputs=2)
    s0 = s.video(0)
    s1 = s.video(1)

    s00 = s0.split(outputs=2).video(0)
    s01 = s0.split(outputs=2).video(1)

    graph = concat(s00, s01, s1, n=3).video(0).output(filename="tmp.mp4")
    return pytest.param(graph, id="reduntant-split-duplicate")


@pytest.mark.parametrize("graph", [reduntant_split_duplicate(), redundant_split_outputs_1(), not_utilize_split()])
def test_rebuild_graph(graph: Stream, drawer: Callable[[str, Node], Path]) -> None:
    drawer("before", graph.node)
    rebuilded = remove_split(graph)
    drawer("after", rebuilded[0].node)


class Validator(Protocol):
    def __call__(self, context: DAGContext = ..., auto_fix: bool = False) -> DAGContext:
        ...


def reuse_stream_same_node() -> Any:
    input1 = input("input1.mp4")
    rev = input1.reverse()
    graph = concat(rev.trim(), rev.trim()).video(0).output(filename="tmp.mp4")

    return pytest.param(graph, _validate_reused_stream, id="reuse-stream")


def reuse_stream_two_node() -> Any:
    input1 = input("input1.mp4")
    rev = input1.reverse()
    rev2 = rev.reverse()

    graph = concat(rev2, rev).video(0)
    return pytest.param(graph, _validate_reused_stream, id="reuse-stream-two-node")


def reuse_multi_stream() -> Any:
    input1 = input("input1.mp4")
    rev = input1.reverse()

    graph = concat(concat(rev, rev).video(0), concat(rev, rev, rev, n=3).video(0)).video(0)
    return pytest.param(graph, _validate_reused_stream, id="reuse-multi-stream")


@pytest.mark.parametrize("graph, validator", [reuse_stream_same_node(), reuse_stream_two_node(), reuse_multi_stream()])
def test_validate(
    graph: Stream,
    validator: Validator,
    snapshot: SnapshotAssertion,
    drawer: Callable[[str, Node], Path],
) -> None:

    drawer("before", graph.node)
    assert snapshot(name="before", extension_class=JSONSnapshotExtension) == asdict(graph)

    context = DAGContext.build(graph)

    with pytest.raises(AssertionError) as e:
        validator(context)

    assert snapshot == e
    new_context = validator(context, auto_fix=True)

    drawer("after", new_context.node)
    assert snapshot(name="after", extension_class=JSONSnapshotExtension) == asdict(new_context.node)
