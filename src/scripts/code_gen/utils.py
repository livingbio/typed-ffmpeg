"""Utils for code generation."""

from pathlib import Path


def get_relative_path(import_path: str, template_path: str) -> str | None:
    """
    Get the relative path of the template.

    Args:
        import_path: The import path (dot notation, e.g., streams.audio)
        template_path: The template path (e.g., streams/audio.py.jinja)

    Returns:
        The relative path of the template, or None if importing from same file

    """
    template_path_obj = Path(template_path)
    template_parent = template_path_obj.parent
    import_path_obj = Path(import_path.replace(".", "/"))

    print(
        f"DEBUG: template_path={template_path}, template_parent='{template_parent}', str(template_parent)='{str(template_parent)}', stem='{template_path_obj.stem}'"
    )

    # Remove both .jinja and .py suffixes to get the module name
    stem = template_path_obj.name
    for ext in (".jinja", ".py"):
        while stem.endswith(ext):
            stem = stem[: -len(ext)]
    print(f"DEBUG: final stem after suffix removal: '{stem}'")
    template_module = (
        ".".join(list(template_parent.parts) + [stem]) if str(template_parent) else stem
    )

    # If importing from the same file, return None
    if import_path == template_module:
        return None

    # If importing from a sibling module (same parent, but not the same module)
    if template_parent == import_path_obj.parent and import_path != template_module:
        return f".{import_path_obj.name}"

    # If template is at root
    if str(template_parent) in ("", "."):
        if "." in import_path:
            if "." in stem:
                return f"..{import_path}"
            else:
                return f".{import_path}"
        return f".{import_path}"

    # Otherwise, number of dots = len(template_parent.parts) + 1
    dots = "." * (len(template_parent.parts) + 1)
    return f"{dots}{import_path}"


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
