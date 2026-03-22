"""
Module redirect setup for multi-version support.

This module sets up import redirects so that root-level imports like
`from ffmpeg.streams.video import VideoStream` resolve to the same class
objects as version-specific imports like `from ffmpeg.v8.streams.video import VideoStream`.

This solves the class identity problem: making isinstance() checks work across
import styles and ensuring CLASS_REGISTRY has only one entry per class.
"""

import sys
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec
from typing import Any


class VersionRedirectFinder(MetaPathFinder):
    """
    Import hook that redirects root ffmpeg.X imports to ffmpeg.vN.X.

    This finder intercepts imports of ffmpeg.streams, ffmpeg.codecs, etc.
    and redirects them to the corresponding version-specific modules
    (ffmpeg.v8.streams, ffmpeg.v8.codecs, etc.).
    """

    def __init__(self, version: str):
        """Initialize with the default version to redirect to."""
        self.version = version
        self.version_prefix = f"v{version}"

        # Modules to redirect
        self.redirect_roots = {
            "streams",
            "codecs",
            "formats",
            "options",
        }

    def find_spec(
        self, fullname: str, path: Any = None, target: Any = None
    ) -> ModuleSpec | None:
        """
        Find module spec for redirected imports.

        Args:
            fullname: Full module name (e.g., 'ffmpeg.streams.video')
            path: Parent module path
            target: Module object to reload

        Returns:
            ModuleSpec if this is a redirected module, None otherwise

        """
        # Check if this is a module we should redirect
        if fullname.startswith("ffmpeg."):
            parts = fullname.split(".")

            if len(parts) >= 2 and parts[1] in self.redirect_roots:
                # This is a root-level import we should redirect
                # e.g., ffmpeg.streams -> ffmpeg.v8.streams
                versioned_name = f"ffmpeg.{self.version_prefix}.{'.'.join(parts[1:])}"

                # Check if this module is already loaded or will cause circular import
                if versioned_name in sys.modules:
                    # Already loaded, create alias
                    sys.modules[fullname] = sys.modules[versioned_name]
                    return None  # Let normal import machinery handle it

                # Try to import the versioned module
                try:
                    versioned_module = __import__(versioned_name, fromlist=[""])

                    # Create alias in sys.modules
                    sys.modules[fullname] = versioned_module

                    return None  # Let normal import machinery proceed
                except ImportError:
                    # Versioned module doesn't exist, fall back to normal import
                    pass

        return None  # Not a module we handle


def setup_module_redirects() -> None:
    """
    Install import hook for module redirects.

    This function installs a MetaPathFinder that intercepts imports of
    ffmpeg.streams, ffmpeg.codecs, etc. and redirects them to the corresponding
    version-specific modules.

    Effect:
        After calling this function:
        - `from ffmpeg.streams.video import VideoStream` imports the exact same
          class as `from ffmpeg.v8.streams.video import VideoStream`
        - `isinstance()` checks work across both import styles
        - CLASS_REGISTRY contains only one entry per class name

    Note:
        This function is called automatically when `ffmpeg` is imported,
        so users don't need to call it manually.

    """
    # Determine default version
    try:
        versions_module = __import__("ffmpeg.versions", fromlist=[""])
        version = getattr(versions_module, "default", None)
    except ImportError:
        version = None

    if not version:
        # No versions available, nothing to redirect
        return

    # Check if finder is already installed
    for finder in sys.meta_path:
        if isinstance(finder, VersionRedirectFinder):
            # Already installed
            return

    # Install the import hook
    finder = VersionRedirectFinder(version)
    sys.meta_path.insert(0, finder)
