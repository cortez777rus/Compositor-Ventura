# Compatibility notes

Target: macOS 13.0 or later. Initial runtime confirmation: Intel, macOS 13.7.8 (22H730), build 49.2. This does not establish support for every Mac, GPU or editor feature.

## Changes for Ventura

- Observation-based state was replaced with Combine `ObservableObject`/`@Published`, including propagation of nested editor and tab changes.
- Newer SwiftUI/AppKit features were replaced or guarded by OS availability checks. Export preview uses an AppKit scroll view; older systems get compatible controls and cursors.
- Camera Raw's cache uses an `NSLock` wrapper in place of `Synchronization.Mutex`; the upstream GPU adjustment algorithm is retained.
- Foreground selection on macOS 13 uses DeepLabV3/Core ML plus Vision and deterministic fallbacks. The newer Vision implementation remains available on supported systems.
- Grayscale mask rendering and resampling preserve row order and edge pixels; model-input orientation has a regression check.
- Shortcut comparisons use `Character` values to avoid the SwiftUI witness-table crash seen on Ventura.

## Differences users may notice

Automatic subject selection, object selection and background removal can produce different masks. The model recognizes a limited set of semantic categories; fallback methods are used when needed.

RAW Highlight Recovery requires a newer API and is unavailable on Ventura. Camera support otherwise follows the RAW decoder provided by the installed macOS.

Some interface styling differs from the official app on new macOS. Automatic upstream updates are disabled. This app is ad-hoc signed and not notarized.

The `.comp` document format was not changed by the port. Important projects should have backups, as with any experimental editor build.

## Version labels

- **1.5.3:** original application version.
- **49.2:** repaired Ventura build number.
- **v1.5.3-ventura.2:** public release tag for this port.

Use this repository's Releases for later port updates. The original application's download and Homebrew package follow upstream requirements and may not run on Ventura.
