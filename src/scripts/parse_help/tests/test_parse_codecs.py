from typing import Literal

import pytest
from syrupy.assertion import SnapshotAssertion

from ..parse_codecs import (
    _extract_codec,
    _extract_list,
)


@pytest.mark.parametrize("type", ["encoders", "decoders", "codecs"])
def test_parse_codecs_help_text(
    snapshot: SnapshotAssertion, type: Literal["encoders", "decoders", "codecs"]
) -> None:
    codecs = _extract_list(type)
    snapshot == codecs


@pytest.mark.parametrize(
    "codec, type",
    [
        ("h263", "encoder"),
        ("h263", "decoder"),
        ("tiff", "decoder"),
        ("h264_nvenc", "encoder"),
    ],
)
def test_parse_codec_option(
    snapshot: SnapshotAssertion, codec: str, type: Literal["encoder", "decoder"]
) -> None:
    options = _extract_codec(codec, type)
    assert snapshot == options


# def test_extract_all_codecs(snapshot: SnapshotAssertion) -> None:
#     codecs = extract_all_codecs()
#     assert snapshot == codecs
