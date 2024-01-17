import os
import pathlib

import typer
from parse_c.cli import parse_filters
from parse_c.schema import AVFilter
from parse_docs.cli import split_documents
from parse_docs.schema import FilterDocument

from .gen import render
from .schema import TYPING_MAP, Choice, FFmpegFilter, FFmpegFilterOption

app = typer.Typer()


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

        doc = filter_doc_mapping[f.name]
        try:
            ffmpeg_filter = FFmpegFilter.load(f.id)
        except IOError:
            ffmpeg_filter = FFmpegFilter(
                id=f.id,
                filter_type=f.type,
                name=f.name,
                description=doc.description,
                ref=doc.url,
                is_input_dynamic=f.is_dynamic_inputs,
                is_output_dynamic=f.is_dynamic_outputs,
                is_support_timeline=f.is_support_timeline,
                is_support_framesync=f.is_support_framesync,
                input_stream_typings=f.input_filter_pads,
                output_stream_typings=f.output_filter_pads,
                options=parse_options(f, doc),
            )

        ffmpeg_filter.filter_type = f.type
        ffmpeg_filter.name = f.name
        ffmpeg_filter.description = doc.description
        ffmpeg_filter.ref = doc.url
        ffmpeg_filter.is_input_dynamic = f.is_dynamic_inputs
        ffmpeg_filter.is_output_dynamic = f.is_dynamic_outputs
        ffmpeg_filter.is_support_timeline = f.is_support_timeline
        ffmpeg_filter.is_support_framesync = f.is_support_framesync
        ffmpeg_filter.input_stream_typings = f.input_filter_pads
        ffmpeg_filter.output_stream_typings = f.output_filter_pads
        ffmpeg_filter.options = parse_options(f, doc)

        ffmpeg_filter.save()
        output.append(ffmpeg_filter)

    render(output, outpath)
    os.system("pre-commit run -a")


if __name__ == "__main__":
    app()
