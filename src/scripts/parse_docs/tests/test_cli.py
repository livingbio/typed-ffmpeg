import pathlib

import pytest

from ..cli import extract_docs, process_docs, process_texi_docs


def test_process_docs() -> None:
    process_docs()


def test_extract_docs() -> None:
    extract_docs("acrossfade")

    with pytest.raises(ValueError):
        extract_docs("nonexistent_filter")


def test_process_texi_docs_real_file():
    """Smoke test with the actual ffmpeg submodule texi if available."""
    repo_root = pathlib.Path(__file__).resolve().parents[5]
    texi_path = repo_root / "ffmpeg" / "doc" / "filters.texi"
    if not texi_path.exists():
        pytest.skip("ffmpeg submodule not available")

    docs = process_texi_docs(texi_path)
    assert len(docs) > 100  # There are hundreds of filters

    # Check a well-known filter exists
    names = {name for doc in docs for name in doc.filter_names}
    assert "crop" in names
    assert "overlay" in names
    assert "volume" in names
