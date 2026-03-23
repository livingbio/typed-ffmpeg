from ffmpeg_core.versions import available, default


def test_available_returns_list() -> None:
    result = available()
    assert isinstance(result, list)
    # In the workspace environment, at least v8 should be available
    assert len(result) >= 1


def test_available_is_sorted() -> None:
    result = available()
    assert result == sorted(result)


def test_default_returns_latest() -> None:
    result = default()
    assert result is not None
    versions = available()
    assert result == versions[-1]
