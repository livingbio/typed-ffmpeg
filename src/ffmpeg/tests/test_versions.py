"""Tests for the versions module."""

import tempfile
from pathlib import Path
from unittest.mock import patch

from ffmpeg import versions


def test_available_returns_list() -> None:
    """available() returns a list (may be empty if no version dirs exist)."""
    result = versions.available()
    assert isinstance(result, list)


def test_latest_type() -> None:
    """latest() returns str or None."""
    result = versions.latest()
    assert result is None or isinstance(result, str)


def test_available_with_mock_dirs() -> None:
    """Test version discovery with synthetic version directories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        base = Path(tmpdir)
        # Create version dirs
        for v in ["v5", "v7", "v6"]:
            d = base / v
            d.mkdir()
            (d / "__init__.py").touch()
        # Create a non-version dir (should be ignored)
        (base / "utils").mkdir()
        (base / "utils" / "__init__.py").touch()
        # Create a v-dir without __init__.py (should be ignored)
        (base / "v9").mkdir()

        with patch.object(versions, "_PACKAGE_DIR", base):
            result = versions.available()
            assert result == ["5", "6", "7"]

            latest = versions.latest()
            assert latest == "7"


def test_available_empty() -> None:
    """When no version dirs exist, returns empty list."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with patch.object(versions, "_PACKAGE_DIR", Path(tmpdir)):
            assert versions.available() == []
            assert versions.latest() is None
