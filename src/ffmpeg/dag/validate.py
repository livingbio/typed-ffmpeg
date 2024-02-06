from __future__ import annotations

from collections import defaultdict

from .context import DAGContext
from .nodes import FilterNode, InputNode
from .schema import Node, Stream


def _validate_reuse_stream(context: DAGContext) -> DAGContext:
    """
    Validate that no stream is reused by multiple nodes.

    Args:
        context: The DAG context to validate.

    Returns:
        The validated DAG context.
    """

    # NOTE: validate there is no reuse stream (each stream can only be used by one node's input)
    stream_nodes: dict[Stream, list[Node]] = defaultdict(list)

    for node in context.all_nodes:
        for stream in node.inputs:
            stream_nodes[stream].append(node)

    # FFmpeg only allows each filter's output stream to be used by one other filter, except for input nodes.
    # This means that a stream can only be consumed by a single filter node.
    # If a stream is used by multiple filter nodes, it will result in an error during compilation.
    # TODO: Add reference from FFmpeg's documentation.
    reuse_streams = [
        stream for stream, nodes in stream_nodes.items() if len(nodes) > 1 and not isinstance(stream.node, InputNode)
    ]
    assert not reuse_streams, f"Found reuse streams: {reuse_streams}"

    return context


def _validate_not_utilize_split(context: DAGContext) -> DAGContext:
    """
    Validate that split nodes are utilized.

    Args:
        context: The DAG context to validate.

    Returns:
        The validated DAG context.
    """

    all_split_node = [
        node for node in context.all_nodes if isinstance(node, FilterNode) and node.name in ("split", "asplit")
    ]

    not_utilize_splits = [
        node
        for node in all_split_node
        if len(context.get_outgoing_streams(node)) < int(dict(node.kwargs).get("outputs", 2))
    ]

    assert not not_utilize_splits, f"Found not utilized split nodes: {not_utilize_splits}"

    # if a split node has only one output, it is reduntant
    reduntant_splits = {node for node in all_split_node if int(dict(node.kwargs).get("outputs", 2) == 1)}

    # if a split node's parent is also a split node, it is reduntant
    reduntant_splits |= {
        node
        for node in all_split_node
        if isinstance(node.inputs[0].node, FilterNode) and node.inputs[0].node.name in ("split", "asplit")
    }

    # NOTE:
    # if not all split outstream used, it is reduntant but is valid.

    assert not reduntant_splits, f"Found reduntant split nodes: {reduntant_splits}"

    return context


def validate(context: DAGContext) -> DAGContext:
    """
    Validate the given DAG context.

    Args:
        context: The DAG context to validate.

    Returns:
        The validated DAG context.
    """

    # NOTE: we don't want to modify the original node
    validators = [_validate_reuse_stream, _validate_not_utilize_split]

    for validator in validators:
        context = validator(context)

    return context
