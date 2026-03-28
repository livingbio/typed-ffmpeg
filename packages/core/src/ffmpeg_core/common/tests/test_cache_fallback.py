import pytest

from ..cache import _get_data_cache_path, load
from ..schema import FFMpegFilter


def test_get_data_cache_path_returns_path() -> None:
    path = _get_data_cache_path()
    # In dev workspace at least one ffmpeg_data_vN is installed
    assert path is not None
    assert path.exists()


def test_load_missing_cache_raises_file_not_found() -> None:
    with pytest.raises(FileNotFoundError, match="Cache file not found"):
        load(FFMpegFilter, "nonexistent_id_that_does_not_exist")


def test_load_from_data_package() -> None:
    from ..schema import FFMpegOption

    # This loads from the data package since core wheel excludes list/*.json
    options = load(list[FFMpegOption], "options")
    assert len(options) > 0
