# Changelog

Upstream application releases and Ventura packaging revisions are distinct. The current release is **1.5.5 / 51.1**; the previous release **1.5.3 / 49.2** remains available.

## v1.5.5-ventura.1 — 2026-10-24

- Rebase the Ventura patch onto upstream v1.5.5 commit `b31ea029762ecb782699df971e1412168602a44d`.
- Retain RGB Split, Progressive Blur/Bloom/RGB Split adjustment layers, Channel Pack, PSD artboards and the intervening 1.5.4 improvements.
- Resolve Xcode version/target, editor-state and export conflicts; keep the character-based shortcut crash fix alongside non-Latin layout support.
- Convert the new PenInput state to Combine; publish line style/cap and artboard tab-name changes, with observation regression tests.
- Keep the readable and embedded CI patches synchronized; validate clean patch application on Linux before Mac builds.
- Expand selected Mac tests from eight to twenty suites; continue checking both Release architectures, minimum OS, signing and startup on the build host.

Validation: 153 logical tests / 201 executions passed; both Release architectures passed build-host startup checks. On 24 October 2026 the maintainer confirmed launch and initial use on Intel macOS 13.7.8 (22H730). The release reuses the exact tested CI application ZIP. Full feature coverage and native Apple Silicon on Ventura remain unconfirmed; see [TESTING.md](docs/TESTING.md).

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
