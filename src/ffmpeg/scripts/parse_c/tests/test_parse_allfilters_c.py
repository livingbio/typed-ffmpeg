from pathlib import Path

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_allfilters_c import parse_all_filter_names


def test_parse_all_filter_names(snapshot: SnapshotAssertion, ffmpeg_path: Path) -> None:
    filters = parse_all_filter_names(ffmpeg_path / "libavfilter/allfilters.c")
    assert snapshot(extension_class=JSONSnapshotExtension) == filters
    assert snapshot == len(filters)
