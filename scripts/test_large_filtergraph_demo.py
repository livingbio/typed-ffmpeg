#!/usr/bin/env python3
"""
Demo script to demonstrate the large filtergraph recursion and performance issues.

This script reproduces the issue from x.py and shows how the tests track it.
"""

import os
import sys
import time

# Add the src directory to the path so we can import ffmpeg
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from ffmpeg import input


def demonstrate_issue():
    """Demonstrate the large filtergraph issue."""
    print("=== Large FilterGraph Issue Demonstration ===")
    print()

    # Test 1: Small chain (should work)
    print("1. Testing small chain (10 filters)...")
    try:
        f = input("test_input.mp4")
        for i in range(10):
            f = f.drawtext(
                text=f"Text {i}",
                x="100",
                y="100",
                fontsize=100,
                fontcolor="red",
            )

        start_time = time.time()
        compiled = f.output(filename="test_output.mp4").compile()
        end_time = time.time()

        print(f"   ✓ Small chain compiled successfully in {end_time - start_time:.3f}s")
        print(f"   Command length: {len(compiled)} characters")

    except Exception as e:
        print(f"   ✗ Small chain failed: {e}")

    print()

    # Test 2: Medium chain (might show performance issues)
    print("2. Testing medium chain (100 filters)...")
    try:
        f = input("test_input.mp4")
        for i in range(100):
            f = f.drawtext(
                text=f"Text {i}",
                x="100",
                y="100",
                fontsize=100,
                fontcolor="red",
            )

        start_time = time.time()
        compiled = f.output(filename="test_output.mp4").compile()
        end_time = time.time()

        print(
            f"   ✓ Medium chain compiled successfully in {end_time - start_time:.3f}s"
        )
        print(f"   Command length: {len(compiled)} characters")

    except Exception as e:
        print(f"   ✗ Medium chain failed: {e}")

    print()

    # Test 3: Large chain (likely to show issues)
    print("3. Testing large chain (500 filters)...")
    try:
        f = input("test_input.mp4")
        for i in range(500):
            f = f.drawtext(
                text=f"Text {i}",
                x="100",
                y="100",
                fontsize=100,
                fontcolor="red",
            )

        start_time = time.time()
        compiled = f.output(filename="test_output.mp4").compile()
        end_time = time.time()

        print(f"   ✓ Large chain compiled successfully in {end_time - start_time:.3f}s")
        print(f"   Command length: {len(compiled)} characters")

    except RecursionError as e:
        print(f"   ✗ Large chain failed with RecursionError: {e}")
        print("   This indicates the recursion limit issue is present.")
    except Exception as e:
        print(f"   ✗ Large chain failed: {e}")

    print()

    # Test 4: Very large chain (likely to fail)
    print("4. Testing very large chain (1000 filters)...")
    try:
        f = input("test_input.mp4")
        for i in range(1000):
            f = f.drawtext(
                text=f"Text {i}",
                x="100",
                y="100",
                fontsize=100,
                fontcolor="red",
            )

        start_time = time.time()
        compiled = f.output(filename="test_output.mp4").compile()
        end_time = time.time()

        print(
            f"   ✓ Very large chain compiled successfully in {end_time - start_time:.3f}s"
        )
        print(f"   Command length: {len(compiled)} characters")

    except RecursionError as e:
        print(f"   ✗ Very large chain failed with RecursionError: {e}")
        print("   This confirms the recursion limit issue is present.")
    except Exception as e:
        print(f"   ✗ Very large chain failed: {e}")


def run_tests():
    """Run the large filtergraph tests."""
    print("=== Running Large FilterGraph Tests ===")
    print()

    # Set environment variable to enable tests
    os.environ["SKIP_LARGE_FILTERGRAPH_TESTS"] = "false"

    try:
        import pytest

        # Run the tests
        test_file = os.path.join("src", "ffmpeg", "tests", "test_large_filtergraph.py")
        if os.path.exists(test_file):
            print(f"Running tests from {test_file}...")
            result = pytest.main([test_file, "-v"])
            print(f"Test result: {result}")
        else:
            print(f"Test file not found: {test_file}")

    except ImportError:
        print("pytest not available, skipping test execution")
    except Exception as e:
        print(f"Error running tests: {e}")


def main():
    """Main function."""
    print("Large FilterGraph Issue Tracker")
    print("=" * 40)
    print()

    # Show current system info
    print(f"Python version: {sys.version}")
    print(f"Recursion limit: {sys.getrecursionlimit()}")
    print()

    # Demonstrate the issue
    demonstrate_issue()

    print()
    print("=" * 40)
    print()

    # Run tests
    run_tests()

    print()
    print("=== Summary ===")
    print("If you see RecursionError or excessive compilation times,")
    print("the large filtergraph issue is present and needs to be fixed.")
    print()
    print("The tests in src/ffmpeg/tests/test_large_filtergraph.py")
    print("can be used to track progress on fixing this issue.")


if __name__ == "__main__":
    main()
