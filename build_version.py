#!/usr/bin/env python3
"""Build a version-specific typed-ffmpeg package.

This script builds a typed-ffmpeg package targeting a specific FFmpeg version.
It copies the correct version cache, generates code, patches pyproject.toml
with the appropriate package name, builds the package, and restores the original
pyproject.toml.

Usage:
    python build_version.py v6          # builds "typed-ffmpeg" (default/latest)
    python build_version.py v5          # builds "typed-ffmpeg-v5"
    python build_version.py v7          # builds "typed-ffmpeg-v7"
    python build_version.py --all       # builds all versions
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# Map version identifiers to PyPI package names
VERSION_PACKAGE_NAMES: dict[str, str] = {
    "v5": "typed-ffmpeg-v5",
    "v6": "typed-ffmpeg",
    "v7": "typed-ffmpeg-v7",
}

REPO_ROOT = Path(__file__).parent
PYPROJECT_PATH = REPO_ROOT / "pyproject.toml"


def build_version(version: str) -> None:
    """Build the package for a specific FFmpeg version."""
    if version not in VERSION_PACKAGE_NAMES:
        print(f"Error: Unknown version '{version}'. Known: {list(VERSION_PACKAGE_NAMES)}")
        sys.exit(1)

    package_name = VERSION_PACKAGE_NAMES[version]
    print(f"Building {package_name} (FFmpeg {version})...")

    # Save original pyproject.toml
    original_content = PYPROJECT_PATH.read_text()

    try:
        # Step 1: Install version cache and generate code
        print(f"  [1/4] Generating code for {version}...")
        subprocess.run(
            [
                sys.executable, "-m", "scripts.code_gen.cli",
                "generate", "--version", version,
            ],
            cwd=REPO_ROOT / "src",
            check=True,
        )

        # Step 2: Patch pyproject.toml if needed
        if package_name != "typed-ffmpeg":
            print(f"  [2/4] Patching pyproject.toml -> {package_name}...")
            patched = original_content.replace(
                'name = "typed-ffmpeg"',
                f'name = "{package_name}"',
            )
            PYPROJECT_PATH.write_text(patched)
        else:
            print(f"  [2/4] Using default package name (typed-ffmpeg)")

        # Step 3: Build the package
        print(f"  [3/4] Building package...")
        dist_dir = REPO_ROOT / "dist" / version
        dist_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [sys.executable, "-m", "build", "--outdir", str(dist_dir)],
            cwd=REPO_ROOT,
            check=True,
        )

        print(f"  [4/4] Done! Package built in {dist_dir}")

    finally:
        # Always restore original pyproject.toml
        PYPROJECT_PATH.write_text(original_content)


def main() -> None:
    """Build version-specific typed-ffmpeg packages."""
    parser = argparse.ArgumentParser(
        description="Build version-specific typed-ffmpeg packages"
    )
    parser.add_argument(
        "version",
        nargs="?",
        choices=list(VERSION_PACKAGE_NAMES),
        help="FFmpeg version to build for",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Build packages for all supported versions",
    )

    args = parser.parse_args()

    if args.all:
        for version in VERSION_PACKAGE_NAMES:
            build_version(version)
    elif args.version:
        build_version(args.version)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
