from typing import Literal

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_formats import (
    _extract_format,
    _extract_list,
    extract,
)

@pytest.mark.dev_only

@pytest.mark.parametrize("type", ["muxers", "demuxers"])
def test_parse_codecs_help_text(
    snapshot: SnapshotAssertion, type: Literal["muxers", "demuxers"]
) -> None:
    codecs = _extract_list(type)
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs


@pytest.mark.parametrize(
    "codec, type",
    [
        ("wav", "demuxer"),
        ("mp3", "demuxer"),
        ("mp4", "muxer"),
        ("mov", "muxer"),
    ],
)
def test_parse_codec_option(
    snapshot: SnapshotAssertion, codec: str, type: Literal["muxer", "demuxer"]
) -> None:
    options = _extract_format(codec, type)
    assert snapshot == options

@pytest.mark.dev_only
def test_extract_all_codecs(snapshot: SnapshotAssertion) -> None:
    codecs = extract()
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs
