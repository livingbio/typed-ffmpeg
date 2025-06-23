#!/bin/bash

# Create and activate virtual environment
uv venv
# Install dependencies
uv pip install -r requirements.in
uv pip install -e .

# Install pre-commit hooks
uv run pre-commit install --install-hooks

# Setup GitHub CLI if available
if command -v gh &> /dev/null; then
  echo "GitHub CLI is installed, you can authenticate with 'gh auth login'"
fi
