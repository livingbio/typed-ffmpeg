#!/bin/bash
# Setup development environment for the monorepo

set -e

echo "🔧 Setting up typed-ffmpeg monorepo development environment..."
echo

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✅ uv is installed"
echo

# Install extract package
echo "📦 Installing extract package..."
cd packages/extract
uv pip install -e ".[dev]"
cd ../..
echo

# Install codegen package
echo "📦 Installing codegen package..."
cd packages/codegen
uv pip install -e ".[dev]"
cd ../..
echo

# Install Python SDK package
echo "📦 Installing Python SDK package..."
cd packages/python
uv pip install -e ".[dev]"
cd ../..
echo

# Install pre-commit hooks (if available)
if [ -f .pre-commit-config.yaml ]; then
    echo "🪝 Installing pre-commit hooks..."
    pre-commit install
    echo
fi

# Verify installations
echo "🔍 Verifying installations..."
python -c "import ffmpeg_extract; print('✅ ffmpeg-extract imported successfully')"
python -c "import ffmpeg_codegen; print('✅ ffmpeg-codegen imported successfully')"
python -c "import ffmpeg; print('✅ typed-ffmpeg imported successfully')"
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Workspace setup complete!"
echo
echo "Next steps:"
echo "  - Run tests: ./scripts/test-all.sh"
echo "  - Develop extract: cd packages/extract"
echo "  - Develop codegen: cd packages/codegen"
echo "  - Develop Python SDK: cd packages/python"
echo
echo "Happy coding! 🚀"
