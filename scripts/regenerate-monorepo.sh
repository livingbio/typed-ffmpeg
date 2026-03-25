#!/bin/bash
# Regenerate all version bindings for monorepo architecture

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

echo "🔄 Regenerating version bindings for monorepo..."
echo ""

# Array of versions to regenerate
VERSIONS=(5 6 7 8)

for VERSION in "${VERSIONS[@]}"; do
    echo "📦 Generating v${VERSION}..."
    
    # Output path: packages/v${VERSION}/src/
    # With --version-dir, it will create ffmpeg/ subdirectory automatically
    # But we want direct output to packages/v${VERSION}/src/ffmpeg/
    # So we need to use the parent directory as outpath
    OUTPATH="${REPO_ROOT}/packages/v${VERSION}/src"
    
    # NOTE: The generate command with --version-dir will:
    # 1. Create outpath/ffmpeg/ (not outpath/v{VERSION}/ffmpeg/)
    # 2. Use absolute imports from ffmpeg_core.* for shared modules
    # 3. Use relative imports for generated modules
    
    # For now, generate without --version-dir and we'll adjust imports manually
    # TODO: Fix the generate command to not create version subdir when in monorepo mode
    python -m scripts.code_gen.cli generate \
        --outpath "${OUTPATH}/ffmpeg" \
        --no-version-dir \
        --ffmpeg-binary "ffmpeg"
    
    echo "✅ Generated v${VERSION} → ${OUTPATH}/ffmpeg"
    echo ""
done

echo "🎉 All versions regenerated successfully!"
echo ""
echo "Next steps:"
echo "  1. Review generated code"
echo "  2. Run tests: pytest packages/"
echo "  3. Commit changes"
