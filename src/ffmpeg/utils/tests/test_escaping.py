from typing import Any

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..escaping import convert_kwargs_to_cmd_line_args, escape


@pytest.mark.parametrize(
    "text",
    [
        "this is a 'string': may contain one, or more, special characters",
        "this is a string[0]",
    ],
)
def test_escaping(snapshot: SnapshotAssertion, text: str) -> None:
    assert snapshot == escape(text, "\\'[],;")


@pytest.mark.parametrize(
    "options",
    [
        {"a": 1, "b": 2},
        {"a": [1, 2, 3], "b": 2},
        {"a": [1, 2, 3], "b": None},
        {"a": None, "b": 2},
        {"true": True, "false": False},
    ],
)
def test_convert_kwargs_to_cmd_line_args(
    snapshot: SnapshotAssertion, options: dict[str, Any]
) -> None:
    assert snapshot(
        extension_class=JSONSnapshotExtension
    ) == convert_kwargs_to_cmd_line_args(options)
