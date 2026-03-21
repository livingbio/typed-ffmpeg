import tempfile
from math import nan
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ffmpeg.common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionChoice,
    FFMpegFilterOptionType,
    FFMpegIOType,
    FFMpegOption,
    FFMpegOptionType,
    StreamType,
)

from ..gen import (
    default_typings,
    default_value,
    filter_option_typing,
    filter_option_typings,
    input_typings,
    normalize_help_text,
    option_name_safe,
    option_typing,
    output_typings,
    render,
    stream_name_safe,
)

# --- Helpers for test data ---


def _filter(
    name: str = "test",
    inputs: tuple[FFMpegIOType, ...] = (),
    outputs: tuple[FFMpegIOType, ...] = (),
    options: tuple[FFMpegFilterOption, ...] = (),
    formula_in: str | None = None,
    formula_out: str | None = None,
    pre: tuple[tuple[str, str], ...] = (),
) -> FFMpegFilter:
    return FFMpegFilter(
        name=name,
        description="test filter",
        is_dynamic_input=False,
        is_dynamic_output=False,
        stream_typings_input=inputs,
        stream_typings_output=outputs,
        options=options,
        formula_typings_input=formula_in,
        formula_typings_output=formula_out,
        pre=pre,
    )


def _opt(
    name: str = "opt",
    type: FFMpegFilterOptionType = FFMpegFilterOptionType.int,
    default: object = 0,
    choices: tuple[FFMpegFilterOptionChoice, ...] = (),
) -> FFMpegFilterOption:
    return FFMpegFilterOption(
        name=name,
        description="test option",
        type=type,
        required=False,
        default=default,
        choices=choices,
    )


# --- filter_option_typing ---


@pytest.mark.parametrize(
    "opt_type, expected",
    [
        (FFMpegFilterOptionType.boolean, "Boolean"),
        (FFMpegFilterOptionType.duration, "Duration"),
        (FFMpegFilterOptionType.color, "Color"),
        (FFMpegFilterOptionType.flags, "Flags"),
        (FFMpegFilterOptionType.dictionary, "Dictionary"),
        (FFMpegFilterOptionType.pix_fmt, "Pix_fmt"),
        (FFMpegFilterOptionType.int, "Int"),
        (FFMpegFilterOptionType.int64, "Int64"),
        (FFMpegFilterOptionType.double, "Double"),
        (FFMpegFilterOptionType.float, "Float"),
        (FFMpegFilterOptionType.string, "String"),
        (FFMpegFilterOptionType.video_rate, "Video_rate"),
        (FFMpegFilterOptionType.image_size, "Image_size"),
        (FFMpegFilterOptionType.rational, "Rational"),
        (FFMpegFilterOptionType.sample_fmt, "Sample_fmt"),
        (FFMpegFilterOptionType.binary, "Binary"),
        (FFMpegFilterOptionType.channel_layout, "String"),
        (FFMpegFilterOptionType.unsigned, "Int"),
    ],
)
def test_filter_option_typing_basic(
    opt_type: FFMpegFilterOptionType, expected: str
) -> None:
    option = _opt(type=opt_type)
    assert filter_option_typing(option) == expected


def test_filter_option_typing_with_choices() -> None:
    choices = (
        FFMpegFilterOptionChoice(name="fast", help="", value="1"),
        FFMpegFilterOptionChoice(name="slow", help="", value="2"),
    )
    option = _opt(type=FFMpegFilterOptionType.int, choices=choices)
    assert filter_option_typing(option) == 'Int| Literal["fast","slow"]'


# --- option_name_safe / stream_name_safe ---


def test_option_name_safe_keyword() -> None:
    assert option_name_safe("class") == "_class"


def test_option_name_safe_digit() -> None:
    assert option_name_safe("0db") == "_0db"


def test_option_name_safe_hyphen() -> None:
    assert option_name_safe("bit-rate") == "bit_rate"


def test_option_name_safe_normal() -> None:
    assert option_name_safe("volume") == "volume"


def test_stream_name_safe_adds_underscore() -> None:
    assert stream_name_safe("input") == "_input"


def test_stream_name_safe_already_prefixed() -> None:
    # keyword: starts with _ after option_name_safe
    assert stream_name_safe("class") == "_class"


# --- option_typing ---


@pytest.mark.parametrize(
    "opt_type, expected",
    [
        (FFMpegOptionType.OPT_TYPE_FUNC, "Func"),
        (FFMpegOptionType.OPT_TYPE_BOOL, "Boolean"),
        (FFMpegOptionType.OPT_TYPE_STRING, "String"),
        (FFMpegOptionType.OPT_TYPE_INT, "Int"),
        (FFMpegOptionType.OPT_TYPE_INT64, "Int64"),
        (FFMpegOptionType.OPT_TYPE_FLOAT, "Float"),
        (FFMpegOptionType.OPT_TYPE_DOUBLE, "Double"),
        (FFMpegOptionType.OPT_TYPE_TIME, "Time"),
    ],
)
def test_option_typing(opt_type: FFMpegOptionType, expected: str) -> None:
    opt = FFMpegOption(name="x", type=opt_type, help="", flags=0, canon="x")
    assert option_typing(opt) == expected


# --- input_typings / output_typings ---


def test_input_typings_from_stream_typings() -> None:
    f = _filter(
        inputs=(
            FFMpegIOType(name="in", type=StreamType.audio),
            FFMpegIOType(name="in2", type=StreamType.video),
        ),
    )
    assert input_typings(f) == "[StreamType.audio, StreamType.video]"


def test_input_typings_from_formula() -> None:
    f = _filter(formula_in="[StreamType.audio] * n")
    assert input_typings(f) == "[StreamType.audio] * n"


def test_output_typings_from_stream_typings() -> None:
    f = _filter(
        outputs=(FFMpegIOType(name="out", type=StreamType.video),),
    )
    assert output_typings(f) == "[StreamType.video]"


def test_output_typings_from_formula() -> None:
    f = _filter(formula_out="[StreamType.video] * n")
    assert output_typings(f) == "[StreamType.video] * n"


# --- default_value ---


def test_default_value_normal() -> None:
    opt = _opt(default=42)
    f = _filter()
    assert default_value(opt, f) == "Default(42)"


def test_default_value_nan() -> None:
    opt = _opt(default=nan)
    f = _filter()
    assert default_value(opt, f) == 'Default("nan")'


def test_default_value_pre_dict() -> None:
    opt = _opt(name="size")
    f = _filter(pre=(("size", "640x480"),))
    assert default_value(opt, f) == "Auto('640x480')"


# --- default_typings ---


def test_default_typings_no_choices() -> None:
    opt = _opt(type=FFMpegFilterOptionType.int, default=5)
    f = _filter()
    assert default_typings(opt, f) == "Int = Default(5)"


def test_default_typings_with_choices() -> None:
    choices = (FFMpegFilterOptionChoice(name="a", help="", value="1"),)
    opt = _opt(type=FFMpegFilterOptionType.int, default=0, choices=choices)
    f = _filter()
    result = default_typings(opt, f)
    assert "Literal" in result
    assert "Default(0)" in result


# --- filter_option_typings ---


def test_filter_option_typings_empty() -> None:
    f = _filter()
    assert filter_option_typings(f) == ""


def test_filter_option_typings_multiple() -> None:
    f = _filter(
        options=(
            _opt(name="width", type=FFMpegFilterOptionType.int, default=0),
            _opt(name="height", type=FFMpegFilterOptionType.int, default=0),
        )
    )
    result = filter_option_typings(f)
    assert "width:" in result
    assert "height:" in result
    assert result.endswith(",")


# --- normalize_help_text ---


def test_normalize_help_text_basic() -> None:
    assert normalize_help_text("hello world") == "hello world"


def test_normalize_help_text_newlines() -> None:
    assert normalize_help_text("line1\n  line2") == "line1 line2"


def test_normalize_help_text_c_continuation() -> None:
    text = 'text ("option1"\\\n        "option2")'
    result = normalize_help_text(text)
    assert "\n" not in result


def test_normalize_help_text_multiple_spaces() -> None:
    assert normalize_help_text("a    b") == "a b"


# --- render ---


def test_render(snapshot: SnapshotAssertion) -> None:
    filters = [
        FFMpegFilter(
            id="ff_af_aap",
            name="aap",
            description="description",
            is_dynamic_input=False,
            is_dynamic_output=False,
            stream_typings_input=(
                FFMpegIOType(name="input", type=StreamType.audio),
                FFMpegIOType(name="desired", type=StreamType.audio),
            ),
            stream_typings_output=(
                FFMpegIOType(name="default", type=StreamType.audio),
            ),
            options=(
                FFMpegFilterOption(
                    name="order",
                    description="set the filter order",
                    type=FFMpegFilterOptionType.int,
                    required=False,
                ),
                FFMpegFilterOption(
                    name="projection",
                    description="set the filter projection",
                    type=FFMpegFilterOptionType.int,
                    required=False,
                ),
            ),
        )
    ]

    with tempfile.TemporaryDirectory() as outpath:
        outputs = render(
            filters=filters, options=[], codecs=[], muxers=[], outpath=Path(outpath)
        )

        for outfile in outputs:
            assert (
                snapshot(name=outfile.name, extension_class=SingleFileSnapshotExtension)
                == outfile.read_bytes()
            )


def test_render_with_version_prefix() -> None:
    """Verify versioned render creates __init__.py and py.typed."""
    filters = [
        FFMpegFilter(
            name="scale",
            description="Scale",
            is_dynamic_input=False,
            is_dynamic_output=False,
            stream_typings_input=(
                FFMpegIOType(name="default", type=StreamType.video),
            ),
            stream_typings_output=(
                FFMpegIOType(name="default", type=StreamType.video),
            ),
            options=(),
        )
    ]

    with tempfile.TemporaryDirectory() as outpath:
        out = Path(outpath) / "v7"
        outputs = render(
            filters=filters,
            options=[],
            codecs=[],
            muxers=[],
            outpath=out,
            version_prefix="v7",
        )

        output_names = [p.name for p in outputs]
        assert "py.typed" in output_names
        assert "__init__.py" in output_names

        init_content = (out / "__init__.py").read_text()
        assert "v7" in init_content


def test_render_no_duplicate_init() -> None:
    """If __init__.py already exists, render should not add it again."""
    with tempfile.TemporaryDirectory() as outpath:
        out = Path(outpath)
        out.mkdir(exist_ok=True)
        init = out / "__init__.py"
        init.write_text("# custom\n")

        outputs = render(
            filters=[],
            options=[],
            codecs=[],
            muxers=[],
            outpath=out,
            version_prefix="v6",
        )

        # __init__.py should NOT be in outputs since it already existed
        output_names = [p.name for p in outputs]
        assert "__init__.py" not in output_names
        # Original content preserved
        assert init.read_text() == "# custom\n"
