import tempfile
from pathlib import Path

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ....common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionTyping,
    FFMpegFilterType,
    FFMpegIOType,
    StreamType,
)
from ..gen import render


def test_render(snapshot: SnapshotAssertion) -> None:
    filters = [
        FFMpegFilter(
            id="ff_af_aap",
            filter_type=FFMpegFilterType.af,
            name="aap",
            description="description",
            is_dynamic_input=False,
            is_dynamic_output=False,
            stream_typings_input=(
                FFMpegIOType(name="input", type=StreamType.audio),
                FFMpegIOType(name="desired", type=StreamType.audio),
            ),
            stream_typings_output=(FFMpegIOType(name="default", type=StreamType.audio),),
            options=(
                FFMpegFilterOption(
                    name="order",
                    description="set the filter order",
                    typing=FFMpegFilterOptionTyping.int,
                    required=False,
                ),
                FFMpegFilterOption(
                    name="projection",
                    description="set the filter projection",
                    typing=FFMpegFilterOptionTyping.int,
                    required=False,
                ),
            ),
        )
    ]

    with tempfile.TemporaryDirectory() as outpath:
        outputs = render(filters, [], Path(outpath))

        for outfile in outputs:
            assert snapshot(name=outfile.name, extension_class=SingleFileSnapshotExtension) == outfile.read_bytes()