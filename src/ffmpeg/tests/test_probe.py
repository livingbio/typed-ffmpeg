from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension
from syrupy.filters import props

from ..probe import probe

test_data = Path(__file__).parent / "test_probe"


@pytest.mark.parametrize("path", test_data.glob("**/*.*"), ids=lambda x: x.name)
def test_probe_default(path: Path, snapshot: SnapshotAssertion) -> None:
    info = probe(path)
    assert (
        snapshot(
            extension_class=JSONSnapshotExtension, exclude=props("format.filename")
        )
        == info
    )


@pytest.mark.parametrize("path", test_data.glob("**/*.*"), ids=lambda x: x.name)
def test_probe_complete(path: Path, snapshot: SnapshotAssertion) -> None:
    info = probe(
        path,
        show_program_version=True,
        show_library_versions=True,
        show_pixel_formats=True,
        show_packets=True,
        show_frames=True,
        show_programs=True,
        show_streams=True,
        show_chapters=True,
        show_format=True,
        show_error=True,
    )
    assert (
        snapshot(
            extension_class=JSONSnapshotExtension, exclude=props("format.filename")
        )
        == info
    )
