from syrupy.assertion import SnapshotAssertion

import ffmpeg


def test_showwavespic(snapshot: SnapshotAssertion) -> None:
    assert snapshot == (
        ffmpeg.input("test-input.mp4")
        .audio.showwavespic()
        .output(filename="pipe:", vframes=1, f="image2", vcodec="mjpeg")
        .compile_line()
    )
