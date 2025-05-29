from dataclasses import asdict
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..probe import probe

test_data = Path(__file__).parent / "test_probe"


@pytest.mark.parametrize("path", test_data.iterdir())
def test_probe(path: str, snapshot: SnapshotAssertion) -> None:
    info = probe(path)

    assert snapshot(extension_class=JSONSnapshotExtension) == asdict(info)
