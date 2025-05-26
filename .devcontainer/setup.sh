#!/bin/bash

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
uv pip install -e .

# Install pre-commit hooks
pre-commit install --install-hooks

# Setup GitHub CLI if available
if command -v gh &> /dev/null; then
  echo "GitHub CLI is installed, you can authenticate with 'gh auth login'"
fi
