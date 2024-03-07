import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..helper import dump
from ..parse_av_option import parse_av_option

folder = pathlib.Path(__file__).parent / "test_parse_av_option"


@pytest.mark.parametrize("filepath", folder.glob("*.c"), ids=lambda path: path.stem)
def test_parse_option(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    text = filepath.read_text()
    assert snapshot(extension_class=JSONSnapshotExtension) == dump(parse_av_option(text))
