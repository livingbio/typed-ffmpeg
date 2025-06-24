from typing import Literal

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_codecs import (
    _extract_codec,
    _extract_list,
    _parse_codec,
    _parse_list,
    extract,
)


@pytest.mark.dev_only
@pytest.mark.parametrize("type", ["encoders", "decoders", "codecs"])
def test_extract_list(
    snapshot: SnapshotAssertion, type: Literal["encoders", "decoders", "codecs"]
) -> None:
    """Test extracting codec lists from ffmpeg help output."""
    codecs = _extract_list(type)
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs


@pytest.mark.parametrize(
    "text",
    [
        pytest.param(
            """
Codecs:
 D..... = Decoding supported
 .E.... = Encoding supported
 ..V... = Video codec
 ..A... = Audio codec
 ..S... = Subtitle codec
 ..D... = Data codec
 ..T... = Attachment codec
 ...I.. = Intra frame-only codec
 ....L. = Lossy compression
 .....S = Lossless compression
 -------
 D.VI.S 012v                 Uncompressed 4:2:2 10-bit
 D.V.L. 4xm                  4X Movie
 D.VI.S 8bps                 QuickTime 8BPS video
""",
            id="codecs",
        ),
        pytest.param(
            """Encoders:
 V..... = Video
 A..... = Audio
 S..... = Subtitle
 .F.... = Frame-level multithreading
 ..S... = Slice-level multithreading
 ...X.. = Codec is experimental
 ....B. = Supports draw_horiz_band
 .....D = Supports direct rendering method 1
 ------
 V....D a64multi             Multicolor charset for Commodore 64 (codec a64_multi)
 V....D a64multi5            Multicolor charset for Commodore 64, extended with 5th color (colram) (codec a64_multi5)
 V....D alias_pix            Alias/Wavefront PIX image
 V..... amv                  AMV Video
 V....D apng                 APNG (Animated Portable Network Graphics) image""",
            id="encoders",
        ),
        pytest.param(
            """Decoders:
 V..... = Video
 A..... = Audio
 S..... = Subtitle
 .F.... = Frame-level multithreading
 ..S... = Slice-level multithreading
 ...X.. = Codec is experimental
 ....B. = Supports draw_horiz_band
 .....D = Supports direct rendering method 1
 ------
 V....D 012v                 Uncompressed 4:2:2 10-bit
 V....D 4xm                  4X Movie
 V....D 8bps                 QuickTime 8BPS video
 V....D aasc                 Autodesk RLE
 V....D agm                  Amuse Graphics Movie""",
            id="decoders",
        ),
    ],
)
def test_parse_list(text: str, snapshot: SnapshotAssertion) -> None:
    """Test parsing codec list text into structured data."""
    codecs = _parse_list(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs


def test_parse_codec_options(snapshot: SnapshotAssertion) -> None:
    """Test parsing codec options from help text."""
    text = """Encoder amv [AMV Video]:
    General capabilities:
    Threading capabilities: none
    Supported pixel formats: yuvj420p
amv encoder AVOptions:
  -mpv_flags         <flags>      E..V....... Flags common for all mpegvideo-based encoders. (default 0)
     skip_rd                      E..V....... RD optimal MB level residual skipping
     strict_gop                   E..V....... Strictly enforce gop size
     qp_rd                        E..V....... Use rate distortion optimization for qp selection
     cbp_rd                       E..V....... use rate distortion optimization for CBP
     naq                          E..V....... normalize adaptive quantization
     mv0                          E..V....... always try a mb with mv=<0,0>
  -luma_elim_threshold <int>        E..V....... single coefficient elimination threshold for luminance (negative values also consider dc coefficient) (from INT_MIN to INT_MAX) (default 0)
    """
    codec_options = _parse_codec(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == codec_options


@pytest.mark.parametrize(
    "codec, type",
    [
        ("h263", "encoder"),
        ("h263", "decoder"),
        ("tiff", "decoder"),
        ("h264_nvenc", "encoder"),
    ],
)
def test_extract_codec_options(
    snapshot: SnapshotAssertion, codec: str, type: Literal["encoder", "decoder"]
) -> None:
    """Test extracting codec options from ffmpeg help output."""
    options = _extract_codec(codec, type)
    assert snapshot(extension_class=JSONSnapshotExtension) == options


@pytest.mark.dev_only
def test_extract_all_codecs(snapshot: SnapshotAssertion) -> None:
    """Test extracting all codecs with their options."""
    codecs = extract()
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs
