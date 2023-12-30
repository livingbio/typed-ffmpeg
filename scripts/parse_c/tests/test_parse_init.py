import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ..parse_init import parse_init

datadir = pathlib.Path(__file__).parent / "test_parse_init"


@pytest.mark.parametrize("path", datadir.glob("*.c"), ids=lambda path: path.stem)
def test_parse_init(path: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    init = parse_init(path.read_text(), "init")
    assert snapshot(extension_class=SingleFileSnapshotExtension) == init.encode("utf-8")
