from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...base import input
from ...filters import concat
from ..context import DAGContext


def test_context(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")
    rev = input1.reverse()
    stream = concat(rev.trim(), rev.trim()).video(0).output(filename="tmp.mp4")

    context = DAGContext.build(stream.node)

    assert snapshot(
        name="all_nodes", extension_class=JSONSnapshotExtension
    ) == context.render(context.all_nodes)
    assert snapshot(
        name="all_streams", extension_class=JSONSnapshotExtension
    ) == context.render(context.all_streams)

    assert snapshot(
        name="outgoing_nodes", extension_class=JSONSnapshotExtension
    ) == context.render(context.outgoing_nodes)
    assert snapshot(
        name="outgoing_streams", extension_class=JSONSnapshotExtension
    ) == context.render(context.outgoing_streams)
    assert snapshot(
        name="node_labels", extension_class=JSONSnapshotExtension
    ) == context.render(context.node_labels)

    assert context.get_node_label(input1.node) == "0"
    assert context.get_outgoing_streams(input1.node) == [input1]
    assert context.get_outgoing_nodes(input1) == [(rev.node, 0)]
