"""
CLI backend for generating FFmpeg command-line arguments.

This backend converts an IR graph into a list of command-line arguments
that can be passed to the FFmpeg executable.
"""

from __future__ import annotations

from ..schema import IRGraph
from .base import IRBackend


class CLIBackend(IRBackend):
    """
    Backend that generates FFmpeg command-line arguments.

    This backend produces a list of strings representing the complete
    FFmpeg command, including inputs, filters, outputs, and options.
    """

    def generate(self, ir: IRGraph) -> list[str]:
        """
        Generate FFmpeg CLI arguments from an IR graph.

        Args:
            ir: The intermediate representation graph.

        Returns:
            List of command-line arguments (without the 'ffmpeg' executable name).

        """
        # TODO: Implement full CLI generation
        # This is a stub that will be properly implemented later
        # by refactoring the existing compile logic

        args: list[str] = []

        # Add global options
        for key, value in ir.global_options.items():
            if isinstance(value, bool):
                if value:
                    args.append(f"-{key}")
            else:
                args.extend([f"-{key}", str(value)])

        # Add inputs
        for input_node in ir.inputs:
            # Add input options
            for key, value in input_node.options.items():
                args.extend([f"-{key}", str(value)])

            # Add input source
            args.extend(["-i", input_node.source])

        # TODO: Add filter_complex if filters exist
        # TODO: Add output options and files

        # Add outputs (simplified)
        for output_node in ir.outputs:
            args.append(output_node.destination)

        return args
