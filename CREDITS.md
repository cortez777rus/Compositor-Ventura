# Credits and provenance

## Original application

**Compositor is developed by Robbie Tilton and the contributors to [robbietilton/Compositor](https://github.com/robbietilton/Compositor).**

- Official website: <https://robbietilton.com/compositor>
- Upstream release used by the current build kit: [v1.5.5](https://github.com/robbietilton/Compositor/releases/tag/v1.5.5)
- Exact base commit: `b31ea029762ecb782699df971e1412168602a44d`
- Original copyright: **Copyright (c) 2026 Wonder Assembly LLC**
- License: [MIT, retained without replacing the original copyright](LICENSE)

The Ventura repository is an independent adaptation. Its owner does not claim to have created Compositor, and the upstream authors have not endorsed this port. Names and links identify the source of the application.

The published 1.5.3 / 49.2 release used commit `554104cf1c2de844c1acbd60b4f7b422bd6ce7bd`. The 1.5.5 source update does not transfer that release’s runtime validation to the new candidate.

## Compatibility work

[cortez777rus](https://github.com/cortez777rus) maintains this Ventura build and its distribution. The port was prepared with AI assistance. Its scope includes macOS API fallbacks, observation changes, Intel/universal builds, startup fixes, compatibility tests and packaging.

The foreground-selection fallback is adapted from the MIT-licensed [vfxbro/Compositor legacy port](https://github.com/vfxbro/Compositor/tree/ca47ed15533786a1d83b08d016ccc952e8501518). Credit for that earlier compatibility work is retained.

## Model and bundled dependency

- DeepLabV3Int8LUT: distributed through [Apple's Core ML model catalog](https://developer.apple.com/machine-learning/models/). The unchanged model's metadata references TensorFlow Models. The [Apache 2.0 license and copyright](licenses/TensorFlow-Models-LICENSE.txt) are retained. [Model provenance](docs/third-party-models.md).
- Sparkle **2.10.0**: [sparkle-project/Sparkle](https://github.com/sparkle-project/Sparkle/tree/2.10.0). Its [complete license, including third-party notices](licenses/Sparkle-LICENSE.txt), is included. Sparkle remains bundled, but the official automatic-update mechanism is disabled in this port.

The [combined notices](THIRD_PARTY_NOTICES.txt) accompany the release. Original source files and license notices remain in the full source archive.
