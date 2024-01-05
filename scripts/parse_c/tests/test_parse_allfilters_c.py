import pathlib

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_allfilters_c import parse_all_filter_names


def test_parse_all_filter_names(shared_datadir: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    filters = parse_all_filter_names(shared_datadir / "allfilters.c")
    assert snapshot(extension_class=JSONSnapshotExtension) == filters
    assert snapshot == len(filters)
