from ..base import input


def test_trim_type() -> None:
    # trim should be able to accept time duration format
    input("input.mp4").trim(start="00:00")


def test_scale_type() -> None:
    input("input.mp4").scale(w=10)
