"""
Concrete operator implementations for lazy evaluation expressions.

This module defines the specific operator classes that implement the LazyOperator
abstract base class. Each class represents a mathematical operation like addition,
subtraction, multiplication, etc., and provides the implementation for evaluating
that operation when all required values are available.
"""

from dataclasses import dataclass
from typing import Any

from .schema import LazyOperator


@dataclass(frozen=True, kw_only=True)
class Add(LazyOperator):
    """
    A lazy operator for addition operations.

    This class implements the addition operation for lazy evaluation expressions.
    It evaluates to the sum of its left and right operands when all required
    values are available.

    Example:
        ```python
        # Create an expression that adds width and height
        from .schema import Symbol

        width = Symbol("width")
        height = Symbol("height")
        expr = Add(left=width, right=height)

        # Evaluate the expression with specific values
        result = expr.eval(width=1280, height=720)  # Returns 2000
        ```
    """

    def _eval(self, left: Any, right: Any) -> Any:
        """
        Evaluate the addition operation with the given operands.

        Args:
            left: The left operand
            right: The right operand

        Returns:
            The sum of the left and right operands
        """
        return left + right

    def __str__(self) -> str:
        """
        Get a string representation of this addition operation.

        Returns:
            A string in the format "(left+right)"
        """
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
