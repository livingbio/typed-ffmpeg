from __future__ import annotations

from dataclasses import replace
from ..streams import AudioStream, VideoStream
from .context import DAGContext
from .nodes import FilterNode

def _validate_reused_stream(context: DAGContext, auto_fix: bool = False) -> DAGContext:
    """
    Validate that no stream is reused by multiple nodes.

    Args:
        context: The DAG context to validate.
        auto_fix: Whether to automatically fix the reuse streams. Defaults to False.

    Returns:
        The validated DAG context.
    """

    # NOTE: validate there is no reuse stream (each filter stream can only be used by one node's input)
    reused_streams = {
        stream
        for stream, nodes in context.outgoing_nodes.items()
        if len(nodes) > 1 and isinstance(stream, (AudioStream, VideoStream))
    }

    if not reused_streams:
        return context

    if not auto_fix:
        assert not reused_streams, f"Found reuse streams: {reused_streams}"
        return context

    current_graph = context.node

    # NOTE: auto fix the reuse streams
    for reused_stream in reused_streams:
        nodes = context.outgoing_nodes[reused_stream]

        if isinstance(reused_stream, VideoStream):
            split_node = reused_stream.split(outputs=len(nodes))
        else:
            split_node = reused_stream.asplit(outputs=len(nodes))

        node_map = {}
        for idx, node in enumerate(nodes):
            node_map[node] = node.replace_one_input(reused_stream, split_node.video(idx))
        
        current_graph = current_graph.replace(node_map)

    return DAGContext.build(current_graph)


def _validate_not_utilize_split(context: DAGContext, auto_fix: bool = False) -> DAGContext:
    """
    Validate that split nodes are utilized.

    Args:
        context: The DAG context to validate.

    Returns:
        The validated DAG context.
    """

    not_utilize_splits = [
        node
        for node in context.all_nodes
        if isinstance(node, FilterNode) and node.name in ("split", "asplit") and len(context.get_outgoing_streams(node)) < int(dict(node.kwargs).get("outputs", 2))
    ]

    if not auto_fix:
        assert not not_utilize_splits, f"Found not utilized split nodes: {not_utilize_splits}"
        return context

    current_node = context.node
    for split_node in not_utilize_splits:
        kwargs = dict(split_node.kwargs)
        kwargs["outputs"] = len(context.get_outgoing_streams(split_node))
        updated_node = replace(split_node, kwargs=tuple(kwargs.items()), output_typings=split_node.output_typings[:kwargs["outputs"]])
        current_node = current_node.replace(split_node, updated_node)

        # NOTE: since we utilize context in loop, need to 
    
    return DAGContext.build(current_node)
    
def _validate_nouse_split(context: DAGContext, auto_fix: bool = False) -> DAGContext:
    # if a split node has only one output, it is reduntant
    nouse_splits = {node for node in context.all_nodes if isinstance(node, FilterNode) and node.name in ("split", "asplit") and int(dict(node.kwargs).get("outputs", 2) == 1)}

    if not auto_fix:
        assert not nouse_splits, f"Found nouse split nodes: {nouse_splits}"
        return context
    
    current_node = context.node

    for split_node in nouse_splits:
        outgoing_stream = context.outgoing_streams[split_node][0]
        outoging_node = context.outgoing_nodes[outgoing_stream][0]

        context.outgoing_nodes[split_node] = context.outgoing_nodes[split_node]
        updated_node = split_node.inputs[0]
        current_node = current_node.replace(split_node, updated_node)

    return DAGContext.build(current_node)

    # # if a split node's parent is also a split node, it is reduntant
    # reduntant_splits |= {
    #     node
    #     for node in all_split_node
    #     if isinstance(node.inputs[0].node, FilterNode) and node.inputs[0].node.name in ("split", "asplit")
    # }

    # # NOTE:
    # # if not all split outstream used, it is reduntant but is valid.

    # assert not reduntant_splits, f"Found reduntant split nodes: {reduntant_splits}"

    # return context


def validate(context: DAGContext) -> DAGContext:
    """
    Validate the given DAG context.

    Args:
        context: The DAG context to validate.

    Returns:
        The validated DAG context.
    """

    # NOTE: we don't want to modify the original node
    validators = [
        _validate_reused_stream,
        #   _validate_not_utilize_split
    ]

    for validator in validators:
        context = validator(context)

    return context
