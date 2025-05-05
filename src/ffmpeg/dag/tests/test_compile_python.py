from syrupy.assertion import SnapshotAssertion

from ffmpeg import filters, input

from ..compile_python import compile_python


def test_compile_python(snapshot: SnapshotAssertion) -> None:
    assert snapshot == compile_python(
        filters.concat(
            input("input.mp4").trim(start=10, end=20).trim(start=30, end=40),
            input("input2.mp4").trim(start=50, end=60),
        ).video(0)
    )
