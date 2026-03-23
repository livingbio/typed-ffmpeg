"""
Conftest for shared tests across typed-ffmpeg v5-v8.

Configures syrupy to use version-specific snapshot directories when
TYPED_FFMPEG_VERSION is set (e.g. v5, v6, v7, v8).
"""

import os

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Set syrupy snapshot dirname to version-specific path."""
    version = os.environ.get("TYPED_FFMPEG_VERSION", "v8")
    config.option.snapshot_dirname = f"__snapshots__/{version}"
