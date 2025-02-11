from __future__ import annotations

import logging
import subprocess
from typing import TYPE_CHECKING

from ...exceptions import FFMpegExecuteError
from ...utils.run import command_line
from .global_args import GlobalArgs

if TYPE_CHECKING:
    from ..nodes import GlobalStream, OutputStream

logger = logging.getLogger(__name__)


class GlobalRunable(GlobalArgs):
    def merge_outputs(self, *streams: OutputStream) -> GlobalStream:
        """
        Merge multiple output streams into one.

        Args:
            *streams: The output streams to merge.

        Returns:
            The merged output stream.
        """
        return self._global_node(*streams).stream()

    def overwrite_output(self) -> GlobalStream:
        """
        Overwrite output files without asking (ffmpeg `-y` option)

        Returns:
            the output stream
        """
        return self._global_node(y=True).stream()

    def compile(
        self,
        cmd: str | list[str] = "ffmpeg",
        overwrite_output: bool = None,
        auto_fix: bool = True,
    ) -> list[str]:
        """
        Build command-line for invoking ffmpeg.

        Args:
            cmd: the command to invoke ffmpeg
            overwrite_output: whether to overwrite output files without asking
            auto_fix: whether to automatically fix the stream

        Returns:
            the command-line
        """
        from ..compile import compile

        if isinstance(cmd, str):
            cmd = [cmd]

        if overwrite_output is True:
            return self.global_args(y=True).compile(cmd, auto_fix=auto_fix)
        elif overwrite_output is False:
            return self.global_args(n=True).compile(cmd, auto_fix=auto_fix)

        return cmd + compile(self._global_node().stream(), auto_fix=auto_fix)

    def compile_line(
        self,
        cmd: str | list[str] = "ffmpeg",
        overwrite_output: bool = None,
        auto_fix: bool = True,
    ) -> str:
        """
        Build command-line for invoking ffmpeg.

        Args:
            cmd: the command to invoke ffmpeg
            overwrite_output: whether to overwrite output files without asking
            auto_fix: whether to automatically fix the stream

        Returns:
            the command-line
        """
        return command_line(
            self.compile(cmd, overwrite_output=overwrite_output, auto_fix=auto_fix)
        )

    def run_async(
        self,
        cmd: str | list[str] = "ffmpeg",
        pipe_stdin: bool = False,
        pipe_stdout: bool = False,
        pipe_stderr: bool = False,
        quiet: bool = False,
        overwrite_output: bool = None,
        auto_fix: bool = True,
    ) -> subprocess.Popen[bytes]:
        """
        Run ffmpeg asynchronously.

        Args:
            cmd: the command to invoke ffmpeg
            pipe_stdin: whether to pipe stdin
            pipe_stdout: whether to pipe stdout
            pipe_stderr: whether to pipe stderr
            quiet: whether to pipe stderr to stdout
            overwrite_output: whether to overwrite output files without asking
            auto_fix: whether to automatically fix the stream

        Returns:
            the process
        """

        args = self.compile(cmd, overwrite_output=overwrite_output, auto_fix=auto_fix)
        stdin_stream = subprocess.PIPE if pipe_stdin else None
        stdout_stream = subprocess.PIPE if pipe_stdout or quiet else None
        stderr_stream = subprocess.PIPE if pipe_stderr or quiet else None

        logger.info(
            f"Running command: {self.compile_line(cmd, overwrite_output=overwrite_output, auto_fix=auto_fix)}"
        )

        return subprocess.Popen(
            args,
            stdin=stdin_stream,
            stdout=stdout_stream,
            stderr=stderr_stream,
        )

    def run(
        self,
        cmd: str | list[str] = "ffmpeg",
        capture_stdout: bool = False,
        capture_stderr: bool = False,
        input: bytes | None = None,
        quiet: bool = False,
        overwrite_output: bool = None,
        auto_fix: bool = True,
    ) -> tuple[bytes, bytes]:
        """
        Run ffmpeg synchronously.

        Args:
            cmd: the command to invoke ffmpeg
            capture_stdout: whether to capture stdout
            capture_stderr: whether to capture stderr
            input: the input
            quiet: whether to pipe stderr to stdout
            overwrite_output: whether to overwrite output files without asking
            auto_fix: whether to automatically fix the stream

        Returns:
            stdout: he stdout
            stderr: the stderr
        """

        process = self.run_async(
            cmd,
            pipe_stdin=input is not None,
            pipe_stdout=capture_stdout,
            pipe_stderr=capture_stderr,
            quiet=quiet,
            overwrite_output=overwrite_output,
            auto_fix=auto_fix,
        )
        stdout, stderr = process.communicate(input)
        retcode = process.poll()

        if retcode:
            raise FFMpegExecuteError(
                retcode=retcode,
                cmd=self.compile_line(
                    cmd, overwrite_output=overwrite_output, auto_fix=auto_fix
                ),
                stdout=stdout,
                stderr=stderr,
            )

        return stdout, stderr
