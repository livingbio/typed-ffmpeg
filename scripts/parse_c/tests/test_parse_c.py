import pathlib

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..helper import dump
from ..parse_c import parse_all_filter_names, parse_c

datadir = pathlib.Path(__file__).parent / "test_parse_c"


@pytest.mark.parametrize("path", datadir.glob("*.c"), ids=lambda path: path.stem)
def test_parse_c(path: pathlib.Path, snapshot: SnapshotAssertion) -> None:
    filters = parse_c(path)
    assert snapshot(extension_class=JSONSnapshotExtension) == dump(filters)
    assert snapshot(extension_class=JSONSnapshotExtension, name="property") == dump(
        [
            {
                "type": filter.type,
                "flags_value": filter.flags_value,
                "priv_class_value": filter.priv_class_value,
                "inputs_value": filter.inputs_value,
                "outputs_value": filter.outputs_value,
                "is_dynamic_inputs": filter.is_dynamic_inputs,
                "is_dynamic_outputs": filter.is_dynamic_outputs,
                "parsed_options": filter.parsed_options,
            }
            for filter in filters
        ]
    )


def test_parse_all_filter_names(snapshot: SnapshotAssertion) -> None:
    filters = parse_all_filter_names(datadir / "allfilters.c")
    assert snapshot(extension_class=JSONSnapshotExtension) == filters
    assert snapshot == len(filters)
