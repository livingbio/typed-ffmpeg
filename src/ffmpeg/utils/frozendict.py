"""
Provides an immutable dictionary implementation.

This module implements a frozen (immutable) dictionary class that can be used
where hashable dictionaries are needed, such as in sets or as keys in other
dictionaries. Once created, a FrozenDict cannot be modified.
"""

from collections.abc import Iterator, Mapping
from typing import Any, Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class FrozenDict(Mapping[K, V], Generic[K, V]):
    """
    An immutable dictionary implementation.

    FrozenDict provides a hashable, immutable view of a dictionary. It implements
    the Mapping interface but does not allow modification after creation.
    This makes it suitable for use as dictionary keys or in sets where
    mutability would cause issues.
    """

    def __init__(self, data: dict[K, V]):
        """
        Initialize a FrozenDict with the provided dictionary data.

        Args:
            data: Dictionary to create a frozen copy of
        """
        self._data = dict(data)
        self._hash: int | None = None  # lazy computed

    def __getitem__(self, key: K) -> V:
        """
        Retrieve a value from the dictionary by key.

        Args:
            key: The key to look up

        Returns:
            The value associated with the key

        Raises:
            KeyError: If the key is not found
        """
        return self._data[key]

    def __iter__(self) -> Iterator[K]:
        """
        Return an iterator over the dictionary keys.

        Returns:
            An iterator yielding the dictionary keys
        """
        return iter(self._data)

    def __len__(self) -> int:
        """
        Return the number of items in the dictionary.

        Returns:
            The number of key-value pairs in the dictionary
        """
        return len(self._data)

    def __repr__(self) -> str:
        """
        Return a string representation of the FrozenDict.

        Returns:
            A string representation showing the dictionary contents
        """
        return f"FrozenDict({self._data})"

    def __eq__(self, other: Any) -> bool:
        """
        Compare this FrozenDict with another object for equality.

        Two FrozenDicts are equal if they contain the same key-value pairs.
        A FrozenDict can also be equal to other Mapping objects with the same contents.

        Args:
            other: Object to compare with

        Returns:
            True if the objects are equal, False otherwise
        """
        if isinstance(other, Mapping):
            return dict(self._data) == dict(other)
        return NotImplemented

    def __hash__(self) -> int:
        """
        Compute a hash value for this FrozenDict.

        The hash is lazily computed the first time it's needed and then cached.
        This makes FrozenDict usable as a dictionary key or in sets.

        Returns:
            An integer hash value
        """
        if self._hash is None:
            # Create a stable hash based on sorted key-value pairs
            self._hash = hash(frozenset(self._data.items()))
        return self._hash
