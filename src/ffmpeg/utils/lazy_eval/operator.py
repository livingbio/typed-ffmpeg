from dataclasses import dataclass
from typing import Any

from .schema import LazyOperator


@dataclass(frozen=True, kw_only=True)
class Add(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left + right

    def __str__(self) -> str:
        return f"({self.left}+{self.right})"


@dataclass(frozen=True, kw_only=True)
class Sub(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left - right

    def __str__(self) -> str:
        return f"({self.left}-{self.right})"


@dataclass(frozen=True, kw_only=True)
class Mul(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left * right

    def __str__(self) -> str:
        return f"({self.left}*{self.right})"


@dataclass(frozen=True, kw_only=True)
class TrueDiv(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left / right

    def __str__(self) -> str:
        return f"({self.left}/{self.right})"


@dataclass(frozen=True, kw_only=True)
class Pow(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left**right

    def __str__(self) -> str:
        return f"({self.left}**{self.right})"


@dataclass(frozen=True, kw_only=True)
class Neg(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return -left

    def __str__(self) -> str:
        return f"-{self.left}"


@dataclass(frozen=True, kw_only=True)
class Pos(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return +left

    def __str__(self) -> str:
        return f"+{self.left}"


@dataclass(frozen=True, kw_only=True)
class Abs(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return abs(left)

    def __str__(self) -> str:
        return f"abs({self.left})"


@dataclass(frozen=True, kw_only=True)
class Mod(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left % right

    def __str__(self) -> str:
        return f"({self.left}%{self.right})"


@dataclass(frozen=True, kw_only=True)
class FloorDiv(LazyOperator):
    def _eval(self, left: Any, right: Any) -> Any:
        return left // right

    def __str__(self) -> str:
        return f"({self.left}//{self.right})"
