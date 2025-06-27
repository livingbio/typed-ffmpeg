import pytest

from ..utils import get_relative_import, get_relative_path


@pytest.mark.parametrize(
    "import_path, template_path, expected",
    [
        ("types", "options/framesync.py.jinja", "..types"),
        ("types", "dag/global_runnable/global_args.py.jinja", "...types"),
        ("streams.audio", "streams/audio.py.jinja", None),
        ("streams.video", "streams/audio.py.jinja", ".video"),
        ("dag.nodes", "filters.py.jinja", ".dag.nodes"),
        ("dag.nodes", "streams/audio.py.jinja", "..dag.nodes"),
        ("types", "streams/audio.py.jinja", "..types"),
        ("filters", "streams/audio.py.jinja", "..filters"),
        ("dag.nodes", "dag/io/_input.py.jinja", "..nodes"),
    ],
)
def test_get_relative_path(
    import_path: str, template_path: str, expected: str | None
) -> None:
    assert get_relative_path(import_path, template_path) == expected


def test_get_relative_import() -> None:
    # Test normal import
    result = get_relative_import(
        "types", "options/framesync.py.jinja", "Binary, Boolean"
    )
    assert result == "from ..types import Binary, Boolean"

    # Test same file import (should return empty string)
    result = get_relative_import(
        "streams.audio", "streams/audio.py.jinja", "AudioStream"
    )
    assert result == ""

    # Test nested import
    result = get_relative_import("dag.nodes", "streams/audio.py.jinja", "FilterNode")
    assert result == "from ..dag.nodes import FilterNode"
