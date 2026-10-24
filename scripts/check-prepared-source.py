#!/usr/bin/env python3
"""Check the pinned source and Ventura port invariants without requiring Xcode.

These checks do not establish compilation or runtime compatibility.
"""
from pathlib import Path
import plistlib
import re
import subprocess
import sys


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def check(source):
    kit = Path(__file__).resolve().parent.parent
    prepare = (kit / "scripts/prepare-source.sh").read_text()
    expected = re.search(r"^upstream_commit=([0-9a-f]{40})$", prepare, re.M).group(1)
    head = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
    require(head == expected, f"Wrong upstream commit: {head}, expected {expected}")
    workflow = (kit / ".github/workflows/ventura-build.yml").read_text()
    refs = re.findall(r"^\s+ref: ([0-9a-f]{40})$", workflow, re.M)
    require(len(refs) == 2 and set(refs) == {expected}, "CI and local upstream pins differ")
    patch = kit / "patches/ventura-1.5.5.patch"
    subprocess.run(["git", "-C", str(source), "apply", "--reverse", "--check", str(patch)], check=True)

    project = (source / "Compositor.xcodeproj/project.pbxproj").read_text()
    for setting, value in [("MACOSX_DEPLOYMENT_TARGET", "13.0"),
                           ("MARKETING_VERSION", "1.5.5"), ("CURRENT_PROJECT_VERSION", "51.1")]:
        values = re.findall(rf"\b{setting} = ([^;]+);", project)
        require(values and set(values) == {value}, f"Unexpected {setting}: {values}")
    require('ARCHS = arm64;' not in project and 'ARCHS = "$(ARCHS_STANDARD)";' in project,
            "Universal architecture setting is missing")
    info = plistlib.loads((source / "Config/Info.plist").read_bytes())
    require(not info.get("SUEnableAutomaticChecks", False) and not info.get("SUFeedURL"),
            "Upstream automatic update feed must remain disabled")
    for path in (source / "Compositor").rglob("*.swift"):
        text = path.read_text()
        require(not re.search(r"import Observation\b|@(?:Observable|ObservationIgnored|Bindable)\b", text),
                f"Observation dependency remains in {path.relative_to(source)}")
        require(not re.search(r"^(?:<<<<<<< |=======$|>>>>>>> )", text, re.M),
                f"Merge conflict remains in {path.relative_to(source)}")
    print(f"PASS: pinned 1.5.5 source, patch reversibility, universal settings and Ventura observation checks ({head}).")
    print("Xcode tests, a Release build and runtime checks on macOS 13 are still required.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: check-prepared-source.py /path/to/prepared/Compositor")
    check(Path(sys.argv[1]).resolve())
