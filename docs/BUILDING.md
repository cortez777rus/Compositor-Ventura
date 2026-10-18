# Building the Ventura port

This repository contains a patch-and-build kit. The original application comes from [robbietilton/Compositor](https://github.com/robbietilton/Compositor), pinned to v1.5.3 commit `554104cf1c2de844c1acbd60b4f7b422bd6ce7bd`.

## GitHub Actions

1. Fork this repository to your account.
2. Open **Actions** and enable workflows if GitHub asks.
3. Choose **Ventura Build → Run workflow** on `main`.
4. After success, download **Compositor-1.5.3-Ventura-universal**. This artifact contains the application ZIP and its checksum.

The workflow selects Xcode 26.6 on `macos-26`, applies the pinned compatibility patch, fetches the model from Apple with a SHA-256 check, runs eight test suites, and builds both Release slices. It checks minimum OS versions, shortcut imports and the ad-hoc signature, then runs a brief startup check for each runnable architecture.

Artifacts are temporary (application: 30 days, diagnostics: 14 days). Published Releases provide the download intended for end users. Actions artifact downloads can require a GitHub login.

## Prepare the source locally

Requirements: Git, Python 3 and curl. The preparation step can run on macOS or Linux; compiling the app requires macOS.

```bash
git clone https://github.com/cortez777rus/Compositor-Ventura.git
cd Compositor-Ventura
bash scripts/prepare-source.sh
```

The script refuses to overwrite an existing destination. To use another empty destination:

```bash
bash scripts/prepare-source.sh /path/to/Compositor-source
```

It verifies the upstream commit, the patch and the model. It does not run the downloaded application or install system components.

## Compile on a newer Mac

Use a Mac that supports **Xcode 26.6**, with the full Xcode installation selected. The minimum OS of the resulting application is 13.0; the build host and runtime target are different requirements.

```bash
cd build/Compositor
bash scripts/build-ventura.sh
```

The result is in `dist/ventura/`. This script builds and validates Release; the eight selected test suites are additionally run by the GitHub Actions workflow. Xcode versions that run on Ventura cannot compile the current upstream Swift syntax.

The complete source asset in Releases can also be unpacked and built from its `source/` directory. GitHub's automatically generated source archives contain the build kit, not the full prepared Xcode project.

## Maintain the patch

The readable patch and the compressed patch inside `.github/workflows/ventura-build.yml` must stay identical. Run:

```bash
python3 scripts/sync-workflow-patch.py --check
```

After deliberately updating `patches/ventura-1.5.3.patch`, run the same script without `--check` to update the embedded payload and checksum. Review both changes before committing. Updating the upstream version or model also requires reviewing their pinned commit/URL/checksum in the source-preparation script and workflow.

Do not use upstream release/publish scripts to publish this port as an official Compositor release. The port uses a separate tag, release description and checksum.
