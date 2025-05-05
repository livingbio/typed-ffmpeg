"""
Graph validation and transformation for FFmpeg filter chains.

This module provides functionality to validate and fix FFmpeg filter graphs,
particularly handling the case of stream reuse. In FFmpeg, a stream cannot
be used as input to multiple filters without explicit split/asplit filters.
This module detects such cases and automatically inserts the necessary split
filters to ensure the graph is valid for FFmpeg processing.
"""

from __future__ import annotations

from dataclasses import replace

from ..dag.nodes import FilterNode, InputNode
from ..dag.schema import Node, Stream
from ..exceptions import FFMpegValueError
from ..streams.audio import AudioStream
from ..streams.video import VideoStream
from .context import DAGContext


def remove_split(
    current_stream: Stream, mapping: dict[Stream, Stream] = None
) -> tuple[Stream, dict[Stream, Stream]]:
    """
    Remove all split nodes from the graph to prepare for reconstruction.

    This function performs the first step of graph repair by recursively traversing
    the graph and removing all existing split/asplit nodes. This creates a clean
    graph without any stream splitting, which will then be reconstructed with proper
    split nodes where needed.

    The function works recursively, processing each node's inputs and creating a
    new graph structure with the split nodes removed.

    Args:
        current_stream: The starting stream to process
        mapping: Dictionary mapping original streams to their new versions without splits
                (used for recursion, pass None for initial call)

    Returns:
        A tuple containing:
        - The new stream corresponding to the input stream but with splits removed
        - A mapping dictionary relating original streams to their new versions
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
            new_stream, _mapping = remove_split(
                current_stream=current_stream.node.inputs[0], mapping=mapping
            )
            mapping[current_stream] = mapping[current_stream.node.inputs[0]]
            return mapping[current_stream.node.inputs[0]], mapping

    inputs = {}
    for idx, input_stream in sorted(
        enumerate(current_stream.node.inputs),
        key=lambda idx_stream: -len(idx_stream[1].node.upstream_nodes),
    ):
        new_stream, _mapping = remove_split(
            current_stream=input_stream, mapping=mapping
        )
        inputs[idx] = new_stream
        mapping |= _mapping

    new_node = replace(
        current_stream.node,
        inputs=tuple(
            stream for idx, stream in sorted(inputs.items(), key=lambda x: x[0])
        ),
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
    """
    Add split nodes to the graph where streams are reused.

    This function performs the second step of graph repair by traversing the
    graph and adding split/asplit nodes where a stream is used as input to
    multiple downstream nodes. In FFmpeg, each stream can only be used once
    unless explicitly split.

    The function detects cases where a stream has multiple outgoing connections
    and inserts the appropriate split filter (split for video, asplit for audio),
    connecting each output of the split to the corresponding downstream node.

    Args:
        current_stream: The stream to process for potential splitting
        down_node: The downstream node that uses current_stream as input (for recursion)
        down_index: The input index in down_node where current_stream connects (for recursion)
        context: The DAG context containing graph relationship information
        mapping: Dictionary tracking the transformations (used for recursion,
                 pass None for initial call)

    Returns:
        Stream: The new stream (possibly from a split node output) for the specified downstream connection
        dict: A mapping dictionary relating original stream/connections to their new versions

    Raises:
        FFMpegValueError: If an unsupported stream type is encountered
    """

    if not context:
        context = DAGContext.build(current_stream.node)

    if mapping is None:
        mapping = {}

    if (current_stream, down_node, down_index) in mapping:
        return mapping[(current_stream, down_node, down_index)], mapping

    inputs = {}

    for idx, input_stream in sorted(
        enumerate(current_stream.node.inputs),
        key=lambda idx_stream: -len(idx_stream[1].node.upstream_nodes),
    ):
        new_stream, _mapping = add_split(
            current_stream=input_stream,
            down_node=current_stream.node,
            down_index=idx,
            mapping=mapping,
            context=context,
        )
        inputs[idx] = new_stream
        mapping |= _mapping

    new_node = replace(
        current_stream.node,
        inputs=tuple(
            stream for idx, stream in sorted(inputs.items(), key=lambda x: x[0])
        ),
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
        raise FFMpegValueError(f"unsupported stream type: {current_stream}")


def fix_graph(stream: Stream) -> Stream:
    """
    Fix stream reuse issues in the filter graph by properly adding split nodes.

    This function performs a complete graph repair operation by:
    1. First removing all existing split/asplit nodes from the graph
    2. Then adding new split/asplit nodes where needed to handle stream reuse

    This ensures that the graph follows FFmpeg's requirement that each stream
    output can only be used as input to one filter unless explicitly split.

    Args:
        stream: The root stream of the graph to fix (typically an output stream)

    Returns:
        A new stream representing the fixed graph with proper splitting

    Note:
        This function creates a new graph structure rather than modifying the
        existing one, preserving the original graph.
    """

    stream, _ = remove_split(stream)
    stream, _ = add_split(stream)
    return stream


def validate(stream: Stream, auto_fix: bool = True) -> Stream:
    """
    Validate a filter graph and optionally fix stream reuse issues.

    This function validates that the filter graph follows FFmpeg's rules,
    particularly regarding stream reuse. In FFmpeg, a stream cannot be used
    as input to multiple filters without an explicit split/asplit filter.

    When auto_fix is True (the default), this function automatically inserts
    the necessary split filters where needed, ensuring the graph is valid for
    FFmpeg processing.

    Args:
        stream: The stream representing the filter graph to validate
        auto_fix: Whether to automatically fix stream reuse issues by adding
                  appropriate split nodes

    Returns:
        Either the original stream (if no fixing needed/requested) or a new
        stream representing the fixed graph

    Example:
        ```python
        # Create a graph where the same stream is used twice (reused)
        input_stream = ffmpeg.input("input.mp4")
        # Use the same stream for both scaling and blurring (invalid in FFmpeg)
        scaled = input_stream.filter("scale", 1280, 720)
        blurred = input_stream.filter("boxblur", 2)
        # Validate will automatically insert a split filter
        valid_stream = ffmpeg.dag.validate(scaled.output("output.mp4"))
        ```
    """
    if auto_fix:
        stream = fix_graph(stream)

    # NOTE: we don't want to modify the original node
    # validators: list[] = []

    # for validator in validators:
    #     context = validator(context)

    return stream
