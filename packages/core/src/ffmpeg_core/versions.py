"""
FFmpeg version discovery for typed-ffmpeg.

Provides utilities to discover which FFmpeg version bindings are installed
and which version is the default.

Example::

    >>> import ffmpeg_core.versions as versions
    >>> versions.available()
    ['8']
    >>> versions.default()
    '8'
"""

from __future__ import annotations

import importlib.metadata


# Supported major FFmpeg versions in typed-ffmpeg
SUPPORTED_VERSIONS = ("5", "6", "7", "8")


def available() -> list[str]:
    """
    Return sorted list of installed FFmpeg version bindings.

    Checks for installed ``typed-ffmpeg-vN`` packages via package metadata.

    Returns:
        List of major version strings (e.g., ``['6', '7', '8']``).

    """
    found: list[str] = []
    for ver in SUPPORTED_VERSIONS:
        try:
            importlib.metadata.distribution(f"typed-ffmpeg-v{ver}")
            found.append(ver)
        except importlib.metadata.PackageNotFoundError:
            pass
    return sorted(found)


def default() -> str | None:
    """
    Return the default (latest installed) FFmpeg version.

    Returns:
        The highest installed major version string, or None if no
        version bindings are installed.

    """
    versions = available()
    return versions[-1] if versions else None
