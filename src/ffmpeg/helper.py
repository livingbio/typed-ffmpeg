from .schema import Default


def calculate_dynamic_types(forumla: str, **kwargs: int | Default | str | None | float | bool) -> list[str]:
    # TODO: This is a hacky way to calculate dynamic types. Only int and str are allowed.
    values: dict[str, int | str | float | bool | None] = {}
    for k in kwargs:
        v = kwargs[k]
        if not v:
            continue

        if isinstance(v, Default):
            v = v.value
        elif isinstance(v, str):
            try:
                v = int(v)
            except ValueError:
                v = v

        values = {k: v}

    return eval(forumla, values)
