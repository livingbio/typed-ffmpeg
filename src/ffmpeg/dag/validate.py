from __future__ import annotations

from dataclasses import replace

from ffmpeg.dag.schema import Stream

from .context import DAGContext
from .nodes import FilterNode


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

    inputs = []
    for input_stream in sorted(current_stream.node.inputs, key=lambda stream: -len(stream.node.upstream_nodes)):
        new_stream, _mapping = remove_split(current_stream=input_stream, mapping=mapping)
        inputs.append(new_stream)
        mapping |= _mapping

    new_node = replace(current_stream.node, inputs=tuple(inputs))
    new_stream = replace(current_stream, node=new_node)

    mapping[current_stream] = new_stream
    return new_stream, mapping


def validate(context: DAGContext) -> DAGContext:
    """
    Validate the given DAG context.

    Args:
        context: The DAG context to validate.

    Returns:
        The validated DAG context.
    """

    # NOTE: we don't want to modify the original node
    # validators: list[] = []

    # for validator in validators:
    #     context = validator(context)

    return context
