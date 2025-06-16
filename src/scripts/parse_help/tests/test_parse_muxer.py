from typing import Literal

import pytest
from syrupy.assertion import SnapshotAssertion

from ..parse_muxer import (
    extract_codec_option,
    extract_muxer_help_text,
)


@pytest.mark.parametrize("type", ["muxers", "demuxers"])
def test_parse_codecs_help_text(
    snapshot: SnapshotAssertion, type: Literal["muxers", "demuxers"]
) -> None:
    codecs = extract_muxer_help_text(type)
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
    options = extract_codec_option(codec, type)
    assert snapshot == options


# def test_extract_all_codecs(snapshot: SnapshotAssertion) -> None:
#     codecs = extract_all_codecs()
#     assert snapshot == codecs
