# Building the Ventura port

This patch-and-build kit obtains the original application from [robbietilton/Compositor](https://github.com/robbietilton/Compositor), pinned to **v1.5.5**, commit `b31ea029762ecb782699df971e1412168602a44d`. The application version is **1.5.5**, candidate build **51.1**. Source preparation does not establish compilation or macOS 13 runtime compatibility; [verification status](TESTING.md) is separate.

## GitHub Actions

1. Open **Actions → Ventura Build → Run workflow** on the candidate branch (or your fork).
2. The Linux job checks patch/payload synchronization, script syntax, clean patch application, the upstream pin and source compatibility invariants.
3. The Mac job selects Xcode 26.6 on `macos-26`, applies the same embedded patch and downloads the segmentation model from Apple with a SHA-256 check.
4. It runs seventeen selected test suites, then builds Release for arm64 and x86_64. It checks Mach-O minimum OS, the shortcut protocol-conformance imports, the ad-hoc signature and brief startup of runnable slices on the build host.
5. After success, download **Compositor-1.5.5-Ventura-candidate-universal**. The artifact contains the app ZIP and its checksum; diagnostics are separate.

The workflow runs for pull requests and pushes changing the workflow, patches or scripts, as well as manual dispatch. No release is published automatically. Artifacts expire after 30 days (app) or 14 days (diagnostics). A successful modern-Mac job is not a Ventura runtime test, and Rosetta is not a native Apple Silicon Ventura check.

## Prepare the source locally

Requirements: Git, Python 3 and curl. Preparation can run on macOS or Linux; compilation needs macOS.

```bash
git clone https://github.com/cortez777rus/Compositor-Ventura.git
cd Compositor-Ventura
# Select the candidate branch if it has not been merged into main.
git switch update/compositor-1.5.5-ventura
bash scripts/prepare-source.sh
```

The script refuses to overwrite an existing destination. To choose another empty destination:

```bash
bash scripts/prepare-source.sh /path/to/Compositor-source
```

For patch review or Linux validation without downloading the model:

```bash
bash scripts/prepare-source.sh --source-only /path/to/source-review
```

A source-only tree is not ready to compile: it lacks `Compositor/Resources/Models/DeepLabV3Int8LUT.mlmodel`. Run the normal preparation into another empty destination to obtain a buildable tree. Both modes verify the tag's exact commit, patch synchronization and prepared source invariants. No downloaded application or system component is installed.

## Compile on a newer Mac

Use full **Xcode 26.6** selected on a supported build Mac. Ventura-compatible Xcode versions cannot compile the upstream Swift syntax. The deployment target of the resulting application is 13.0.

```bash
cd build/Compositor
bash scripts/build-ventura.sh
```

Output is in `dist/ventura/`. This script builds and validates Release; selected unit/integration suites are additionally run by the workflow. See its `xcodebuild test` command to reproduce them locally. Preserve test/build logs and report the actual host OS and architectures tested.

The separate full-source asset of the published **1.5.3** release remains a historical build tree. GitHub-generated source archives contain this kit, not the prepared Xcode project. A new 1.5.5 release/source asset has not been published by this change.

## Maintain the patch

`patches/ventura-1.5.5.patch` and the compressed payload inside `.github/workflows/ventura-build.yml` must remain identical:

```bash
python3 scripts/sync-workflow-patch.py --check
python3 scripts/check-prepared-source.py /path/to/prepared/Compositor
```

After deliberately editing the readable patch, run the sync script without `--check` and review both changes. The source checker is portable; it does not replace Xcode or runtime tests. Upstream updates also require review of the source-preparation pin, both workflow checkout refs, source checker expectations, build labels and tests. The older 1.5.3 patch remains available in Git history and the 1.5.3 release tag.

Do not use upstream publish scripts to publish this port as an official Compositor release. Keep a separate port tag, release description and checksum. Keep upstream attribution, license and third-party notices.
