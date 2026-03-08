from ..cli import parse_ffmpeg_options, pre_compile


def test_pre_compile() -> None:
    pre_compile()


def test_parse_ffmpeg_options() -> None:
    assert len(parse_ffmpeg_options()) > 0
