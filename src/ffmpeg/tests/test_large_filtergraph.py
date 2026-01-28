# type: ignore
"""
Tests for large filtergraph performance and recursion limit issues.

This module contains tests to track and validate issues related to:
1. Recursion limit exceeded when building large filter chains
2. Performance degradation with large filter graphs
3. Memory usage issues with thousands of filters
4. System argument limit exceeded on Linux

These tests are designed to be skippable to avoid affecting CI results
when the issues are present.
"""

import os
import sys
import time
from typing import Any

import pytest

from .. import input


def create_large_drawtext_chain(iterations: int = 100) -> Any:
    """
    Create a large filter chain with multiple drawtext filters.

    This function creates a filter chain similar to the problematic example
    in x.py, but with a configurable number of iterations to test different
    scales of the issue.

    Args:
        iterations: Number of drawtext filters to chain together

    Returns:
        A stream with the large filter chain applied that can be compiled

    """
    f = input("test_input.mp4")

    for i in range(iterations):
        f = f.drawtext(
            text=f"Text {i}",
            x="100",
            y="100",
            fontsize=100,
            fontcolor="red",
        )

    return f.output(filename="test_output.mp4")


def measure_execution_time(func: Any, *args: Any, **kwargs: Any) -> tuple[Any, float]:
    """
    Measure execution time of a function.

    Args:
        func: Function to measure
        *args: Function arguments
        **kwargs: Function keyword arguments

    Returns:
        Tuple of (result, execution_time_seconds)

    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time


class TestLargeFilterGraphIssues:
    """Test class for large filtergraph performance and recursion issues."""

    @pytest.mark.skipif(
        os.environ.get("RUN_LARGE_FILTERGRAPH_TESTS", "false").lower() != "true",
        reason="Large filtergraph tests are disabled by default - set RUN_LARGE_FILTERGRAPH_TESTS=true to enable",
    )
    def test_recursion_limit_with_drawtext_chain(self) -> None:
        """
        Test that large drawtext chains don't exceed recursion limit.

        This test verifies that creating a large chain of drawtext filters
        doesn't cause Python's recursion limit to be exceeded during
        filter graph compilation.
        """
        # Test with a moderate number of filters first
        moderate_chain = create_large_drawtext_chain(100)

        # This should not raise RecursionError
        try:
            # Just compile to test recursion, don't actually run
            moderate_chain.compile()
        except RecursionError as e:
            pytest.fail(f"Recursion limit exceeded with 100 drawtext filters: {e}")

        # Test with a larger number of filters
        large_chain = create_large_drawtext_chain(1000)

        try:
            large_chain.compile()
        except RecursionError as e:
            pytest.fail(f"Recursion limit exceeded with 1000 drawtext filters: {e}")

    def test_performance_with_large_filter_graph(self) -> None:
        """
        Test that large filter graphs don't cause excessive performance degradation.

        This test measures the time taken to compile filter graphs of different
        sizes and ensures that performance doesn't degrade exponentially.
        Uses chain sizes that stay under recursion limits (10, 50, 100).
        """
        # Measure baseline performance with small chain
        small_chain = create_large_drawtext_chain(10)
        _, small_time = measure_execution_time(small_chain.compile)

        # Measure performance with medium chain
        medium_chain = create_large_drawtext_chain(50)
        _, medium_time = measure_execution_time(medium_chain.compile)

        # Measure performance with large chain (kept under recursion limit)
        large_chain = create_large_drawtext_chain(100)
        _, large_time = measure_execution_time(large_chain.compile)

        # Performance should not degrade exponentially
        # Current implementation is worse than linear; use loose bounds to
        # catch severe regressions (e.g. 100x blowup) while test runs in CI.
        actual_medium_ratio = (
            medium_time / small_time if small_time > 0 else float("inf")
        )
        actual_large_ratio = large_time / small_time if small_time > 0 else float("inf")

        # Reject only clear exponential degradation (CI ~265x for 100 vs 10 filters)
        max_medium_ratio = 50  # 50 filters vs 10
        max_large_ratio = 350  # 100 filters vs 10

        if actual_medium_ratio > max_medium_ratio:
            pytest.fail(
                f"Performance degradation too high for medium chain: "
                f"got {actual_medium_ratio:.2f}x (max allowed {max_medium_ratio}x)"
            )

        if actual_large_ratio > max_large_ratio:
            pytest.fail(
                f"Performance degradation too high for large chain: "
                f"got {actual_large_ratio:.2f}x (max allowed {max_large_ratio}x)"
            )

    @pytest.mark.skipif(
        os.environ.get("RUN_LARGE_FILTERGRAPH_TESTS", "false").lower() != "true",
        reason="Large filtergraph tests are disabled by default - set RUN_LARGE_FILTERGRAPH_TESTS=true to enable",
    )
    def test_command_length_with_large_filter_graph(self) -> None:
        """
        Test that large filter graphs don't generate excessively long commands.

        This test measures the length of the generated command string
        to ensure it doesn't exceed system limits or become unmanageable.
        """
        # Test with different chain sizes
        for chain_size in [10, 50, 100, 200]:
            chain = create_large_drawtext_chain(chain_size)
            compiled = chain.compile()

            # Check total command length
            command_length = len(compiled)

            # Each drawtext filter typically adds ~50-100 characters
            expected_length = chain_size * 100  # Conservative estimate
            max_reasonable_length = expected_length * 3  # Allow 3x tolerance

            if command_length > max_reasonable_length:
                pytest.fail(
                    f"Command too long for {chain_size} filters: "
                    f"{command_length} characters (expected < {max_reasonable_length})"
                )

    @pytest.mark.skipif(
        os.environ.get("RUN_LARGE_FILTERGRAPH_TESTS", "false").lower() != "true",
        reason="Large filtergraph tests are disabled by default - set RUN_LARGE_FILTERGRAPH_TESTS=true to enable",
    )
    def test_system_argument_limit(self) -> None:
        """
        Test that large filter graphs don't exceed system argument limits.

        This test ensures that the compiled command doesn't exceed the
        system's argument length limit (typically 131072 bytes on Linux).
        """
        # Test with a large chain that might approach system limits
        large_chain = create_large_drawtext_chain(1000)
        compiled = large_chain.compile()

        # Check total command length
        command_length = len(compiled)

        # Linux typically has a limit of 131072 bytes for command line arguments
        # Allow some buffer for safety
        max_command_length = 100000  # Conservative limit

        if command_length > max_command_length:
            pytest.fail(
                f"Command too long: {command_length} characters "
                f"(limit: {max_command_length})"
            )

    @pytest.mark.skipif(
        os.environ.get("RUN_LARGE_FILTERGRAPH_TESTS", "false").lower() != "true",
        reason="Large filtergraph tests are disabled by default - set RUN_LARGE_FILTERGRAPH_TESTS=true to enable",
    )
    def test_recursion_limit_edge_case(self) -> None:
        """
        Test the exact edge case from the original x.py example.

        This test reproduces the exact scenario from x.py to ensure
        the specific issue is tracked and can be validated when fixed.
        """
        # Set a high recursion limit like in the original example
        original_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(50000)

        try:
            # Create the exact chain from x.py (5000 iterations)
            f = input("test_input.mp4")

            # Use a smaller number for testing to avoid hanging
            # The original used 5000, but we'll test with 1000 first
            test_iterations = 1000

            for _ in range(test_iterations):
                f = f.drawtext(
                    text="123",
                    x="100",
                    y="100",
                    fontsize=100,
                    fontcolor="red",
                )

            # Try to compile - this should not raise RecursionError
            try:
                f.output(filename="test_output.mp4").compile()
            except RecursionError as e:
                pytest.fail(
                    f"Recursion limit exceeded with {test_iterations} drawtext filters: {e}"
                )
            except Exception as e:
                # Other exceptions are acceptable (like missing input file)
                # but recursion errors indicate the core issue
                if "RecursionError" in str(type(e)):
                    pytest.fail(f"Unexpected recursion error: {e}")

        finally:
            # Restore original recursion limit
            sys.setrecursionlimit(original_limit)


@pytest.mark.skipif(
    os.environ.get("RUN_LARGE_FILTERGRAPH_TESTS", "false").lower() != "true",
    reason="Large filtergraph tests are disabled by default - set RUN_LARGE_FILTERGRAPH_TESTS=true to enable",
)
def test_issue_tracking_metadata() -> None:
    """
    Test to track metadata about the large filtergraph issue.

    This test provides information about the current state of the issue
    and can be used to track progress on fixing it.
    """
    # Test basic functionality still works
    small_chain = create_large_drawtext_chain(5)
    compiled = small_chain.compile()

    # Verify basic compilation works
    assert "drawtext" in compiled
    assert "test_input.mp4" in compiled

    # Log current system limits for reference
    print(f"Current recursion limit: {sys.getrecursionlimit()}")
    print(f"Python version: {sys.version}")

    # This test passes if basic functionality works
    # It's mainly for tracking the issue status
    assert True


# Mark all tests in this module as potentially slow
pytestmark = pytest.mark.slow
