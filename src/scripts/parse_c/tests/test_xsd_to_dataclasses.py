#!/usr/bin/env python3
"""
Tests for the XSD to Python Dataclasses Generator.

This module contains tests for the xsd_to_dataclasses.py script.
"""

from pathlib import Path

from syrupy.assertion import SnapshotAssertion

from ..xsd_to_dataclasses import (
    generate_dataclasses,
    parse_xsd_file,
)


def test_parse_ffprobe_xsd(snapshot: SnapshotAssertion, datadir: Path) -> None:
    xsd_file = datadir / "ffprobe.xsd"
    root, ns = parse_xsd_file(str(xsd_file))
    output, _ = generate_dataclasses(root, ns)
    assert snapshot == output
