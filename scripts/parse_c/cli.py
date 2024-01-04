import pathlib

import typer
from devtools import sprint

from .parse_c import parse_all_filter_names, parse_c
from .pre_compile import precompile, source_folder
from .schema import AVFilter

app = typer.Typer()


@app.command()
def pre_compile(folder: pathlib.Path) -> None:
    precompile(folder)


@app.command()
def parse_filters() -> list[AVFilter]:
    allfilter_c = source_folder / "allfilters.c"
    root = source_folder
    all_filter_names = set(k[2] for k in parse_all_filter_names(allfilter_c))

    total = 0
    parsed_filters: list[AVFilter] = []
    for path in root.glob("*.c"):
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
            parsed_filters.extend(filters)

    parsed_filter_names = {f.id for f in parsed_filters}
    print(f"Total filters: {total} / {len(all_filter_names)}")

    print(f"not exists filters {parsed_filter_names - all_filter_names}")
    print(f"not found filters {all_filter_names - parsed_filter_names}")

    return parsed_filters


if __name__ == "__main__":
    app()
