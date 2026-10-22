# Compositor for macOS Ventura

[Русская версия](README.ru.md) · [Download](https://github.com/cortez777rus/Compositor-Ventura/releases/latest) · [Original Compositor](https://github.com/robbietilton/Compositor)

**An unofficial compatibility port of Compositor for macOS 13 Ventura, targeting Intel and Apple Silicon.**

Compositor is the work of **Robbie Tilton and the upstream contributors**. Its original copyright is **© 2026 Wonder Assembly LLC**. Please visit and support the **[original repository: robbietilton/Compositor](https://github.com/robbietilton/Compositor)** and the [official website](https://robbietilton.com/compositor).

This repository maintains the Ventura compatibility changes and build instructions. It does not claim authorship of Compositor and is not an official release or an endorsement by its original authors. The upstream [MIT license](LICENSE) and copyright notice are preserved.

## 1.5.5 port candidate

The build kit now targets upstream **v1.5.5**, commit [`b31ea029`](https://github.com/robbietilton/Compositor/commit/b31ea029762ecb782699df971e1412168602a44d), as **Ventura candidate build 51.1**. This is a source update under validation, not a published working release. The latest published Ventura release remains **1.5.3 / 49.2** below. Its test results do not apply to 1.5.5.

The port retains upstream RGB Split, the new adjustment layers, Channel Pack and Photoshop artboards, alongside the 1.5.4 changes. See the [migration review](docs/UPGRADING-1.5.5.md), [build instructions](docs/BUILDING.md) and [current verification status](docs/TESTING.md). **Native Apple Silicon runtime on macOS Ventura remains unconfirmed.**

## Published 1.5.3 release: download and install

Get **Compositor 1.5.3 — Ventura build 49.2** from [Releases](https://github.com/cortez777rus/Compositor-Ventura/releases/latest).

1. Download **`Compositor-1.5.3-Ventura-universal.zip`** under **Assets**.
2. Quit any older copy, unzip the download, and move `Compositor.app` to **Applications**, replacing the old copy if needed.
3. Open the installed copy. This build is ad-hoc signed and **not notarized by Apple**. If macOS blocks it, use **System Settings → Privacy & Security → Open Anyway** for this app, if offered.

The GitHub-generated **Source code** downloads contain this build kit. For the complete patched Xcode project, download the separately attached **`Compositor-1.5.3-Ventura-source.zip`**.

No Xcode or GitHub account is needed to download and run the release. Keep the accompanying [third-party notices](THIRD_PARTY_NOTICES.txt) when redistributing it.

## Published 1.5.3 release: compatibility and verification

| Item | Status |
| --- | --- |
| Based on | Official Compositor **v1.5.3**, commit [`554104c`](https://github.com/robbietilton/Compositor/commit/554104cf1c2de844c1acbd60b4f7b422bd6ce7bd) |
| App build | **49.2** |
| Minimum deployment target | macOS **13.0** |
| Architectures | Universal: **Intel x86_64 + Apple Silicon arm64** |
| Ventura runtime report | Launch and initial use confirmed by the maintainer on **Intel, macOS 13.7.8 (22H730)** on 18 October 2026 |
| Automated tests | **71 passed**, 0 failed; 104 cases including parameterized runs |
| Release startup checks | Both slices passed on macOS 26.6.2; Intel ran through Rosetta |
| Signing | Ad-hoc; no Developer ID certificate or Apple notarization |

The Ventura report is an initial-use confirmation, not a complete feature or hardware certification. Native Apple Silicon on Ventura has not yet been reported as tested. Details: [test evidence](docs/TESTING.md).

## Known differences

- Automatic subject/object selection and background removal use a Core ML/Vision fallback on Ventura. Their results can differ from the official version on newer macOS.
- **RAW Highlight Recovery is unavailable on Ventura.** Other RAW support depends on the system's decoder.
- Some interface details use older macOS controls.
- Official automatic updates are disabled so they cannot replace this build with an incompatible release. Install future Ventura releases manually.
- Upstream 1.5.5 saves `.comp` format 16, which 1.5.3 cannot open. The port preserves that behavior; keep original projects separately and test using copies.

Read [compatibility notes](docs/COMPATIBILITY.md) and the [changelog](CHANGELOG.md). The earlier internal build 49 had a startup crash; use **49.2**.

## Source and builds

This is a **patch-and-build repository**. It keeps a readable [compatibility patch](patches/ventura-1.5.5.patch), the original license, build scripts and documentation. It obtains the original application from the pinned upstream commit rather than presenting that application as a new project.

To prepare the full source:

```bash
git clone https://github.com/cortez777rus/Compositor-Ventura.git
cd Compositor-Ventura
git switch update/compositor-1.5.5-ventura
bash scripts/prepare-source.sh
```

The project appears in `build/Compositor`. To compile it, use **Xcode 26.6 on a supported newer macOS**, or run the existing GitHub Actions workflow in your own fork. You do not need to upgrade the Mac that will run the resulting app. See [building instructions](docs/BUILDING.md).

## Credits and licenses

- **Application:** [Robbie Tilton / Compositor and its contributors](https://github.com/robbietilton/Compositor); copyright Wonder Assembly LLC; [MIT](LICENSE).
- **Ventura port maintenance and packaging:** [cortez777rus](https://github.com/cortez777rus). Port changes were prepared with AI assistance and tested as described above. This credit applies to the port, not authorship of the original application.
- **Earlier compatibility work:** [vfxbro/Compositor legacy port](https://github.com/vfxbro/Compositor/tree/ca47ed15533786a1d83b08d016ccc952e8501518), used as a reference and for the foreground-selection fallback.
- **Segmentation model:** Apple's distributed DeepLabV3Int8LUT model, with TensorFlow Models attribution and Apache 2.0 license retained.
- **Bundled dependency:** [Sparkle 2.10.0](https://github.com/sparkle-project/Sparkle/tree/2.10.0), with its license and third-party notices retained. Its automatic-update path is disabled in this port.

Full attribution: [CREDITS.md](CREDITS.md) · [THIRD_PARTY_NOTICES.txt](THIRD_PARTY_NOTICES.txt).

## Report a problem or contribute

Use [this repository's Issues](https://github.com/cortez777rus/Compositor-Ventura/issues) for Ventura-port problems. Include the app build, macOS version, CPU/GPU and steps to reproduce. Remove private paths and identifiers from crash reports before posting. Please do not send port-specific support requests to the upstream authors.

English and Russian reports are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
