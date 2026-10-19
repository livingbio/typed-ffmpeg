import tempfile
from pathlib import Path

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ffmpeg_core.common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionType,
    FFMpegIOType,
    StreamType,
)

from ..gen import filter_option_typings, render


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
        outpath_obj = Path(outpath)
        outputs = render(
            filters=filters, options=[], codecs=[], muxers=[], outpath=outpath_obj
        )

        for outfile in outputs:
            name = str(outfile.relative_to(outpath_obj))
            assert (
                snapshot(name=name, extension_class=SingleFileSnapshotExtension)
                == outfile.read_bytes()
            )


def test_filter_option_typings_expression() -> None:
    drawbox = FFMpegFilter(
        name="drawbox",
        description="description",
        options=(
            FFMpegFilterOption(
                name="x",
                description="set horizontal position",
                type=FFMpegFilterOptionType.string,
                default="0",
            ),
            FFMpegFilterOption(
                name="color",
                description="set color",
                type=FFMpegFilterOptionType.string,
                default="black",
            ),
            FFMpegFilterOption(
                name="t",
                description="set thickness",
                type=FFMpegFilterOptionType.int,
                default="3",
            ),
            FFMpegFilterOption(
                name="ratio",
                description="set ratio",
                type=FFMpegFilterOptionType.double,
                default="-0.5",
            ),
        ),
    )

    assert filter_option_typings(drawbox, {"drawbox": ["x"]}).split(",") == [
        "x: Expr = Default(0)",
        "color: String = Default('black')",
        "t: Int = Default(3)",
        "ratio: Double = Default(-0.5)",
        "",
    ]
    # without expression metadata the option stays a plain String
    assert filter_option_typings(drawbox).startswith("x: String = Default('0'),")
