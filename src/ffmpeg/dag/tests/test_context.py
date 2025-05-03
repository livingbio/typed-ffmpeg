from syrupy.assertion import SnapshotAssertion

from ...base import input
from ...filters import concat
from ..context import DAGContext


def test_context(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")
    rev = input1.reverse()
    stream = concat(rev.trim(), rev.trim()).video(0).output(filename="tmp.mp4")

    context = DAGContext.build(stream.node)

    assert context.get_outgoing_streams(input1.node) == [input1]
    assert context.get_outgoing_nodes(input1) == [(rev.node, 0)]
