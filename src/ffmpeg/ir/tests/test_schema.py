"""Tests for IR schema."""

import pytest

from ..schema import (
    IRFilterNode,
    IRGraph,
    IRInputNode,
    IROutputNode,
    IRStream,
    IRStreamType,
)


def test_ir_stream_creation():
    """Test creating an IR stream."""
    stream = IRStream(
        id="stream_0",
        type=IRStreamType.VIDEO,
        optional=False,
    )
    assert stream.id == "stream_0"
    assert stream.type == IRStreamType.VIDEO
    assert not stream.optional
    assert stream.metadata == {}


def test_ir_input_node():
    """Test creating an IR input node."""
    output_stream = IRStream(id="0:v", type=IRStreamType.VIDEO)
    node = IRInputNode(
        id="input_0",
        source="input.mp4",
        outputs=(output_stream,),
        format="mp4",
        options={"framerate": 30},
    )
    assert node.id == "input_0"
    assert node.source == "input.mp4"
    assert node.format == "mp4"
    assert node.options == {"framerate": 30}
    assert len(node.outputs) == 1
    assert node.outputs[0] == output_stream


def test_ir_filter_node():
    """Test creating an IR filter node."""
    input_stream = IRStream(id="0:v", type=IRStreamType.VIDEO)
    output_stream = IRStream(id="filter_0_out", type=IRStreamType.VIDEO)
    node = IRFilterNode(
        id="filter_0",
        filter_name="hflip",
        inputs=(input_stream,),
        outputs=(output_stream,),
        params={},
    )
    assert node.id == "filter_0"
    assert node.filter_name == "hflip"
    assert len(node.inputs) == 1
    assert len(node.outputs) == 1


def test_ir_output_node():
    """Test creating an IR output node."""
    input_stream = IRStream(id="filter_0_out", type=IRStreamType.VIDEO)
    node = IROutputNode(
        id="output_0",
        destination="output.mp4",
        inputs=(input_stream,),
        codec_options={"video_codec": "libx264"},
    )
    assert node.id == "output_0"
    assert node.destination == "output.mp4"
    assert node.codec_options == {"video_codec": "libx264"}


def test_ir_graph_creation():
    """Test creating a complete IR graph."""
    # Create streams
    input_stream = IRStream(id="0:v", type=IRStreamType.VIDEO)
    filter_stream = IRStream(id="filter_0_out", type=IRStreamType.VIDEO)

    # Create nodes
    input_node = IRInputNode(
        id="input_0",
        source="input.mp4",
        outputs=(input_stream,),
    )
    filter_node = IRFilterNode(
        id="filter_0",
        filter_name="hflip",
        inputs=(input_stream,),
        outputs=(filter_stream,),
    )
    output_node = IROutputNode(
        id="output_0",
        destination="output.mp4",
        inputs=(filter_stream,),
    )

    # Create graph
    graph = IRGraph(
        inputs=(input_node,),
        filters=(filter_node,),
        outputs=(output_node,),
        global_options={"loglevel": "info"},
    )

    assert len(graph.inputs) == 1
    assert len(graph.filters) == 1
    assert len(graph.outputs) == 1
    assert graph.global_options == {"loglevel": "info"}


def test_ir_graph_to_dict():
    """Test serializing IR graph to dictionary."""
    input_stream = IRStream(id="0:v", type=IRStreamType.VIDEO)
    input_node = IRInputNode(
        id="input_0",
        source="input.mp4",
        outputs=(input_stream,),
    )
    graph = IRGraph(
        inputs=(input_node,),
        global_options={"loglevel": "info"},
    )

    data = graph.to_dict()
    assert "inputs" in data
    assert "filters" in data
    assert "outputs" in data
    assert "global_options" in data
    assert data["global_options"] == {"loglevel": "info"}
    assert len(data["inputs"]) == 1
    assert data["inputs"][0]["source"] == "input.mp4"


def test_ir_graph_from_dict():
    """Test deserializing IR graph from dictionary."""
    data = {
        "inputs": [
            {
                "id": "input_0",
                "type": "input",
                "source": "input.mp4",
                "format": None,
                "options": {},
                "inputs": [],
                "outputs": [{"id": "0:v", "type": "video", "optional": False}],
                "metadata": {},
            }
        ],
        "filters": [],
        "outputs": [],
        "global_options": {"loglevel": "info"},
    }

    graph = IRGraph.from_dict(data)
    assert len(graph.inputs) == 1
    assert graph.inputs[0].source == "input.mp4"
    assert graph.global_options == {"loglevel": "info"}


def test_ir_graph_roundtrip():
    """Test that to_dict/from_dict roundtrip preserves data."""
    input_stream = IRStream(id="0:v", type=IRStreamType.VIDEO)
    filter_stream = IRStream(id="filter_0_out", type=IRStreamType.VIDEO)

    graph = IRGraph(
        inputs=(
            IRInputNode(
                id="input_0",
                source="input.mp4",
                outputs=(input_stream,),
            ),
        ),
        filters=(
            IRFilterNode(
                id="filter_0",
                filter_name="hflip",
                inputs=(input_stream,),
                outputs=(filter_stream,),
            ),
        ),
        outputs=(
            IROutputNode(
                id="output_0",
                destination="output.mp4",
                inputs=(filter_stream,),
            ),
        ),
        global_options={"loglevel": "info"},
    )

    # Roundtrip
    data = graph.to_dict()
    graph2 = IRGraph.from_dict(data)

    # Verify structure is preserved
    assert len(graph2.inputs) == len(graph.inputs)
    assert len(graph2.filters) == len(graph.filters)
    assert len(graph2.outputs) == len(graph.outputs)
    assert graph2.inputs[0].source == graph.inputs[0].source
    assert graph2.filters[0].filter_name == graph.filters[0].filter_name
    assert graph2.outputs[0].destination == graph.outputs[0].destination
