import pytest
from syrupy.assertion import SnapshotAssertion

from ...compile.context import DAGContext
from ...compile.validate import add_split, remove_split
from ...dag.schema import Stream
from ...utils.snapshot import DAGSnapshotExtension
from .cases import shared_cases


@pytest.mark.parametrize("graph", shared_cases)
def test_rebuild_graph(graph: Stream, snapshot: SnapshotAssertion) -> None:
    context = DAGContext.build(graph.node)
    assert snapshot(name="all_nodes") == context.all_nodes
    assert snapshot(name="all_streams") == context.all_streams
    assert snapshot(name="outgoing_streams") == context.outgoing_streams
    assert snapshot(name="outgoing_nodes") == context.outgoing_nodes

    assert snapshot(name="before", extension_class=DAGSnapshotExtension) == graph.node
    removed_split = remove_split(graph)
    assert (
        snapshot(name="remove-split", extension_class=DAGSnapshotExtension)
        == removed_split[0].node
    )

    added_split = add_split(removed_split[0])
    assert (
        snapshot(name="add-split", extension_class=DAGSnapshotExtension)
        == added_split[0].node
    )
