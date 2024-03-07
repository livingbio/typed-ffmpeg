import os
from pathlib import Path

import typer

from ..parse_help.cli import all_filters
from .gen import render

app = typer.Typer()


@app.command()
def generate(outpath: Path = Path("./src/ffmpeg")) -> None:
    for f in all_filters():
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

    ffmpeg_options = parse_ffmpeg_options()

    render(output, ffmpeg_options, outpath)
    os.system("pre-commit run -a")


if __name__ == "__main__":
    app()
