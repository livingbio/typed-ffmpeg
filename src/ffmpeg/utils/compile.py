from __future__ import annotations

from ..dag.context import DAGContext
from ..dag.nodes import FilterNode, GlobalNode, InputNode, OutputNode
from ..dag.schema import Node

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

    for node in sorted(filter_nodes, key=lambda node: context.node_labels[node]):
        vf_commands += ["".join(node.get_args(context))]

    if vf_commands:
        commands += ["-filter_complex", ";".join(vf_commands)]

    # compile the output nodes
    output_nodes = [node for node in context.all_nodes if isinstance(node, OutputNode)]
    for node in output_nodes:
        commands += node.get_args(context)

    return commands
