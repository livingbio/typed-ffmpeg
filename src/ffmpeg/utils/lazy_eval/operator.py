from dataclasses import dataclass
from typing import Any

from .schema import LazyOperator


@dataclass(frozen=True, kw_only=True, repr=False)
class Add(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left + right

    def __repr__(self) -> str:
        return f"{self.left}+{self.right}"


@dataclass(frozen=True, kw_only=True, repr=False)
class Sub(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left - right

    def __repr__(self) -> str:
        return f"{self.left}-{self.right}"


@dataclass(frozen=True, kw_only=True, repr=False)
class Mul(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left * right

    def __repr__(self) -> str:
        return f"{self.left}*{self.right}"


@dataclass(frozen=True, kw_only=True, repr=False)
class TrueDiv(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left / right

    def __repr__(self) -> str:
        return f"{self.left}/{self.right}"


@dataclass(frozen=True, kw_only=True, repr=False)
class Pow(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left**right

    def __repr__(self) -> str:
        return f"{self.left}**{self.right}"


@dataclass(frozen=True, kw_only=True, repr=False)
class Neg(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return -left

    def __repr__(self) -> str:
        return f"-{self.left}"


@dataclass(frozen=True, kw_only=True, repr=False)
class Pos(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return +left

    def __repr__(self) -> str:
        return f"+{self.left}"


@dataclass(frozen=True, kw_only=True, repr=False)
class Abs(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return abs(left)

    def __repr__(self) -> str:
        return f"abs({self.left})"


@dataclass(frozen=True, kw_only=True, repr=False)
class Mod(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left % right

    def __repr__(self) -> str:
        return f"{self.left}%{self.right}"


@dataclass(frozen=True, kw_only=True, repr=False)
class FloorDiv(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left // right

    def __repr__(self) -> str:
        return f"{self.left}//{self.right}"


@dataclass(frozen=True, kw_only=True, repr=False)
class DivMod(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return divmod(left, right)

    def __repr__(self) -> str:
        return f"divmod({self.left},{self.right})"
