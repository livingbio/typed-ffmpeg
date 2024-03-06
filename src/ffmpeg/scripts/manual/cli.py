import json
from pathlib import Path

import typer

from ..cache import load, save
from ..parse_help.cli import extract
from .schema import FFMpegFilterManuallyDefined

app = typer.Typer()


@app.command()
def init_config() -> None:
    for filter in extract():
        if filter.is_dynamic_input or filter.is_dynamic_ouptut:
            info = FFMpegFilterManuallyDefined(name=filter.name)
            save(info, filter.name)


@app.command()
def migrate_config() -> None:  # pragma: no cover
    """
    Migrate the old schema to the new schema (it should only used once)
    """

    for file in Path("./scripts/code_gen/schemas").glob("*.json"):
        with open(file) as ifile:
            info = json.load(ifile)

        if not info["formula_input_typings"] and not info["formula_output_typings"]:
            continue

        print(f"migrating {info['name']}")

        info = FFMpegFilterManuallyDefined(
            name=info["name"],
            forumla_typings_input=info["formula_input_typings"],
            formula_typings_output=info["formula_output_typings"],
        )

        save(info, info.name)


@app.command()
def load(name: str) -> FFMpegFilterManuallyDefined:
    return load(FFMpegFilterManuallyDefined, name)
