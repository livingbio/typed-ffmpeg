from importlib.resources import files


def test_py_typed_marker() -> None:
    # Without the PEP 561 marker mypy treats ffmpeg_core as untyped, so names
    # re-exported through ffmpeg.expressions / ffmpeg.types are unresolved.
    assert files("ffmpeg_core").joinpath("py.typed").is_file()
