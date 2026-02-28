# Large FilterGraph Issue Tracker

This document tracks the recursion limit and performance issues that occur when building very large filter graphs with the typed-ffmpeg package, specifically with chains of drawtext filters.

## Issue Description

The typed-ffmpeg package currently has both recursion limit and performance issues when working with very large filter graphs. This is demonstrated by the following example:

```python
import ffmpeg
import sys
f = ffmpeg.input("in.mp4")
sys.setrecursionlimit(50000)

# Increase loop count to exceed system argument limit (e.g., 5000+ on Linux)
for _ in range(5000):
    f = f.drawtext(
        text="123",
        x="100",
        y="100",
        fontsize=100,
        fontcolor="red",
    )
f = f.output(filename="out.mp4")
f.run()
```

## Root Cause Analysis

Based on code analysis, the issue stems from several factors:

### 1. Deep Filter Chain Recursion
- The `_collect` function in `src/ffmpeg/compile/context.py` recursively traverses the DAG
- With 5000+ drawtext filters, this creates a very deep call stack
- Python's default recursion limit (typically 1000) is exceeded

### 2. Filter Graph Compilation Performance
- The `compile_as_list` function processes all filter nodes
- With thousands of filters, string concatenation and processing becomes expensive
- O(n²) or worse complexity in graph compilation

### 3. Stream Label Generation
- Each filter node generates stream labels
- With 5000+ filters, this creates a massive filter complex string
- Memory usage grows linearly with filter count

### 4. DAG Context Building
- The `DAGContext.build` method recursively collects all nodes and streams
- Becomes very expensive with large filter graphs
- Memory usage scales with graph size

### 5. System Argument Limits
- Linux has a command line argument limit (typically 131072 bytes)
- Large filter complex strings can exceed this limit
- Causes "Argument list too long" errors

## Test Suite

A comprehensive test suite has been created to track these issues:

### Test File: `src/ffmpeg/tests/test_large_filtergraph.py`

The test suite includes:

1. **Recursion Limit Tests**
   - Tests that large drawtext chains don't exceed recursion limit
   - Tests with 100, 1000, and 5000+ filters
   - Validates that compilation doesn't cause RecursionError

2. **Performance Tests**
   - Measures compilation time for different filter chain sizes
   - Ensures performance doesn't degrade exponentially
   - Tests with 10, 100, and 500 filters

3. **Command Length Tests**
   - Validates that generated commands don't become excessively long
   - Checks against system argument limits
   - Tests with various chain sizes

4. **Edge Case Tests**
   - Reproduces the exact scenario from the example above
   - Tests with high recursion limits
   - Validates specific failure conditions

### Test Configuration

Tests are designed to be skippable to avoid affecting CI results:

```bash
# Disable tests (default behavior)
# No environment variable needed - tests are skipped by default

# Enable tests for development/debugging
export RUN_LARGE_FILTERGRAPH_TESTS=true
```

## Usage

### Running the Demo

```bash
# Run the demonstration script
python scripts/test_large_filtergraph_demo.py
```

This will:
1. Test filter chains of increasing size (10, 100, 500, 1000 filters)
2. Measure compilation time and command length
3. Identify when recursion or performance issues occur
4. Run the test suite if pytest is available

### Running Tests

```bash
# Run specific test file (tests will be skipped by default)
pytest src/ffmpeg/tests/test_large_filtergraph.py -v

# Run with tests enabled
RUN_LARGE_FILTERGRAPH_TESTS=true pytest src/ffmpeg/tests/test_large_filtergraph.py -v
```

### Running Individual Tests

```bash
# Test recursion limit
pytest src/ffmpeg/tests/test_large_filtergraph.py::TestLargeFilterGraphIssues::test_recursion_limit_with_drawtext_chain -v

# Test performance
pytest src/ffmpeg/tests/test_large_filtergraph.py::TestLargeFilterGraphIssues::test_performance_with_large_filter_graph -v

# Test command length
pytest src/ffmpeg/tests/test_large_filtergraph.py::TestLargeFilterGraphIssues::test_command_length_with_large_filter_graph -v
```

## Expected Behavior

### Current Behavior (Issues Present)
- RecursionError with chains of 1000+ filters
- Exponential performance degradation
- Command length exceeding system limits
- Memory usage growing excessively

### Target Behavior (After Fix)
- No RecursionError with any reasonable filter count
- Linear or sub-linear performance scaling
- Command length within system limits
- Reasonable memory usage

## Potential Solutions

### 1. Iterative DAG Traversal
Replace recursive `_collect` function with iterative approach:
```python
def _collect_iterative(node: Node) -> tuple[list[Node], list[Stream]]:
    """Iterative version of _collect to avoid recursion."""
    nodes = []
    streams = []
    stack = [node]
    visited = set()
    
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        nodes.append(current)
        streams.extend(current.inputs)
        stack.extend(stream.node for stream in current.inputs)
    
    return nodes, streams
```

### 2. Optimized Filter Graph Compilation
- Use string builders instead of concatenation
- Batch process filter nodes
- Implement lazy evaluation for large graphs

### 3. Stream Label Optimization
- Use shorter, more efficient labels
- Implement label compression
- Consider using filter complex scripts for very large graphs

### 4. Memory Management
- Implement object pooling for filter nodes
- Use weak references where appropriate
- Add garbage collection hints

## Monitoring Progress

The test suite provides metrics to track progress:

1. **Recursion Limit**: Tests pass when no RecursionError occurs
2. **Performance**: Compilation time scales linearly with filter count
3. **Command Length**: Generated commands stay within system limits
4. **Memory Usage**: Memory consumption remains reasonable

## Contributing

When working on fixing this issue:

1. Run the test suite before making changes
2. Implement fixes incrementally
3. Test with various filter chain sizes
4. Monitor performance metrics
5. Update this document with progress

## Related Issues

- [Issue #XXX] - Recursion limit exceeded with large filter graphs
- [Issue #XXX] - Performance degradation with thousands of filters
- [Issue #XXX] - System argument limit exceeded on Linux

## References

- [FFmpeg Filter Complex Documentation](https://ffmpeg.org/ffmpeg-filters.html#Filtergraph-syntax-1)
- [Python Recursion Limit](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit)
- [Linux Argument List Limits](https://man7.org/linux/man-pages/man2/execve.2.html) 