from dataclasses import dataclass

from syrupy.assertion import SnapshotAssertion

from ..dataclasses_helper import dump, load


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
    serialized = dump(person)
    assert snapshot(name="serialized") == serialized

    deserialized = load(Person, serialized)

    assert isinstance(deserialized, Person)
    assert snapshot(name="deserialized") == deserialized
    assert person == deserialized
