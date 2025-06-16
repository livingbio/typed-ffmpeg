from typing import Literal

import pytest
from syrupy.assertion import SnapshotAssertion

from ..parse_formats import (
    extract_format_help_text,
    extract_format_option,
)


@pytest.mark.parametrize("type", ["muxers", "demuxers"])
def test_parse_codecs_help_text(
    snapshot: SnapshotAssertion, type: Literal["muxers", "demuxers"]
) -> None:
    codecs = extract_format_help_text(type)
    snapshot == codecs


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
    options = extract_format_option(codec, type)
    assert snapshot == options


# def test_extract_all_codecs(snapshot: SnapshotAssertion) -> None:
#     codecs = extract_all_codecs()
#     assert snapshot == codecs
