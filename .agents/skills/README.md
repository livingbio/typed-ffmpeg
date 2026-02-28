# Agent Skills (Universal)

This directory contains universal agent skills compatible with all agent systems following the [Agent Skills Specification](https://agentskills.io/specification).

## About This Location

Skills in `.agents/skills/` are recognized by:
- Any AI agent supporting the open Agent Skills standard
- GitHub Copilot
- Claude/Anthropic systems
- Cursor
- Other compatible AI development tools

This is part of a multi-location strategy to support all major agent systems. The same skill is also available in:
- `.github/skills/` - For GitHub Copilot and general use
- `.claude/skills/` - For Claude/Anthropic-specific tools

## Available Skills

### typed-ffmpeg-usage

Comprehensive guide for using typed-ffmpeg, a modern Python FFmpeg wrapper with extensive typing support.

**Location**: [typed-ffmpeg-usage/SKILL.md](typed-ffmpeg-usage/SKILL.md)

## Maintenance

Skills are maintained in sync across all three locations (`.github/skills/`, `.claude/skills/`, `.agents/skills/`) to ensure consistent experience across different AI agent systems.

## Standards Compliance

All skills in this directory follow the Agent Skills Specification:
- YAML frontmatter with required metadata
- Markdown-formatted instructions
- Lowercase, hyphenated directory names (max 64 characters)
- Directory name matches skill `name` in frontmatter

For more information, see:
- [Agent Skills Specification](https://agentskills.io/specification)
- [Agent Skills Directory](https://www.skillsdirectory.org/)
