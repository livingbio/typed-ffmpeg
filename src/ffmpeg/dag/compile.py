"""
Compiles FFmpeg filter graphs into command-line arguments.

This module provides functionality to convert the internal DAG (Directed Acyclic Graph)
representation of an FFmpeg filter chain into the actual command-line arguments
that would be passed to FFmpeg. It traverses the graph in the correct order,
handling global options, inputs, complex filtergraphs, and outputs.
"""

from __future__ import annotations

from ..compile.context import DAGContext
from .nodes import FilterNode, GlobalNode, InputNode, OutputNode
from .schema import Stream
from .validate import validate


def compile(stream: Stream, auto_fix: bool = True) -> list[str]:
    """
    Compile a stream into a list of FFmpeg command-line arguments.

    This function takes a Stream object representing an FFmpeg filter graph
    and converts it into a list of command-line arguments that can be passed
    to FFmpeg. It processes the graph in the correct order:
    1. Global nodes (general FFmpeg options)
    2. Input nodes (input files and their options)
    3. Filter nodes (combined into a -filter_complex argument)
    4. Output nodes (output files and their options)

    The function validates the graph before compilation to ensure it's properly
    formed. If auto_fix is enabled, it will attempt to fix common issues.

    Args:
        stream: The Stream object to compile into arguments
        auto_fix: Whether to automatically fix issues in the stream
                 (e.g., reconnecting disconnected nodes)

    Returns:
        A list of strings representing FFmpeg command-line arguments

    Example:
        ```python
        # Create a simple video scaling filter graph
        input_stream = ffmpeg.input("input.mp4")
        scaled = input_stream.filter("scale", 1280, 720)
        output_stream = scaled.output("output.mp4")

        # Compile to FFmpeg arguments
        args = ffmpeg.dag.compile(output_stream)
        print(
            args
        )  # ['ffmpeg', '-i', 'input.mp4', '-filter_complex', '...', 'output.mp4']
        ```
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
