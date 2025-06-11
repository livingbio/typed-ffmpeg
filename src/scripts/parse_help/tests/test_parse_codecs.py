from syrupy.assertion import SnapshotAssertion

from ..parse_codecs import (
    extract_decoders_help_text,
    extract_encoders_help_text,
    parse_decoders_help_text,
    parse_encoders_help_text,
)


def test_parse_encoders_help_text(snapshot: SnapshotAssertion) -> None:
    text = extract_encoders_help_text()
    encoders = parse_encoders_help_text(text)
    assert snapshot == encoders


def test_parse_decoders_help_text(snapshot: SnapshotAssertion) -> None:
    text = extract_decoders_help_text()
    decoders = parse_decoders_help_text(text)
    assert snapshot == decoders
