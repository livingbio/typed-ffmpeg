#!/usr/bin/env python3
"""Bump version across all monorepo packages."""

import re
import sys
from pathlib import Path

PACKAGES = ["core", "v5", "v6", "v7", "v8", "latest"]
REPO_ROOT = Path(__file__).parent.parent


def bump(version: str) -> None:
    for pkg in PACKAGES:
        path = REPO_ROOT / "packages" / pkg / "pyproject.toml"
        text = path.read_text()
        updated = re.sub(r'^version = ".*"', f'version = "{version}"', text, count=1, flags=re.MULTILINE)
        if text == updated:
            print(f"  WARN: no version line found in packages/{pkg}/pyproject.toml")
        else:
            path.write_text(updated)
            print(f"  packages/{pkg}: {version}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/bump-version.py <version>")
        print("Example: python scripts/bump-version.py 1.0.1")
        print("Example: python scripts/bump-version.py 1.0.0a1")
        sys.exit(1)

    version = sys.argv[1]
    print(f"Bumping all packages to {version}...")
    bump(version)
    print("Done.")
