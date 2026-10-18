# Verification of build 49.2

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
