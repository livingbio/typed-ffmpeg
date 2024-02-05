from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import TypeVar

from ..dag.base import Node, Stream, _DAGContext
from ..dag.nodes import FilterNode, GlobalNode, InputNode, OutputNode

T = TypeVar("T")


def _remove_duplicates(seq: list[T]) -> list[T]:
    seen = set()
    output = []

    for x in seq:
        if x not in seen:
            output.append(x)
            seen.add(x)

    return output


def _collect(node: Node) -> tuple[list[Node], list[Stream]]:
    """Collect all nodes and streams that are upstreamed to the given node"""
    nodes, streams = [node], [*node.incoming_streams]

    for stream in node.incoming_streams:
        _nodes, _streams = _collect(stream.node)
        nodes += _nodes
        streams += _streams

    return nodes, streams


def _calculate_node_max_depth(node: Node, outgoing_streams: dict[Node, list[Stream]]) -> int:
    if not node.incoming_streams:
        return 0

    return max(_calculate_node_max_depth(stream.node, outgoing_streams) for stream in node.incoming_streams) + 1


def _node_max_depth(all_nodes: list[Node], outgoing_streams: dict[Node, list[Stream]]) -> dict[Node, int]:
    return {node: _calculate_node_max_depth(node, outgoing_streams) for node in all_nodes}


def _build_outgoing_streams(nodes: list[Node], streams: list[Stream]) -> dict[Node, list[Stream]]:
    outgoing_streams: dict[Node, list[Stream]] = {}

    for node in nodes:
        outgoing_streams[node] = []

    for stream in streams:
        outgoing_streams[stream.node].append(stream)

    return outgoing_streams


def _build_node_labels(nodes: list[Node], outgoing_streams: dict[Node, list[Stream]]) -> dict[Node, str]:
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
    node: Node

    node_labels: dict[Node, str]
    outgoing_streams: dict[Node, list[Stream]]

    all_nodes: list[Node]
    all_streams: list[Stream]

    @classmethod
    def build(cls, node: Node) -> DAGContext:
        """create a DAG context based on the given node"""
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
        assert isinstance(node, (InputNode, FilterNode)), "Only input and filter nodes have labels"
        return self.node_labels[node]

    def get_outgoing_streams(self, node: Node) -> list[Stream]:
        return self.outgoing_streams[node]


# TODO:
# implement auto split or validate


def _validate_reuse_stream(context: DAGContext) -> DAGContext:
    # NOTE: validate there is no reuse stream (each stream can only be used by one node's input)
    stream_nodes: dict[Stream, list[Node]] = defaultdict(list)

    for node in context.all_nodes:
        for stream in node.incoming_streams:
            stream_nodes[stream].append(node)

    # FFmpeg only allows each filter's output stream to be used by one other filter, except for input nodes.
    # This means that a stream can only be consumed by a single filter node.
    # If a stream is used by multiple filter nodes, it will result in an error during compilation.
    # TODO: Add reference from FFmpeg's documentation.
    reuse_streams = [
        stream for stream, nodes in stream_nodes.items() if len(nodes) > 1 and not isinstance(stream.node, InputNode)
    ]
    assert not reuse_streams, f"Found reuse streams: {reuse_streams}"

    return context


def _validate_not_utilize_split(context: DAGContext) -> DAGContext:
    all_split_node = [
        node for node in context.all_nodes if isinstance(node, FilterNode) and node.name in ("split", "asplit")
    ]

    not_utilize_splits = [
        node
        for node in all_split_node
        if len(context.get_outgoing_streams(node)) < int(dict(node.kwargs).get("outputs", 2))
    ]

    assert not not_utilize_splits, f"Found not utilized split nodes: {not_utilize_splits}"

    # if a split node has only one output, it is reduntant
    reduntant_splits = {node for node in all_split_node if int(dict(node.kwargs).get("outputs", 2) == 1)}

    # if a split node's parent is also a split node, it is reduntant
    reduntant_splits |= {
        node
        for node in all_split_node
        if isinstance(node.inputs[0].node, FilterNode) and node.inputs[0].node.name in ("split", "asplit")
    }

    assert not reduntant_splits, f"Found reduntant split nodes: {reduntant_splits}"

    return context


def validate(context: DAGContext) -> DAGContext:
    # NOTE: we don't want to modify the original node
    validators = [_validate_reuse_stream, _validate_not_utilize_split]

    for validator in validators:
        context = validator(context)

    return context


def compile(node: Node, auto_fix: bool = True) -> list[str]:
    context = DAGContext.build(node)
    context = validate(context)

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

    for node in sorted(filter_nodes, key=lambda node: context.node_labels[node]):
        vf_commands += ["".join(node.get_args(context))]

    if vf_commands:
        commands += ["-filter_complex", ";".join(vf_commands)]

    # compile the output nodes
    output_nodes = [node for node in context.all_nodes if isinstance(node, OutputNode)]
    for node in output_nodes:
        commands += node.get_args(context)

    return commands
