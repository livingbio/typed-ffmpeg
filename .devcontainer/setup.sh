# Install dependencies
poetry install --with dev
poetry run pre-commit install --install-hooks

# Setup GitHub CLI if available
if command -v gh &> /dev/null; then
  echo "GitHub CLI is installed, you can authenticate with 'gh auth login'"
fi
