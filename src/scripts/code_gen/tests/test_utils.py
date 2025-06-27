from pathlib import Path

from ..utils import get_relative_import, get_relative_path


def test_get_relative_path() -> None:
    print(
        "types/options/framesync:",
        get_relative_path("types", "options/framesync.py.jinja"),
    )
    assert get_relative_path("types", "options/framesync.py.jinja") == "..types"
    print(
        "types/dag/global_runnable/global_args:",
        get_relative_path("types", "dag/global_runnable/global_args.py.jinja"),
    )
    assert (
        get_relative_path("types", "dag/global_runnable/global_args.py.jinja")
        == "...types"
    )
    print(
        "streams.audio/streams/audio:",
        get_relative_path("streams.audio", "streams/audio.py.jinja"),
    )
    assert get_relative_path("streams.audio", "streams/audio.py.jinja") is None
    print(
        "streams.video/streams/audio:",
        get_relative_path("streams.video", "streams/audio.py.jinja"),
    )
    assert get_relative_path("streams.video", "streams/audio.py.jinja") == ".video"
    print("dag.nodes/filters:", get_relative_path("dag.nodes", "filters.py.jinja"))
    assert get_relative_path("dag.nodes", "filters.py.jinja") == ".dag.nodes"
    print(
        "dag.nodes/streams.audio:",
        get_relative_path("dag.nodes", "streams.audio.py.jinja"),
    )
    print("import_path_obj.parts:", Path("dag/nodes").parts)
    assert get_relative_path("dag.nodes", "streams.audio.py.jinja") == "..dag.nodes"
    # New test case: importing from nested directory to root-level module
    print("types/streams/audio:", get_relative_path("types", "streams/audio.py.jinja"))
    assert get_relative_path("types", "streams/audio.py.jinja") == "..types"
    # New test case: importing between different root-level modules
    print(
        "filters/streams/audio:", get_relative_path("filters", "streams/audio.py.jinja")
    )
    assert get_relative_path("filters", "streams/audio.py.jinja") == "..filters"


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
