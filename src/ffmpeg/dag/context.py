"""
Context management for FFmpeg filter graph traversal and manipulation.

This module provides the DAGContext class, which represents the context
of a Directed Acyclic Graph (DAG) of FFmpeg filter nodes. It provides methods
for traversing, manipulating, and rendering the graph structure, and is used
during graph validation and command-line compilation.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from typing import Any, TypeVar

from ..utils.typing import override
from .nodes import FilterNode, InputNode
from .schema import Node, Stream

T = TypeVar("T")


def _remove_duplicates(seq: list[T]) -> list[T]:
    """
    Remove duplicates from a list while preserving the original order.

    This helper function processes a list and removes any duplicate elements
    while maintaining the relative ordering of elements. The first occurrence
    of each element is kept, subsequent duplicates are removed.

    Args:
        seq: The list to remove duplicates from

    Returns:
        A new list with duplicates removed, preserving the original order
    """
    seen = set()
    output = []

    for x in seq:
        if x not in seen:
            output.append(x)
            seen.add(x)

    return output


def _collect(node: Node) -> tuple[list[Node], list[Stream]]:
    """
    Recursively collect all nodes and streams in the upstream path of a given node.

    This function traverses the graph starting from the given node and collects
    all nodes and streams that are upstream (input sources) to the node. The
    traversal is performed recursively to ensure all dependencies are captured.

    Args:
        node: The starting node to collect dependencies from

    Returns:
        A tuple containing two lists:
        - A list of all nodes in the upstream path (including the starting node)
        - A list of all streams connecting these nodes
    """
    nodes, streams = [node], [*node.inputs]

    for stream in node.inputs:
        _nodes, _streams = _collect(stream.node)
        nodes += _nodes
        streams += _streams

    return nodes, streams


@dataclass(frozen=True, kw_only=True)
class DAGContext:
    """
    Context class for working with a Directed Acyclic Graph (DAG) of FFmpeg filter nodes.

    This immutable class provides methods and properties for analyzing, traversing,
    and manipulating a filter graph. It maintains information about nodes and streams
    in the graph, their relationships, and provides efficient lookups for graph operations.

    The context is built from a "root" node (typically an output node) and captures all
    upstream dependencies (input nodes, filter nodes, and connecting streams).
    """

    node: Node
    """
    The root node (the destination) of the DAG.

    This is typically an output node where the graph traversal begins.
    All nodes collected in the context are upstream from this node.
    """

    nodes: tuple[Node, ...]
    """
    All nodes in the graph as an immutable tuple.

    This includes the root node and all upstream nodes (inputs, filters)
    that contribute to the filter graph.
    """

    streams: tuple[Stream, ...]
    """
    All streams in the graph as an immutable tuple.

    These streams represent the connections between nodes in the filter graph.
    """

    @classmethod
    def build(cls, node: Node) -> DAGContext:
        """
        Create a DAG context by traversing the graph from the specified root node.

        This factory method builds a complete DAGContext by recursively collecting
        all nodes and streams that are upstream from the specified node. It removes
        duplicates to ensure each node and stream is represented only once in the context.

        Args:
            node: The root node to build the context from (typically an output node)

        Returns:
            A fully initialized DAGContext containing all nodes and streams in the graph
        """
        nodes, streams = _collect(node)

        return cls(
            node=node,
            nodes=tuple(_remove_duplicates(nodes)),
            streams=tuple(_remove_duplicates(streams)),
        )

    @cached_property
    def all_nodes(self) -> list[Node]:
        """
        Get all nodes in the graph sorted by their position in the processing chain.

        This property returns a list of all nodes in the graph, sorted by the number
        of upstream nodes. This ensures that nodes earlier in the processing chain
        (closer to inputs) come before nodes later in the chain (closer to outputs).

        Returns:
            A sorted list of all nodes in the graph
        """
        return sorted(self.nodes, key=lambda node: len(node.upstream_nodes))

    @cached_property
    def all_streams(self) -> list[Stream]:
        """
        Get all streams in the graph sorted by their position in the processing chain.

        This property returns a list of all streams in the graph, sorted first by the
        number of upstream nodes of the source node, and then by the stream index.
        This ensures a consistent and logical ordering of streams based on their
        position in the processing pipeline.

        Returns:
            A sorted list of all streams in the graph
        """
        return sorted(
            self.streams,
            key=lambda stream: (len(stream.node.upstream_nodes), stream.index),
        )

    @cached_property
    def outgoing_nodes(self) -> dict[Stream, list[tuple[Node, int]]]:
        """
        Get a mapping of streams to the nodes they connect to.

        This property builds a dictionary that maps each stream to a list of
        tuples containing (node, input_index) pairs. Each tuple represents a node
        that receives this stream as input, along with the index position where
        the stream connects to that node.

        Returns:
            A dictionary mapping streams to their destination nodes and connection indices
        """
        outgoing_nodes: dict[Stream, list[tuple[Node, int]]] = defaultdict(list)

        for node in self.nodes:
            for idx, stream in enumerate(node.inputs):
                outgoing_nodes[stream].append((node, idx))

        return outgoing_nodes

    @cached_property
    def outgoing_streams(self) -> dict[Node, list[Stream]]:
        """
        Get a mapping of nodes to the streams they output.

        This property builds a dictionary that maps each node to a list of streams
        that originate from it. This is particularly useful for determining all the
        outputs from a specific filter or input node.

        Returns:
            A dictionary mapping nodes to their output streams
        """

        outgoing_streams: dict[Node, list[Stream]] = defaultdict(list)

        for stream in self.streams:
            outgoing_streams[stream.node].append(stream)

        return outgoing_streams

    @cached_property
    def node_labels(self) -> dict[Node, str]:
        """
        Get a mapping of nodes to their string labels used in FFmpeg filter graphs.

        This property assigns a unique label to each node in the graph, following
        the FFmpeg filter graph labeling conventions:
        - Input nodes are labeled with sequential numbers (0, 1, 2...)
        - Filter nodes are labeled with 's' followed by a number (s0, s1, s2...)
        - Output nodes are labeled as 'out'

        These labels are used when generating the filter_complex argument for FFmpeg.

        Returns:
            A dictionary mapping nodes to their string labels
        """

        input_node_index = 0
        filter_node_index = 0
        node_labels: dict[Node, str] = {}

        for node in sorted(self.nodes, key=lambda node: node.max_depth):
            if isinstance(node, InputNode):
                node_labels[node] = str(input_node_index)
                input_node_index += 1
            elif isinstance(node, FilterNode):
                node_labels[node] = f"s{filter_node_index}"
                filter_node_index += 1
            else:
                node_labels[node] = "out"

        return node_labels

    @override
    def get_outgoing_nodes(self, stream: Stream) -> list[tuple[Node, int]]:
        """
        Get all nodes that receive a specific stream as input.

        This method returns a list of (node, index) tuples representing the nodes
        that receive the given stream as input, along with the input index position
        where the stream connects to each node.

        Args:
            stream: The stream to get the destination nodes for

        Returns:
            A list of (node, input_index) tuples for nodes that receive this stream
        """
        return self.outgoing_nodes[stream]

    @override
    def get_node_label(self, node: Node) -> str:
        """
        Get the string label for a specific node in the filter graph.

        This method returns the label assigned to the node, which is used in FFmpeg
        filter graph notation. The label format depends on the node type:
        - Input nodes: sequential numbers (0, 1, 2...)
        - Filter nodes: 's' prefix followed by a number (s0, s1, s2...)

        Args:
            node: The node to get the label for (must be an InputNode or FilterNode)

        Returns:
            The string label for the node

        Raises:
            AssertionError: If the node is not an InputNode or FilterNode
        """

        assert isinstance(node, (InputNode, FilterNode)), (
            "Only input and filter nodes have labels"
        )
        return self.node_labels[node]

    @override
    def get_outgoing_streams(self, node: Node) -> list[Stream]:
        """
        Get all streams that originate from a specific node.

        This method returns all streams where the given node is the source.
        It's particularly useful because nodes natively only track their inputs,
        not their outputs, so this context method provides a way to look up
        a node's outputs.

        Args:
            node: The node to get the output streams for

        Returns:
            A list of streams that originate from this node
        """
        return self.outgoing_streams[node]

    def render(self, obj: Any) -> Any:
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
            return [self.render(o) for o in obj]
        elif isinstance(obj, dict):
            return {self.render(k): self.render(v) for k, v in obj.items()}

        if isinstance(obj, Node):
            return f"Node({obj.repr()}#{self.node_labels[obj]})"

        if isinstance(obj, Stream):
            return f"Stream({self.render(obj.node)}#{obj.index})"

        return obj
