# Changelog

Upstream application releases and Ventura packaging revisions are distinct. The application version remains **1.5.3**; **49.2** is this port's build number.

## v1.5.3-ventura.2 — 2026-10-18

First public release of the Ventura port, based on official Compositor v1.5.3.

- Fix the macOS 13 startup crash caused by the unavailable SwiftUI `KeyEquivalent` equality conformance. Compare key characters instead.
- Reject that protocol-conformance dependency in both Release executable slices during packaging.
- Test all default shortcuts, Delete normalization, navigation and Unicode characters.
- Build a universal Intel/Apple Silicon app with minimum target macOS 13.0.
- Adapt observation, UI APIs, Camera Raw cache locking and foreground segmentation to Ventura.
- Preserve bitmap edge pixels and model-input orientation in the segmentation fallback.
- Disable the upstream automatic update feed for this compatibility build.
- Retain the original application license and third-party attribution.

Validation: 71 tests passed; both Release slices passed a startup check on macOS 26.6.2. The maintainer subsequently confirmed launch and initial use on Intel macOS 13.7.8. See [TESTING.md](docs/TESTING.md) for limits.

## Internal build 49 — not recommended

The initial experimental build compiled and passed its selected tests on newer macOS, but failed at startup on Ventura. It is superseded by **49.2** and is not the public download.
