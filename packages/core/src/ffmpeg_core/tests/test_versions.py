from ffmpeg_core.versions import available, default


def test_available_returns_list() -> None:
    result = available()
    assert isinstance(result, list)
    # All entries should be valid version strings
    for v in result:
        assert v.isdigit()


def test_available_is_sorted() -> None:
    result = available()
    assert result == sorted(result)


def test_default_returns_latest_or_none() -> None:
    result = default()
    versions = available()
    if versions:
        assert result == versions[-1]
    else:
        # No version packages installed (e.g., core tested in isolation)
        assert result is None
