"""Tests for code_gen schema module."""

import pytest

from ..schema import (
    FFMpegAVOption,
    FFMpegCodec,
    FFMpegDecoder,
    FFMpegDemuxer,
    FFMpegEncoder,
    FFMpegFormat,
    FFMpegMuxer,
    FFMpegOptionChoice,
    is_supported_version,
    parse_version,
    version_cache_key,
)


# --- Version helpers ---


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


# --- FFMpegAVOption.code_gen_type ---


def _make_option(
    type: str,
    choices: tuple[FFMpegOptionChoice, ...] = (),
) -> FFMpegAVOption:
    return FFMpegAVOption(
        section="test",
        name="opt",
        type=type,
        flags="E..VA......",
        help="test",
        choices=choices,
    )


@pytest.mark.parametrize(
    "opt_type, expected",
    [
        ("boolean", "bool | None"),
        ("int", "int | None"),
        ("int64", "int | None"),
        ("unsigned", "int | None"),
        ("float", "float | None"),
        ("double", "float | None"),
        ("string", "str | None"),
        ("channel_layout", "str | None"),
        ("flags", "str | None"),
        ("duration", "str | None"),
        ("dictionary", "str | None"),
        ("image_size", "str | None"),
        ("pixel_format", "str | None"),
        ("sample_rate", "int | None"),
        ("sample_fmt", "str | None"),
        ("binary", "str | None"),
        ("rational", "str | None"),
        ("color", "str | None"),
        ("video_rate", "str | None"),
        ("pix_fmt", "str | None"),
    ],
)
def test_code_gen_type(opt_type: str, expected: str) -> None:
    assert _make_option(opt_type).code_gen_type == expected


def test_code_gen_type_invalid() -> None:
    with pytest.raises(ValueError, match="Invalid option type"):
        _make_option("unknown_type").code_gen_type


def test_code_gen_type_with_choices() -> None:
    choices = (
        FFMpegOptionChoice(name="fast", help="fast", flags="", value="1"),
        FFMpegOptionChoice(name="slow", help="slow", flags="", value="2"),
    )
    result = _make_option("int", choices=choices).code_gen_type
    assert result == 'int | None| Literal["fast", "slow"]'


def test_code_gen_type_flags_ignores_choices() -> None:
    """flags type does NOT include Literal choices."""
    choices = (FFMpegOptionChoice(name="opt1", help="", flags="", value="1"),)
    assert _make_option("flags", choices=choices).code_gen_type == "str | None"


# --- FFMpegCodec ---


class TestFFMpegCodec:
    def test_encoder_identity(self) -> None:
        enc = FFMpegEncoder(name="libx264", flags="V....D", description="H.264")
        assert enc.is_encoder is True
        assert enc.is_decoder is False

    def test_decoder_identity(self) -> None:
        dec = FFMpegDecoder(name="h264", flags="V....D", description="H.264")
        assert dec.is_decoder is True
        assert dec.is_encoder is False

    @pytest.mark.parametrize(
        "flags, expected",
        [("V....D", "video"), ("A....D", "audio"), ("S....D", "subtitle")],
    )
    def test_codec_type(self, flags: str, expected: str) -> None:
        codec = FFMpegEncoder(name="x", flags=flags, description="")
        assert codec.codec_type == expected

    def test_codec_type_invalid(self) -> None:
        codec = FFMpegEncoder(name="bad", flags="X....D", description="")
        with pytest.raises(ValueError, match="Invalid stream type"):
            codec.codec_type

    def test_filtered_options(self) -> None:
        opts = (
            FFMpegAVOption(section="s", name="o1", type="int", flags="", help=""),
        )
        codec = FFMpegEncoder(name="x", flags="V....D", description="", options=opts)
        assert list(codec.filtered_options()) == list(opts)


# --- FFMpegFormat ---


class TestFFMpegFormat:
    def test_muxer_identity(self) -> None:
        mux = FFMpegMuxer(name="mp4", flags="E", description="MP4")
        assert mux.is_muxer is True
        assert mux.is_demuxer is False

    def test_demuxer_identity(self) -> None:
        demux = FFMpegDemuxer(name="mp4", flags="D", description="MP4")
        assert demux.is_demuxer is True
        assert demux.is_muxer is False
