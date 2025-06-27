"""Utils for code generation."""

from pathlib import Path


def get_relative_path(import_path: str, template_path: str) -> str:
    """
    Get the relative path of the template.

    Args:
        import_path: The import path
        template_path: The template path

    Returns:
        The relative path of the template

    """
    template_parent = Path(template_path).parent
    import_path_obj = Path(import_path)

    # If import_path is a top-level directory, return the correct number of dots + import_path
    if len(import_path_obj.parts) == 1:
        dots = "." * (len(template_parent.parts) + 1)
        return dots + str(import_path_obj)

    try:
        return str(import_path_obj.relative_to(template_parent))
    except ValueError:
        # Find common ancestor and calculate relative path
        common_parts = 0
        for i, (part1, part2) in enumerate(
            zip(template_parent.parts, import_path_obj.parts)
        ):
            if part1 == part2:
                common_parts = i + 1
            else:
                break
        up_levels = len(template_parent.parts) - common_parts
        down_parts = import_path_obj.parts[common_parts:]
        if up_levels == 0:
            return str(Path(*down_parts)) if down_parts else "."
        else:
            # Return as many dots as up_levels + 1 + import_path
            dots = "." * (up_levels + 1)
            return dots + str(import_path_obj)
