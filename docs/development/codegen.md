# Code Generation

Typed-ffmpeg generates its filter/codec/format bindings by introspecting real FFmpeg binaries. Each version package (`v5`, `v6`, `v7`, `v8`) is generated from the corresponding FFmpeg major version.

## CI

In CI, code generation uses [`jrottenberg/ffmpeg`](https://hub.docker.com/r/jrottenberg/ffmpeg) Docker images — one per FFmpeg major version. See `.github/workflows/ci-codegen-versions.yml`.

## Local Development

For local code generation you need multiple FFmpeg versions installed side by side. On macOS, use Homebrew:

```bash
brew install ffmpeg@5 ffmpeg@6 ffmpeg@7 ffmpeg      # ffmpeg (no suffix) = latest (v8+)
```

Then invoke the generator by pointing `PATH` at the desired version:

```bash
# Generate bindings for FFmpeg 6
PATH="$(brew --prefix ffmpeg@6)/bin:$PATH" \
  python -m scripts.code_gen.cli generate --outpath packages/v6/src/ffmpeg --rebuild

# Generate bindings for FFmpeg 7
PATH="$(brew --prefix ffmpeg@7)/bin:$PATH" \
  python -m scripts.code_gen.cli generate --outpath packages/v7/src/ffmpeg --rebuild
```

Or export `FFMPEG_BINARY` if the codegen respects it:

```bash
FFMPEG_BINARY="$(brew --prefix ffmpeg@6)/bin/ffmpeg" \
  python -m scripts.code_gen.cli generate --outpath packages/v6/src/ffmpeg --rebuild
```

Verify which binary is active before generating:

```bash
PATH="$(brew --prefix ffmpeg@6)/bin:$PATH" ffmpeg -version | head -1
# ffmpeg version 6.1.x ...
```
