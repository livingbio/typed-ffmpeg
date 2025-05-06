"""
Execution capabilities for FFmpeg filter graphs.

This module provides the GlobalRunable class, which extends GlobalArgs with
methods for executing FFmpeg commands. It enables compiling filter graphs
into command-line arguments and running FFmpeg processes both synchronously
and asynchronously.
"""

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
    """
    Base class that provides execution capabilities for FFmpeg filter graphs.

    This class extends GlobalArgs with methods for compiling filter graphs into
    FFmpeg command-line arguments and executing FFmpeg processes. It serves as
    a mixin for stream classes that need to be executed as FFmpeg commands.
    """

    def merge_outputs(self, *streams: OutputStream) -> GlobalStream:
        """
        Merge multiple output streams into a single command.

        This method allows combining multiple output files into a single FFmpeg
        command, which is more efficient than running separate commands for each
        output. It creates a GlobalNode that includes all the specified output
        streams.

        Args:
            *streams: Additional output streams to include in the same command

        Returns:
            A GlobalStream that represents the combined outputs

        Example:
            ```python
            # Create two output files with one command
            video = ffmpeg.input("input.mp4").video
            output1 = video.output("output1.mp4")
            output2 = video.output("output2.webm")
            merged = output1.merge_outputs(output2)
            merged.run()  # Creates both output files with one FFmpeg command
            ```
        """
        return self._global_node(*streams).stream()

    def overwrite_output(self) -> GlobalStream:
        """
        Set the FFmpeg command to overwrite output files without asking.

        This method adds the `-y` option to the FFmpeg command, which causes
        FFmpeg to overwrite output files without prompting for confirmation.
        It's equivalent to calling `global_args(y=True)`.

        Returns:
            A GlobalStream with the overwrite option enabled

        Example:
            ```python
            # Overwrite output file if it already exists
            ffmpeg.input("input.mp4").output("output.mp4").overwrite_output().run()
            ```
        """
        return self._global_node(y=True).stream()

    def compile(
        self,
        cmd: str | list[str] = "ffmpeg",
        overwrite_output: bool | None = None,
        auto_fix: bool = True,
    ) -> list[str]:
        """
        Build command-line arguments for invoking FFmpeg.

        This method converts the filter graph into a list of command-line
        arguments that can be passed to subprocess functions or executed
        directly. It handles the FFmpeg executable name, overwrite options,
        and automatic fixing of the filter graph.

        Args:
            cmd: The FFmpeg executable name or path, or a list containing
                 the executable and initial arguments
            overwrite_output: If True, add the -y option to overwrite output files
                             If False, add the -n option to never overwrite
                             If None (default), use the current settings
            auto_fix: Whether to automatically fix issues in the filter graph,
                     such as adding split filters for reused streams

        Returns:
            A list of strings representing the complete FFmpeg command

        Example:
            ```python
            # Get the command-line arguments for a filter graph
            args = ffmpeg.input("input.mp4").output("output.mp4").compile()
            # Result: ['ffmpeg', '-i', 'input.mp4', 'output.mp4']
            ```
        """
        from ...compile.compile_cli import compile_as_list

        if isinstance(cmd, str):
            cmd = [cmd]

        if overwrite_output is True:
            return self.global_args(y=True).compile(cmd, auto_fix=auto_fix)
        elif overwrite_output is False:
            return self.global_args(n=True).compile(cmd, auto_fix=auto_fix)

        return cmd + compile_as_list(self._global_node().stream(), auto_fix=auto_fix)

    def compile_line(
        self,
        cmd: str | list[str] = "ffmpeg",
        overwrite_output: bool | None = None,
        auto_fix: bool = True,
    ) -> str:
        """
        Build a command-line string for invoking FFmpeg.

        This method is similar to compile(), but returns a single string with
        proper escaping instead of a list of arguments. This is useful for
        logging or displaying the command to users.

        Args:
            cmd: The FFmpeg executable name or path, or a list containing
                 the executable and initial arguments
            overwrite_output: If True, add the -y option to overwrite output files
                             If False, add the -n option to never overwrite
                             If None (default), use the current settings
            auto_fix: Whether to automatically fix issues in the filter graph

        Returns:
            A string representing the complete FFmpeg command with proper escaping

        Example:
            ```python
            # Get a command-line string for a filter graph
            cmd_str = ffmpeg.input("input.mp4").output("output.mp4").compile_line()
            # Result: 'ffmpeg -i input.mp4 output.mp4'
            ```
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
        overwrite_output: bool | None = None,
        auto_fix: bool = True,
    ) -> subprocess.Popen[bytes]:
        """
        Run FFmpeg asynchronously as a subprocess.

        This method executes the FFmpeg command in a separate process without
        waiting for it to complete. This is useful for long-running operations
        or when you need to interact with the process while it's running.

        Args:
            cmd: The FFmpeg executable name or path, or a list containing
                 the executable and initial arguments
            pipe_stdin: Whether to create a pipe for writing to the process's stdin
            pipe_stdout: Whether to create a pipe for reading from the process's stdout
            pipe_stderr: Whether to create a pipe for reading from the process's stderr
            quiet: Whether to capture stderr (implies pipe_stderr=True)
            overwrite_output: If True, add the -y option to overwrite output files
                             If False, add the -n option to never overwrite
                             If None (default), use the current settings
            auto_fix: Whether to automatically fix issues in the filter graph

        Returns:
            A subprocess.Popen object representing the running FFmpeg process

        Example:
            ```python
            # Start FFmpeg process and interact with it
            process = ffmpeg.input("input.mp4").output("output.mp4").run_async()
            # Do something while FFmpeg is running
            process.wait()  # Wait for completion
            ```
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
        overwrite_output: bool | None = None,
        auto_fix: bool = True,
    ) -> tuple[bytes, bytes]:
        """
        Run FFmpeg synchronously and wait for completion.

        This method executes the FFmpeg command in a separate process and waits
        for it to complete before returning. It's the most common way to run
        FFmpeg commands when you just want to process media files.

        Args:
            cmd: The FFmpeg executable name or path, or a list containing
                 the executable and initial arguments
            capture_stdout: Whether to capture and return the process's stdout
            capture_stderr: Whether to capture and return the process's stderr
            input: Optional bytes to write to the process's stdin
            quiet: Whether to suppress output to the console
            overwrite_output: If True, add the -y option to overwrite output files
                             If False, add the -n option to never overwrite
                             If None (default), use the current settings
            auto_fix: Whether to automatically fix issues in the filter graph

        Returns:
            A tuple of (stdout_bytes, stderr_bytes), which will be empty bytes
            objects if the respective capture_* parameter is False

        Raises:
            FFMpegExecuteError: If the FFmpeg process returns a non-zero exit code

        Example:
            ```python
            # Process a video file
            stdout, stderr = ffmpeg.input("input.mp4").output("output.mp4").run()

            # Capture FFmpeg's output
            stdout, stderr = (
                ffmpeg.input("input.mp4").output("output.mp4").run(capture_stderr=True)
            )
            print(stderr.decode())  # Print FFmpeg's progress information
            ```
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
