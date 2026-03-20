"""
Version discovery for typed-ffmpeg multi-version bindings.

This module exposes which FFmpeg versions have pre-generated typed bindings
available, and which version is the default (used by ``from ffmpeg.filters import ...``).

Example::

    import ffmpeg.versions

    ffmpeg.versions.available()  # ['7']  (depends on what's generated)
    ffmpeg.versions.default  # '7'
"""

from __future__ import annotations

from pathlib import Path

_PACKAGE_DIR = Path(__file__).parent


def available() -> list[str]:
    """
    Return sorted list of FFmpeg major versions with generated bindings.

    Discovers version subpackages by scanning for ``v{N}/`` directories
    that contain an ``__init__.py``.

    Returns:
        Sorted list of version strings (e.g., ['5', '6', '7', '8']).

    """
    versions: list[str] = []
    for child in sorted(_PACKAGE_DIR.iterdir()):
        if (
            child.is_dir()
            and child.name.startswith("v")
            and child.name[1:].isdigit()
            and (child / "__init__.py").exists()
        ):
            versions.append(child.name[1:])  # "v7" → "7"
    return versions


def latest() -> str | None:
    """
    Return the latest (highest) available version, or None if none exist.

    Returns:
        Version string or None.

    """
    versions = available()
    return versions[-1] if versions else None


# The default version used by root-level re-exports (e.g., ffmpeg.filters).
# This is the highest available version, determined at import time.
default: str | None = latest()
