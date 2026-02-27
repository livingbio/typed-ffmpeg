# Agent Skills

This directory contains agent skills for the typed-ffmpeg project. Skills help AI agents (like GitHub Copilot) understand how to effectively use this package.

## Available Skills

### typed-ffmpeg-usage

**Description**: Comprehensive guide for using typed-ffmpeg, a modern Python FFmpeg wrapper with extensive typing support.

**When to use**: Use this skill when working with:
- FFmpeg operations in Python
- Video/audio processing and transcoding
- Filter graphs and complex filters
- Media file analysis with ffprobe
- Type-safe media processing workflows

**Location**: [.github/skills/typed-ffmpeg-usage/SKILL.md](typed-ffmpeg-usage/SKILL.md)

## About Agent Skills

Agent skills follow the [Agent Skills Specification](https://agentskills.io/specification) and can be used by:
- GitHub Copilot in VS Code
- GitHub Copilot CLI
- Claude and other compatible AI agents

Each skill is stored in its own subdirectory with a `SKILL.md` file containing:
- YAML frontmatter with metadata
- Comprehensive instructions and examples
- Best practices and common patterns
- Type safety guidelines

## Adding New Skills

To add a new skill:

1. Create a new directory under `.github/skills/`
2. Name the directory with lowercase letters, numbers, and hyphens only
3. Create a `SKILL.md` file with proper YAML frontmatter
4. Ensure the `name` in frontmatter matches the directory name
5. Follow the [specification format](https://agentskills.io/specification)

Example structure:
```
.github/skills/
└── my-skill/
    └── SKILL.md
```
