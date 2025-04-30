from dataclasses import dataclass
from enum import Enum

from syrupy.assertion import SnapshotAssertion

from ...base import input, output
from ...filters import concat
from ..serialize import Serializable, dumps, load_class, loads, serializable


def test_serializable_decorator() -> None:
    @serializable
    class TestEnum(Enum):
        VALUE1 = "value1"
        VALUE2 = "value2"

    # Test that classes can be loaded by name
    assert load_class("TestEnum") is TestEnum

    # Test that duplicate registration raises an error
    try:

        @serializable
        class TestEnum(Enum):  # type: ignore[no-redef]
            pass

        assert False, "Should have raised an AssertionError"
    except AssertionError as e:
        assert "Class TestEnum already registered" in str(e)


def test_load_and_dump(snapshot: SnapshotAssertion) -> None:
    # Define your dataclasses
    @dataclass
    class Address(Serializable):
        street: str
        city: str

    @dataclass
    class Person(Serializable):
        name: str
        age: int
        address: Address

    # Example usage
    person = Person("John Doe", 30, Address("123 Main St", "Anytown"))
    serialized = dumps(person)
    assert snapshot(name="serialized") == serialized

    deserialized = loads(serialized)

    assert isinstance(deserialized, Person)
    assert snapshot(name="deserialized") == deserialized
    assert person == deserialized


def test_load_and_dump_on_duplicate_input(snapshot: SnapshotAssertion) -> None:
    in_file = input("input.mp4")
    in_file2 = input("input.mp4")

    out_file_1 = output(in_file, in_file2, filename="out.mp4")
    out_file_2 = output(in_file, in_file, filename="out.mp4")

    assert snapshot(name="cmd_1") == out_file_1.compile_line()
    assert out_file_1 == out_file_2, (
        "typed-ffmpeg will automatically deduplicate inputs and Nodes"
    )


def test_load_and_dump_on_complex_filter(snapshot: SnapshotAssertion) -> None:
    in_file = input("input.mp4")
    overlay_file = input("overlay.png")
    stream = (
        concat(
            in_file.trim(start_frame=10, end_frame=20),
            in_file.trim(start_frame=30, end_frame=40),
        )
        .video(0)
        .overlay(overlay_file.hflip())
        .drawbox(x="50", y="50", width="120", height="120", color="red", thickness="5")
        .output(filename="out.mp4")
    )
    serialized = dumps(stream)
    assert snapshot(name="serialized") == serialized

    deserialized = loads(serialized)

    assert isinstance(deserialized, type(stream))
    assert stream == deserialized


def test_load_and_dump_mixed_type(snapshot: SnapshotAssertion) -> None:
    in_file = input("input.mp4")

    serialized = dumps((in_file, True))
    assert snapshot(name="serialized") == serialized

    deserialized = loads(serialized)

    assert [in_file, True] == deserialized
