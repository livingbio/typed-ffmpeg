"""Code generation CLI for typed-ffmpeg."""

import logging
import os
from dataclasses import asdict, replace
from pathlib import Path
from typing import Annotated

import typer
from ffmpeg_core.common.cache import load, save
from ffmpeg_core.common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionChoice,
    FFMpegFilterOptionType,
    FFMpegIOType,
    FFMpegOption,
    FFMpegOptionType,
    StreamType,
)

from .. import manual, parse_c, parse_docs, parse_help
from ..parse_help.schema import FFMpegAVOption as ParseHelpFFMpegAVOption
from .gen import render
from .schema import (
    MIN_FFMPEG_VERSION_MAJOR,
    MIN_FFMPEG_VERSION_MINOR,
    FFMpegAVOption,
    FFMpegCodec,
    FFMpegDecoder,
    FFMpegDemuxer,
    FFMpegEncoder,
    FFMpegFormat,
    FFMpegMuxer,
    FFMpegOptionChoice,
    is_supported_version,
    version_cache_key,
)

app = typer.Typer()


def _convert_av_options(
    options: tuple[ParseHelpFFMpegAVOption, ...] | list[ParseHelpFFMpegAVOption],
) -> tuple[FFMpegAVOption, ...]:
    """
    Convert parse_help AV options to code_gen AV options.

    This is the shared conversion logic used by load_codecs, load_formats,
    and load_av_option_set.

    Returns:
        Tuple of converted FFMpegAVOption instances.

    """
    return tuple(
        FFMpegAVOption(
            section=i.section,
            name=i.name,
            type=str(i.type),
            flags=str(i.flags),
            help=i.help,
            min=i.min,
            max=i.max,
            default=i.default,
            choices=tuple(
                FFMpegOptionChoice(
                    name=choice.name,
                    help=choice.help,
                    flags=choice.flags,
                    value=choice.value,
                )
                for choice in i.choices
            ),
        )
        for i in options
    )


def gen_filter_info(ffmpeg_filter: FFMpegFilter) -> FFMpegFilter:
    """
    Generate filter info.

    Args:
        ffmpeg_filter: The filter

    Returns:
        The filter info

    """
    try:
        filter_doc = parse_docs.cli.extract_docs(ffmpeg_filter.name)
    except ValueError:
        # Filter not found in FFmpeg HTML docs (e.g. hardware-accelerated
        # filters like avgblur_opencl or tonemap_vaapi).  Return the filter
        # without a documentation URL rather than dropping it entirely.
        return ffmpeg_filter

    # NOTE:
    # currently we only use filter_doc's url info
    return replace(ffmpeg_filter, ref=filter_doc.url)


def load_options(
    rebuild: bool,
    ffmpeg_binary: str,
    version_key: str,
) -> list[FFMpegOption]:
    """
    Load options from the output path.

    Args:
        rebuild: Whether to use the cache
        ffmpeg_binary: Path or name of the ffmpeg executable
        version_key: Cache key suffix for this FFmpeg version

    Returns:
        The option info

    """
    cache_id = f"options_{version_key}"
    if not rebuild:
        try:
            return load(list[FFMpegOption], cache_id)
        except Exception as e:
            logging.error(f"Failed to load options from cache: {e}")

    options = [
        FFMpegOption(
            name=i.name,
            type=FFMpegOptionType(i.type),
            flags=i.flags,
            help=i.help,
            argname=i.argname,
            canon=i.canon,
        )
        for i in parse_c.cli.parse_ffmpeg_options(ffmpeg_binary=ffmpeg_binary)
    ]
    save(options, cache_id)
    return options


def load_av_option_set(
    rebuild: bool,
    ffmpeg_binary: str,
    version_key: str,
) -> list[FFMpegAVOption]:
    """
    Load AV options from the output path.

    Args:
        rebuild: Whether to use the cache
        ffmpeg_binary: Path or name of the ffmpeg executable
        version_key: Cache key suffix for this FFmpeg version

    Returns:
        The options

    """
    cache_id = f"av_option_sets_{version_key}"
    if not rebuild:
        try:
            return load(list[FFMpegAVOption], cache_id)
        except Exception as e:
            logging.error(f"Failed to load options from cache: {e}")

    parsed_options = [
        k
        for k in parse_help.parse_help.extract(ffmpeg_binary=ffmpeg_binary)
        if isinstance(k, ParseHelpFFMpegAVOption)
    ]
    output = list(_convert_av_options(parsed_options))

    save(output, cache_id)
    return output


def load_filters(
    rebuild: bool,
    ffmpeg_binary: str,
    version_key: str,
) -> list[FFMpegFilter]:
    """
    Load filters from the output path.

    Args:
        rebuild: Whether to use the cache
        ffmpeg_binary: Path or name of the ffmpeg executable
        version_key: Cache key suffix for this FFmpeg version

    Returns:
        The filters

    """
    cache_id = f"filters_{version_key}"
    if not rebuild:
        try:
            return load(list[FFMpegFilter], cache_id)
        except Exception as e:
            logging.error(f"Failed to load filters from cache: {e}")

    ffmpeg_filters = []
    for f in sorted(
        parse_help.parse_filters.extract(ffmpeg_binary=ffmpeg_binary),
        key=lambda i: i.name,
    ):
        if f.name == "afir":
            continue

        # Convert parse_help filter to main filter schema
        converted_filter = FFMpegFilter(
            name=f.name,
            description=f.help,
            # flags
            is_support_timeline=f.is_timeline,
            is_support_slice_threading=f.is_slice_threading,
            is_support_command=False,
            # NOTE: is_support_framesync can only be determined by filter_info_from_help
            is_support_framesync=f.is_framesync,
            is_filter_sink=f.io_flags.endswith("->|"),
            is_filter_source=f.io_flags.startswith("|->"),
            # IO Typing
            is_dynamic_input="N->" in f.io_flags,
            is_dynamic_output="->N" in f.io_flags,
            # stream_typings's name can only be determined by filter_info_from_help
            stream_typings_input=tuple(
                FFMpegIOType(name=i.name, type=StreamType(i.type))
                for i in f.stream_typings_input
            ),
            stream_typings_output=tuple(
                FFMpegIOType(name=i.name, type=StreamType(i.type))
                for i in f.stream_typings_output
            ),
            options=tuple(
                FFMpegFilterOption(
                    name=option.name,
                    type=FFMpegFilterOptionType(option.type),
                    default=option.default,
                    description=option.help,
                    choices=tuple(
                        FFMpegFilterOptionChoice(
                            name=choice.name,
                            help=choice.help,
                            flags=choice.flags,
                            value=choice.value,
                        )
                        for choice in option.choices
                    ),
                )
                for option in f.options
            ),
        )

        manual_config = manual.cli.load_config(converted_filter.name)
        if manual_config:
            converted_filter = replace(converted_filter, **asdict(manual_config))

        filter_info = gen_filter_info(converted_filter)
        save(filter_info, filter_info.name)
        ffmpeg_filters.append(filter_info)

    save(ffmpeg_filters, cache_id)

    hw = [f.name for f in ffmpeg_filters if "vaapi" in f.name or "opencl" in f.name]
    print(f"[DEBUG] load_filters returning {len(ffmpeg_filters)} filters, {len(hw)} hw: {hw[:5]}")

    return ffmpeg_filters


def load_codecs(
    rebuild: bool,
    ffmpeg_binary: str,
    version_key: str,
) -> list[FFMpegCodec]:
    """
    Load codecs from the output path.

    Args:
        rebuild: Whether to use the cache
        ffmpeg_binary: Path or name of the ffmpeg executable
        version_key: Cache key suffix for this FFmpeg version

    Returns:
        The codecs

    Raises:
        ValueError: If a codec is invalid.

    """
    cache_id = f"codecs_{version_key}"
    if not rebuild:
        try:
            return load(list[FFMpegCodec], cache_id)
        except Exception as e:
            logging.error(f"Failed to load codecs from cache: {e}")

    codecs: list[FFMpegCodec] = []
    for k in parse_help.parse_codecs.extract(ffmpeg_binary=ffmpeg_binary):
        cls: type[FFMpegDecoder] | type[FFMpegEncoder]
        if k.is_encoder:
            cls = FFMpegEncoder
        elif k.is_decoder:
            cls = FFMpegDecoder
        else:
            raise ValueError(f"Invalid codec: {k.name}")

        codecs.append(
            cls(
                name=k.name,
                flags=k.flags,
                description=k.help,
                options=_convert_av_options(k.options),
            )
        )

    save(codecs, cache_id)
    return codecs


def load_formats(
    rebuild: bool,
    ffmpeg_binary: str,
    version_key: str,
) -> list[FFMpegFormat]:
    """
    Load muxers from the output path.

    Args:
        rebuild: Whether to use the cache
        ffmpeg_binary: Path or name of the ffmpeg executable
        version_key: Cache key suffix for this FFmpeg version

    Returns:
        The muxers

    Raises:
        ValueError: If a format is invalid.

    """
    cache_id = f"formats_{version_key}"
    if not rebuild:
        try:
            return load(list[FFMpegFormat], cache_id)
        except Exception as e:
            logging.error(f"Failed to load muxers from cache: {e}")

    formats: list[FFMpegFormat] = []
    for k in parse_help.parse_formats.extract(ffmpeg_binary=ffmpeg_binary):
        cls: type[FFMpegDemuxer] | type[FFMpegMuxer]
        if k.is_muxer:
            cls = FFMpegMuxer
        elif k.is_demuxer:
            cls = FFMpegDemuxer
        else:
            raise ValueError(f"Invalid format: {k.name}")

        formats.append(
            cls(
                name=k.name,
                flags=k.flags,
                description=k.help,
                options=_convert_av_options(k.options),
            )
        )

    save(formats, cache_id)
    return formats


@app.command()
def generate(
    outpath: Path | None = None,
    rebuild: bool = False,
    ffmpeg_binary: Annotated[
        str,
        typer.Option(
            help="Path or name of the ffmpeg executable (used to detect version and parse help).",
        ),
    ] = "ffmpeg",
    version_dir: Annotated[
        bool,
        typer.Option(
            help="Generate into a version subdirectory (e.g., v7/) with absolute imports for shared core.",
        ),
    ] = False,
) -> None:
    """
    Generate filter and option documents.

    Only FFmpeg versions >= 5.0 are supported. Metadata is cached per version.

    Args:
        outpath: The output path
        rebuild: Whether to rebuild the filters and options from scratch, ignoring the cache
        ffmpeg_binary: Path or name of the ffmpeg executable
        version_dir: If True, output to a version subdirectory (e.g., outpath/v7/)

    Raises:
        BadParameter: If FFmpeg version is < 5.0.

    """
    from ..parse_help.utils import get_ffmpeg_version

    version = get_ffmpeg_version(ffmpeg_binary)
    if not outpath:
        repo_root = Path(__file__).resolve().parents[4]
        major = version.split(".")[0]
        outpath = repo_root / "packages" / f"v{major}" / "src" / "ffmpeg"
    if not is_supported_version(version):
        raise typer.BadParameter(
            f"FFmpeg version {version} is not supported; need >= {MIN_FFMPEG_VERSION_MAJOR}.{MIN_FFMPEG_VERSION_MINOR}"
        )
    version_key = version_cache_key(version)
    major_version = version_key.split("_")[0]

    ffmpeg_filters = load_filters(rebuild, ffmpeg_binary, version_key)
    ffmpeg_options = load_options(rebuild, ffmpeg_binary, version_key)
    ffmpeg_codecs = load_codecs(rebuild, ffmpeg_binary, version_key)
    ffmpeg_muxers = load_formats(rebuild, ffmpeg_binary, version_key)
    ffmpeg_av_option_set = load_av_option_set(rebuild, ffmpeg_binary, version_key)

    version_prefix = f"v{major_version}" if version_dir else None
    render_outpath = outpath / version_prefix if version_prefix else outpath

    # Build cross-version metadata for deprecation hints in docstrings
    version_metadata = None
    if version_dir:
        from ffmpeg_core.common.cache import get_cache_path

        from .version_diff import build_version_metadata

        cache_dir = get_cache_path() / "list"
        available = set()
        for cache_file in cache_dir.glob("filters_*.json"):
            # "filters_7_1.json" → "7.1"
            parts = cache_file.stem.replace("filters_", "").split("_")
            if len(parts) == 2:
                available.add(f"{parts[0]}.{parts[1]}")
        if available:
            version_metadata = build_version_metadata(sorted(available))

    render(
        filters=ffmpeg_filters,
        options=ffmpeg_options,
        codecs=ffmpeg_codecs,
        muxers=ffmpeg_muxers,
        av_option_sets=ffmpeg_av_option_set,
        outpath=render_outpath,
        ffmpeg_version=version,
        version_prefix=version_prefix,
        version_metadata=version_metadata,
    )
    # Debug: check if hw filters made it into generated video.py
    _vpy = render_outpath / "streams" / "video.py"
    if _vpy.exists():
        _content = _vpy.read_text()
        _has_hw = "avgblur_opencl" in _content
        _methods = _content.count("    def ")
        print(f"[DEBUG] After render: video.py has {_methods} methods, avgblur_opencl={'YES' if _has_hw else 'NO'}")
    if Path(".pre-commit-config.yaml").exists():
        os.system("prek run -a")
    # Debug: check after prek
    if _vpy.exists():
        _content2 = _vpy.read_text()
        _has_hw2 = "avgblur_opencl" in _content2
        _methods2 = _content2.count("    def ")
        print(f"[DEBUG] After prek: video.py has {_methods2} methods, avgblur_opencl={'YES' if _has_hw2 else 'NO'}")


@app.command()
def reexport(
    outpath: Path | None = None,
    version: Annotated[
        str,
        typer.Argument(
            help="Default version to re-export from (e.g., '8'). Uses latest if omitted.",
        ),
    ] = "",
) -> None:
    """
    Generate explicit re-export modules at the root ffmpeg package level.

    Creates thin modules (e.g., ffmpeg/filters.py) that re-export all public
    symbols from the specified version submodule (e.g., ffmpeg/v8/filters.py).

    Raises:
        Exit: If no version directories exist or specified version not found.

    """
    import ast

    if not outpath:
        outpath = Path(__file__).parent.parent.parent / "ffmpeg"

    if not version:
        # Find latest version dir
        version_dirs = sorted(
            d.name
            for d in outpath.iterdir()
            if d.is_dir() and d.name.startswith("v") and d.name[1:].isdigit()
        )
        if not version_dirs:
            print("No version directories found. Run 'generate --version-dir' first.")
            raise typer.Exit(1)
        version = version_dirs[-1][1:]  # "v8" → "8"

    version_prefix = f"v{version}"
    version_dir = outpath / version_prefix
    if not version_dir.exists():
        print(f"Version directory {version_dir} does not exist.")
        raise typer.Exit(1)

    # Generated template output files that have re-exportable symbols.
    # These root-level files get replaced with thin re-exports from the
    # version submodule.
    # NOTE: dag/io/ and dag/global_runnable/ are excluded because they're
    # imported by hand-written dag/nodes.py, creating circular imports
    # if replaced with re-exports.
    # Only re-export the user-facing "entry point" modules. Other generated
    # files (streams, codecs, formats, options, dag) are tightly coupled via
    # cross-imports and must remain as original generated files at root level
    # to avoid circular import issues.
    reexport_targets = [
        "filters.py",
        "sources.py",
    ]

    for filename in reexport_targets:
        src = version_dir / filename
        if not src.exists():
            continue

        with open(src) as f:
            tree = ast.parse(f.read())

        # Collect all top-level function and class names
        names = []
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef):
                if not node.name.startswith("_"):
                    names.append(node.name)

        if not names:
            continue

        module_name = filename.replace(".py", "").replace("/", ".")
        reexport_path = outpath / filename

        lines = [
            "# NOTE: this file is auto-generated, do not modify",
            f'"""Re-exports from ffmpeg.{version_prefix}.{module_name} (default version)."""',
            "",
            f"from ffmpeg.{version_prefix}.{module_name} import (",
        ]
        for name in sorted(names):
            lines.append(f"    {name} as {name},")
        lines.append(")")
        lines.append("")
        lines.append("__all__ = [")
        for name in sorted(names):
            lines.append(f'    "{name}",')
        lines.append("]")
        lines.append("")

        reexport_path.write_text("\n".join(lines))
        print(
            f"  Generated {reexport_path} ({len(names)} symbols from {version_prefix})"
        )


@app.command()
def diff(
    from_version: Annotated[
        str,
        typer.Argument(help="Source FFmpeg version (e.g., '6.0')"),
    ],
    to_version: Annotated[
        str,
        typer.Argument(help="Target FFmpeg version (e.g., '7.0')"),
    ],
) -> None:
    """
    Show what changed between two FFmpeg versions.

    Compares cached metadata to report filters, codecs, and formats that
    were added or removed between the specified versions.
    """
    from .version_diff import diff_versions

    delta = diff_versions(from_version, to_version)

    print(f"\n  FFmpeg {from_version} → {to_version}\n")

    def _print_section(
        title: str, added: tuple[str, ...], removed: tuple[str, ...]
    ) -> None:
        if not added and not removed:
            print(f"  {title}: no changes")
            return
        print(f"  {title}:")
        for name in added:
            print(f"    + {name}")
        for name in removed:
            print(f"    - {name}")

    _print_section("Filters", delta.filters_added, delta.filters_removed)
    _print_section("Codecs", delta.codecs_added, delta.codecs_removed)
    _print_section("Formats", delta.formats_added, delta.formats_removed)

    total = (
        len(delta.filters_added)
        + len(delta.filters_removed)
        + len(delta.codecs_added)
        + len(delta.codecs_removed)
        + len(delta.formats_added)
        + len(delta.formats_removed)
    )
    print(f"\n  Total changes: {total}")


if __name__ == "__main__":
    app()
