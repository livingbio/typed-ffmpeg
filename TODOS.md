# TODOS

## Multi-Version Support Follow-ups

### CI Auto-Generation Matrix
**What:** GitHub Actions workflow with FFmpeg version matrix (5.x, 6.x, 7.x, 8.x) that auto-generates typed bindings using Docker images.
**Why:** Achieves the "near-zero maintenance" goal — when FFmpeg 9.0 releases, CI generates new bindings automatically without manual intervention.
**Pros:** Eliminates manual code gen workflow, ensures bindings stay current, catches regressions across versions.
**Cons:** CI complexity increases, Docker image dependency, longer CI run times.
**Context:** The core multi-version submodule infrastructure must land first. CI workflow should use `jrottenberg/ffmpeg:X-ubuntu` Docker images and run `generate --ffmpeg-binary /usr/bin/ffmpeg --outpath src/ffmpeg/v{N}/`. Consider a scheduled weekly job plus on-demand trigger.
**Depends on:** Multi-version submodule implementation (version dirs, absolute imports, re-export modules).

### Schema Deduplication (parse_help vs code_gen)
**What:** Unify or create explicit adapters between the two parallel schema hierarchies — `parse_help.schema.FFMpegAVOption` and `code_gen.schema.FFMpegAVOption`.
**Why:** Both define similar dataclasses with different fields, causing conversion overhead in cli.py (the ~38-line option-wrapping blocks). A unified schema or adapter pattern would reduce confusion and the DRY violations.
**Pros:** Cleaner pipeline, less conversion code, easier to extend.
**Cons:** Refactoring risk — both schemas are load-bearing. Needs careful testing.
**Context:** The `load_codecs()` and `load_formats()` functions in cli.py contain nearly identical conversion blocks. The DRY helper extraction (decided in eng review) partially addresses this, but the root cause is the dual schema hierarchy.
**Depends on:** Nothing — can be done independently.

### Version Diff Tooling
**Status:** IN SCOPE — accepted as cherry-pick #5 in CEO review (2026-03-20). Now part of the multi-version plan as a migration CLI command (`typed-ffmpeg diff v6 v7`).
**What:** CLI command that compares generated outputs between FFmpeg versions and produces a human-readable report of added/removed/changed filters, codecs, and options.
**Why:** Helps users understand what changes when they switch FFmpeg versions. Also powers deprecation hints in generated docstrings.
**Context:** Implemented as `version_diff.py` in code_gen/, shared between the diff CLI command and the deprecation annotation pipeline.
