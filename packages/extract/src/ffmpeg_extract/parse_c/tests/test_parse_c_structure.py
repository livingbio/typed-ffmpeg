import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_c_structure import parse_c_structure

test_data = pathlib.Path(__file__).parent / "test_parse_c_structure"


@pytest.mark.parametrize("filepath", test_data.glob("*.c"), ids=lambda path: path.stem)
def test_parse_c_structure(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    text = filepath.read_text()
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_c_structure(text)


def test_parse_c_structure_samples(snapshot: SnapshotAssertion) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_c_structure(
        """{{ .str = "" }}"""
    )
