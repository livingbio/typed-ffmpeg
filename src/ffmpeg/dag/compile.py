from __future__ import annotations

from .context import DAGContext
from .nodes import FilterNode, GlobalNode, InputNode, OutputNode
from .schema import Stream
from .validate import validate


def compile(stream: Stream, auto_fix: bool = True) -> list[str]:
    """
    Compile the stream into a list of arguments.

    Args:
        stream: The stream to compile.
        auto_fix: Whether to automatically fix the stream.

    Returns:
        The list of arguments.
    """

    stream = validate(stream, auto_fix=auto_fix)
    node = stream.node
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

    for node in sorted(filter_nodes, key=lambda node: len(node.upstream_nodes)):
        vf_commands += ["".join(node.get_args(context))]

    if vf_commands:
        commands += ["-filter_complex", ";".join(vf_commands)]

    # compile the output nodes
    output_nodes = [node for node in context.all_nodes if isinstance(node, OutputNode)]
    for node in output_nodes:
        commands += node.get_args(context)

    return commands
