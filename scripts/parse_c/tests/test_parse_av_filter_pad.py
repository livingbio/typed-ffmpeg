import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..helper import dump
from ..parse_av_filter_pad import parse_av_filter_pad

test_data = pathlib.Path(__file__).parent / "test_parse_av_filter_pad"


@pytest.mark.parametrize("filepath", test_data.glob("*.c"), ids=lambda path: path.stem)
def test_parse_av_filter(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    text = filepath.read_text()
    assert snapshot(extension_class=JSONSnapshotExtension) == dump(parse_av_filter_pad(text))
