import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_init import parse_init

datadir = pathlib.Path(__file__).parent / "test_parse_init"


@pytest.mark.parametrize("path", datadir.glob("*.c"), ids=lambda path: path.stem)
def test_parse_init(path: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    init = parse_init(path.read_text())
    assert snapshot(extension_class=JSONSnapshotExtension) == init
