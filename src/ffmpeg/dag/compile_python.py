from __future__ import annotations

from ffmpeg.streams.audio import AudioStream
from ffmpeg.streams.video import VideoStream

from ..common.cache import load
from ..common.schema import FFMpegFilter
from .context import DAGContext
from .nodes import FilterNode, InputNode, OutputNode
from .schema import Node, Stream
from .validate import validate


def get_stream_name(stream: Stream, context: DAGContext) -> str:
    match stream.node:
        case InputNode():
            return f"i{context.node_ids[stream.node]}"
        case FilterNode():
            if len(context.outgoing_streams[stream.node]) > 1:
                return f"s{context.node_ids[stream.node]}_{stream.index}"
            else:
                return f"s{context.node_ids[stream.node]}"
        case OutputNode():
            return f"o{context.node_ids[stream.node]}"
        case _:
            raise ValueError(f"Unknown node type: {type(stream.node)}")


def get_node_name(node: Node, context: DAGContext) -> str:
    match node:
        case FilterNode():
            return f"node_{context.node_ids[node]}"
        case _:
            raise ValueError(f"Unknown node type: {type(node)}")


def compile_python(stream: Stream, auto_fix: bool = True) -> str:
    stream = validate(stream, auto_fix=auto_fix)
    node = stream.node
    context = DAGContext.build(node)

    code = []

    input_nodes = sorted(
        (node for node in context.nodes if isinstance(node, InputNode)),
        key=lambda k: context.node_ids[k],
    )

    for node in input_nodes:
        code.append(
            f"{get_stream_name(node, context)} = input('{node.filename}', **{node.kwargs})"
        )

    filter_data = load(list[FFMpegFilter], "filters")
    filter_data_dict = {f.name: f for f in filter_data}
    filter_nodes = sorted(
        (node for node in context.nodes if isinstance(node, FilterNode)),
        key=lambda k: context.node_ids[k],
    )

    for node in filter_nodes:
        filter_def = filter_data_dict[node.name]

        if (
            not filter_def.is_dynamic_input
            and len(filter_def.stream_typings_input) == 1
        ):
            expression = f"{get_stream_name(node.inputs[0], context)}.{node.name}(**{node.kwargs})"
        else:
            expression = f"ffmpeg.filters.{node.name}({','.join(get_stream_name(stream, context) for stream in node.inputs)}, **{node.kwargs})"

        if not filter_def.is_dynamic_output:
            if len(filter_def.stream_typings_output) == 1:
                assign_to = (
                    f"{get_stream_name(context.outgoing_streams[node][0], context)}"
                )
            else:
                assign_to = ", ".join(
                    get_stream_name(stream, context)
                    for stream in context.outgoing_streams[node]
                )
            code.append(f"{assign_to} = {expression}")

        else:
            assign_to = f"{get_node_name(node, context)}"
            code.append(f"{assign_to} = {expression}")
            videos_output = sorted(
                [
                    stream
                    for stream in context.outgoing_streams[node]
                    if isinstance(stream, VideoStream)
                ],
                key=lambda k: k.index,
            )
            audios_output = sorted(
                [
                    stream
                    for stream in context.outgoing_streams[node]
                    if isinstance(stream, AudioStream)
                ],
                key=lambda k: k.index,
            )

            video_assign_tos = ", ".join(
                get_stream_name(stream, context) for stream in videos_output
            )
            audio_assign_tos = ", ".join(
                get_stream_name(stream, context) for stream in audios_output
            )

            video_expression_froms = ", ".join(
                f"{assign_to}.video({index})"
                for index, stream in enumerate(videos_output)
            )
            audio_expression_froms = ", ".join(
                f"{assign_to}.audio({index})"
                for index, stream in enumerate(audios_output)
            )

            if len(videos_output) > 0:
                code.append(f"{video_assign_tos} = {video_expression_froms}")
            if len(audios_output) > 0:
                code.append(f"{audio_assign_tos} = {audio_expression_froms}")

    output_nodes = sorted(
        (node for node in context.nodes if isinstance(node, OutputNode)),
        key=lambda k: context.node_ids[k],
    )

    for node in output_nodes:
        code.append(
            f"output('{node.filename}', {get_stream_name(node.stream, context)})"
        )

    return "\n".join(code)
