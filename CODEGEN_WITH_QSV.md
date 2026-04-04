# Regenerating FFmpeg 8.0 Bindings with QSV Support

## Current Situation

- PR #890 adds Intel QSV support to `Dockerfile.8.0`
- Current FFmpeg 8.0 Docker image does **not** have QSV filters
- We need to rebuild the Docker image first, then regenerate bindings

## Required Steps

### Step 1: Merge PR #890 (or push Dockerfile to main)

**Option A: Merge PR** (recommended)
```bash
# Review and merge PR #890
gh pr merge 890 --squash
```

**Option B: Direct push to main** (if you have access and want to skip PR review)
```bash
git checkout main
git pull origin main
git merge feat/hardware-acceleration --ff-only
git push origin main
```

### Step 2: Build New FFmpeg 8.0 Docker Image

After merging, the Docker build workflow will trigger automatically (it watches `docker/ffmpeg-builder/Dockerfile.*`).

**Or trigger manually:**
```bash
gh workflow run build-ffmpeg-images.yml --ref main -f ffmpeg-version=8.0
```

**Monitor build:**
```bash
gh run watch
# or
gh run list --workflow=build-ffmpeg-images.yml --limit 5
```

**Expected build time:** ~20-30 minutes

**Verify the new image has QSV:**
```bash
docker pull ghcr.io/livingbio/typed-ffmpeg/ffmpeg:8.0
docker run --rm ghcr.io/livingbio/typed-ffmpeg/ffmpeg:8.0 -filters 2>&1 | grep qsv
```

Expected output:
```
 ... scale_qsv         V->V       Scale using Intel Quick Sync Video
 ... overlay_qsv       VV->V      Overlay using Intel Quick Sync Video
 ... deinterlace_qsv   V->V       Deinterlace using Intel Quick Sync Video
 ... vpp_qsv           V->V       Quick Sync Video VPP
```

### Step 3: Regenerate FFmpeg 8.0 Bindings

Once the Docker image is ready, trigger codegen:

```bash
gh workflow run ci-codegen-versions.yml --ref main -f ffmpeg-version=8 -f create_pr=true
```

This will:
1. Pull the new `ghcr.io/livingbio/typed-ffmpeg/ffmpeg:8.0` image (with QSV)
2. Extract FFmpeg binary and libraries
3. Run `python -m scripts.code_gen.cli generate` for v8
4. Create a PR with the regenerated bindings

**Monitor codegen:**
```bash
gh run watch
```

**Expected changes:**
- New filter functions in `packages/v8/src/ffmpeg/filters.py`:
  - `scale_qsv()`
  - `overlay_qsv()`
  - `deinterlace_qsv()`
  - `vpp_qsv()`
- Updated filter count in cache JSON

### Step 4: Review and Merge Codegen PR

The codegen workflow will create a PR with title like:
```
chore: regenerate FFmpeg bindings for v8
```

Review the changes and merge.

## Alternative: Local Codegen (if you have QSV-enabled FFmpeg)

If you have an FFmpeg 8.0 binary with QSV support installed locally:

```bash
# Check your FFmpeg has QSV
ffmpeg -filters 2>&1 | grep qsv

# Generate bindings
cd typed-ffmpeg
python -m scripts.code_gen.cli generate \
  --outpath packages/v8/src/ffmpeg \
  --ffmpeg-binary $(which ffmpeg) \
  --rebuild

# Test
cd packages/v8
uv sync
uv run pytest tests/
```

## Expected Filter Additions

After codegen with QSV support, FFmpeg 8.0 should gain:

| Filter | Type | Description |
|--------|------|-------------|
| `scale_qsv` | Video | Hardware-accelerated scaling via Intel QSV |
| `overlay_qsv` | Video | Hardware-accelerated overlay via Intel QSV |
| `deinterlace_qsv` | Video | Hardware-accelerated deinterlacing via Intel QSV |
| `vpp_qsv` | Video | Intel QSV Video Post-Processing |

Plus encoders (not filters, but available via `-c:v` option):
- `h264_qsv`, `hevc_qsv`, `av1_qsv`, `vp9_qsv`, `mjpeg_qsv`, `mpeg2_qsv`

## Troubleshooting

### Docker build fails
Check the workflow logs:
```bash
gh run view --log-failed
```

### Codegen doesn't detect new filters
Verify the Docker image was updated:
```bash
docker pull ghcr.io/livingbio/typed-ffmpeg/ffmpeg:8.0
docker run --rm ghcr.io/livingbio/typed-ffmpeg/ffmpeg:8.0 -buildconf 2>&1 | grep -i qsv
```

Should show:
```
--enable-libmfx
--enable-libvpl
```

### PR not created
Check if `create_pr=true` was set:
```bash
gh run view <run-id> --log
```

## Timeline Estimate

1. Merge PR #890: **5 minutes**
2. Docker build: **20-30 minutes**
3. Codegen: **5-10 minutes**
4. Review + merge codegen PR: **5 minutes**

**Total: ~40-50 minutes**

## Quick Command Summary

```bash
# 1. Merge Dockerfile changes
gh pr merge 890 --squash

# 2. Wait for Docker build to complete (automatic), or trigger manually:
gh workflow run build-ffmpeg-images.yml --ref main -f ffmpeg-version=8.0
gh run watch  # monitor progress

# 3. Verify image
docker pull ghcr.io/livingbio/typed-ffmpeg/ffmpeg:8.0
docker run --rm ghcr.io/livingbio/typed-ffmpeg/ffmpeg:8.0 -filters 2>&1 | grep qsv

# 4. Trigger codegen
gh workflow run ci-codegen-versions.yml --ref main -f ffmpeg-version=8 -f create_pr=true
gh run watch  # monitor progress

# 5. Merge codegen PR
gh pr list --search "regenerate FFmpeg bindings"
gh pr merge <pr-number> --squash
```
