# typed-ffmpeg TypeScript Demo

A sample project demonstrating how to use the `@typed-ffmpeg/v8` package to build FFmpeg filter graphs with full type safety.

## Setup

```bash
npm install
```

## Run

```bash
npm run dev
```

This compiles the TypeScript source and runs the demo, printing the generated FFmpeg commands for each example.

## Examples

| # | Description |
|---|-------------|
| 1 | Simple transcode with codec options |
| 2 | Scale video with type-safe filter parameters |
| 3 | Chain multiple video filters (hflip, scale, drawbox) |
| 4 | Overlay an image on a video |
| 5 | Audio processing (volume, echo) |
| 6 | Multiple outputs at different resolutions |
| 7 | Input options (seeking, duration) |
| 8 | Compile to argument list for programmatic use |

## Notes

- FFmpeg does **not** need to be installed to compile filter graphs. It is only needed if you call `.run()` to execute the command.
- All filter methods have full JSDoc documentation and IDE autocomplete support.
- Replace `@typed-ffmpeg/v8` with `@typed-ffmpeg/v5`, `v6`, or `v7` to target a different FFmpeg version.
