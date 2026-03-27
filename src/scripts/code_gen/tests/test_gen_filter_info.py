"""Tests for gen_filter_info with texi enrichment."""

from ffmpeg_core.common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionType,
)

from ...parse_docs.cli import process_texi_docs
from ..cli import gen_filter_info

SAMPLE_TEXI = """\
@section testfilter

This is a detailed description of the test filter.
It processes audio in a special way.

The filter accepts the following options:

@table @option
@item threshold
Set the detection threshold. Range is 0 to 1. Default is 0.5.

@item mode, m
Set the processing mode.
@end table
"""


def test_gen_filter_info_enriches_description(tmp_path):
    texi_file = tmp_path / "filters.texi"
    texi_file.write_text(SAMPLE_TEXI)
    texi_docs = process_texi_docs(texi_file)

    base_filter = FFMpegFilter(
        name="testfilter",
        description="short help text",
        options=(
            FFMpegFilterOption(
                name="threshold",
                description="set threshold (from 0 to 1) (default 0.5)",
                type=FFMpegFilterOptionType.double,
            ),
            FFMpegFilterOption(
                name="mode",
                description="set mode",
                type=FFMpegFilterOptionType.int,
            ),
        ),
    )

    enriched = gen_filter_info(base_filter, texi_docs=texi_docs)

    # Description should be enriched with texi content
    assert "detailed description" in enriched.description
    assert enriched.ref == "https://ffmpeg.org/ffmpeg-filters.html#testfilter"

    # Option descriptions should be enriched
    threshold_opt = next(o for o in enriched.options if o.name == "threshold")
    assert "detection threshold" in threshold_opt.description

    mode_opt = next(o for o in enriched.options if o.name == "mode")
    assert "processing mode" in mode_opt.description


def test_gen_filter_info_missing_filter(tmp_path):
    """Filter not in texi docs should keep original description."""
    texi_file = tmp_path / "filters.texi"
    texi_file.write_text(SAMPLE_TEXI)
    texi_docs = process_texi_docs(texi_file)

    base_filter = FFMpegFilter(
        name="unknown_hw_filter",
        description="original description",
    )

    result = gen_filter_info(base_filter, texi_docs=texi_docs)
    assert result.description == "original description"
    assert result.ref is None
