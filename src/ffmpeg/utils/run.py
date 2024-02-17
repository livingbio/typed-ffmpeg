import shlex


def command_line(args: list[str]) -> str:
    """
    Get the command line representation of the arguments.

    Args:
        args: The arguments to convert.

    Returns:
        The command line representation of the arguments.
    """
    return " ".join(shlex.quote(arg) for arg in args)
