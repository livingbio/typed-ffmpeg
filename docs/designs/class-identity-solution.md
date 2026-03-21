# Design: Class Identity Solution for Multi-Version Support

**Status:** PROPOSED  
**Date:** 2026-03-21  
**Problem:** Root imports (`from ffmpeg.streams.video import VideoStream`) create different class objects than version imports (`from ffmpeg.v8.streams.video import VideoStream`), breaking `isinstance()` checks and `CLASS_REGISTRY`.

## Problem Analysis

### Current Situation

```python
# Root import (OLD generated code)
from ffmpeg.streams.video import VideoStream as RootVS

# Version import (NEW generated code)
from ffmpeg.v8.streams.video import VideoStream as V8VS

# These are DIFFERENT classes!
assert RootVS is not V8VS  # Currently TRUE (bad!)
```

### Why This Breaks

1. **isinstance() checks fail**:
   ```python
   stream = V8VS(...)
   isinstance(stream, RootVS)  # False!
   ```

2. **CLASS_REGISTRY breaks**:
   ```python
   # Both register as "VideoStream"
   CLASS_REGISTRY["VideoStream"] = RootVS
   CLASS_REGISTRY["VideoStream"] = V8VS  # Overwrites!
   ```

3. **Serialization fails**:
   ```python
   # Serialize with v8 class
   data = v8_stream.to_dict()
   
   # Deserialize gets root class
   restored = load_class("VideoStream")  # Returns RootVS, not V8VS
   ```

### Why Re-Exports Don't Work

The current `reexport` command tries to create re-export modules like:

```python
# ffmpeg/streams/video.py
from ffmpeg.v8.streams.video import VideoStream
```

But this causes **circular import issues** because:
- `ffmpeg.v8.streams.video` imports `from ffmpeg.dag.nodes import FilterableStream`
- `ffmpeg.dag.nodes` imports `from ffmpeg.streams.video import VideoStream` (for type hints)
- Circular dependency!

## Solution: Import Redirection Strategy

Instead of re-exporting, make root modules **conditionally import from the latest version**.

### Approach

**Replace root generated files with import redirectors** that:
1. Import everything from the latest version submodule
2. Re-export with the same names
3. Use `__getattr__` for dynamic symbol access
4. Maintain module identity

### Implementation

#### Step 1: Create Import Redirector Template

```python
# Template for root module redirector
# Used by codegen to generate ffmpeg/streams/video.py, etc.

"""
{module_docstring}

This module re-exports all symbols from the latest FFmpeg version ({version}).
"""

# Import all public symbols from the versioned module
from ffmpeg.{version_prefix}.{submodule_path} import *  # noqa: F403, F401

# Make this module behave exactly like the versioned module
import sys
from ffmpeg.{version_prefix} import {submodule_path} as _versioned_module

# Redirect all attribute access to the versioned module
def __getattr__(name):
    return getattr(_versioned_module, name)

# Copy module-level attributes
__all__ = getattr(_versioned_module, '__all__', [])
__doc__ = _versioned_module.__doc__

# CRITICAL: Make classes use versioned module as their __module__
# This ensures CLASS_REGISTRY sees them as the same class
for _name in dir(_versioned_module):
    if not _name.startswith('_'):
        _obj = getattr(_versioned_module, _name)
        if isinstance(_obj, type):
            # Monkey-patch the class to appear from this module
            # This makes isinstance() work across import styles
            try:
                object.__setattr__(_obj, '__module__', __name__)
            except (AttributeError, TypeError):
                pass  # Some classes are immutable
```

Wait, that won't work either because changing `__module__` after class creation is problematic.

### Better Solution: Module Aliasing

Instead of creating new modules, make root module locations **alias** to the versioned modules in `sys.modules`.

```python
# ffmpeg/streams/__init__.py
import sys
from ffmpeg import versions

# Determine which version to use
_version = versions.default or '8'
_version_prefix = f'v{_version}'

# Import the versioned module
_versioned = __import__(f'ffmpeg.{_version_prefix}.streams', fromlist=[''])

# Make this module an alias to the versioned module
# This ensures ffmpeg.streams.video.VideoStream IS ffmpeg.v8.streams.video.VideoStream
sys.modules['ffmpeg.streams'] = _versioned

# For submodules, create aliases
for _submod in ['video', 'audio', 'av', 'subtitle']:
    _versioned_submod = f'ffmpeg.{_version_prefix}.streams.{_submod}'
    if _versioned_submod in sys.modules:
        sys.modules[f'ffmpeg.streams.{_submod}'] = sys.modules[_versioned_submod]
```

This approach:
- ✅ Makes `ffmpeg.streams.video` literally the same module as `ffmpeg.v8.streams.video`
- ✅ `isinstance()` checks work
- ✅ `CLASS_REGISTRY` has single entry per class
- ✅ Serialization works
- ✅ No circular imports (uses runtime aliasing, not import statements)

## Implementation Plan

### Phase 1: Create Redirector System

1. **Create `ffmpeg/__init__.py` hook** that sets up module aliasing:
   ```python
   # ffmpeg/__init__.py (add at end)
   from ffmpeg._setup_redirects import setup_module_redirects
   setup_module_redirects()
   ```

2. **Create `ffmpeg/_setup_redirects.py`**:
   ```python
   import sys
   from pathlib import Path
   
   def setup_module_redirects():
       """Redirect root ffmpeg.X imports to ffmpeg.vN.X for the latest version."""
       from ffmpeg import versions
       
       version = versions.default
       if not version:
           return  # No versions available
       
       version_prefix = f'v{version}'
       
       # Modules to redirect
       redirects = {
           'ffmpeg.streams': f'ffmpeg.{version_prefix}.streams',
           'ffmpeg.codecs': f'ffmpeg.{version_prefix}.codecs', 
           'ffmpeg.formats': f'ffmpeg.{version_prefix}.formats',
           'ffmpeg.options': f'ffmpeg.{version_prefix}.options',
       }
       
       for root_module, versioned_module in redirects.items():
           # Import versioned module
           try:
               __import__(versioned_module)
               # Alias root module to versioned module
               sys.modules[root_module] = sys.modules[versioned_module]
           except ImportError:
               pass  # Version might not have this module
   ```

3. **Update filters.py and sources.py** to use import redirects instead of re-exports.

### Phase 2: Update CLASS_REGISTRY

Update `serialize.py` to handle version-prefixed class names:

```python
def serializable(cls):
    # Register both with and without version prefix
    name = cls.__name__
    CLASS_REGISTRY[name] = cls
    
    # If class is from versioned module, register version-prefixed name too
    module = cls.__module__
    if module.startswith('ffmpeg.v') and '.' in module:
        version_prefix = module.split('.')[1]  # 'v8'
        CLASS_REGISTRY[f"{version_prefix}.{name}"] = cls
    
    return cls
```

### Phase 3: Testing

1. Test class identity:
   ```python
   from ffmpeg.streams.video import VideoStream as RootVS
   from ffmpeg.v8.streams.video import VideoStream as V8VS
   assert RootVS is V8VS  # Should pass!
   ```

2. Test isinstance:
   ```python
   stream = V8VS(...)
   assert isinstance(stream, RootVS)  # Should pass!
   ```

3. Test serialization:
   ```python
   stream = RootVS(...)
   data = stream.to_dict()
   restored = load_class("VideoStream")
   assert type(restored) is RootVS
   ```

## Pros and Cons

### Module Aliasing Approach

**Pros:**
- ✅ True class identity (same class object)
- ✅ No circular imports
- ✅ Works with isinstance() and CLASS_REGISTRY
- ✅ Simple implementation
- ✅ No code generation needed

**Cons:**
- ❌ Relies on sys.modules manipulation (somewhat magical)
- ❌ May confuse some IDEs (though should work)
- ❌ Users can't import both root and versioned simultaneously

### Alternative: Shared Base Classes

**Pros:**
- ✅ Explicit class hierarchy
- ✅ Can import both root and versioned

**Cons:**
- ❌ Requires major refactoring
- ❌ isinstance() still needs updating everywhere
- ❌ Doesn't solve CLASS_REGISTRY single-entry problem

## Decision

**Go with Module Aliasing** because:
1. Minimal code changes
2. Solves all problems (class identity, isinstance, CLASS_REGISTRY)
3. Clean user experience (imports "just work")
4. No generation complexity

## Success Criteria

- `from ffmpeg.streams.video import VideoStream` gives exact same class as `from ffmpeg.v8.streams.video import VideoStream`
- `isinstance()` checks work across import styles
- `CLASS_REGISTRY` has single entry per class
- Serialization roundtrips correctly
- All existing tests pass
- New tests verify class identity
