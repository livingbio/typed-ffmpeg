import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion

from ..parser import parse_filter_document

test_data = pathlib.Path(__file__).parent / "data"


@pytest.mark.parametrize("filepath", test_data.glob("*.html"), ids=lambda x: x.name)
def test_parse_filter_document(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    with filepath.open() as ifile:
        body = ifile.read()
    assert snapshot == parse_filter_document(body)
