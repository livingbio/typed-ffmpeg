import os
import pathlib

import pydantic
import typer
from parse_c.cli import parse_filters
from parse_docs.cli import split_documents
from parse_docs.schema import FilterDocument
from parse_help.parse import extract
from parse_help.schema import AVFilter as HelpAVFilter

from .gen import render
from .schema import FFmpegFilter, FFmpegFilterOption

app = typer.Typer()


def parse_help_options(filter: HelpAVFilter) -> list[FFmpegFilterOption]:
    options: list[FFmpegFilterOption] = []

    for option in filter.options:
        options.append(
            FFmpegFilterOption(
                name=option.name,
                alias=option.alias,
                description=option.description,
                typing=option.typing.capitalize(),
                required=False,
                default=option.default,
                choices=[k.model_dump() for k in option.choices],
            )
        )

    if filter.is_support_timeline:
        options.append(
            FFmpegFilterOption(
                name="enable",
                description="timeline editing",
                typing="str",
                required=False,
                default=None,
            )
        )

    return options


def update_or_create(
    id: str,
    filter_type: str,
    name: str,
    description: str,
    ref: str,
    is_input_dynamic: bool,
    is_output_dynamic: bool,
    is_support_timeline: bool,
    is_support_framesync: bool,
    input_stream_typings: list[tuple[str, str]],
    output_stream_typings: list[tuple[str, str]],
    options: list[FFmpegFilterOption],
) -> FFmpegFilter:
    try:
        ffmpeg_filter = FFmpegFilter.load(id)
    except IOError:
        ffmpeg_filter = FFmpegFilter(
            id=id,
        )

    ffmpeg_filter.filter_type = filter_type
    ffmpeg_filter.name = name
    ffmpeg_filter.description = description
    ffmpeg_filter.ref = pydantic.parse_obj_as(pydantic.HttpUrl, ref)
    ffmpeg_filter.is_input_dynamic = is_input_dynamic
    ffmpeg_filter.is_output_dynamic = is_output_dynamic
    ffmpeg_filter.is_support_timeline = is_support_timeline
    ffmpeg_filter.is_support_framesync = is_support_framesync
    ffmpeg_filter.input_stream_typings = input_stream_typings
    ffmpeg_filter.output_stream_typings = output_stream_typings
    ffmpeg_filter.options = options
    return ffmpeg_filter


@app.command()
def generate(outpath: pathlib.Path = pathlib.Path("./src/ffmpeg")) -> None:
    filters = parse_filters()

    filter_doc_mapping: dict[str, FilterDocument] = {}
    for doc in split_documents():
        for filter_name in doc.filter_names:
            filter_doc_mapping[filter_name] = doc

    filters.sort(key=lambda i: i.name)
    output = []
    for f in filters:
        if f.name not in filter_doc_mapping:
            print(f"WARNING: {f.name} not found in docs")
            continue

        help_info = None
        try:
            help_info = extract(f.name)
        except ValueError:
            typer.echo(typer.style("ERROR: ", fg=typer.colors.RED) + f"Unknown filter {f.name}")
            continue
        except Exception as e:
            typer.echo(typer.style("ERROR: ", fg=typer.colors.RED) + f"{f.name} {e}")
            continue

        # TODO:
        # verify parse_c and parse_help results is consistent

        doc = filter_doc_mapping[f.name]
        ffmpeg_filter = update_or_create(
            id=f.id,
            filter_type=f.type,
            name=f.name,
            description=help_info.description,
            ref=doc.url,
            is_input_dynamic=help_info.is_dynamic_inputs,
            is_output_dynamic=help_info.is_dynamic_outputs,
            is_support_timeline=help_info.is_support_timeline,
            is_support_framesync=help_info.is_support_framesync,
            input_stream_typings=help_info.input_types,
            output_stream_typings=help_info.output_types,
            options=parse_help_options(help_info),
        )

        ffmpeg_filter.save()
        output.append(ffmpeg_filter)

    render(output, outpath)
    os.system("pre-commit run -a")


if __name__ == "__main__":
    app()
