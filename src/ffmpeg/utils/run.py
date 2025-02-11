import shlex

from ..schema import Default
from ..utils.lazy_eval.schema import LazyValue


def command_line(args: list[str]) -> str:
    """
    Get the command line representation of the arguments.

    Args:
        args: The arguments to convert.

    Returns:
        The command line representation of the arguments.
    """
    return " ".join(shlex.quote(arg) for arg in args)


# Filter_Node_Option_Type
def ignore_default(
    kwargs: dict[str, str | int | float | bool | Default],
) -> tuple[tuple[str, str | int | float | bool | LazyValue], ...]:
    """
    Convert the values of the dictionary to strings.
    """
    return tuple((k, v) for k, v in kwargs.items() if not isinstance(v, Default))
