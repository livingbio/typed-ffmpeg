from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class LazyEvalInterface:
    def __add__(self, v: Any) -> LazyOperator:
        from .operator import Add

        return Add(left=self, right=v)

    def __radd__(self, v: Any) -> LazyOperator:
        from .operator import Add

        return Add(left=v, right=self)

    def __sub__(self, v: Any) -> LazyOperator:
        from .operator import Sub

        return Sub(left=self, right=v)

    def __rsub__(self, v: Any) -> LazyOperator:
        from .operator import Sub

        return Sub(left=v, right=self)

    def __mul__(self, v: Any) -> LazyOperator:
        from .operator import Mul

        return Mul(left=self, right=v)

    def __rmul__(self, v: Any) -> LazyOperator:
        from .operator import Mul

        return Mul(left=v, right=self)

    def __truediv__(self, v: Any) -> LazyOperator:
        from .operator import TrueDiv

        return TrueDiv(left=self, right=v)

    def __rtruediv__(self, v: Any) -> LazyOperator:
        from .operator import TrueDiv

        return TrueDiv(left=v, right=self)

    def __pow__(self, v: Any) -> LazyOperator:
        from .operator import Pow

        return Pow(left=self, right=v)

    def __rpow__(self, v: Any) -> LazyOperator:
        from .operator import Pow

        return Pow(left=v, right=self)

    def __neg__(self) -> LazyOperator:
        from .operator import Neg

        return Neg(left=self)

    def __pos__(self) -> LazyOperator:
        from .operator import Pos

        return Pos(left=self)

    def __abs__(self) -> LazyOperator:
        from .operator import Abs

        return Abs(left=self)

    def __mod__(self, v: Any) -> LazyOperator:
        from .operator import Mod

        return Mod(left=self, right=v)

    def __rmod__(self, v: Any) -> LazyOperator:
        from .operator import Mod

        return Mod(left=v, right=self)

    def __floordiv__(self, v: Any) -> LazyOperator:
        from .operator import FloorDiv

        return FloorDiv(left=self, right=v)

    def __rfloordiv__(self, v: Any) -> LazyOperator:
        from .operator import FloorDiv

        return FloorDiv(left=v, right=self)


@dataclass(frozen=True, kw_only=True)
class PlaceHolder(LazyEvalInterface):
    # NOTE: internal use only
    key: str

    def __str__(self) -> str:
        return str(self.key)


@dataclass(frozen=True, kw_only=True)
class LazyOperator(LazyEvalInterface, ABC):
    left: Any = None
    right: Any = None

    def ready(self) -> bool:
        return not self.keys()

    @abstractmethod
    def _eval(self, left: Any, right: Any) -> Any:
        ...

    def eval(self, **values: Any) -> Any:

        if isinstance(self.left, LazyOperator):
            left = self.left.eval(**values)
        elif isinstance(self.left, PlaceHolder):
            left = values[self.left.key]
        else:
            left = self.left

        if isinstance(self.right, LazyOperator):
            right = self.right.eval(**values)
        elif isinstance(self.right, PlaceHolder):
            right = values[self.right.key]
        else:
            right = self.right

        return self._eval(left, right)

    def keys(self) -> set[str]:
        r = set()
        if isinstance(self.left, LazyOperator):
            r |= self.left.keys()
        elif isinstance(self.left, PlaceHolder):
            r |= {self.left.key}

        if isinstance(self.right, LazyOperator):
            r |= self.right.keys()
        elif isinstance(self.right, PlaceHolder):
            r |= {self.right.key}

        return r
