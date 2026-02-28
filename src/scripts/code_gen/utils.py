"""Utils for code generation."""

from pathlib import Path


def get_relative_path(import_path: str, template_path: str | Path) -> str | None:
    """
    Get the relative path of the template.

    Args:
        import_path: The import path (dot notation, e.g., streams.audio)
        template_path: The template path (e.g., streams/audio.py.jinja)

    Returns:
        The relative path of the template, or None if importing from same file

    """
    template_path_obj = Path(str(template_path).split(".")[0])
    import_path_obj = Path(import_path.replace(".", "/"))

    if template_path_obj == import_path_obj:
        # NOTE: this is a special case that should not import itself
        return None

    file_parts = template_path_obj.parts
    import_parts = import_path_obj.parts

    for idx in range(len(file_parts)):
        if file_parts[idx] != import_parts[idx]:
            return (
                "."
                + "." * (len(file_parts) - idx - 1)
                + ".".join(import_path_obj.parts[idx:])
            )

    return str(import_path)


def get_relative_import(import_path: str, template_path: str, imports: str) -> str:
    """
    Get a complete import statement or empty string if importing from same file.

    Args:
        import_path: The import path (dot notation, e.g., streams.audio)
        template_path: The template path (e.g., streams/audio.py.jinja)
        imports: The comma-separated list of imports

    Returns:
        The complete import statement or empty string if importing from same file

    """
    relative_path = get_relative_path(import_path, template_path)
    if relative_path is None:
        return ""
    return f"from {relative_path} import {imports}"
