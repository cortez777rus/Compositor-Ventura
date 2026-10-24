# Compatibility notes

Target: macOS 13.0 or later, Intel and Apple Silicon. The current release is 1.5.5 / 51.1. Launch and initial use on Intel macOS 13.7.8 (22H730) were confirmed on 24 October 2026. This is not exhaustive feature coverage. Build and runtime evidence is tracked in [TESTING.md](TESTING.md); native Apple Silicon on Ventura remains unconfirmed.

## Changes for Ventura

- Observation-based state was replaced with Combine `ObservableObject`/`@Published`, including propagation of nested editor and tab changes. The 1.5.5 port also converts PenInput and publishes new line-style/cap and artboard-name changes.
- Newer SwiftUI/AppKit features were replaced or guarded by OS availability checks. Export preview uses an AppKit scroll view; older systems get compatible controls and cursors.
- Camera Raw's cache uses an `NSLock` wrapper in place of `Synchronization.Mutex`; the upstream GPU adjustment algorithm is retained.
- Foreground selection on macOS 13 uses DeepLabV3/Core ML plus Vision and deterministic fallbacks. The newer Vision implementation remains available on supported systems.
- Grayscale mask rendering and resampling preserve row order and edge pixels; model-input orientation has a regression check.
- Shortcut comparisons use `Character` values to avoid the SwiftUI witness-table crash seen on Ventura.

## Differences users may notice

Automatic subject selection, object selection and background removal can produce different masks. The model recognizes a limited set of semantic categories; fallback methods are used when needed.

RAW Highlight Recovery requires a newer API and is unavailable on Ventura. Camera support otherwise follows the RAW decoder provided by the installed macOS.

Some interface styling differs from the official app on new macOS. Automatic upstream updates are disabled. This app is ad-hoc signed and not notarized.

The port does not add its own `.comp` format changes. Upstream 1.5.5 writes **format version 16** (line styles arrived in 15; new filter adjustment layers in 16), and reads versions 1–16. **Compositor 1.5.3 only accepts versions through 14 and rejects new 1.5.5 saves**, including documents without new features. Keep original projects separately and test using copies.

## Version labels

- **1.5.5 / 51.1:** current upstream version / Ventura build.
- **1.5.3 / 49.2:** previously verified upstream version / repaired Ventura build.
- **v1.5.5-ventura.1:** current port release tag.
- **v1.5.3-ventura.2:** previous port release tag.

Use this repository's Releases for later port updates. The original application's download and Homebrew package follow upstream requirements and may not run on Ventura.
