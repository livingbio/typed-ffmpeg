"""Tests for FFmpeg schema classes."""

from ..schema import Auto, Default, FFMpegOptionGroup


def test_default_class() -> None:
    """Test Default class for representing default values."""
    default = Default("23")
    assert str(default) == "23"
    assert isinstance(default, str)


def test_auto_class() -> None:
    """Test Auto class for representing auto-derived values."""
    auto = Auto("len(streams)")
    assert str(auto) == "len(streams)"
    assert isinstance(auto, Default)
    assert isinstance(auto, str)


def test_ffmpeg_option_group_basic() -> None:
    """Test FFMpegOptionGroup basic functionality."""
    options = FFMpegOptionGroup({"crf": 23, "preset": "fast"})
    assert options["crf"] == 23
    assert options["preset"] == "fast"


def test_ffmpeg_option_group_as_av_options() -> None:
    """Test as_av_options converts boolean to 0/1."""
    options = FFMpegOptionGroup({
        "flag1": True,
        "flag2": False,
        "string": "value",
        "number": 42,
    })

    av_options = options.as_av_options()

    assert av_options["flag1"] == 1
    assert av_options["flag2"] == 0
    assert av_options["string"] == "value"
    assert av_options["number"] == 42


def test_ffmpeg_option_group_as_av_options_none() -> None:
    """Test as_av_options filters out None values."""
    options = FFMpegOptionGroup({"keep": "value", "remove": None, "also_keep": 123})

    av_options = options.as_av_options()

    assert "keep" in av_options
    assert "also_keep" in av_options
    assert "remove" not in av_options
    assert av_options["keep"] == "value"
    assert av_options["also_keep"] == 123


def test_ffmpeg_option_group_as_av_options_empty() -> None:
    """Test as_av_options with empty group."""
    options = FFMpegOptionGroup()
    av_options = options.as_av_options()
    assert av_options == {}


def test_ffmpeg_option_group_as_av_options_all_none() -> None:
    """Test as_av_options with all None values."""
    options = FFMpegOptionGroup({"a": None, "b": None, "c": None})
    av_options = options.as_av_options()
    assert av_options == {}
