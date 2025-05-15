"""
Compiles FFmpeg filter graphs into command-line arguments.

This module provides functionality to convert the internal DAG (Directed Acyclic Graph)
representation of an FFmpeg filter chain into the actual command-line arguments
that would be passed to FFmpeg. It handles the following components:

1. Global Options: General FFmpeg settings like log level, overwrite flags
2. Input Files: Source media files with their specific options
3. Filter Graphs: Complex filter chains with proper stream labeling
4. Output Files: Destination files with codec and format settings

The module ensures proper ordering of arguments and handles stream mapping,
filter graph syntax, and escaping of special characters in FFmpeg commands.
"""

from __future__ import annotations

from ..dag.nodes import FilterableStream, FilterNode, GlobalNode, InputNode, OutputNode
from ..dag.schema import Node, Stream
from ..exceptions import FFMpegValueError
from ..schema import Default
from ..utils.escaping import escape
from ..utils.lazy_eval.schema import LazyValue
from ..utils.run import command_line
from .context import DAGContext
from .validate import validate


def compile(stream: Stream, auto_fix: bool = True) -> str:
    """
    Compile a stream into a command-line string.

    This function takes a Stream object representing an FFmpeg filter graph
    and converts it into a command-line string that can be passed to FFmpeg.

    Args:
        stream: The Stream object to compile into a command-line string
        auto_fix: Whether to automatically fix issues in the stream

    Returns:
        A command-line string that can be passed to FFmpeg
    """
    return command_line(compile_as_list(stream, auto_fix))


def compile_as_list(stream: Stream, auto_fix: bool = True) -> list[str]:
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
    formed. If auto_fix is enabled, it will attempt to fix common issues like
    disconnected nodes or invalid stream mappings.

    Args:
        stream: The Stream object to compile into arguments
        auto_fix: Whether to automatically fix issues in the stream
                 (e.g., reconnecting disconnected nodes)

    Returns:
        A list of strings representing FFmpeg command-line arguments

    Raises:
        FFMpegValueError: If the stream contains invalid configurations that cannot be fixed

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
        commands += get_args(node, context)

    # compile the input nodes
    input_nodes = [node for node in context.all_nodes if isinstance(node, InputNode)]
    for node in input_nodes:
        commands += get_args(node, context)

    # compile the filter nodes
    vf_commands = []
    filter_nodes = [node for node in context.all_nodes if isinstance(node, FilterNode)]

    for node in sorted(filter_nodes, key=lambda node: len(node.upstream_nodes)):
        vf_commands += ["".join(get_args(node, context))]

    if vf_commands:
        commands += ["-filter_complex", ";".join(vf_commands)]

    # compile the output nodes
    output_nodes = [node for node in context.all_nodes if isinstance(node, OutputNode)]
    for node in output_nodes:
        commands += get_args(node, context)

    return commands


def get_stream_label(stream: Stream, context: DAGContext | None = None) -> str:
    """
    Generate the FFmpeg label for this stream in filter graphs.

    This method creates the label string used to identify this stream in
    FFmpeg filter graphs. The format of the label depends on the stream's
    source (input file or filter) and type (video or audio).

    For input streams, labels follow FFmpeg's stream specifier syntax:
    - Video streams: "0:v" (first input, video stream)
    - Audio streams: "0:a" (first input, audio stream)
    - AV streams: "0" (first input, all streams)

    For filter outputs, labels use the filter's label:
    - Single output filters: "filterlabel"
    - Multi-output filters: "filterlabel#index"

    Args:
        stream: The stream to generate a label for
        context: Optional DAG context for resolving node labels.
                If not provided, a new context will be built.

    Returns:
        A string label for this stream in FFmpeg filter syntax

    Raises:
        FFMpegValueError: If the stream has an unknown type or node type
    """
    from ..streams.audio import AudioStream
    from ..streams.av import AVStream
    from ..streams.video import VideoStream

    if not context:
        context = DAGContext.build(stream.node)

    match stream.node:
        case InputNode():
            match stream:
                case AVStream():
                    return f"{get_node_label(stream.node, context)}"
                case VideoStream():
                    if stream.index is not None:
                        return (
                            f"{get_node_label(stream.node, context)}:v:{stream.index}"
                        )
                    return f"{get_node_label(stream.node, context)}:v"
                case AudioStream():
                    if stream.index is not None:
                        return (
                            f"{get_node_label(stream.node, context)}:a:{stream.index}"
                        )
                    return f"{get_node_label(stream.node, context)}:a"
                case _:
                    raise FFMpegValueError(
                        f"Unknown stream type: {stream.__class__.__name__}"
                    )  # pragma: no cover
        case FilterNode():
            if len(stream.node.output_typings) > 1:
                return f"{get_node_label(stream.node, context)}#{stream.index}"
            return f"{get_node_label(stream.node, context)}"
        case _:
            raise FFMpegValueError(
                f"Unknown node type: {stream.node.__class__.__name__}"
            )  # pragma: no cover


def get_args_filter_node(node: FilterNode, context: DAGContext) -> list[str]:
    """
    Generate the FFmpeg filter string for this filter node.

    This method creates the filter string that will be used in the
    filter_complex argument of the FFmpeg command. The format follows
    FFmpeg's syntax where input labels are followed by the filter name
    and parameters, and then output labels.

    The filter string format is:
    [input_label]filter_name=param1=value1:param2=value2[output_label]

    Args:
        node: The FilterNode to generate arguments for
        context: DAG context for resolving stream labels

    Returns:
        A list of strings that, when joined, form the filter string
        for this node in the filter_complex argument

    Example:
        For a scale filter with width=1280 and height=720, this might return:
        ['[0:v]', 'scale=', 'width=1280:height=720', '[s0]']
    """

    incoming_labels = "".join(f"[{get_stream_label(k, context)}]" for k in node.inputs)
    outputs = context.get_outgoing_streams(node)

    outgoing_labels = ""
    for output in sorted(outputs, key=lambda stream: stream.index or 0):
        # NOTE: all outgoing streams must be filterable
        assert isinstance(output, FilterableStream)
        outgoing_labels += f"[{get_stream_label(output, context)}]"

    commands = []
    for key, value in node.kwargs.items():
        assert not isinstance(value, LazyValue), (
            f"LazyValue should have been evaluated: {key}={value}"
        )

        # Note: the -nooption syntax cannot be used for boolean AVOptions, use -option 0/-option 1.
        if isinstance(value, bool):
            value = str(int(value))

        if not isinstance(value, Default):
            commands += [f"{key}={escape(value)}"]

    if commands:
        return (
            [incoming_labels]
            + [f"{node.name}="]
            + [escape(":".join(commands), "\\'[],;")]
            + [outgoing_labels]
        )
    return [incoming_labels] + [f"{node.name}"] + [outgoing_labels]


def get_args_input_node(node: InputNode, context: DAGContext) -> list[str]:
    """
    Generate the FFmpeg command-line arguments for this input file.

    This method creates the command-line arguments needed to specify
    this input file to FFmpeg, including any input-specific options.
    Options are converted to FFmpeg's command-line format, with boolean
    options using -option or -nooption syntax.

    Args:
        node: The InputNode to generate arguments for
        context: DAG context (not used for input nodes)

    Returns:
        A list of strings representing FFmpeg command-line arguments

    Example:
        For an input file "input.mp4" with options like seeking to 10 seconds:
        ['-ss', '10', '-i', 'input.mp4']
    """
    commands = []
    for key, value in node.kwargs.items():
        if isinstance(value, bool):
            if value is True:
                commands += [f"-{key}"]
            elif value is False:
                commands += [f"-no{key}"]
        else:
            commands += [f"-{key}", str(value)]
    commands += ["-i", node.filename]
    return commands


def get_args_output_node(node: OutputNode, context: DAGContext) -> list[str]:
    """
    Generate the FFmpeg command-line arguments for this output file.

    This method creates the command-line arguments needed to specify
    this output file to FFmpeg, including stream mapping and output-specific
    options like codecs and formats. It handles both direct input streams
    and filter output streams appropriately.

    Args:
        node: The OutputNode to generate arguments for
        context: DAG context for resolving stream labels

    Returns:
        A list of strings representing FFmpeg command-line arguments

    Example:
        For an output file "output.mp4" with H.264 video codec:
        ['-map', '[v0]', '-c:v', 'libx264', 'output.mp4']
    """
    # !handle mapping
    commands = []

    if context:
        for input in node.inputs:
            if isinstance(input.node, InputNode):
                commands += ["-map", get_stream_label(input, context)]
            else:
                commands += ["-map", f"[{get_stream_label(input, context)}]"]

    for key, value in node.kwargs.items():
        if isinstance(value, bool):
            if value is True:
                commands += [f"-{key}"]
            elif value is False:
                commands += [f"-no{key}"]
        else:
            commands += [f"-{key}", str(value)]
    commands += [node.filename]
    return commands


def get_args_global_node(node: GlobalNode, context: DAGContext) -> list[str]:
    """
    Generate the FFmpeg command-line arguments for these global options.

    This method creates the command-line arguments needed to specify
    global options to FFmpeg, such as -y for overwrite or -loglevel for
    controlling log output. Boolean options are converted to -option or
    -nooption syntax.

    Args:
        node: The GlobalNode to generate arguments for
        context: DAG context (not used for global options)

    Returns:
        A list of strings representing FFmpeg command-line arguments

    Example:
        For global options like overwrite and quiet logging:
        ['-y', '-loglevel', 'quiet']
    """
    commands = []
    for key, value in node.kwargs.items():
        if isinstance(value, bool):
            if value is True:
                commands += [f"-{key}"]
            elif value is False:
                commands += [f"-no{key}"]
        else:
            commands += [f"-{key}", str(value)]
    return commands


def get_args(node: Node, context: DAGContext | None = None) -> list[str]:
    """
    Get the FFmpeg command-line arguments for a specific node.

    This function dispatches to the appropriate argument generation function
    based on the node type. It handles all node types in the FFmpeg DAG:
    FilterNode, InputNode, OutputNode, and GlobalNode.

    Args:
        node: The node to generate arguments for
        context: Optional DAG context for resolving stream labels.
                If not provided, a new context will be built.

    Returns:
        A list of strings representing FFmpeg command-line arguments

    Raises:
        FFMpegValueError: If the node type is not recognized
    """

    context = context or DAGContext.build(node)

    match node:
        case FilterNode():
            return get_args_filter_node(node, context)
        case InputNode():
            return get_args_input_node(node, context)
        case OutputNode():
            return get_args_output_node(node, context)
        case GlobalNode():
            return get_args_global_node(node, context)
        case _:
            raise FFMpegValueError(f"Unknown node type: {node.__class__.__name__}")


def get_node_label(node: Node, context: DAGContext) -> str:
    """
    Get the string label for a specific node in the filter graph.

    This method returns the label assigned to the node, which is used in FFmpeg
    filter graph notation. The label format depends on the node type:
    - Input nodes: sequential numbers (0, 1, 2...)
    - Filter nodes: 's' prefix followed by a number (s0, s1, s2...)
    - Output nodes: 'out'

    Args:
        node: The node to get the label for
        context: DAG context containing node ID mappings

    Returns:
        The string label for the node

    Raises:
        AssertionError: If the node is not an InputNode or FilterNode
    """

    node_id = context.node_ids[node]
    match node:
        case InputNode():
            return str(node_id)
        case FilterNode():
            return f"s{node_id}"
        case _:
            return "out"
