from __future__ import annotations

from typing import Iterable

from ..nodes.base import Node, Stream, _DAGContext
from ..nodes.nodes import FilterNode, InputNode


def _collect(node: Node) -> tuple[set[Node], set[Stream]]:
    """Collect all nodes and streams that are upstreamed to the given node"""
    nodes, streams = set(), set()

    for stream in node.incoming_streams:
        _nodes, _streams = _collect(stream.node)
        nodes |= _nodes
        streams |= _streams

    return nodes, streams


class DAGContext(_DAGContext):
    node: Node

    node_labels: dict[Node, str]
    outgoing_streams: dict[Node, list[Stream]]

    @classmethod
    def build(cls, node: Node) -> DAGContext:
        """create a DAG context based on the given node"""
        nodes, streams = _collect(node)

        input_node_index = 0
        filter_node_index = 0
        node_labels: dict[Node, str] = {}
        outgoing_streams: dict[Node, list[Stream]] = {}

        for node in nodes:
            if isinstance(node, InputNode):
                node_labels[node] = str(input_node_index)
                input_node_index += 1
            elif isinstance(node, FilterNode):
                node_labels[node] = f"s{filter_node_index}"
                filter_node_index += 1

            outgoing_streams[node] = []

        for stream in streams:
            outgoing_streams[stream.node].append(stream)

        return cls(node=node, node_labels=node_labels, outgoing_streams=outgoing_streams)

    def get_node_label(self, node: Node) -> str:
        assert isinstance(node, (InputNode, FilterNode)), "Only input and filter nodes have labels"
        return self.node_labels[node]

    def get_outgoing_streams(self, node: Node) -> Iterable[Stream]:
        return self.outgoing_streams[node]


# TODO:
# for FFMpeg
# each filter's output stream can only be used by one other filter
# implement auto split or validate
