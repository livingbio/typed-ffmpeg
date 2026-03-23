# Shared Tests for typed-ffmpeg v5-v8

These tests are reused across all version packages (typed-ffmpeg-v5 through typed-ffmpeg-v8).

## Running tests

Run with the desired version's package installed and `TYPED_FFMPEG_VERSION` set:

```bash
# v8 (default)
uv sync --package typed-ffmpeg-v8
TYPED_FFMPEG_VERSION=v8 pytest packages/tests-shared -v

# v5
uv sync --package typed-ffmpeg-v5
TYPED_FFMPEG_VERSION=v5 pytest packages/tests-shared -v
```

Snapshots are stored per-version under `__snapshots__/{version}/` (e.g. `__snapshots__/v5/`).

## Skipping test_view

The `test_view` tests require graphviz. To skip them:

```bash
pytest packages/tests-shared -v -k "not test_view"
```
