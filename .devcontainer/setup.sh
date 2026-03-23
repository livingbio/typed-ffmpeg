#!/bin/bash

# Create and activate virtual environment
uv venv
# Install dependencies
uv pip install -r requirements.txt
uv pip install -e .

# Install prek hooks
uv run prek install --install-hooks

# Setup GitHub CLI if available
if command -v gh &> /dev/null; then
  echo "GitHub CLI is installed, you can authenticate with 'gh auth login'"
fi
