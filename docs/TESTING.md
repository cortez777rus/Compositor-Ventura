# Verification status

## 1.5.5 / candidate build 51.1

This candidate is based on upstream commit `b31ea029762ecb782699df971e1412168602a44d`. Historical 1.5.3 / 49.2 results below do not validate it.

| Check | Candidate status |
| --- | --- |
| Readable patch vs embedded payload SHA-256 | Passed locally on Linux |
| Apply patch to pristine pinned 1.5.5 source | Passed locally, without rejected hunks |
| Source-only preparation, pin and observation/target checks | Passed locally on Linux |
| Xcode compilation and selected tests | Pending CI evidence |
| Universal Release metadata, signature and build-host startup | Pending CI evidence |
| Intel macOS Ventura launch and feature checks | Not performed for 1.5.5 |
| Native Apple Silicon macOS Ventura | **Unconfirmed** |

CI retains the previous eight suites and adds AdjustmentLayerTests, ChannelPackTests, FilterLayerTests, FilterTests, FontMenuFacesTests, PDFImportTests, PSDArtboardTests, PenPressureTests and ShapeToolTests. Two port regression tests check notifications for line style/cap and changing artboard tab names, including detaching closed tabs. No total pass count is claimed before the run.

Before promoting the candidate, record the exact CI commit/run and repeat launch and feature checks on actual Ventura: create/paint/Undo/Redo, multiple tabs, save/reopen a `.comp` copy, RGB Split Linear/Radial and Split to Layers, all three new adjustment layers, PNG Channel Pack including RGB beneath alpha=0, PSD artboards and ordinary PSD import, PDF pages, font search, Russian-layout shortcuts and Save/Open panel clipboard operations. Check RAW and foreground selection for retained fallbacks. Pen UI and pressure additionally need a physical tablet. Record CPU/GPU and macOS version for each result.

## Historical 1.5.3 / build 49.2

## Actual Ventura report

On **18 October 2026**, the maintainer confirmed that build **49.2 opened and worked on Intel macOS 13.7.8 (22H730)** after the startup fix. This is a report of successful launch and initial use, not an exhaustive feature test. Native Apple Silicon on Ventura has not yet been confirmed.

## Automated evidence

The published binary comes from [successful build #8](https://github.com/cortez777rus/Compositor-Ventura/actions/runs/39140583803), workflow commit `25eeefc0f8eba9b08107a652faf1da5c8fa278d9`.

- Build host: macOS **26.6.2**, Apple Silicon, Xcode **26.6**.
- **71 logical tests passed**, zero failed; **104 cases** including parameterized executions.
- Suites: VenturaCompatibilityTests, VenturaSegmentationTests, HistoryTests, CommandPaletteTests, KeyboardShortcutTests, ProjectWorkspaceTests, CameraRawGPUTests and GPUCanvasTests. This is not every upstream test suite.
- Release compiled for `arm64` and `x86_64`.
- All six Mach-O binaries contain both architectures; main executable minimum OS 13.0, embedded Sparkle minimum OS 12.0.
- The missing shortcut protocol conformance is absent in both slices. The check correctly rejects the earlier faulty binary.
- `codesign --verify --deep --strict` passed with an ad-hoc signature.
- Both Release slices stayed alive through ten seconds of startup on the build host. The Intel slice ran through Rosetta. This check does not emulate Ventura.
- Downloaded ZIP checksums, CRC, app version/build, executable mode, bundled model and notices were verified.

Application ZIP SHA-256:

```text
ca3d92e248d58631951999903dd28c462fa8f08b79a5e5b5b299686e7187de79
```

The full source release asset includes build-time logs and validation reports. Those reports predate the later Ventura confirmation above. GitHub Actions diagnostics have limited retention; the release source archive keeps the text evidence.

## Useful further checks

Reports of native Apple Silicon on Ventura and additional Intel/GPU configurations are welcome. Useful workflows include creating a canvas, painting, Undo/Redo, multiple tabs, saving/reopening a copy of a `.comp` document, PNG/JPEG export, Camera Raw and automatic selections.

Submit results through this repository's issue template. Do not include private source images or unredacted personal identifiers in public reports.
