import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--run-dev",
        action="store_true",
        default=False,
        help="Run tests marked as dev_only",
    )


def pytest_runtest_setup(item: pytest.Item) -> None:
    if "dev_only" in item.keywords and not item.config.getoption("--run-dev"):
        pytest.skip("Skipping dev_only test. Use --run-dev to run it.")
