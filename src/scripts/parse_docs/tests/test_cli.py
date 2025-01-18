import pytest

from scripts.parse_docs.cli import extract_docs, process_docs


def test_process_docs() -> None:
    process_docs()


def test_extract_docs() -> None:
    extract_docs("acrossfade")

    with pytest.raises(ValueError):
        extract_docs("nonexistent_filter")
