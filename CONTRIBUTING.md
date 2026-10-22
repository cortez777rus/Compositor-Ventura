# Contributing

This project maintains an unofficial Ventura port of [Compositor](https://github.com/robbietilton/Compositor). Preserve the original project's attribution and license in changes and distributions.

For a bug report, include the app version/build, macOS version, processor/GPU, expected behavior, actual behavior and minimal reproduction steps. Attach a redacted crash excerpt if relevant. English and Russian are welcome. Use copies of projects when preparing examples.

Port-specific issues belong here. Do not ask the original authors to support this unofficial build. If a problem can also be reproduced in their supported official release, follow the upstream project's own contribution rules.

For code changes:

1. Prepare the pinned source as described in [BUILDING.md](docs/BUILDING.md).
2. Keep the change focused and explain why Ventura needs it.
3. Update the readable patch and embedded workflow payload together; run `python3 scripts/sync-workflow-patch.py --check`.
4. Run the relevant tests and a Release build, and state the OS/architecture actually tested. Run `python3 scripts/check-prepared-source.py /path/to/prepared/Compositor` for portable source checks; see [the 1.5.5 migration review](docs/UPGRADING-1.5.5.md).
5. Preserve licenses and third-party notices. Do not commit credentials, personal crash reports, build output or private projects.

Do not claim runtime testing on an OS merely because its deployment target compiled successfully. Contributions to the port are provided under the repository's MIT license; third-party files retain their own licenses.
