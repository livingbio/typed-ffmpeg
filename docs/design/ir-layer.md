# Intermediate Representation (IR) Layer Design

## Overview

This document describes the design and implementation of an Intermediate Representation (IR) layer for typed-ffmpeg. The IR layer sits between the DAG (Directed Acyclic Graph) representation and the backend code generation, enabling support for multiple language backends (Python, TypeScript, etc.) while maintaining a single source of truth for filter graph semantics.

## Motivation

Currently, typed-ffmpeg directly compiles from DAG nodes to FFmpeg command-line arguments. While this works well for Python, it makes supporting additional language backends challenging because:

1. **Backend-specific logic is mixed with graph semantics** - Compilation logic contains both graph traversal/validation and CLI formatting
2. **No abstraction boundary** - Direct coupling between DAG and CLI prevents reuse for other targets
3. **Limited extensibility** - Adding TypeScript or other backends requires duplicating graph logic

## Architecture

```
┌──────────────────┐
│   User Code      │
│  (Python API)    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   DAG Layer      │  ← Existing: Node, Stream, FilterNode, etc.
│  (Graph Model)   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   IR Layer       │  ← NEW: Language-agnostic intermediate form
│  (Semantic)      │
└────────┬─────────┘
         │
         ├─────────────┬──────────────┬──────────────┐
         ▼             ▼              ▼              ▼
    ┌────────┐   ┌──────────┐   ┌──────────┐   ┌─────────┐
    │  CLI   │   │TypeScript│   │   JSON   │   │  Future │
    │Backend │   │ Backend  │   │ Backend  │   │Backends │
    └────────┘   └──────────┘   └──────────┘   └─────────┘
```

## IR Data Structures

### Core IR Types

```python
from dataclasses import dataclass
from typing import Literal, Any
from enum import Enum

class IRStreamType(Enum):
    """Stream type in IR."""
    VIDEO = "video"
    AUDIO = "audio"
    SUBTITLE = "subtitle"
    ATTACHMENT = "attachment"
    DATA = "data"

@dataclass(frozen=True)
class IRStream:
    """Represents a stream in the IR."""
    id: str  # Unique identifier for this stream
    type: IRStreamType
    optional: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class IRNode:
    """Base class for all IR nodes."""
    id: str  # Unique identifier
    inputs: tuple[IRStream, ...]
    outputs: tuple[IRStream, ...]
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class IRInputNode(IRNode):
    """Represents an input file or stream."""
    source: str  # File path or URL
    format: str | None = None
    options: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class IRFilterNode(IRNode):
    """Represents a filter operation."""
    filter_name: str
    params: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class IROutputNode(IRNode):
    """Represents an output file or stream."""
    destination: str
    format: str | None = None
    codec_options: dict[str, Any] = field(default_factory=dict)
    mux_options: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class IRGraph:
    """Complete intermediate representation of a filter graph."""
    inputs: tuple[IRInputNode, ...]
    filters: tuple[IRFilterNode, ...]
    outputs: tuple[IROutputNode, ...]
    global_options: dict[str, Any] = field(default_factory=dict)
    
    def validate(self) -> list[str]:
        """Validate the IR graph and return list of errors."""
        ...
    
    def to_dict(self) -> dict:
        """Serialize to dictionary format."""
        ...
    
    @classmethod
    def from_dict(cls, data: dict) -> 'IRGraph':
        """Deserialize from dictionary format."""
        ...
```

## Conversion: DAG → IR

The conversion process transforms the existing DAG representation into the IR:

```python
class DAGToIRConverter:
    """Converts DAG nodes to IR representation."""
    
    def convert(self, node: Node) -> IRGraph:
        """
        Convert a DAG node (typically GlobalNode or OutputNode) to IR.
        
        This traverses the entire graph starting from the output node,
        collecting all inputs, filters, and outputs.
        """
        ...
    
    def _convert_node(self, node: Node, stream_map: dict) -> IRNode:
        """Convert a single DAG node to IR node."""
        if isinstance(node, InputNode):
            return self._convert_input(node, stream_map)
        elif isinstance(node, FilterNode):
            return self._convert_filter(node, stream_map)
        elif isinstance(node, OutputNode):
            return self._convert_output(node, stream_map)
        ...
```

## Backend Interface

Each backend implements a common interface:

```python
from abc import ABC, abstractmethod

class IRBackend(ABC):
    """Base class for all IR backends."""
    
    @abstractmethod
    def generate(self, ir: IRGraph) -> Any:
        """
        Generate backend-specific output from IR.
        
        Returns:
            Backend-specific representation (list[str] for CLI, str for code, etc.)
        """
        ...
    
    @abstractmethod
    def validate(self, ir: IRGraph) -> list[str]:
        """
        Validate IR for this specific backend.
        
        Returns:
            List of validation errors (empty if valid)
        """
        ...

class CLIBackend(IRBackend):
    """Generates FFmpeg command-line arguments."""
    
    def generate(self, ir: IRGraph) -> list[str]:
        """Generate FFmpeg CLI arguments from IR."""
        ...

class TypeScriptBackend(IRBackend):
    """Generates TypeScript code for fluent-ffmpeg."""
    
    def generate(self, ir: IRGraph) -> str:
        """Generate TypeScript code from IR."""
        ...

class JSONBackend(IRBackend):
    """Generates JSON representation (already exists, but can use IR)."""
    
    def generate(self, ir: IRGraph) -> dict:
        """Generate JSON from IR."""
        return ir.to_dict()
```

## Integration with Existing Code

### Minimal Changes to Public API

The public API remains unchanged. Internally, compilation flows through IR:

```python
# In runnable.py
def compile(self, ...) -> list[str]:
    """Build command-line arguments for invoking FFmpeg."""
    # OLD: compile_as_list(self._global_node().stream(), ...)
    
    # NEW:
    from ..ir.converter import DAGToIRConverter
    from ..ir.backends.cli import CLIBackend
    
    converter = DAGToIRConverter()
    ir_graph = converter.convert(self._global_node())
    backend = CLIBackend()
    return cmd + backend.generate(ir_graph)
```

### Migration Strategy

1. **Phase 1**: Implement IR layer alongside existing compilation
   - Add IR module structure
   - Implement DAG→IR conversion
   - Implement CLI backend using IR
   - Keep existing compilation as fallback

2. **Phase 2**: Validate IR implementation
   - Add comprehensive tests comparing IR vs. direct compilation
   - Ensure feature parity
   - Fix edge cases

3. **Phase 3**: Switch to IR by default
   - Make IR the default compilation path
   - Keep old path behind feature flag for one release
   - Update documentation

4. **Phase 4**: Add new backends
   - Implement TypeScript backend
   - Implement other backends as needed
   - Remove old compilation path

## Benefits

1. **Separation of Concerns**
   - Graph semantics (DAG) vs. serialization (IR) vs. target generation (Backends)
   - Each layer has clear responsibility

2. **Multi-language Support**
   - Single IR enables multiple target languages
   - TypeScript, Rust, Go, etc. can all consume the same IR

3. **Testing & Validation**
   - IR can be validated independently
   - Backend-specific validation is isolated
   - Easier to test edge cases

4. **Serialization**
   - IR naturally serializes to JSON
   - Enables saving/loading filter graphs
   - Facilitates debugging and visualization

5. **Optimization Opportunities**
   - IR can be optimized before backend generation
   - Common optimizations benefit all backends

## Examples

### Example 1: Simple Filter Chain

```python
# User code (unchanged)
f = ffmpeg.input("input.mp4").hflip().output("output.mp4")

# Generated IR (internal)
IRGraph(
    inputs=(
        IRInputNode(
            id="input_0",
            source="input.mp4",
            inputs=(),
            outputs=(IRStream(id="0:v", type=IRStreamType.VIDEO),)
        ),
    ),
    filters=(
        IRFilterNode(
            id="filter_0",
            filter_name="hflip",
            inputs=(IRStream(id="0:v", type=IRStreamType.VIDEO),),
            outputs=(IRStream(id="filter_0_out", type=IRStreamType.VIDEO),),
            params={}
        ),
    ),
    outputs=(
        IROutputNode(
            id="output_0",
            destination="output.mp4",
            inputs=(IRStream(id="filter_0_out", type=IRStreamType.VIDEO),),
            outputs=()
        ),
    )
)

# CLI Backend output: ["ffmpeg", "-i", "input.mp4", "-vf", "hflip", "output.mp4"]
# TypeScript Backend output: "ffmpeg('input.mp4').videoFilter('hflip').output('output.mp4')"
```

## File Structure

```
src/ffmpeg/
├── dag/              # Existing DAG layer
├── ir/               # NEW: IR layer
│   ├── __init__.py
│   ├── schema.py     # IR data structures
│   ├── converter.py  # DAG → IR conversion
│   ├── validator.py  # IR validation
│   ├── backends/
│   │   ├── __init__.py
│   │   ├── base.py       # IRBackend abstract class
│   │   ├── cli.py        # CLI backend (refactored from compile/)
│   │   ├── typescript.py # TypeScript backend
│   │   └── json.py       # JSON backend
│   └── tests/
│       ├── test_schema.py
│       ├── test_converter.py
│       ├── test_validator.py
│       └── test_backends.py
└── compile/          # Existing compile module (to be refactored)
```

## Backward Compatibility

- **Public API**: No changes to user-facing API
- **Internal API**: Existing compile functions will call IR layer internally
- **Feature Flags**: `use_ir_backend=True` parameter for opt-in during migration
- **Deprecation Path**: Old compilation will be deprecated after one stable release

## Future Extensions

1. **Optimization Pass**: Add IR optimization layer between converter and backend
2. **More Backends**: Rust, Go, Java, etc.
3. **IR Tooling**: Standalone tools for IR manipulation, visualization, validation
4. **Cross-language Testing**: Generate test cases from IR for all backends

## References

- Existing compile module: `src/ffmpeg/compile/`
- DAG schema: `src/ffmpeg/dag/schema.py`
- Filter definitions: `src/ffmpeg/common/schema.py`
