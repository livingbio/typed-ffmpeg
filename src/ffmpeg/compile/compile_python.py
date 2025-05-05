from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ffmpeg.streams.audio import AudioStream
from ffmpeg.streams.av import AVStream
from ffmpeg.streams.video import VideoStream

from ..common.cache import load
from ..common.schema import FFMpegFilter
from ..dag.nodes import (
    FilterableStream,
    FilterNode,
    GlobalNode,
    GlobalStream,
    InputNode,
    OutputNode,
    OutputStream,
)
from ..dag.schema import Node, Stream
from .context import DAGContext
from .validate import validate


def filter_stream_typed_index(
    matched_stream: FilterableStream, context: DAGContext
) -> int:
    matched_outgoing_streams = [
        k
        for k in context.get_outgoing_streams(matched_stream.node)
        if isinstance(k, matched_stream.__class__)
    ]
    assert matched_stream in matched_outgoing_streams
    assert all(k.index is not None for k in matched_outgoing_streams)
    matched_outgoing_streams = sorted(
        matched_outgoing_streams, key=lambda s: s.index or 9999
    )

    return matched_outgoing_streams.index(matched_stream)


def get_input_var_name(stream: Stream, context: DAGContext) -> str:
    match stream:
        case AVStream():
            assert stream.index is None
            return get_output_var_name(stream.node, context)
        case VideoStream():
            if isinstance(stream.node, InputNode):
                return f"{get_output_var_name(stream.node, context)}.video"
            elif isinstance(stream.node, FilterNode):
                return f"{get_output_var_name(stream.node, context)}.video({filter_stream_typed_index(stream, context)})"
            else:
                return f"{get_output_var_name(stream.node, context)}[{stream.index}]"
        case AudioStream():
            if isinstance(stream.node, InputNode):
                return f"{get_output_var_name(stream.node, context)}.audio"
            elif isinstance(stream.node, FilterNode):
                return f"{get_output_var_name(stream.node, context)}.audio({filter_stream_typed_index(stream, context)})"
            else:
                return f"{get_output_var_name(stream.node, context)}[{stream.index}]"
        case OutputStream():
            return f"{get_output_var_name(stream.node, context)}"
        case GlobalStream():
            return f"{get_output_var_name(stream.node, context)}"
        case _:
            raise ValueError(f"Unknown node type: {type(stream.node)}")


def get_output_var_name(node: Node, context: DAGContext) -> str:
    match node:
        case InputNode():
            return f"input_{context.node_ids[node]}"
        case FilterNode():
            return f"node_{context.node_ids[node]}"
        case OutputNode():
            return f"output_{context.node_ids[node]}"
        case GlobalNode():
            return f"global_{context.node_ids[node]}"
        case _:
            raise ValueError(f"Unknown node type: {type(node)}")


def compile_kwargs(kwargs: Mapping[str, Any]) -> str:
    return ", ".join(f"{k}={v}" for k, v in kwargs.items())


def compile_fluent(code: list[str]) -> list[str]:
    buffer = [k.split("=", 1)[:2] for k in code]

    # if the var used in the following expr only once, we can remove the assignment and replace the var with the expr, otherwise, we keep it
    processed_index = 0
    while processed_index < len(buffer):
        var, expr = buffer[processed_index]
        var = var.strip()
        expr = expr.strip()

        matched_times = sum(
            _expr.count(var) for _var, _expr in buffer[processed_index + 1 :]
        )
        if matched_times != 1:
            processed_index += 1
            continue

        for i, (_var, _expr) in enumerate(buffer[processed_index + 1 :]):
            if var in _expr:
                buffer[processed_index + 1 + i] = [_var, _expr.replace(var, expr)]

        del buffer[processed_index]

    return [f"{k.strip()} = {v.strip()}" for k, v in buffer]


def compile_python(stream: Stream, auto_fix: bool = True, fluent: bool = True) -> str:
    stream = validate(stream, auto_fix=auto_fix)
    node = stream.node
    context = DAGContext.build(node)

    code = []

    input_nodes = sorted(
        (node for node in context.nodes if isinstance(node, InputNode)),
        key=lambda k: context.node_ids[k],
    )

    for node in input_nodes:
        # NOTE: technically, the expression returns a stream, but since input node can reuse the same stream multiple times, we need to assign the stream to the node
        code.append(
            f"{get_output_var_name(node, context)} = ffmpeg.input('{node.filename}', {compile_kwargs(node.kwargs)})"
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
            expression = f"{get_input_var_name(node.inputs[0], context)}.{node.name}({compile_kwargs(node.kwargs)})"
        else:
            in_streams_names = ", ".join(
                get_input_var_name(stream, context) for stream in node.inputs
            )
            expression = f"ffmpeg.filters.{node.name}({in_streams_names}, {compile_kwargs(node.kwargs)})"

        code.append(f"{get_output_var_name(node, context)} = {expression}")

    output_nodes = sorted(
        (node for node in context.nodes if isinstance(node, OutputNode)),
        key=lambda k: context.node_ids[k],
    )

    for node in output_nodes:
        in_streams_names = ", ".join(
            get_input_var_name(stream, context) for stream in node.inputs
        )

        if len(node.inputs) == 1:
            code.append(
                f"{get_output_var_name(node, context)} = {get_input_var_name(node.inputs[0], context)}.output(filename='{node.filename}', {compile_kwargs(node.kwargs)})"
            )
        else:
            code.append(
                f"{get_output_var_name(node, context)} = ffmpeg.output({in_streams_names}, filename='{node.filename}', {compile_kwargs(node.kwargs)})"
            )

    global_nodes = sorted(
        (node for node in context.nodes if isinstance(node, GlobalNode)),
        key=lambda k: context.node_ids[k],
    )

    for node in global_nodes:
        if len(node.inputs) > 1:
            in_streams_names = ", ".join(
                get_input_var_name(s, context) for s in node.inputs
            )
            code.append(
                f"{get_output_var_name(node, context)} = ffmpeg.merge_outputs({in_streams_names}, {compile_kwargs(node.kwargs)})"
            )
        else:
            code.append(
                f"{get_output_var_name(node, context)} = {get_input_var_name(node.inputs[0], context)}.gloabl_args({compile_kwargs(node.kwargs)})"
            )

    code = [k.replace(", )", ")") for k in code]

    if fluent:
        code = compile_fluent(code)

    return "\n".join(code)
