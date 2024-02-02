from dataclasses import dataclass

from syrupy.assertion import SnapshotAssertion

from ...base import input
from ...filters import concat
from ..serialize import dumps, loads


# Define your dataclasses
@dataclass
class Address:
    street: str
    city: str


@dataclass
class Person:
    name: str
    age: int
    address: Address


def test_load_and_dump(snapshot: SnapshotAssertion) -> None:
    # Example usage
    person = Person("John Doe", 30, Address("123 Main St", "Anytown"))
    serialized = dumps(person)
    assert snapshot(name="serialized") == serialized

    deserialized = loads(serialized)

    assert isinstance(deserialized, Person)
    assert snapshot(name="deserialized") == deserialized
    assert person == deserialized


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
