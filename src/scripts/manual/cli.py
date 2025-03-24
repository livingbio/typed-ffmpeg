import json
from pathlib import Path

import typer

from ..cache import load, save
from ..parse_help.cli import all_filters
from .schema import FFMpegFilterManuallyDefined

app = typer.Typer()


@app.command()
def init_config() -> None:
    """
    Initialize manual configuration files for filters

    This command creates default manual configuration files for all filters that have
    dynamic inputs or outputs. These configuration files can then be manually edited
    to provide custom typing information for complex filters.
    """
    for ffmpeg_filter in all_filters():
        if ffmpeg_filter.is_dynamic_input or ffmpeg_filter.is_dynamic_output:
            try:
                info = load(FFMpegFilterManuallyDefined, ffmpeg_filter.name)
            except OSError:  # pragma: no cover
                info = FFMpegFilterManuallyDefined(name=ffmpeg_filter.name)
                save(info, ffmpeg_filter.name)


@app.command()
def migrate_config() -> None:  # pragma: no cover
    """
    Migrate legacy configuration files to the current schema format

    This command is meant to be run only once when transitioning from an older
    version of the schema format to the current one. It locates legacy JSON schema
    files, extracts relevant information, and saves them in the new format.

    Note: This function is not covered by tests as it's a one-time migration utility.
    """

    for file in Path("./scripts/code_gen/schemas").glob("*.json"):
        with open(file) as ifile:
            info = json.load(ifile)

        if not info["formula_input_typings"] and not info["formula_output_typings"]:
            continue

        print(f"migrating {info['name']}")

        info = FFMpegFilterManuallyDefined(
            name=info["name"],
            formula_typings_input=info["formula_input_typings"],
            formula_typings_output=info["formula_output_typings"],
        )

        save(info, info.name)


@app.command()
def load_config(name: str) -> FFMpegFilterManuallyDefined | None:
    """
    Load manual configuration for a specific filter

    This function attempts to load the manual configuration for a given filter by name.
    If the configuration exists in the cache, it returns the configuration object.
    If no configuration is found, it returns None.

    Args:
        name: The name of the filter to load configuration for

    Returns:
        The filter's manual configuration if found, None otherwise
    """
    try:
        return load(FFMpegFilterManuallyDefined, name)
    except OSError:
        return None
