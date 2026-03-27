"""
Cross-version comparison for FFmpeg typed bindings.

Computes deltas between FFmpeg version caches to power:
- Deprecation hints in generated docstrings
- Migration CLI command (``typed-ffmpeg diff v6 v7``)
- Per-version documentation pages
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from ffmpeg_core.common.cache import load
from ffmpeg_core.common.schema import FFMpegFilter

from .schema import FFMpegCodec, FFMpegFormat, version_cache_key

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class VersionDelta:
    """Diff between two FFmpeg versions."""

    from_version: str
    to_version: str
    filters_added: tuple[str, ...] = ()
    filters_removed: tuple[str, ...] = ()
    codecs_added: tuple[str, ...] = ()
    codecs_removed: tuple[str, ...] = ()
    formats_added: tuple[str, ...] = ()
    formats_removed: tuple[str, ...] = ()


@dataclass
class VersionMetadata:
    """Aggregated version info across all available caches."""

    # Maps filter/codec/format name → set of version strings where it exists
    filter_versions: dict[str, set[str]] = field(default_factory=dict)
    codec_versions: dict[str, set[str]] = field(default_factory=dict)
    format_versions: dict[str, set[str]] = field(default_factory=dict)
    available_versions: list[str] = field(default_factory=list)


def _load_names_from_cache(
    cache_prefix: str, version_key: str, cls: type
) -> set[str] | None:
    """
    Load item names from a version-specific cache, or None if unavailable.

    Returns:
        Set of item names, or None if cache is unavailable.

    """
    cache_id = f"{cache_prefix}_{version_key}"
    try:
        items = load(list[cls], cache_id)  # type: ignore[arg-type]
        return {item.name for item in items}
    except Exception:
        return None


def diff_versions(from_version: str, to_version: str) -> VersionDelta:
    """
    Compute the delta between two FFmpeg versions.

    Args:
        from_version: Source version (e.g., "6.0").
        to_version: Target version (e.g., "7.0").

    Returns:
        VersionDelta with added/removed filters, codecs, and formats.

    """
    from_key = version_cache_key(from_version)
    to_key = version_cache_key(to_version)

    def _diff_names(prefix: str, cls: type) -> tuple[tuple[str, ...], tuple[str, ...]]:
        from_names = _load_names_from_cache(prefix, from_key, cls)
        to_names = _load_names_from_cache(prefix, to_key, cls)
        if from_names is None or to_names is None:
            return (), ()
        added = tuple(sorted(to_names - from_names))
        removed = tuple(sorted(from_names - to_names))
        return added, removed

    filters_added, filters_removed = _diff_names("filters", FFMpegFilter)
    codecs_added, codecs_removed = _diff_names("codecs", FFMpegCodec)
    formats_added, formats_removed = _diff_names("formats", FFMpegFormat)

    return VersionDelta(
        from_version=from_version,
        to_version=to_version,
        filters_added=filters_added,
        filters_removed=filters_removed,
        codecs_added=codecs_added,
        codecs_removed=codecs_removed,
        formats_added=formats_added,
        formats_removed=formats_removed,
    )


def build_version_metadata(versions: list[str]) -> VersionMetadata:
    """
    Build aggregated metadata across all available version caches.

    This is used by the template renderer to add deprecation/addition
    annotations to generated docstrings.

    Args:
        versions: List of version strings to analyze (e.g., ["5.0", "6.0", "7.0"]).

    Returns:
        VersionMetadata with per-item version availability maps.

    """
    metadata = VersionMetadata(available_versions=sorted(versions))

    for version in versions:
        vkey = version_cache_key(version)
        major = version.split(".")[0]

        filter_names = _load_names_from_cache("filters", vkey, FFMpegFilter)
        if filter_names:
            for name in filter_names:
                metadata.filter_versions.setdefault(name, set()).add(major)

        codec_names = _load_names_from_cache("codecs", vkey, FFMpegCodec)
        if codec_names:
            for name in codec_names:
                metadata.codec_versions.setdefault(name, set()).add(major)

        format_names = _load_names_from_cache("formats", vkey, FFMpegFormat)
        if format_names:
            for name in format_names:
                metadata.format_versions.setdefault(name, set()).add(major)

    return metadata


def format_version_note(
    item_name: str,
    version_map: dict[str, set[str]],
    all_versions: list[str],
    current_version: str,
) -> str | None:
    """
    Generate a version availability note for a docstring.

    Args:
        item_name: Name of the filter/codec/format.
        version_map: Maps item names to sets of version strings where they exist.
        all_versions: All known version strings (sorted).
        current_version: The version being generated (major only, e.g., "7").

    Returns:
        A note string like "New in FFmpeg 7.0" or "Removed in FFmpeg 8.0",
        or None if no note is needed.

    """
    if item_name not in version_map:
        return None

    present_in = version_map[item_name]
    all_majors = sorted(v.split(".")[0] for v in all_versions)

    if not all_majors:
        return None

    # Item exists in current version
    if current_version in present_in:
        # Check if it's new (not in earlier versions)
        earlier = [v for v in all_majors if int(v) < int(current_version)]
        if earlier and not any(v in present_in for v in earlier):
            return f"New in FFmpeg {current_version}.0."

        # Check if it's removed in a later version
        later = [v for v in all_majors if int(v) > int(current_version)]
        removed_in = [v for v in later if v not in present_in]
        if removed_in:
            return f"Removed in FFmpeg {removed_in[0]}.0."

    # Item doesn't exist in current version
    else:
        # Check if it existed in earlier versions (deprecated)
        earlier = [v for v in all_majors if int(v) < int(current_version)]
        if any(v in present_in for v in earlier):
            return f"No longer available in FFmpeg {current_version}.0."

    return None
