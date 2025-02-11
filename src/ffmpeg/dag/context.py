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
    Remove duplicates from a list while preserving order.

    Args:
        seq: The list to remove duplicates from.

    Returns:
        The list with duplicates removed.
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
    Collect all nodes and streams that are upstreamed to the given node

    Args:
        node: The node to collect from.

    Returns:
        A tuple of all nodes and streams that are upstreamed to the given node.
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
    A context for a directed acyclic graph (DAG).
    """

    node: Node
    """
    The root node (the destination) of the DAG.
    """

    nodes: tuple[Node, ...]
    """
    All nodes in the graph.
    """

    streams: tuple[Stream, ...]
    """
    All streams in the graph.
    """

    @classmethod
    def build(cls, node: Node) -> DAGContext:
        """
        create a DAG context based on the given node

        Args:
            node: The root node of the DAG.

        Returns:
            A DAG context based on the given node.
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
        All nodes in the graph sorted by the number of upstream nodes.
        """
        return sorted(self.nodes, key=lambda node: len(node.upstream_nodes))

    @cached_property
    def all_streams(self) -> list[Stream]:
        """
        All streams in the graph sorted by the number of upstream nodes and the index of the stream.
        """
        return sorted(
            self.streams,
            key=lambda stream: (len(stream.node.upstream_nodes), stream.index),
        )

    @cached_property
    def outgoing_nodes(self) -> dict[Stream, list[tuple[Node, int]]]:
        """
        A dictionary of outgoing nodes for each stream.
        """
        outgoing_nodes: dict[Stream, list[tuple[Node, int]]] = defaultdict(list)

        for node in self.nodes:
            for idx, stream in enumerate(node.inputs):
                outgoing_nodes[stream].append((node, idx))

        return outgoing_nodes

    @cached_property
    def outgoing_streams(self) -> dict[Node, list[Stream]]:
        """
        A dictionary of outgoing streams for each node.
        """

        outgoing_streams: dict[Node, list[Stream]] = defaultdict(list)

        for stream in self.streams:
            outgoing_streams[stream.node].append(stream)

        return outgoing_streams

    @cached_property
    def node_labels(self) -> dict[Node, str]:
        """
        A dictionary of outgoing streams for each node.
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
        Get all outgoing nodes of the stream.

        Args:
            stream: The stream to get the outgoing nodes of.

        Returns:
            The outgoing nodes of the stream.
        """
        return self.outgoing_nodes[stream]

    @override
    def get_node_label(self, node: Node) -> str:
        """
        Get the label of the node.

        Args:
            node: The node to get the label of.

        Returns:
            The label of the node.
        """

        assert isinstance(node, (InputNode, FilterNode)), (
            "Only input and filter nodes have labels"
        )
        return self.node_labels[node]

    @override
    def get_outgoing_streams(self, node: Node) -> list[Stream]:
        """
        Extract all node's outgoing streams from the given set of streams, Because a node only know its incoming streams.

        Args:
            node: The node to get the outgoing streams of.

        Returns:
            The outgoing streams of the node.
        """
        return self.outgoing_streams[node]

    def render(self, obj: Any) -> Any:
        """
        Render the object to a string.

        Args:
            obj: The object to render.

        Returns:
            The rendered object.
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
