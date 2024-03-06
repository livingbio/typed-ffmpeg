from ...common.schema import FFMpegFilter
from ..cache import load, save


def test_save_and_load() -> None:
    ffmpeg_filter = FFMpegFilter(name="foo", description="bar")
    save(ffmpeg_filter, ffmpeg_filter.name)

    assert load(FFMpegFilter, ffmpeg_filter.name) == ffmpeg_filter
