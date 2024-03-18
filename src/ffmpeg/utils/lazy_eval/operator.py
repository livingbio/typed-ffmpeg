from dataclasses import dataclass
from typing import Any

from .schema import LazyOperator


@dataclass(frozen=True, kw_only=True)
class Add(LazyOperator):
    """
    A lazy operator for addition.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return left + right

    def __str__(self) -> str:
        return f"({self.left}+{self.right})"


@dataclass(frozen=True, kw_only=True)
class Sub(LazyOperator):
    """
    A lazy operator for subtraction.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return left - right

    def __str__(self) -> str:
        return f"({self.left}-{self.right})"


@dataclass(frozen=True, kw_only=True)
class Mul(LazyOperator):
    """
    A lazy operator for multiplication.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return left * right

    def __str__(self) -> str:
        return f"({self.left}*{self.right})"


@dataclass(frozen=True, kw_only=True)
class TrueDiv(LazyOperator):
    """
    A lazy operator for true division.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return left / right

    def __str__(self) -> str:
        return f"({self.left}/{self.right})"


@dataclass(frozen=True, kw_only=True)
class Pow(LazyOperator):
    """
    A lazy operator for exponentiation.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return left**right

    def __str__(self) -> str:
        return f"({self.left}**{self.right})"


@dataclass(frozen=True, kw_only=True)
class Neg(LazyOperator):
    """
    A lazy operator for negation.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return -left

    def __str__(self) -> str:
        return f"-{self.left}"


@dataclass(frozen=True, kw_only=True)
class Pos(LazyOperator):
    """
    A lazy operator for positive.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return +left

    def __str__(self) -> str:
        return f"+{self.left}"


@dataclass(frozen=True, kw_only=True)
class Abs(LazyOperator):
    """
    A lazy operator for absolute value.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return abs(left)

    def __str__(self) -> str:
        return f"abs({self.left})"


@dataclass(frozen=True, kw_only=True)
class Mod(LazyOperator):
    """
    A lazy operator for modulo.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return left % right

    def __str__(self) -> str:
        return f"({self.left}%{self.right})"


@dataclass(frozen=True, kw_only=True)
class FloorDiv(LazyOperator):
    """
    A lazy operator for floor division.
    """

    def _eval(self, left: Any, right: Any) -> Any:
        return left // right

    def __str__(self) -> str:
        return f"({self.left}//{self.right})"
