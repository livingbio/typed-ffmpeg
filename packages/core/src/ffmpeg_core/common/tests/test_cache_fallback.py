import pytest

from ..cache import _get_data_cache_path, load
from ..schema import FFMpegFilter


def test_get_data_cache_path() -> None:
    path = _get_data_cache_path()
    # Returns a valid path if a data package is installed, None otherwise
    if path is not None:
        assert path.exists()


def test_load_missing_cache_raises_file_not_found() -> None:
    with pytest.raises(FileNotFoundError, match="Cache file not found"):
        load(FFMpegFilter, "nonexistent_id_that_does_not_exist")


def test_load_from_cache() -> None:
    from ..schema import FFMpegOption

    # Loads from local cache (dev) or data package (installed)
    options = load(list[FFMpegOption], "options")
    assert len(options) > 0
