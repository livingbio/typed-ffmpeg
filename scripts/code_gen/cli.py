import os
import pathlib

import typer
from parse_c.cli import parse_filters
from parse_c.schema import AVFilter
from parse_docs.cli import split_documents
from parse_docs.schema import FilterDocument
from parse_help.parse import extract
from parse_help.schema import AVFilter as HelpAVFilter

from .gen import render
from .schema import TYPING_MAP, Choice, FFmpegFilter, FFmpegFilterOption

app = typer.Typer()


def parse_help_options(filter: HelpAVFilter) -> list[FFmpegFilterOption]:
    options: list[FFmpegFilterOption] = []

    MAPPING = {
        "boolean": "bool",
        "duration": "str",
        "color": "str",
        "flags": "str",
        "dictionary": "str",
        "pix_fmt": "str",
        "int": "int",
        "int64": "int",
        "double": "float",
        "float": "float",
        "string": "str",
        "video_rate": "str",
        "image_size": "str",
        "rational": "str",
        "sample_fmt": "str",
        "binary": "str",
    }

    names = set()
    for option in filter.options:
        if option.name in names:
            continue
        names.add(option.name)
        options.append(
            FFmpegFilterOption(
                name=option.name,
                alias=option.alias,
                description=option.description,
                typing=MAPPING[option.typing],
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


def parse_options(filter: AVFilter, doc: FilterDocument) -> list[FFmpegFilterOption]:
    options: list[FFmpegFilterOption] = []
    parameter_docs = doc.parameter_descs

    for option in filter.parsed_options:
        desc = parameter_docs.get(option.name)
        options.append(
            FFmpegFilterOption(
                name=option.name,
                alias=option.alias,
                description=desc or option.help,
                typing=TYPING_MAP[option.type],
                required=option.required,
                default=option.default_value,
                choices=option.choices,
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

    if filter.is_support_framesync:
        framesync_options = [
            FFmpegFilterOption(
                name="eof_action",
                description="The action to take when EOF is encountered on the secondary input; it accepts one of the following values",
                typing="str",
                default="repeat",
                choices=[
                    Choice(name="repeat", help="Repeat the last frame.", value="repeat"),
                    Choice(name="endall", help="End both streams.", value="endall"),
                    Choice(name="pass", help="Pass the main input through.", value="pass"),
                ],
            ),
            FFmpegFilterOption(
                name="shortest",
                description="Force the output to terminate when the shortest input terminates.",
                typing="bool",
                default=False,
            ),
            FFmpegFilterOption(
                name="repeatlast",
                description="force the filter to extend the last frame of secondary streams until the end of the primary stream.",
                typing="bool",
                default=True,
            ),
            FFmpegFilterOption(
                name="ts_sync_mode",
                description="How strictly to sync streams based on secondary input timestamps; it accepts one of the following values:",
                typing="str",
                default="default",
                choices=[
                    Choice(
                        name="default",
                        help="Frame from secondary input with the nearest lower or equal timestamp to the primary input frame.",
                        value="default",
                    ),
                    Choice(
                        name="nearest",
                        help="Frame from secondary input with the absolute nearest timestamp to the primary input frame.",
                        value="nearest",
                    ),
                ],
            ),
        ]

        for frame_sync_option in framesync_options:
            if not any(k.name == frame_sync_option.name for k in options):
                options.append(frame_sync_option)

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
    ffmpeg_filter.ref = ref
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
        except Exception as e:
            typer.echo(typer.style("ERROR: ", fg=typer.colors.RED) + f"{f.name} {e}")

        doc = filter_doc_mapping[f.name]
        ffmpeg_filter = update_or_create(
            id=f.id,
            filter_type=f.type,
            name=f.name,
            description=help_info.description if help_info else doc.description,
            ref=doc.url,
            is_input_dynamic=f.is_dynamic_inputs,
            is_output_dynamic=f.is_dynamic_outputs,
            is_support_timeline=f.is_support_timeline,
            is_support_framesync=help_info.is_support_framesync if help_info else f.is_support_framesync,
            input_stream_typings=f.input_filter_pads,
            output_stream_typings=f.output_filter_pads,
            options=parse_help_options(help_info) if help_info else parse_options(f, doc),
        )

        ffmpeg_filter.save()
        output.append(ffmpeg_filter)

    render(output, outpath)
    os.system("pre-commit run -a")


if __name__ == "__main__":
    app()
