# Add Intermediate Representation (IR) Layer for Multi-Backend Support

## 🎯 Overview

This PR introduces an **Intermediate Representation (IR) layer** to typed-ffmpeg, establishing a foundation for supporting multiple language backends (TypeScript, JSON, etc.) while maintaining a single source of truth for FFmpeg filter graph semantics.

## 🏗️ Architecture

The IR layer sits between the existing DAG (Directed Acyclic Graph) representation and backend code generation:

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

## 📦 What's Included

### 1. IR Schema (`src/ffmpeg/ir/schema.py`)
- **IRStream**: Represents connections between nodes
- **IRNode**: Base class for all operations
- **IRInputNode**: Input sources (files, streams, devices)
- **IRFilterNode**: Filter operations with parameters
- **IROutputNode**: Output destinations
- **IRGraph**: Complete filter graph representation

All IR types support:
- JSON serialization/deserialization
- Immutability (frozen dataclasses)
- Rich metadata support

### 2. Converter Stub (`src/ffmpeg/ir/converter.py`)
- **DAGToIRConverter**: Framework for converting DAG → IR
- Stream ID mapping and management
- Type inference utilities
- Ready for full implementation

### 3. Backend Framework (`src/ffmpeg/ir/backends/`)
- **IRBackend**: Abstract base class for all backends
- **CLIBackend**: Stub for FFmpeg CLI generation
- **Extensible**: Easy to add new backends (TypeScript, Rust, Go, etc.)

### 4. Comprehensive Tests (`src/ffmpeg/ir/tests/`)
- ✅ IR schema creation
- ✅ Serialization to dictionary
- ✅ Deserialization from dictionary
- ✅ Roundtrip preservation
- **8 tests, all passing**

### 5. Design Documentation (`docs/design/ir-layer.md`)
- Detailed architecture explanation
- Migration strategy (4 phases)
- Benefits and use cases
- Examples and file structure

## 🎁 Benefits

### 1. **Separation of Concerns**
- Graph semantics (DAG) vs. serialization (IR) vs. code generation (Backends)
- Each layer has clear, focused responsibility
- Easier to understand and maintain

### 2. **Multi-Language Support**
- Single IR enables multiple target languages
- TypeScript backend → Fluent-ffmpeg compatibility
- Future: Rust, Go, Java, etc.

### 3. **Better Testing**
- IR can be validated independently
- Backend-specific tests are isolated
- Easier to test edge cases

### 4. **Serialization & Portability**
- IR naturally serializes to JSON
- Save/load filter graphs
- Cross-language interoperability

### 5. **Optimization Opportunities**
- IR can be optimized before backend generation
- Common optimizations benefit all backends
- Prepare for future JIT compilation

## 🚀 Migration Strategy

This PR implements **Phase 1** of a 4-phase migration:

### Phase 1: Foundation (✅ This PR)
- ✅ Add IR module structure
- ✅ Implement IR schema
- ✅ Create converter and backend stubs
- ✅ Add comprehensive tests
- ✅ Document architecture

### Phase 2: Implementation (Future)
- Implement full DAG→IR conversion
- Implement CLIBackend using IR
- Add extensive validation
- Ensure feature parity with existing compilation

### Phase 3: Integration (Future)
- Make IR the default compilation path
- Keep old path as fallback
- Update documentation
- Gather user feedback

### Phase 4: Expansion (Future)
- Implement TypeScript backend
- Add other backends as needed
- Remove old compilation path
- Optimize IR processing

## 🔍 Example Usage (Future)

Once fully implemented, the IR layer will enable:

```python
from ffmpeg.ir.converter import DAGToIRConverter
from ffmpeg.ir.backends.cli import CLIBackend
from ffmpeg.ir.backends.typescript import TypeScriptBackend

# Build filter graph as usual
graph = ffmpeg.input("input.mp4").hflip().output("output.mp4")

# Convert to IR
converter = DAGToIRConverter()
ir = converter.convert(graph)

# Generate CLI command
cli_backend = CLIBackend()
cmd_args = cli_backend.generate(ir)  # ["ffmpeg", "-i", "input.mp4", "-vf", "hflip", "output.mp4"]

# Generate TypeScript code
ts_backend = TypeScriptBackend()
ts_code = ts_backend.generate(ir)  # "ffmpeg('input.mp4').videoFilter('hflip').output('output.mp4')"

# Serialize to JSON
json_data = ir.to_dict()
```

## 🧪 Testing

All tests pass:

```bash
$ python -m pytest src/ffmpeg/ir/tests/test_schema.py -v
============================= test session starts ==============================
...
collected 8 items

src/ffmpeg/ir/tests/test_schema.py::test_ir_stream_creation PASSED       [ 12%]
src/ffmpeg/ir/tests/test_schema.py::test_ir_input_node PASSED            [ 25%]
src/ffmpeg/ir/tests/test_schema.py::test_ir_filter_node PASSED           [ 37%]
src/ffmpeg/ir/tests/test_schema.py::test_ir_output_node PASSED           [ 50%]
src/ffmpeg/ir/tests/test_schema.py::test_ir_graph_creation PASSED        [ 62%]
src/ffmpeg/ir/tests/test_schema.py::test_ir_graph_to_dict PASSED         [ 75%]
src/ffmpeg/ir/tests/test_schema.py::test_ir_graph_from_dict PASSED       [ 87%]
src/ffmpeg/ir/tests/test_schema.py::test_ir_graph_roundtrip PASSED       [100%]

============================== 8 passed in 0.07s ===============================
```

## 🔄 Backward Compatibility

- ✅ **No changes to public API** - Users see no difference
- ✅ **No changes to existing code** - DAG and compile modules untouched
- ✅ **Purely additive** - Only adds new modules, doesn't modify existing ones
- ✅ **Zero breaking changes**

## 📚 Documentation

- **Design Document**: `docs/design/ir-layer.md` - Comprehensive architecture guide
- **Inline Documentation**: All IR classes and methods fully documented
- **Examples**: Design doc includes usage examples and migration patterns

## 🔮 Future Work

After this PR is merged, follow-up PRs will:

1. **Implement DAGToIRConverter** - Full conversion logic
2. **Implement CLIBackend** - Refactor existing compile logic
3. **Add TypeScriptBackend** - Generate fluent-ffmpeg code
4. **Add optimization passes** - Filter graph optimizations
5. **Add more backends** - Rust, Go, JSON Schema, etc.

## 🤝 Related Issues

This PR lays the groundwork for:
- Multi-language backend support
- Cross-language filter graph sharing
- Better testing infrastructure
- Future optimization opportunities

## 📝 Checklist

- [x] IR schema implemented with full type hints
- [x] All IR types are immutable (frozen dataclasses)
- [x] Serialization/deserialization working
- [x] Comprehensive test coverage
- [x] Design documentation complete
- [x] No breaking changes
- [x] All tests passing
- [x] Code follows project style (dataclasses, type hints, docstrings)

## 💬 Questions for Reviewers

1. Does the IR schema capture all necessary information for backends?
2. Is the architecture clear and maintainable?
3. Any suggestions for the DAGToIRConverter implementation approach?
4. Should we add any additional metadata fields to IR types?

---

This PR establishes a solid foundation for typed-ffmpeg's multi-backend future while maintaining full backward compatibility and code quality. 🎉
