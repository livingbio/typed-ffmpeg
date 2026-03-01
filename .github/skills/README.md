# Agent Skills

This directory contains agent skills for the typed-ffmpeg project. Skills help AI agents (like GitHub Copilot) understand how to effectively use this package.

## Multi-Location Support

To ensure compatibility with all major AI agent systems, skills are provided in three standard locations:

- **`.github/skills/`** (this directory) - GitHub Copilot, Cursor, and general use
- **`.claude/skills/`** - Claude/Anthropic systems (also recognized by Copilot)
- **`.agents/skills/`** - Universal, agent-agnostic location for any compliant system

All three locations contain the same skills, maintained in sync for consistent experience across different AI agents.

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
- **GitHub Copilot** (VS Code, CLI, Chat)
- **Claude** (Anthropic's AI assistant and SDK)
- **Cursor** (AI-powered code editor)
- **Gemini CLI** and other Google AI tools
- Any other agent system supporting the specification

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
