"""
Utilities for managing version-specific FFmpeg cache data.

This module provides functions to install and save cache data for specific
FFmpeg versions, enabling the code generation pipeline to target different
FFmpeg versions (v5, v6, v7).
"""

import logging
import shutil
from pathlib import Path

SUPPORTED_VERSIONS = ["v5", "v6", "v7"]

# Repository root (two levels up from src/scripts/)
_REPO_ROOT = Path(__file__).parent.parent.parent
VERSIONS_DIR = _REPO_ROOT / "versions"

# The active cache directory used by the package at runtime and build time
_ACTIVE_CACHE_DIR = Path(__file__).parent.parent / "ffmpeg" / "common" / "cache"


def get_version_cache_path(version: str) -> Path:
    """
    Get the cache directory for a specific FFmpeg version.

    Args:
        version: The FFmpeg version identifier (e.g., "v5", "v6", "v7")

    Returns:
        Path to the version-specific cache directory

    Raises:
        ValueError: If the version is not supported

    """
    if version not in SUPPORTED_VERSIONS:
        raise ValueError(
            f"Unsupported version: {version}. Supported versions: {SUPPORTED_VERSIONS}"
        )
    return VERSIONS_DIR / version / "cache"


def install_version_cache(version: str) -> None:
    """
    Copy version-specific cache data into the active cache directory.

    This replaces the contents of ``list/`` and ``FFMpegFilterManuallyDefined/``
    in the active cache with data from the specified version.

    Args:
        version: The FFmpeg version identifier (e.g., "v5", "v6", "v7")

    """
    src = get_version_cache_path(version)
    if not src.exists():
        logging.warning(
            f"Version cache directory does not exist: {src}. "
            f"Run data collection for {version} first."
        )
        return

    # Subdirectories to sync
    subdirs = ["list", "FFMpegFilterManuallyDefined"]

    for subdir in subdirs:
        src_subdir = src / subdir
        dst_subdir = _ACTIVE_CACHE_DIR / subdir

        if not src_subdir.exists():
            logging.warning(f"Source subdirectory does not exist: {src_subdir}")
            continue

        # Skip if source directory is empty (no collected data yet)
        src_files = list(src_subdir.glob("*.json"))
        if not src_files:
            logging.info(
                f"Source subdirectory {src_subdir} has no data. "
                f"Keeping existing active cache for {subdir}."
            )
            continue

        # Clear destination and copy
        if dst_subdir.exists():
            shutil.rmtree(dst_subdir)
        shutil.copytree(src_subdir, dst_subdir)

    logging.info(f"Installed cache data for FFmpeg {version}")


def save_version_cache(version: str) -> None:
    """
    Save the current active cache data back to the version-specific directory.

    This copies the contents of ``list/`` and ``FFMpegFilterManuallyDefined/``
    from the active cache into the version-specific directory.

    Args:
        version: The FFmpeg version identifier (e.g., "v5", "v6", "v7")

    """
    dst = get_version_cache_path(version)
    dst.mkdir(parents=True, exist_ok=True)

    subdirs = ["list", "FFMpegFilterManuallyDefined"]

    for subdir in subdirs:
        src_subdir = _ACTIVE_CACHE_DIR / subdir
        dst_subdir = dst / subdir

        if not src_subdir.exists():
            logging.warning(f"Active cache subdirectory does not exist: {src_subdir}")
            continue

        if dst_subdir.exists():
            shutil.rmtree(dst_subdir)
        shutil.copytree(src_subdir, dst_subdir)

    logging.info(f"Saved cache data for FFmpeg {version}")
