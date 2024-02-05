from __future__ import annotations

from dataclasses import dataclass, replace
from typing import TypeVar, cast

from .nodes import FilterableStream, FilterNode, GlobalNode, InputNode, OutputNode
from .schema import Node, Stream, _DAGContext

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
    nodes, streams = [node], [*node.incoming_streams]

    for stream in node.incoming_streams:
        _nodes, _streams = _collect(stream.node)
        nodes += _nodes
        streams += _streams

    return nodes, streams


def _calculate_node_max_depth(node: Node, outgoing_streams: dict[Node, list[Stream]]) -> int:
    """
    Calculate the maximum depth of a node in the graph.

    Args:
        node: The node to calculate the maximum depth of.
        outgoing_streams: The outgoing streams of the node.

    Returns:
        The maximum depth of the node in the graph.
    """
    if not node.incoming_streams:
        return 0

    return max(_calculate_node_max_depth(stream.node, outgoing_streams) for stream in node.incoming_streams) + 1


def _node_max_depth(all_nodes: list[Node], outgoing_streams: dict[Node, list[Stream]]) -> dict[Node, int]:
    """
    Calculate the maximum depth of each node in the graph.

    Args:
        all_nodes: All nodes in the graph.
        outgoing_streams: The outgoing streams of each node.

    Returns:
        A dictionary of the maximum depth of each node in the graph.
    """

    return {node: _calculate_node_max_depth(node, outgoing_streams) for node in all_nodes}


def _build_outgoing_streams(nodes: list[Node], streams: list[Stream]) -> dict[Node, list[Stream]]:
    """
    Build a dictionary of outgoing streams for each node.

    Args:
        nodes: All nodes in the graph.
        streams: All streams in the graph.

    Returns:
        A dictionary of outgoing streams for each node.
    """

    outgoing_streams: dict[Node, list[Stream]] = {}

    for node in nodes:
        outgoing_streams[node] = []

    for stream in streams:
        outgoing_streams[stream.node].append(stream)

    return outgoing_streams


def _build_node_labels(nodes: list[Node], outgoing_streams: dict[Node, list[Stream]]) -> dict[Node, str]:
    """
    Build a dictionary of labels for each node.

    Args:
        nodes: All nodes in the graph.
        outgoing_streams: The outgoing streams of each node.

    Returns:
        A dictionary of labels for each node.
    """

    node_max_depth = _node_max_depth(nodes, outgoing_streams)
    input_node_index = 0
    filter_node_index = 0
    node_labels: dict[Node, str] = {}

    for node in sorted(nodes, key=lambda node: node_max_depth[node]):
        if isinstance(node, InputNode):
            node_labels[node] = str(input_node_index)
            input_node_index += 1
        elif isinstance(node, FilterNode):
            node_labels[node] = f"s{filter_node_index}"
            filter_node_index += 1
        else:
            node_labels[node] = "out"

    return node_labels


@dataclass(frozen=True, kw_only=True)
class DAGContext(_DAGContext):
    """
    A context for a directed acyclic graph (DAG).
    """

    node: Node
    """
    The root node (the destination) of the DAG.
    """

    node_labels: dict[Node, str]
    """
    A dictionary of labels for each node.
    """

    outgoing_streams: dict[Node, list[Stream]]
    """
    A dictionary of outgoing streams for each node.
    """

    all_nodes: list[Node]
    """
    All nodes in the graph.
    """
    all_streams: list[Stream]
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
        nodes = _remove_duplicates(nodes)
        streams = _remove_duplicates(streams)

        outgoing_streams = _build_outgoing_streams(nodes, streams)
        node_labels = _build_node_labels(nodes, outgoing_streams)

        all_nodes = sorted(nodes, key=lambda node: node_labels[node])
        all_streams = sorted(streams, key=lambda stream: (node_labels[stream.node], stream.index))

        return cls(
            node=node,
            node_labels=node_labels,
            outgoing_streams=outgoing_streams,
            all_nodes=all_nodes,
            all_streams=all_streams,
        )

    def get_node_label(self, node: Node) -> str:
        """
        Get the label of the node.

        Args:
            node: The node to get the label of.

        Returns:
            The label of the node.
        """

        assert isinstance(node, (InputNode, FilterNode)), "Only input and filter nodes have labels"
        return self.node_labels[node]

    def get_outgoing_streams(self, node: Node) -> list[Stream]:
        """
        Extract all node's outgoing streams from the given set of streams, Because a node only know its incoming streams.

        Args:
            node: The node to get the outgoing streams of.

        Returns:
            The outgoing streams of the node.
        """
        return self.outgoing_streams[node]

    def replace_stream(self, old_stream: Stream, new_stream: Stream) -> DAGContext:
        """
        Replace the old stream with the new stream in the DAG context.

        Args:
            old_stream: The old stream to replace.
            new_stream: The new stream to replace with.

        Returns:
            The new DAG context with the old stream replaced with the new stream.
        """
        if old_stream not in self.all_streams:
            return self

        for node in self.all_nodes:
            if isinstance(node, (FilterNode, OutputNode)):
                if old_stream in node.inputs:
                    new_stream = cast(FilterableStream, new_stream)
                    new_inputs = tuple([new_stream if s == old_stream else s for s in node.inputs])
                    new_node = replace(node, inputs=new_inputs)
                    return self.replace_node(node, new_node).replace_stream(old_stream, new_stream)
            elif isinstance(node, GlobalNode):
                if old_stream == node.input:
                    new_node = replace(node, input=new_stream)
                    return self.replace_node(node, new_node).replace_stream(old_stream, new_stream)

        raise ValueError(f"Stream {old_stream} not found in the DAG context")

    def replace_node(self, old_node: Node, new_node: Node) -> DAGContext:
        """
        Replace the old node with the new node in the DAG context.

        Args:
            old_node: The old node to replace.
            new_node: The new node to replace with.

        Returns:
            The new DAG context with the old node replaced with the new node.
        """
        if old_node not in self.all_nodes:
            return self

        if not self.outgoing_streams[old_node]:
            # only destination node has no outgoing streams
            return DAGContext.build(new_node)

        for stream in self.outgoing_streams[old_node]:
            new_stream = replace(stream, node=new_node)
            return self.replace_stream(stream, new_stream).replace_node(old_node, new_node)

        raise ValueError(f"Node {old_node} not found in the DAG context")
