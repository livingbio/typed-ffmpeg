"""
Directed Acyclic Graph (DAG) implementation for FFmpeg filter chains.

This package provides the core components for representing FFmpeg filter chains
as directed acyclic graphs. It includes classes for different types of nodes
(inputs, filters, outputs) and streams, as well as utilities for validating,
compiling, and manipulating these graphs.

The DAG structure enables type-safe construction and validation of complex
FFmpeg filter chains, ensuring that the resulting FFmpeg commands are valid
and correctly structured.
"""

from .nodes import (
    FilterableStream,
    FilterNode,
    GlobalNode,
    InputNode,
    OutputNode,
    OutputStream,
)
from .schema import Node, Stream

__all__ = [
    "Node",
    "Stream",
    "FilterableStream",
    "FilterNode",
    "GlobalNode",
    "InputNode",
    "OutputNode",
    "OutputStream",
]
