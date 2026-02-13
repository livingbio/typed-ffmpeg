"""Tests for FFmpeg filter graph visualization utilities."""

import pytest

import ffmpeg
from ..view import _get_node_color, view
from ...dag.nodes import InputNode
from ...utils.frozendict import FrozenDict


def test_get_node_color_input() -> None:
    """Test color assignment for InputNode."""
    input_node = InputNode(filename="input.mp4", kwargs=FrozenDict({}))
    color = _get_node_color(input_node)
    assert color == "#99cc00"


def test_get_node_color_with_real_nodes() -> None:
    """Test color assignment with real filter graph nodes."""
    # Create a simple filter graph
    output = ffmpeg.input("input.mp4").video.output(filename="output.mp4")

    # Test that we can get colors for different node types
    # This exercises the _get_node_color function indirectly through view
    try:
        import graphviz  # type: ignore # noqa: F401

        result = view(output, format="dot")
        assert isinstance(result, str)
    except ImportError:
        pytest.skip("graphviz not installed")


def test_view_requires_graphviz() -> None:
    """Test that view() raises ImportError if graphviz is not available."""
    output = ffmpeg.input("input.mp4").output(filename="output.mp4")

    # Try to import graphviz to see if it's available
    try:
        import graphviz  # type: ignore # noqa: F401

        # If graphviz is available, test that view works
        result = view(output, format="dot")
        assert isinstance(result, str)
    except ImportError:
        # If graphviz is not available, test that view raises ImportError
        with pytest.raises(ImportError) as exc_info:
            view(output, format="dot")
        assert "graphviz" in str(exc_info.value).lower()


def test_view_with_simple_graph() -> None:
    """Test view() with a simple filter graph."""
    try:
        import graphviz  # type: ignore # noqa: F401

        output = ffmpeg.input("input.mp4").output(filename="output.mp4")
        result = view(output, format="dot")
        assert isinstance(result, str)
    except ImportError:
        pytest.skip("graphviz not installed")


def test_view_with_filter_chain() -> None:
    """Test view() with a filter chain."""
    try:
        import graphviz  # type: ignore # noqa: F401

        output = (
            ffmpeg.input("input.mp4")
            .filter("scale", 1280, 720)
            .filter("fps", fps=30)
            .output(filename="output.mp4")
        )
        result = view(output, format="dot")
        assert isinstance(result, str)
    except ImportError:
        pytest.skip("graphviz not installed")


def test_view_format_options() -> None:
    """Test view() with different format options."""
    try:
        import graphviz  # type: ignore # noqa: F401

        output = ffmpeg.input("input.mp4").output(filename="output.mp4")

        # Test different format options
        for fmt in ["png", "svg", "dot"]:
            result = view(output, format=fmt)
            assert isinstance(result, str)
    except ImportError:
        pytest.skip("graphviz not installed")
