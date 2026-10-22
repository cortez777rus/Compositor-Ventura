# Review: upstream 1.5.3 → 1.5.5 on Ventura

This is an unreleased source candidate, **1.5.5 / 51.1**. A deployment target of 13.0 and successful modern-Mac compilation do not establish runtime support on Ventura. Native Apple Silicon on Ventura remains unconfirmed. See [TESTING.md](TESTING.md) for evidence and remaining checks.

## Reproducible bases

- Original application: [Robbie Tilton and contributors / Compositor](https://github.com/robbietilton/Compositor), © 2026 Wonder Assembly LLC, MIT.
- Previous upstream base: `554104cf1c2de844c1acbd60b4f7b422bd6ce7bd` (`v1.5.3`).
- New base: `b31ea029762ecb782699df971e1412168602a44d` (`v1.5.5`, including the final Channel Pack PNG fix, not just the preceding version-number commit).
- Build-kit base reviewed: `012567dbcd7b0603ac9fb954d1d34cc9eea60a61`.
- Upstream comparison: **38 commits, 56 changed files**; **19 files overlap** the previous compatibility patch.

The application is obtained from the exact upstream base and patched, preserving upstream credit and licenses. No new release, tag, automatic update feed or change to the existing published binary is part of this update.

## Conflicts and overlapping files

A direct `git apply --check` of the 1.5.3 patch fails on four files: `project.pbxproj`, `EditorSession.swift`, `ExportAsSheet.swift`, and `KeyboardShortcutTests.swift`. With base objects available, a three-way application resolves the shortcut test overlap automatically and leaves three textual conflicts. The replacement patch applies directly to clean 1.5.5; users do not need a three-way merge.

Paths below are relative to `Compositor/`, except the project, tests and plist.

| Overlapping file | Resolution / review |
| --- | --- |
| `Compositor.xcodeproj/project.pbxproj` | Resolve version conflicts to 1.5.5 / candidate 51.1, all deployment targets 13.0 and standard universal architectures. |
| `CompositorApp.swift` | Retain upstream new filter menus and Save/Open text routing inside the Combine-observed scene; keep upstream updater disabled. |
| `Document/EditorSession.swift` | Keep pressure, PDF import and artboard callback; remove new ObservationIgnored attributes. Publish line width/style/cap. |
| `Document/Filters.swift` | Keep upstream RGB Split settings, preview and radial-center updates with the existing ObservableObject filter edit and forwarding. |
| `Document/ProjectWorkspace.swift` | Keep artboard tab attachment; make mutable defaultName published and forward both tab and session notifications. |
| `IO/CompositorApplicationDelegate.swift` | Keep PenInput installation and previous window/observation adaptations. |
| `Rendering/EditorCanvas.swift` | Retain pressure events, RGB Split dragging and line drawing with the previous compatible resize cursors. |
| `Rendering/GPUCanvas.swift` | Retain upstream GPU implementations for new adjustment layers; keep the compatible cursor change. |
| `Rendering/TransformOverlay.swift` | Retain RGB Split center overlay and previous resize cursor fallback. |
| `UI/BrushControls.swift` | Explicitly observe the converted PenInput singleton, retaining pressure toggles and compatible change callbacks. |
| `UI/ExportAsSheet.swift` | Resolve conflict by keeping snapshot, channel sources/choices and format filtering, ObservedObject session and AppKit zoom preview. |
| `UI/FilterSheet.swift` | Keep RGB Split settings / Split to Layers with ObservedObject session. |
| `UI/KeyboardShortcuts.swift` | Keep LatinKeys event translation and the character-based KeyEquivalent comparison fix. |
| `UI/LayersPanel.swift` | Keep split image-adjustment/filter menus with ObservedObject session. |
| `UI/NewCanvasSheet.swift` | Preserve upstream Import label and compatible change callbacks. |
| `UI/ShapeControls.swift` | Preserve style/cap pickers and sample drawings; session remains explicitly observed. |
| `UI/TypeControls.swift` | Preserve upstream native searchable FontListPanel with compatible change callbacks. |
| `CompositorTests/KeyboardShortcutTests.swift` | Preserve non-Latin layout test and port tests; avoid unavailable KeyEquivalent/KeyboardShortcut equality conformances. |
| `Config/Info.plist` | Preserve upstream PDF document type and keep automatic checks/feed disabled. |

A new dependency outside the old overlap list also needs adaptation: **`UI/PenInput.swift`** imports Observation and declares an Observable class upstream. It now uses Combine `ObservableObject` / `@Published`, with `BrushControls` observing it explicitly. A clean textual merge alone would miss this Ventura issue.

New `ChannelPack.swift`, `MetalDispersion.swift`, `LatinKeys.swift` and `FontListPanel.swift` were reviewed for platform dependencies. Channel Pack's own PNG writer (including RGB under alpha=0), the Metal/Core Image dispersion path, Carbon keyboard translation and native AppKit font panel are retained. Actual behavior remains subject to Xcode tests and Ventura runtime checks, particularly GPU/driver and keyboard-layout differences.

## Build and CI changes

- Rename the active patch to `patches/ventura-1.5.5.patch`; regenerate the embedded workflow payload and checksum.
- Pin local preparation and both CI upstream checkouts to the exact 1.5.5 commit.
- Add `--source-only` preparation for review without downloading the model; retain model URL and verified SHA-256 in the normal build path.
- Validate clean patch application on Linux before the Mac job. The source checker verifies the source pin, CI pin agreement, patch reversibility, version/build/target settings, universal architecture setting, disabled upstream feed and absence of Observation declarations/imports and conflict markers in app Swift files.
- Trigger validation/build on PRs and pushes affecting workflow, patches or scripts. Keep publication manual and label uploaded artifacts as candidates.
- Expand selected tests from eight to **seventeen suites**, covering new filters/adjustments, Channel Pack transparency, PSD artboards, PDF, pen pressure, font faces and line styles.
- Add regression tests for line style/cap UI notifications and artboard tab-name notifications, including disconnection of closed tabs.
- Retain segmentation/model-orientation tests, Camera Raw locking, binary minimum-OS and shortcut-conformance checks, ad-hoc signature verification and startup checks for both runnable Release slices.

## Verification performed during preparation

On Linux, the new readable and embedded patches matched; the new patch applied to pristine pinned 1.5.5 without rejections; the prepared-source checks passed; the source-only script ran to completion using a local upstream mirror at the pinned tag. The local mirror avoids treating network or model availability as source validation. Script syntax, Python compilation and workflow YAML parsing were also checked.

Linux has no Xcode, AppKit, Metal runtime or Ventura host. Compilation, test execution and binary checks require the Mac CI job. Runtime checks on Intel Ventura and separately native Apple Silicon Ventura remain required. Record actual CI evidence in [TESTING.md](TESTING.md); do not reuse the old 49.2 counts as a 1.5.5 result.

## Document compatibility

The port adds no separate file-format changes. Upstream 1.5.5 adds optional persisted line styles and filter-layer settings; retain those upstream fields and their defaults. Back up files and test save/reopen using the new features. A document edited with them should not be assumed to look the same when opened in 1.5.3.
