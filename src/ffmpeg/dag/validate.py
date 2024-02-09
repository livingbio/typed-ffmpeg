from __future__ import annotations

from dataclasses import dataclass, replace

from ffmpeg.dag.schema import Node, Stream
from ffmpeg.streams.filter import FilterStream

from ..streams import AudioStream, VideoStream
from .context import DAGContext
from .nodes import FilterNode


@dataclass(frozen=True, kw_only=True)
class FullStream:
    stream: Stream
    down_node: Node
    down_index: int


def insert_split(
    current_stream: FullStream, context: DAGContext, mapping: dict[FullStream, Stream] = None
) -> tuple[Stream, dict[FullStream, Stream]]:
    if mapping is None:
        mapping = {}

    if current_stream in mapping:
        return mapping[current_stream], mapping

    if isinstance(current_stream.stream, (VideoStream, AudioStream)) and context.get_split_num(current_stream) > 1:
        # NOTE: this stream need convert to split
        if isinstance(current_stream.stream, VideoStream):
            split_node = current_stream.stream.split(outputs=context.get_split_num(current_stream))
            new_streams = [split_node.video(idx) for idx in range(context.get_split_num(current_stream))]
        elif isinstance(current_stream.stream, AudioStream):
            split_node = current_stream.stream.asplit(outputs=context.get_split_num(current_stream))
            new_streams = [split_node.audio(idx) for idx in range(context.get_split_num(current_stream))]
        else:
            raise ValueError(f"Invalid split node: {current_stream}")

        for (down_node, down_idx), new_stream in zip(context.get_outgoing_nodes(current_stream), new_streams):
            mapping[FullStream(stream=current_stream, down_node=down_node, down_index=down_idx)] = new_stream

        return mapping[current_stream], mapping

    inputs = []
    for idx, input_stream in sorted(
        enumerate(current_stream.stream.node.inputs), key=lambda k: -len(k[1].node.upstream_nodes)
    ):
        new_stream, _mapping = insert_split(
            current_stream=FullStream(stream=input_stream, down_node=current_stream.stream.node, down_index=idx),
            context=context,
            mapping=mapping,
        )
        inputs.append(new_stream)
        mapping |= _mapping

    new_node = replace(current_stream.stream.node, inputs=tuple(inputs))
    new_stream = replace(current_stream.stream, node=new_node)

    mapping[current_stream] = new_stream
    return new_stream, mapping


# NOTE:
# ensure all output stream is consumed by a node


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
        stream: nodes
        for stream, nodes in context.outgoing_nodes.items()
        if len(nodes) > 1 and isinstance(stream, (AudioStream, VideoStream))
    }

    if not auto_fix:
        assert not reused_streams, f"Found reuse streams: {reused_streams}"
        return context

    # NOTE: auto fix the reuse streams
    current_node = context.node
    for reused_stream, nodes in reused_streams.items():
        new_streams: list[FilterStream]
        if isinstance(reused_stream, VideoStream):
            split_node = reused_stream.split(outputs=len(nodes))
            new_streams = [split_node.video(idx) for idx in range(len(nodes))]
        else:
            split_node = reused_stream.asplit(outputs=len(nodes))
            new_streams = [split_node.audio(idx) for idx in range(len(nodes))]

        index = 0
        for node in sorted(set(nodes), key=lambda node: -len(node.upstream_nodes)):
            inputs: list[Stream] = []
            for _input in node.inputs:
                if _input == reused_stream:
                    inputs.append(new_streams[index])
                    index += 1
                else:
                    inputs.append(_input)

            new_node = replace(node, inputs=tuple(inputs))
            current_node = current_node.replace(node, new_node)

    # NOTE: do we need to fix the reused streams in the new context?
    return DAGContext.build(current_node)


# def _validate_not_utilize_split(context: DAGContext, auto_fix: bool = False) -> DAGContext:
#     """
#     Validate that split nodes are utilized.

#     Args:
#         context: The DAG context to validate.

#     Returns:
#         The validated DAG context.
#     """

#     all_split_node = [
#         node for node in context.all_nodes if isinstance(node, FilterNode) and node.name in ("split", "asplit")
#     ]

#     not_utilize_splits = [
#         node
#         for node in all_split_node
#         if len(context.get_outgoing_streams(node)) < int(dict(node.kwargs).get("outputs", 2))
#     ]

#     if not auto_fix:
#         assert not not_utilize_splits, f"Found not utilized split nodes: {not_utilize_splits}"
#         return context

#     for node in sorted(not_utilize_splits, key=lambda node: -len(node.upstream_nodes)):
#         # NOTE: auto fix the not utilized split nodes
#         count = len(context.get_outgoing_streams(node))

#         if isinstance(node.inputs[0], VideoStream):
#             new_split_node = node.inputs[0].split(outputs=count)
#         elif isinstance(node.inputs[0], AudioStream):
#             new_split_node = node.inputs[0].asplit(outputs=count)
#         else:
#             raise ValueError(f"Invalid split node: {node}")

#     # # if a split node has only one output, it is reduntant
#     # reduntant_splits = {node for node in all_split_node if int(dict(node.kwargs).get("outputs", 2) == 1)}

#     # # if a split node's parent is also a split node, it is reduntant
#     # reduntant_splits |= {
#     #     node
#     #     for node in all_split_node
#     #     if isinstance(node.inputs[0].node, FilterNode) and node.inputs[0].node.name in ("split", "asplit")
#     # }

#     # # NOTE:
#     # # if not all split outstream used, it is reduntant but is valid.

#     # assert not reduntant_splits, f"Found reduntant split nodes: {reduntant_splits}"

#     # return context


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
