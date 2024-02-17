from __future__ import annotations

from dataclasses import replace

from ..streams.audio import AudioStream
from ..streams.video import VideoStream
from .context import DAGContext
from .nodes import FilterNode, InputNode
from .schema import Node, Stream


def remove_split(current_stream: Stream, mapping: dict[Stream, Stream] = None) -> tuple[Stream, dict[Stream, Stream]]:
    """
    Rebuild the graph with the given mapping.

    Args:
        node: The node to rebuild the graph from.
        mapping: The mapping to rebuild the graph with.

    Returns:
        A tuple of the new node and the new mapping.
    """

    # remove all split nodes
    # add split nodes to the graph
    if mapping is None:
        mapping = {}

    if current_stream in mapping:
        return mapping[current_stream], mapping

    if not current_stream.node.inputs:
        mapping[current_stream] = current_stream
        return current_stream, mapping

    if isinstance(current_stream.node, FilterNode):
        # if the current node is a split node, we need to remove it
        if current_stream.node.name in ("split", "asplit"):
            new_stream, _mapping = remove_split(current_stream=current_stream.node.inputs[0], mapping=mapping)
            mapping[current_stream] = mapping[current_stream.node.inputs[0]]
            return mapping[current_stream.node.inputs[0]], mapping

    inputs = {}
    for idx, input_stream in sorted(
        enumerate(current_stream.node.inputs), key=lambda idx_stream: -len(idx_stream[1].node.upstream_nodes)
    ):
        new_stream, _mapping = remove_split(current_stream=input_stream, mapping=mapping)
        inputs[idx] = new_stream
        mapping |= _mapping

    new_node = replace(
        current_stream.node, inputs=tuple(stream for idx, stream in sorted(inputs.items(), key=lambda x: x[0]))
    )
    new_stream = replace(current_stream, node=new_node)

    mapping[current_stream] = new_stream
    return new_stream, mapping


def add_split(
    current_stream: Stream,
    down_node: Node = None,
    down_index: int = None,
    context: DAGContext = None,
    mapping: dict[tuple[Stream, Node | None, int | None], Stream] = None,
) -> tuple[Stream, dict[tuple[Stream, Node | None, int | None], Stream]]:
    if not context:
        context = DAGContext.build(current_stream.node)

    if mapping is None:
        mapping = {}

    if (current_stream, down_node, down_index) in mapping:
        return mapping[(current_stream, down_node, down_index)], mapping

    inputs = {}

    for idx, input_stream in sorted(
        enumerate(current_stream.node.inputs), key=lambda idx_stream: -len(idx_stream[1].node.upstream_nodes)
    ):
        new_stream, _mapping = add_split(
            current_stream=input_stream, down_node=current_stream.node, down_index=idx, mapping=mapping, context=context
        )
        inputs[idx] = new_stream
        mapping |= _mapping

    new_node = replace(
        current_stream.node, inputs=tuple(stream for idx, stream in sorted(inputs.items(), key=lambda x: x[0]))
    )
    new_stream = replace(current_stream, node=new_node)

    num = len(context.get_outgoing_nodes(current_stream))
    if num < 2:
        mapping[(current_stream, down_node, down_index)] = new_stream
        return new_stream, mapping

    if isinstance(current_stream.node, InputNode):
        for idx, (node, index) in enumerate(context.get_outgoing_nodes(current_stream)):
            # if the current node is InputNode, we don't need to split it
            mapping[(current_stream, node, index)] = new_stream
        return new_stream, mapping

    if isinstance(new_stream, VideoStream):
        split_node = new_stream.split(outputs=num)
        for idx, (node, index) in enumerate(context.get_outgoing_nodes(current_stream)):
            mapping[(current_stream, node, index)] = split_node.video(idx)
        return mapping[(current_stream, down_node, down_index)], mapping
    elif isinstance(new_stream, AudioStream):
        split_node = new_stream.asplit(outputs=num)
        for idx, (node, index) in enumerate(context.get_outgoing_nodes(current_stream)):
            mapping[(current_stream, node, index)] = split_node.audio(idx)
        return mapping[(current_stream, down_node, down_index)], mapping
    else:
        raise ValueError(f"unsupported stream type: {current_stream}")


def fix_graph(stream: Stream) -> Stream:
    stream, _ = remove_split(stream)
    stream, _ = add_split(stream)
    return stream


def validate(stream: Stream, auto_fix: bool = True) -> Stream:
    """
    Validate the given DAG context.

    Args:
        context: The DAG context to validate.

    Returns:
        The validated DAG context.
    """
    if auto_fix:
        stream = fix_graph(stream)

    # NOTE: we don't want to modify the original node
    # validators: list[] = []

    # for validator in validators:
    #     context = validator(context)

    return stream
