from syrupy.assertion import SnapshotAssertion

from ..remove_typing_from_docstrings import remove_typing_from_docstrings


def test_remove_typing_from_docstrings(snapshot: SnapshotAssertion) -> None:
    # 測試
    docstring = """
        Run ffprobe on the given file and return a JSON representation of the output

        Args:
            filename: The path to the file to probe.
            cmd: The ffprobe command to run. Defaults to "ffprobe".
            timeout: The timeout for the command. Defaults to None.
            **kwargs: The arguments for the ffprobe command.

        Returns:
             The JSON representation of the ffprobe output.
        """

    assert snapshot == remove_typing_from_docstrings(docstring)
