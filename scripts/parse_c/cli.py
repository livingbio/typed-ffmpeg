import pathlib

import typer
from devtools import sprint

from .parse_allfilters_c import parse_all_filter_names
from .parse_c import parse_c
from .parse_ffmpeg_opt_c import parse_ffmpeg_opt_c
from .pre_compile import precompile, source_folder
from .schema import AVFilter, OptionDef

app = typer.Typer()


@app.command()
def pre_compile(folder: pathlib.Path) -> None:
    precompile(folder)


@app.command()
def parse_ffmpeg_options() -> list[OptionDef]:
    ffmpeg_opt_c = source_folder / "fftools/ffmpeg_opt.c"
    return parse_ffmpeg_opt_c(ffmpeg_opt_c.read_text())


@app.command()
def parse_filters() -> list[AVFilter]:
    allfilter_c = source_folder / "libavfilter/allfilters.c"
    root = source_folder
    all_filter_names = set(k[2] for k in parse_all_filter_names(allfilter_c))

    total = 0
    parsed_filters: dict[str, AVFilter] = {}

    for path in root.glob("**/*.[cm]"):
        try:
            filters = parse_c(path)
        except Exception as e:
            sprint(f"ERROR: {path} {e}", sprint.red)
            continue

        if len(filters) == 0:
            sprint(f"Processing {path}... {len(filters)} filters", sprint.cyan)
        else:
            sprint(f"Processing {path}... {len(filters)} filters " + ",".join(k.name for k in filters), sprint.green)
            total += len(filters)

            for f in filters:
                if f.id in parsed_filters:
                    sprint(f"Duplicate filter {f.id}")

                parsed_filters[f.id] = f

    parsed_filter_names = parsed_filters.keys()
    print(f"Total filters: {total} / {len(all_filter_names)}")

    print(f"not exists filters {parsed_filter_names - all_filter_names}")
    print(f"not found filters {all_filter_names - parsed_filter_names}")

    return list(parsed_filters.values())


if __name__ == "__main__":
    app()
