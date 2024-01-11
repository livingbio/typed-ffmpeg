from __future__ import annotations

from typing import Iterable

from ..nodes.base import Node, Stream, _DAGContext
from ..nodes.nodes import FilterNode, GlobalNode, InputNode, OutputNode


def _collect(node: Node) -> tuple[set[Node], set[Stream]]:
    """Collect all nodes and streams that are upstreamed to the given node"""
    nodes, streams = {node}, {*node.incoming_streams}

    for stream in node.incoming_streams:
        _nodes, _streams = _collect(stream.node)
        nodes |= _nodes
        streams |= _streams

    return nodes, streams


class DAGContext(_DAGContext):
    node: Node

    node_labels: dict[Node, str]
    outgoing_streams: dict[Node, list[Stream]]
    all_nodes: set[Node]
    all_streams: set[Stream]

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

        return cls(
            node=node, node_labels=node_labels, outgoing_streams=outgoing_streams, all_nodes=nodes, all_streams=streams
        )

    def get_node_label(self, node: Node) -> str:
        assert isinstance(node, (InputNode, FilterNode)), "Only input and filter nodes have labels"
        return self.node_labels[node]

    def get_outgoing_streams(self, node: Node) -> Iterable[Stream]:
        return self.outgoing_streams[node]


# TODO:
# for FFMpeg
# each filter's output stream can only be used by one other filter
# implement auto split or validate


def compile(node: Node) -> list[str]:
    context = DAGContext.build(node)

    # compile the global nodes
    commands = []
    global_nodes = [node for node in context.all_nodes if isinstance(node, GlobalNode)]
    for node in global_nodes:
        commands += node.get_args(context)

    # compile the input nodes
    input_nodes = [node for node in context.all_nodes if isinstance(node, InputNode)]
    for node in input_nodes:
        commands += node.get_args(context)

    # compile the filter nodes
    vf_commands = []
    filter_nodes = [node for node in context.all_nodes if isinstance(node, FilterNode)]

    for node in filter_nodes:
        vf_commands += ["".join(node.get_args(context))]

    if vf_commands:
        vf_commands.sort()
        commands += ["-filter_complex", ";".join(vf_commands)]

    # compile the output nodes
    output_nodes = [node for node in context.all_nodes if isinstance(node, OutputNode)]
    for node in output_nodes:
        commands += node.get_args(context)

    return commands
