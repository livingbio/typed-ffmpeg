from syrupy.assertion import SnapshotAssertion

from ffmpeg.common.schema import FFMpegFilter

from ..cache import list_all, load, save


def test_save_and_load(snapshot: SnapshotAssertion) -> None:
    ffmpeg_filter = FFMpegFilter(name="foo", description="bar")
    save(ffmpeg_filter, ffmpeg_filter.name)

    assert load(FFMpegFilter, ffmpeg_filter.name) == ffmpeg_filter

    assert snapshot == list_all(FFMpegFilter)
