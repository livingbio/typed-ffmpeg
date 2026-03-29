from ..schema import Auto, Default, FFMpegOptionGroup


def test_default_is_str() -> None:
    d = Default("23")
    assert isinstance(d, str)
    assert d == "23"


def test_auto_is_default() -> None:
    a = Auto("len(streams)")
    assert isinstance(a, Default)
    assert isinstance(a, str)
    assert a == "len(streams)"


def test_option_group_as_av_options() -> None:
    group = FFMpegOptionGroup(
        {"crf": 23, "preset": "fast", "flag": True, "other": False, "skip": None}
    )
    result = group.as_av_options()
    assert result == {"crf": 23, "preset": "fast", "flag": 1, "other": 0}
    assert "skip" not in result


def test_option_group_as_av_options_empty() -> None:
    group = FFMpegOptionGroup()
    assert group.as_av_options() == {}
