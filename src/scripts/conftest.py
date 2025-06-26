"""Pytest configuration for typed-ffmpeg scripts."""

import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Add custom command line options to pytest.

    Args:
        parser: The pytest argument parser

    """
    parser.addoption(
        "--run-dev",
        action="store_true",
        default=False,
        help="Run tests marked as dev_only",
    )


def pytest_runtest_setup(item: pytest.Item) -> None:
    """
    Set up test execution with custom options.

    Args:
        item: The pytest test item

    """
    if "dev_only" in item.keywords and not item.config.getoption("--run-dev"):
        pytest.skip("Skipping dev_only test. Use --run-dev to run it.")
