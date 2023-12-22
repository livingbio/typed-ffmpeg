import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_c import parse_c

datadir = pathlib.Path(__file__).parent / "test_parse_c"


@pytest.mark.parametrize("path", datadir.glob("*.c"), ids=lambda path: path.stem)
def test_parse_c(path: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_c(path)
