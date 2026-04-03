#!/bin/bash
# Verification script for hardware acceleration support in FFmpeg Docker image
#
# Usage:
#   ./verify-hardware-accel.sh [image-name]
#
# Example:
#   ./verify-hardware-accel.sh ffmpeg:8.0-hw

set -e

IMAGE="${1:-ffmpeg:8.0}"

echo "============================================================"
echo "FFmpeg Hardware Acceleration Verification"
echo "Image: $IMAGE"
echo "============================================================"
echo ""

# Check if image exists
if ! docker image inspect "$IMAGE" > /dev/null 2>&1; then
    echo "❌ Error: Image '$IMAGE' not found"
    echo "   Build it first with:"
    echo "   docker build -f Dockerfile.8.0 -t $IMAGE ."
    exit 1
fi

echo "✅ Image found"
echo ""

# 1. Check FFmpeg version
echo "=== FFmpeg Version ==="
docker run --rm "$IMAGE" -version 2>&1 | head -5
echo ""

# 2. Check hardware acceleration methods
echo "=== Hardware Acceleration Methods ==="
docker run --rm "$IMAGE" -hwaccels 2>&1 | tail -n +2
echo ""

# 3. Check QSV encoders
echo "=== Intel QSV Encoders ==="
QSV_ENCODERS=$(docker run --rm "$IMAGE" -encoders 2>&1 | grep qsv || echo "None found")
if echo "$QSV_ENCODERS" | grep -q "h264_qsv"; then
    echo "✅ QSV encoders available:"
    echo "$QSV_ENCODERS"
else
    echo "❌ QSV encoders NOT found"
    echo "   Expected: h264_qsv, hevc_qsv, av1_qsv, etc."
fi
echo ""

# 4. Check VAAPI encoders
echo "=== VAAPI Encoders ==="
VAAPI_ENCODERS=$(docker run --rm "$IMAGE" -encoders 2>&1 | grep vaapi || echo "None found")
if echo "$VAAPI_ENCODERS" | grep -q "h264_vaapi"; then
    echo "✅ VAAPI encoders available:"
    echo "$VAAPI_ENCODERS"
else
    echo "❌ VAAPI encoders NOT found"
fi
echo ""

# 5. Check NVENC encoders
echo "=== NVIDIA NVENC Encoders ==="
NVENC_ENCODERS=$(docker run --rm "$IMAGE" -encoders 2>&1 | grep nvenc || echo "None found")
if echo "$NVENC_ENCODERS" | grep -q "h264_nvenc"; then
    echo "✅ NVENC encoders available:"
    echo "$NVENC_ENCODERS"
else
    echo "⚠️  NVENC encoders not found (requires NVIDIA GPU)"
fi
echo ""

# 6. Check hardware filters
echo "=== Hardware Filters ==="
echo ""
echo "QSV Filters:"
QSV_FILTERS=$(docker run --rm "$IMAGE" -filters 2>&1 | grep qsv || echo "None found")
if echo "$QSV_FILTERS" | grep -q "scale_qsv"; then
    echo "✅ $QSV_FILTERS"
else
    echo "❌ No QSV filters found"
fi
echo ""

echo "VAAPI Filters:"
VAAPI_FILTERS=$(docker run --rm "$IMAGE" -filters 2>&1 | grep vaapi | head -5)
if [ -n "$VAAPI_FILTERS" ]; then
    echo "✅ $VAAPI_FILTERS"
    echo "   ... and more"
else
    echo "❌ No VAAPI filters found"
fi
echo ""

echo "CUDA Filters:"
CUDA_FILTERS=$(docker run --rm "$IMAGE" -filters 2>&1 | grep cuda || echo "None found")
if echo "$CUDA_FILTERS" | grep -q "scale_cuda"; then
    echo "✅ $CUDA_FILTERS"
else
    echo "⚠️  No CUDA filters found (requires NVIDIA GPU at build time)"
fi
echo ""

# 7. Summary
echo "============================================================"
echo "Summary"
echo "============================================================"
echo ""

SUCCESS=0
TOTAL=0

check_feature() {
    local feature=$1
    local check_cmd=$2
    TOTAL=$((TOTAL + 1))
    
    if eval "$check_cmd" > /dev/null 2>&1; then
        echo "✅ $feature"
        SUCCESS=$((SUCCESS + 1))
    else
        echo "❌ $feature"
    fi
}

check_feature "Intel QSV Support" "docker run --rm '$IMAGE' -encoders 2>&1 | grep -q h264_qsv"
check_feature "VAAPI Support" "docker run --rm '$IMAGE' -encoders 2>&1 | grep -q h264_vaapi"
check_feature "Vulkan Support" "docker run --rm '$IMAGE' -hwaccels 2>&1 | grep -q vulkan"
check_feature "OpenCL Support" "docker run --rm '$IMAGE' -version 2>&1 | grep -q opencl"

echo ""
echo "Score: $SUCCESS/$TOTAL features available"
echo ""

if [ $SUCCESS -eq $TOTAL ]; then
    echo "🎉 All expected hardware acceleration features are available!"
    exit 0
elif [ $SUCCESS -gt 0 ]; then
    echo "⚠️  Some hardware acceleration features are available"
    echo "   (NVIDIA features may require GPU at runtime)"
    exit 0
else
    echo "❌ No hardware acceleration features found"
    exit 1
fi
