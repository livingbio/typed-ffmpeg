import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..helper import dump
from ..parse_c import parse_all_filter_names, parse_c

datadir = pathlib.Path(__file__).parent / "test_parse_c"


@pytest.mark.parametrize("path", datadir.glob("*.c"), ids=lambda path: path.stem)
def test_parse_c(path: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    filters = parse_c(path)
    assert snapshot(extension_class=JSONSnapshotExtension) == dump(filters)
    assert snapshot(extension_class=JSONSnapshotExtension) == dump([k.parsed_options for k in filters])


def test_parse_all_filter_names(snapshot: SnapshotAssertion) -> None:
    filters = parse_all_filter_names(datadir / "allfilters.c")
    assert snapshot(extension_class=JSONSnapshotExtension) == filters
    assert snapshot == len(filters)
