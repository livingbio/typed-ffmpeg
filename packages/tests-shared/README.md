# Shared Tests for typed-ffmpeg v5-v8

These tests are reused across all version packages (typed-ffmpeg-v5 through typed-ffmpeg-v8).
Snapshots are identical across versions and stored in a single `__snapshots__/` dir.

## Running tests

Run with the desired version's package installed:

```bash
# v8
uv sync --package typed-ffmpeg-v8
pytest packages/tests-shared -v

# v5
uv sync --package typed-ffmpeg-v5
pytest packages/tests-shared -v
```

## Skipping test_view

The `test_view` tests require graphviz. To skip them:

```bash
pytest packages/tests-shared -v -k "not test_view"
```
