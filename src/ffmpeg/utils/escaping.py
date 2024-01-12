def escape(text: str | int | tuple[int, int], chars: str = "\\'=:") -> str:
    """Helper function to escape uncomfortable characters."""
    text = str(text)
    _chars = list(set(chars))
    if "\\" in _chars:
        _chars.remove("\\")
        _chars.insert(0, "\\")

    for ch in _chars:
        text = text.replace(ch, "\\" + ch)

    return text
