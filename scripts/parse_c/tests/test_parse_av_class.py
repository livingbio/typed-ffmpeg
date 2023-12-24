import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..helper import dump
from ..parse_av_class import parse_av_class

test_data = pathlib.Path(__file__).parent / "test_parse_av_class"


@pytest.mark.parametrize("filepath", test_data.glob("*.c"), ids=lambda path: path.stem)
def test_parse_av_class(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    text = filepath.read_text()
    assert snapshot(extension_class=JSONSnapshotExtension) == dump(parse_av_class(text))
