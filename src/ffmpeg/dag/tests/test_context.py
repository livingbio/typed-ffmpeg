from syrupy.assertion import SnapshotAssertion

from ...base import input
from ...filters import concat
from ..context import DAGContext


def test_context(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")
    rev = input1.reverse()
    context = DAGContext.build(concat(rev.trim(), rev.trim()).video(0).output(filename="tmp.mp4"))

    assert snapshot(name="all_nodes") == context.render(context.all_nodes)
    assert snapshot(name="all_streams") == context.render(context.all_streams)
    assert snapshot(name="outgoing_nodes") == context.render(context.outgoing_nodes)
    assert snapshot(name="outgoing_streams") == context.render(context.outgoing_streams)
    assert snapshot(name="node_labels") == context.render(context.node_labels)
