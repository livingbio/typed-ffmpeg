"""Tests for code_gen schema version helpers."""

import pytest

from ..schema import (
    is_supported_version,
    parse_version,
    version_cache_key,
)


def test_version_cache_key() -> None:
    assert version_cache_key("6.0") == "6_0"
    assert version_cache_key("5.1") == "5_1"


def test_parse_version() -> None:
    assert parse_version("6.0") == (6, 0)
    assert parse_version("ffmpeg version 6.0 Copyright (c)") == (6, 0)
    assert parse_version("5.1.2") == (5, 1)


def test_parse_version_invalid() -> None:
    with pytest.raises(ValueError, match="Cannot parse version"):
        parse_version("nover")


def test_is_supported_version() -> None:
    assert is_supported_version("5.0") is True
    assert is_supported_version("6.0") is True
    assert is_supported_version("7.1") is True
    assert is_supported_version("4.4") is False
    assert is_supported_version("4.9") is False
