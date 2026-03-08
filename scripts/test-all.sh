#!/bin/bash
# Test all packages in the monorepo

set -e

echo "🧪 Testing all packages in monorepo..."
echo

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Track failures
FAILED=0

# Test extract package
echo "📦 Testing extract package..."
cd packages/extract
if pytest tests/ -v; then
    echo -e "${GREEN}✅ Extract tests passed${NC}"
else
    echo -e "${RED}❌ Extract tests failed${NC}"
    FAILED=1
fi
cd ../..
echo

# Test codegen package
echo "📦 Testing codegen package..."
cd packages/codegen
if pytest tests/ -v; then
    echo -e "${GREEN}✅ Codegen tests passed${NC}"
else
    echo -e "${RED}❌ Codegen tests failed${NC}"
    FAILED=1
fi
cd ../..
echo

# Test Python SDK package
echo "📦 Testing Python SDK package..."
cd packages/python
if pytest tests/ -v; then
    echo -e "${GREEN}✅ Python SDK tests passed${NC}"
else
    echo -e "${RED}❌ Python SDK tests failed${NC}"
    FAILED=1
fi
cd ../..
echo

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}❌ Some tests failed${NC}"
    exit 1
fi
