import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_option import parse_av_option, parse_option_str

folder = pathlib.Path(__file__).parent / "test_parse_option"


@pytest.mark.parametrize("filepath", folder.glob("*.c"), ids=lambda path: path.stem)
def test_parse_option(snapshot: SnapshotAssertion, filepath: pathlib.Path) -> None:
    text = filepath.read_text()
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_option_str(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_av_option(text)
