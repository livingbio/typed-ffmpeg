from collections.abc import Iterator, Mapping
from typing import Any, Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class FrozenDict(Mapping[K, V], Generic[K, V]):
    def __init__(self, data: dict[K, V]):
        self._data = dict(data)
        self._hash: int | None = None  # lazy computed

    def __getitem__(self, key: K) -> V:
        return self._data[key]

    def __iter__(self) -> Iterator[K]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"FrozenDict({self._data})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Mapping):
            return dict(self._data) == dict(other)
        return NotImplemented

    def __hash__(self) -> int:
        if self._hash is None:
            # Create a stable hash based on sorted key-value pairs
            self._hash = hash(frozenset(self._data.items()))
        return self._hash
