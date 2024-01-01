import pathlib

import typer
from parse_c.cli import parse_filters
from parse_c.schema import AVFilter
from parse_docs.cli import split_documents
from parse_docs.schema import FilterDocument

from .gen import render
from .schema import TYPING_MAP, FFmpegFilter, FFmpegFilterOption

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
                description=desc,
                typing=TYPING_MAP[option.type],
                required=option.required,
                default=option.default_value,
            )
        )

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
        ffmpeg_filter = FFmpegFilter.load(f.id)
        ffmpeg_filter.filter_type = f.type
        ffmpeg_filter.name = f.name
        ffmpeg_filter.description = doc.description
        ffmpeg_filter.ref = doc.url
        ffmpeg_filter.is_input_dynamic = f.is_dynamic_inputs
        ffmpeg_filter.is_output_dynamic = f.is_dynamic_outputs
        ffmpeg_filter.input_stream_typings = f.input_filter_pads
        ffmpeg_filter.output_stream_typings = f.output_filter_pads
        ffmpeg_filter.options = parse_options(f, doc)

        ffmpeg_filter.save()
        output.append(ffmpeg_filter)

    render(output, outpath)


if __name__ == "__main__":
    app()
