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
            )
        )

    return options


@app.command()
def generate(outpath: pathlib.Path = pathlib.Path("./tmp")) -> None:
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

        output.append(
            FFmpegFilter(
                id=f.id,
                filter_type=f.type,
                name=f.name,
                description=doc.description,
                ref=doc.url,
                is_input_dynamic=f.is_dynamic_inputs,
                is_output_dynamic=f.is_dynamic_outputs,
                options=parse_options(f, doc),
            )
        )

    render(output, outpath)


if __name__ == "__main__":
    app()
