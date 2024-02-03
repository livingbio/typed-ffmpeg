import shlex


def command_line(args: list[str]) -> str:
    return " ".join(shlex.quote(arg) for arg in args)
