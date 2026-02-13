"""Tests for FFmpeg filter schema definitions."""

from ...common.schema import (
    FFMpegFilter,
    FFMpegIOType,
    StreamType,
)


def test_filter_pre_dict_property() -> None:
    """Test that pre_dict property converts pre list to dict."""
    filter_def = FFMpegFilter(
        name="scale",
        description="Scale video",
        pre=(("width", "1280"), ("height", "720")),
        stream_typings_input=(),
        stream_typings_output=(),
    )

    pre_dict = filter_def.pre_dict
    assert isinstance(pre_dict, dict)
    assert pre_dict["width"] == "1280"
    assert pre_dict["height"] == "720"


def test_filter_to_def_property() -> None:
    """Test that to_def property creates FFMpegFilterDef."""
    from ...common.schema import FFMpegFilterDef

    filter_def = FFMpegFilter(
        name="scale",
        description="Scale video",
        stream_typings_input=(FFMpegIOType(name="default", type=StreamType.video),),
        stream_typings_output=(FFMpegIOType(name="default", type=StreamType.video),),
    )

    simple_def = filter_def.to_def
    assert isinstance(simple_def, FFMpegFilterDef)
    assert simple_def.name == "scale"
    assert simple_def.typings_input == ("video",)
    assert simple_def.typings_output == ("video",)


def test_filter_input_typings_source() -> None:
    """Test input_typings for filter source (no inputs)."""
    filter_def = FFMpegFilter(
        name="color",
        description="Generate color",
        stream_typings_input=(),
        stream_typings_output=(),
        is_filter_source=True,
    )

    typings = filter_def.input_typings
    assert isinstance(typings, set)
    assert len(typings) == 0


def test_filter_input_typings_static() -> None:
    """Test input_typings for static input filter."""
    filter_def = FFMpegFilter(
        name="scale",
        description="Scale video",
        stream_typings_input=(FFMpegIOType(name="default", type=StreamType.video),),
        stream_typings_output=(),
    )

    typings = filter_def.input_typings
    assert StreamType.video in typings
    assert len(typings) == 1


def test_filter_input_typings_dynamic_video() -> None:
    """Test input_typings for dynamic input filter with video only."""
    filter_def = FFMpegFilter(
        name="concat",
        description="Concatenate videos",
        stream_typings_input=(),
        stream_typings_output=(),
        is_dynamic_input=True,
        formula_typings_input="video",
    )

    typings = filter_def.input_typings
    assert StreamType.video in typings
    assert StreamType.audio not in typings


def test_filter_input_typings_dynamic_audio() -> None:
    """Test input_typings for dynamic input filter with audio only."""
    filter_def = FFMpegFilter(
        name="amix",
        description="Mix audio",
        stream_typings_input=(),
        stream_typings_output=(),
        is_dynamic_input=True,
        formula_typings_input="audio",
    )

    typings = filter_def.input_typings
    assert StreamType.audio in typings
    assert StreamType.video not in typings


def test_filter_input_typings_dynamic_both() -> None:
    """Test input_typings for dynamic input filter with both video and audio."""
    filter_def = FFMpegFilter(
        name="amerge",
        description="Merge audio and video",
        stream_typings_input=(),
        stream_typings_output=(),
        is_dynamic_input=True,
        formula_typings_input="videoaudio",
    )

    typings = filter_def.input_typings
    assert StreamType.video in typings
    assert StreamType.audio in typings


def test_filter_output_typings_static() -> None:
    """Test output_typings for static output filter."""
    filter_def = FFMpegFilter(
        name="scale",
        description="Scale video",
        stream_typings_input=(),
        stream_typings_output=(FFMpegIOType(name="default", type=StreamType.video),),
    )

    typings = filter_def.output_typings
    assert StreamType.video in typings
    assert len(typings) == 1


def test_filter_output_typings_multiple() -> None:
    """Test output_typings for filter with multiple outputs."""
    filter_def = FFMpegFilter(
        name="split",
        description="Split video",
        stream_typings_input=(),
        stream_typings_output=(
            FFMpegIOType(name="output1", type=StreamType.video),
            FFMpegIOType(name="output2", type=StreamType.video),
        ),
    )

    typings = filter_def.output_typings
    assert StreamType.video in typings
    assert len(typings) == 1  # Both outputs are video, so set has 1 element


def test_filter_output_typings_dynamic() -> None:
    """Test output_typings for dynamic output filter."""
    filter_def = FFMpegFilter(
        name="split",
        description="Split stream",
        stream_typings_input=(),
        stream_typings_output=(),
        is_dynamic_output=True,
        formula_typings_output="video",
    )

    typings = filter_def.output_typings
    assert StreamType.video in typings
