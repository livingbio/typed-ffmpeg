import pathlib

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_src import all_filter_names


def test_all_filter_names(snapshot: SnapshotAssertion, datadir: pathlib.Path) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == all_filter_names(datadir / "allfilters.c")
