from ..utils import get_relative_path


def test_get_relative_path() -> None:
    assert get_relative_path("types", "options/framesync.py.jinja") == "..types"
    assert (
        get_relative_path("types", "dag/global_runnable/global_args.py.jinja")
        == "...types"
    )
