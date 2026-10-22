#!/bin/bash
set -euo pipefail

kit_root=$(cd "$(dirname "$0")/.." && pwd)
source_only=false
if [[ "${1:-}" == --source-only ]]; then
    source_only=true
    shift
fi
if [[ $# -gt 1 ]]; then
    echo "Usage: $0 [--source-only] [empty-destination]" >&2
    exit 1
fi
destination=${1:-"$kit_root/build/Compositor"}
upstream_tag=v1.5.5
upstream_commit=b31ea029762ecb782699df971e1412168602a44d
model_sha=935d8c71cdf1e6c2f7941d5ee8c5f4cc4e93363e785d2da7f0ca83cc44981ae2

if [[ -e "$destination" ]]; then
    echo "Destination already exists; choose a new empty path: $destination" >&2
    exit 1
fi
python3 "$kit_root/scripts/sync-workflow-patch.py" --check
mkdir -p "$(dirname "$destination")"
git clone --quiet --depth 1 --branch "$upstream_tag" https://github.com/robbietilton/Compositor.git "$destination"
actual_commit=$(git -C "$destination" rev-parse HEAD)
if [[ "$actual_commit" != "$upstream_commit" ]]; then
    echo "Upstream commit mismatch; stopping before applying the patch." >&2
    exit 1
fi
git -C "$destination" apply --check "$kit_root/patches/ventura-1.5.5.patch"
git -C "$destination" apply --binary "$kit_root/patches/ventura-1.5.5.patch"

python3 "$kit_root/scripts/check-prepared-source.py" "$destination"
if $source_only; then
    echo "Prepared source only (model not downloaded; not ready to build): $destination"
    exit 0
fi

model="$destination/Compositor/Resources/Models/DeepLabV3Int8LUT.mlmodel"
mkdir -p "$(dirname "$model")"
curl --fail --location --retry 3 \
    https://ml-assets.apple.com/coreml/models/Image/ImageSegmentation/DeepLabV3/DeepLabV3Int8LUT.mlmodel \
    -o "$model.download"
python3 - "$model.download" "$model_sha" <<'PY'
import hashlib, sys
from pathlib import Path
actual = hashlib.sha256(Path(sys.argv[1]).read_bytes()).hexdigest()
if actual != sys.argv[2]:
    sys.exit(f"Model checksum mismatch: {actual}")
PY
mv "$model.download" "$model"
echo "Prepared Compositor 1.5.5 / Ventura candidate build 51.1 in: $destination"
echo "Build and macOS 13 runtime validation are still required."
echo "Original application: https://github.com/robbietilton/Compositor"
echo "On a supported build Mac with Xcode 26.6, run scripts/build-ventura.sh inside that directory."
