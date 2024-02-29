from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from ..typing import override


class LazyValue(ABC):
    def __add__(self, v: Any) -> LazyValue:
        from .operator import Add

        return Add(left=self, right=v)

    def __radd__(self, v: Any) -> LazyValue:
        from .operator import Add

        return Add(left=v, right=self)

    def __sub__(self, v: Any) -> LazyValue:
        from .operator import Sub

        return Sub(left=self, right=v)

    def __rsub__(self, v: Any) -> LazyValue:
        from .operator import Sub

        return Sub(left=v, right=self)

    def __mul__(self, v: Any) -> LazyValue:
        from .operator import Mul

        return Mul(left=self, right=v)

    def __rmul__(self, v: Any) -> LazyValue:
        from .operator import Mul

        return Mul(left=v, right=self)

    def __truediv__(self, v: Any) -> LazyValue:
        from .operator import TrueDiv

        return TrueDiv(left=self, right=v)

    def __rtruediv__(self, v: Any) -> LazyValue:
        from .operator import TrueDiv

        return TrueDiv(left=v, right=self)

    def __pow__(self, v: Any) -> LazyValue:
        from .operator import Pow

        return Pow(left=self, right=v)

    def __rpow__(self, v: Any) -> LazyValue:
        from .operator import Pow

        return Pow(left=v, right=self)

    def __neg__(self) -> LazyValue:
        from .operator import Neg

        return Neg(left=self)

    def __pos__(self) -> LazyValue:
        from .operator import Pos

        return Pos(left=self)

    def __abs__(self) -> LazyValue:
        from .operator import Abs

        return Abs(left=self)

    def __mod__(self, v: Any) -> LazyValue:
        from .operator import Mod

        return Mod(left=self, right=v)

    def __rmod__(self, v: Any) -> LazyValue:
        from .operator import Mod

        return Mod(left=v, right=self)

    def __floordiv__(self, v: Any) -> LazyValue:
        from .operator import FloorDiv

        return FloorDiv(left=self, right=v)

    def __rfloordiv__(self, v: Any) -> LazyValue:
        from .operator import FloorDiv

        return FloorDiv(left=v, right=self)

    def eval(self, **values: Any) -> Any:
        v = self.partial(**values)
        if isinstance(v, LazyValue):
            raise KeyError(v.keys())
        return v

    @abstractmethod
    def partial(self, **values: Any) -> Any:
        ...

    def ready(self) -> bool:
        return not self.keys()

    @abstractmethod
    def keys(self) -> set[str]:
        ...


@dataclass(frozen=True, kw_only=True)
class PlaceHolder(LazyValue):
    key: str

    def __str__(self) -> str:
        return str(self.key)

    @override
    def partial(self, **values: Any) -> Any:
        if self.key in values:
            return values[self.key]
        return self

    @override
    def keys(self) -> set[str]:
        return {self.key}


@dataclass(frozen=True, kw_only=True)
class LazyOperator(LazyValue):
    left: Any = None
    right: Any = None

    @abstractmethod
    def _eval(self, left: Any, right: Any) -> Any:
        ...

    @override
    def partial(self, **values: Any) -> Any:
        if isinstance(self.left, LazyValue):
            left = self.left.partial(**values)
        else:
            left = self.left

        if isinstance(self.right, LazyValue):
            right = self.right.partial(**values)
        else:
            right = self.right

        return self._eval(left, right)

    @override
    def keys(self) -> set[str]:
        r = set()
        if isinstance(self.left, LazyValue):
            r |= self.left.keys()

        if isinstance(self.right, LazyValue):
            r |= self.right.keys()

        return r
