"""
Intermediate Representation (IR) layer for typed-ffmpeg.

This package provides a language-agnostic intermediate representation
of FFmpeg filter graphs, enabling support for multiple backend targets
(CLI, TypeScript, JSON, etc.).

The IR layer sits between the DAG (Directed Acyclic Graph) layer and
the backend code generation, providing:

1. Separation of graph semantics from code generation
2. Multi-language backend support
3. Independent validation and optimization
4. Serialization and deserialization

Example:
    ```python
    from ffmpeg.ir.converter import DAGToIRConverter
    from ffmpeg.ir.backends.cli import CLIBackend

    # Convert DAG to IR
    converter = DAGToIRConverter()
    ir_graph = converter.convert(dag_node)

    # Generate CLI output
    backend = CLIBackend()
    cmd_args = backend.generate(ir_graph)
    ```

"""

from .schema import (
    IRFilterNode,
    IRGraph,
    IRInputNode,
    IRNode,
    IROutputNode,
    IRStream,
    IRStreamType,
)

__all__ = [
    "IRGraph",
    "IRNode",
    "IRInputNode",
    "IRFilterNode",
    "IROutputNode",
    "IRStream",
    "IRStreamType",
]
