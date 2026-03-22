# CI/CD Status for Monorepo

**Date:** 2026-03-22  
**Branch:** `refactor/monorepo-architecture`  
**Status:** ✅ Workflows Created and Pushed

---

## Overview

GitHub Actions workflows have been created and configured for the monorepo architecture.

## Workflows Created

### 1. CI Monorepo - Test ✅

**File:** `.github/workflows/ci-monorepo-test.yml`

**What it does:**
- Tests core package on Python 3.10, 3.11, 3.12
- Tests v8 package on Python 3.10, 3.11, 3.12
- Runs integration tests
- Uploads coverage to Codecov

**Triggers:**
- Push to `main` or `refactor/monorepo-architecture`
- Pull requests to `main`
- Changes to `packages/**` or `pyproject-workspace.toml`

**Status:** Ready to run

### 2. CI Monorepo - Lint ✅

**File:** `.github/workflows/ci-monorepo-lint.yml`

**What it does:**
- Runs prek linter on all packages
- Checks for invalid imports (e.g., `ffmpeg_core.dag` in core)
- Detects circular import warnings

**Triggers:**
- Push to `main` or `refactor/monorepo-architecture`
- Pull requests to `main`
- Changes to `packages/**` or `pyproject-workspace.toml`

**Status:** Ready to run

### 3. Publish Monorepo Packages ✅

**File:** `.github/workflows/monorepo-publish.yml`

**What it does:**
- Builds all packages in dependency order
- Can publish to TestPyPI first
- Publishes to production PyPI
- Creates release notes

**Triggers:**
- Manual workflow dispatch
- Release published

**Status:** Ready (needs secrets configured)

## Required Configuration

### GitHub Secrets Needed

Before publishing, configure these secrets in GitHub Settings → Secrets:

1. **PYPI_API_TOKEN** (Required for publishing)
   - Get from: https://pypi.org/manage/account/token/
   - Scope: Entire account or specific projects

2. **TEST_PYPI_API_TOKEN** (Recommended for testing)
   - Get from: https://test.pypi.org/manage/account/token/
   - Scope: Entire account

3. **CODECOV_TOKEN** (Optional, for coverage)
   - Get from: https://codecov.io/
   - Only needed if using Codecov

### How to Configure Secrets

```bash
# Using GitHub web interface:
# 1. Go to https://github.com/livingbio/typed-ffmpeg/settings/secrets/actions
# 2. Click "New repository secret"
# 3. Add each secret

# Or using gh CLI:
gh secret set PYPI_API_TOKEN
gh secret set TEST_PYPI_API_TOKEN
gh secret set CODECOV_TOKEN
```

## Testing the Workflows

### Check Workflow Status

**Option 1: GitHub Web Interface**
1. Go to: https://github.com/livingbio/typed-ffmpeg/actions
2. Look for workflow runs on `refactor/monorepo-architecture` branch
3. Click on a run to see details

**Option 2: gh CLI**
```bash
# List recent workflow runs
gh run list --branch refactor/monorepo-architecture

# View specific run
gh run view <run-id>

# Watch a run in real-time
gh run watch
```

### Expected Workflow Runs

After the trigger commit (62757fe3), you should see:

- ✅ **CI Monorepo - Test** (triggered by packages/core/README.md change)
- ✅ **CI Monorepo - Lint** (triggered by packages/core/README.md change)

### What to Look For

**In Test Workflow:**
- [ ] Core tests pass on all Python versions
- [ ] V8 tests pass on all Python versions  
- [ ] Integration tests pass
- [ ] Coverage uploaded successfully

**In Lint Workflow:**
- [ ] Prek runs without errors
- [ ] No invalid import checks fail
- [ ] No circular import warnings

## Current Status

### Workflows Pushed ✅
- All 3 workflows committed and pushed
- Documentation created (.github/WORKFLOWS.md)
- Trigger commit sent

### Next Steps

1. **Monitor First Run** ⏳
   - Check https://github.com/livingbio/typed-ffmpeg/actions
   - Verify workflows trigger correctly
   - Review any failures

2. **Fix Any Issues** (if needed)
   - Adjust workflow configuration
   - Update package dependencies
   - Fix test failures

3. **Configure Secrets** ⏳
   - Add PYPI_API_TOKEN
   - Add TEST_PYPI_API_TOKEN (optional)
   - Add CODECOV_TOKEN (optional)

4. **Test Publishing** ⏳
   - Run manual workflow dispatch
   - Choose "test-pypi: true"
   - Verify packages install from TestPyPI

5. **Production Release** ⏳
   - Create a GitHub release
   - Workflows automatically publish
   - Verify on PyPI

## Known Issues

### Potential Issues to Watch

1. **uv sync might fail**
   - Solution: Check pyproject-workspace.toml is valid
   - Verify all package dependencies are correct

2. **Import tests might fail**
   - Solution: Ensure PYTHONPATH includes both src and ../core/src
   - Check all imports are using correct paths

3. **Coverage upload might fail**
   - Solution: Verify CODECOV_TOKEN is set
   - Check coverage.xml files are generated

4. **FFmpeg not found**
   - Solution: Workflow includes apt-get install ffmpeg
   - Should work on ubuntu-latest

## Monitoring Commands

```bash
# Check latest workflow status
gh run list --limit 5

# View logs for failed run
gh run view <run-id> --log-failed

# Re-run failed jobs
gh run rerun <run-id> --failed

# Watch current run
gh run watch
```

## Success Criteria

Workflows are successful when:

- ✅ All tests pass on all Python versions (3.10, 3.11, 3.12)
- ✅ Lint checks pass with no errors
- ✅ Integration tests confirm import system works
- ✅ Coverage reports upload successfully
- ✅ No circular import warnings detected

## Documentation

Full workflow documentation available at:
- `.github/WORKFLOWS.md` - Complete guide
- This file - Current status

## Links

- **Workflows:** https://github.com/livingbio/typed-ffmpeg/actions
- **Branch:** https://github.com/livingbio/typed-ffmpeg/tree/refactor/monorepo-architecture
- **Codecov:** https://codecov.io/gh/livingbio/typed-ffmpeg (if configured)

---

**Summary:** All CI workflows are created, committed, and pushed. Waiting for first run results.

**Action Required:** 
1. Monitor workflow runs
2. Configure secrets for publishing
3. Fix any failures that appear
