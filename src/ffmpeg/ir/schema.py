"""
Intermediate Representation (IR) schema for typed-ffmpeg.

This module defines language-agnostic data structures that represent
FFmpeg filter graphs in a way that can be consumed by multiple backends
(CLI, TypeScript, JSON, etc.).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class IRStreamType(Enum):
    """Type of media stream in the IR."""

    VIDEO = "video"
    AUDIO = "audio"
    SUBTITLE = "subtitle"
    ATTACHMENT = "attachment"
    DATA = "data"


@dataclass(frozen=True)
class IRStream:
    """
    Represents a stream in the intermediate representation.

    A stream is a connection between nodes, carrying media data of a specific type.
    Streams are uniquely identified and may carry metadata about their properties.
    """

    id: str = ""
    """Unique identifier for this stream."""

    type: IRStreamType = IRStreamType.VIDEO
    """Type of media carried by this stream."""

    optional: bool = False
    """Whether this stream is optional in the graph."""

    metadata: dict[str, Any] = field(default_factory=dict)
    """Additional metadata about the stream."""


@dataclass(frozen=True)
class IRNode:
    """
    Base class for all IR nodes.

    Nodes represent operations or endpoints in the filter graph.
    Each node has inputs, outputs, and optional metadata.
    """

    id: str = ""
    """Unique identifier for this node."""

    inputs: tuple[IRStream, ...] = field(default_factory=tuple)
    """Input streams consumed by this node."""

    outputs: tuple[IRStream, ...] = field(default_factory=tuple)
    """Output streams produced by this node."""

    metadata: dict[str, Any] = field(default_factory=dict)
    """Additional metadata about the node."""


@dataclass(frozen=True)
class IRInputNode(IRNode):
    """
    Represents an input source (file, stream, device, etc.).

    Input nodes are the entry points of the filter graph,
    providing media streams from external sources.
    """

    source: str = ""
    """Source identifier (file path, URL, device name, etc.)."""

    format: str | None = None
    """Input format (e.g., 'mp4', 'rawvideo'). None means auto-detect."""

    options: dict[str, Any] = field(default_factory=dict)
    """Input-specific options (e.g., framerate, pixel_format)."""


@dataclass(frozen=True)
class IRFilterNode(IRNode):
    """
    Represents a filter operation.

    Filter nodes transform media streams according to the specified
    filter name and parameters.
    """

    filter_name: str = ""
    """Name of the FFmpeg filter (e.g., 'hflip', 'scale', 'concat')."""

    params: dict[str, Any] = field(default_factory=dict)
    """Filter parameters (e.g., {'width': 1920, 'height': 1080})."""


@dataclass(frozen=True)
class IROutputNode(IRNode):
    """
    Represents an output destination (file, stream, etc.).

    Output nodes are the exit points of the filter graph,
    writing media streams to external destinations.
    """

    destination: str = ""
    """Destination identifier (file path, URL, device name, etc.)."""

    format: str | None = None
    """Output format (e.g., 'mp4', 'webm'). None means auto-detect."""

    codec_options: dict[str, Any] = field(default_factory=dict)
    """Codec-specific options (e.g., video_codec, audio_codec, bitrate)."""

    mux_options: dict[str, Any] = field(default_factory=dict)
    """Muxer-specific options (e.g., movflags, segment_time)."""


@dataclass(frozen=True)
class IRGraph:
    """
    Complete intermediate representation of a filter graph.

    An IRGraph contains all inputs, filters, outputs, and global options
    needed to generate a complete FFmpeg command or equivalent code.
    """

    inputs: tuple[IRInputNode, ...] = field(default_factory=tuple)
    """All input nodes in the graph."""

    filters: tuple[IRFilterNode, ...] = field(default_factory=tuple)
    """All filter nodes in the graph."""

    outputs: tuple[IROutputNode, ...] = field(default_factory=tuple)
    """All output nodes in the graph."""

    global_options: dict[str, Any] = field(default_factory=dict)
    """Global FFmpeg options (e.g., loglevel, overwrite)."""

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize the IR graph to a dictionary.

        Returns:
            Dictionary representation of the graph suitable for JSON serialization.

        """
        return {
            "inputs": [self._node_to_dict(n) for n in self.inputs],
            "filters": [self._node_to_dict(n) for n in self.filters],
            "outputs": [self._node_to_dict(n) for n in self.outputs],
            "global_options": self.global_options,
        }

    @staticmethod
    def _node_to_dict(node: IRNode) -> dict[str, Any]:
        """Convert an IR node to dictionary representation."""
        result: dict[str, Any] = {
            "id": node.id,
            "inputs": [
                {"id": s.id, "type": s.type.value, "optional": s.optional}
                for s in node.inputs
            ],
            "outputs": [
                {"id": s.id, "type": s.type.value, "optional": s.optional}
                for s in node.outputs
            ],
            "metadata": node.metadata,
        }

        if isinstance(node, IRInputNode):
            result["type"] = "input"
            result["source"] = node.source
            result["format"] = node.format
            result["options"] = node.options
        elif isinstance(node, IRFilterNode):
            result["type"] = "filter"
            result["filter_name"] = node.filter_name
            result["params"] = node.params
        elif isinstance(node, IROutputNode):
            result["type"] = "output"
            result["destination"] = node.destination
            result["format"] = node.format
            result["codec_options"] = node.codec_options
            result["mux_options"] = node.mux_options

        return result

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> IRGraph:
        """
        Deserialize an IR graph from a dictionary.

        Args:
            data: Dictionary representation of the graph.

        Returns:
            IRGraph instance reconstructed from the dictionary.

        """

        def stream_from_dict(s: dict[str, Any]) -> IRStream:
            return IRStream(
                id=s["id"],
                type=IRStreamType(s["type"]),
                optional=s.get("optional", False),
            )

        def node_from_dict(n: dict[str, Any]) -> IRNode:
            inputs = tuple(stream_from_dict(s) for s in n.get("inputs", []))
            outputs = tuple(stream_from_dict(s) for s in n.get("outputs", []))
            metadata = n.get("metadata", {})
            node_id = n["id"]

            if n["type"] == "input":
                return IRInputNode(
                    id=node_id,
                    inputs=inputs,
                    outputs=outputs,
                    metadata=metadata,
                    source=n["source"],
                    format=n.get("format"),
                    options=n.get("options", {}),
                )
            elif n["type"] == "filter":
                return IRFilterNode(
                    id=node_id,
                    inputs=inputs,
                    outputs=outputs,
                    metadata=metadata,
                    filter_name=n["filter_name"],
                    params=n.get("params", {}),
                )
            elif n["type"] == "output":
                return IROutputNode(
                    id=node_id,
                    inputs=inputs,
                    outputs=outputs,
                    metadata=metadata,
                    destination=n["destination"],
                    format=n.get("format"),
                    codec_options=n.get("codec_options", {}),
                    mux_options=n.get("mux_options", {}),
                )
            else:
                raise ValueError(f"Unknown node type: {n['type']}")

        return cls(
            inputs=tuple(node_from_dict(n) for n in data.get("inputs", [])),  # type: ignore
            filters=tuple(node_from_dict(n) for n in data.get("filters", [])),  # type: ignore
            outputs=tuple(node_from_dict(n) for n in data.get("outputs", [])),  # type: ignore
            global_options=data.get("global_options", {}),
        )
