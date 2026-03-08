"""
Base class for IR backends.

This module defines the abstract interface that all IR backends must implement.
Backends convert the intermediate representation to a specific target format
(CLI commands, TypeScript code, JSON, etc.).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from ..schema import IRGraph


class IRBackend(ABC):
    """
    Abstract base class for all IR backends.

    A backend takes an IR graph and generates output in a specific format.
    This could be command-line arguments, source code, configuration files, etc.
    """

    @abstractmethod
    def generate(self, ir: IRGraph) -> Any:
        """
        Generate backend-specific output from an IR graph.

        Args:
            ir: The intermediate representation graph to convert.

        Returns:
            Backend-specific output. The type depends on the backend:
            - CLI backend: list[str] (command-line arguments)
            - TypeScript backend: str (TypeScript code)
            - JSON backend: dict (JSON-serializable data)

        """
        ...

    def validate(self, ir: IRGraph) -> list[str]:
        """
        Validate an IR graph for this specific backend.

        Performs backend-specific validation beyond the general IR validation.
        For example, a CLI backend might check for FFmpeg-specific limitations.

        Args:
            ir: The intermediate representation graph to validate.

        Returns:
            List of validation error messages. Empty list if valid.

        """
        # Default implementation: no additional validation
        return []
