from typing import Any

from syrupy.assertion import SnapshotAssertion

from ...base import input
from ...compile.compile_cli import get_node_label
from ...compile.context import DAGContext
from ...dag.schema import Node, Stream
from ...filters import concat


def render(context: DAGContext, obj: Any) -> Any:
    """
    Recursively convert graph objects to a human-readable representation.
    This method processes arbitrary objects, with special handling for graph
    elements like nodes and streams. It converts them to a readable string format
    that includes node labels. It recursively handles nested structures like
    lists, tuples, and dictionaries.
    This is primarily used for debugging, logging, and visualization purposes.
    Args:
        obj: The object to render, which may be a Node, Stream, or a container
            with these objects nested inside
    Returns:
        The rendered representation of the object:
        - For nodes: "Node(repr#label)"
        - For streams: "Stream(node_repr#label#index)"
        - For containers: recursively rendered contents
        - For other objects: the original object unchanged
    """

    if isinstance(obj, (list, tuple)):
        return [render(context, o) for o in obj]
    elif isinstance(obj, dict):
        return {render(context, k): render(context, v) for k, v in obj.items()}

    if isinstance(obj, Node):
        return f"Node({obj.repr()}#{get_node_label(obj, context)})"

    if isinstance(obj, Stream):
        return f"Stream({render(context, obj.node)}#{obj.index})"

    return obj


def test_context(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")
    rev = input1.reverse()
    stream = concat(rev.trim(), rev.trim()).video(0).output(filename="tmp.mp4")

    context = DAGContext.build(stream.node)

    assert snapshot(name="all_nodes") == render(context, context.all_nodes)
    assert snapshot(name="all_streams") == render(context, context.all_streams)

    assert snapshot(name="outgoing_nodes") == render(context, context.outgoing_nodes)
    assert snapshot(name="outgoing_streams") == render(
        context, context.outgoing_streams
    )
    assert snapshot(name="node_labels") == render(context, context.node_ids)

    assert context.get_outgoing_streams(input1.node) == [input1]
    assert context.get_outgoing_nodes(input1) == [(rev.node, 0)]
