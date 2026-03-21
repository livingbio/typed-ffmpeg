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


def get_relative_import(
    import_path: str,
    template_path: str,
    imports: str,
    version_prefix: str | None = None,
    generated_modules: set[str] | None = None,
) -> str:
    """
    Get a complete import statement or empty string if importing from same file.

    When version_prefix is set, generated files live in a version subdirectory
    (e.g., src/ffmpeg/v6/). Imports between generated files use relative paths,
    but imports to shared hand-written core use absolute paths from the root
    ffmpeg package.

    Args:
        import_path: The import path (dot notation, e.g., streams.audio)
        template_path: The template path (e.g., streams/audio.py.jinja)
        imports: The comma-separated list of imports
        version_prefix: Version subdirectory name (e.g., "v6"). None for
            non-versioned mode (backward compatible).
        generated_modules: Set of module paths that are generated (have
            templates). When version_prefix is set, these use relative imports;
            all others use absolute imports from ffmpeg.{module}.

    Returns:
        The complete import statement or empty string if importing from same file

    """
    # Self-import check (unchanged)
    relative_path = get_relative_path(import_path, template_path)
    if relative_path is None:
        return ""

    # Non-versioned mode: use relative imports (backward compatible)
    if version_prefix is None:
        return f"from {relative_path} import {imports}"

    # Versioned mode: check if target is generated or shared
    is_generated = generated_modules is not None and import_path in generated_modules

    if is_generated:
        # Both files are in the version dir → relative import
        return f"from {relative_path} import {imports}"
    else:
        # Target is shared core → absolute import from ffmpeg_core.{module}
        # Note: In monorepo, core modules are in ffmpeg_core package
        return f"from ffmpeg_core.{import_path} import {imports}"
