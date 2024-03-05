import tempfile
from pathlib import Path

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ....common.schema import FFmpegFilter, FFmpegFilterOption, FFMpegIOType
from ..gen import render


def test_render(snapshot: SnapshotAssertion) -> None:
    filters = [
        FFmpegFilter(
            id="ff_af_aap",
            filter_type="af",
            name="aap",
            description="description",
            is_input_dynamic=False,
            is_output_dynamic=False,
            input_stream_typings=(
                FFMpegIOType(name="input", type="audio"),
                FFMpegIOType(name="desired", type="audio"),
            ),
            output_stream_typings=(FFMpegIOType(name="default", type="audio"),),
            options=(
                FFmpegFilterOption(
                    name="order",
                    description="set the filter order",
                    typing="int",
                    required=False,
                ),
                FFmpegFilterOption(
                    name="projection",
                    description="set the filter projection",
                    typing="int",
                    required=False,
                ),
            ),
        )
    ]

    with tempfile.TemporaryDirectory() as outpath:
        outputs = render(filters, [], Path(outpath))

        for outfile in outputs:
            assert snapshot(name=outfile.name, extension_class=SingleFileSnapshotExtension) == outfile.read_bytes()
