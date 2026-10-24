# hased: the Python package

All reusable code lives here; scripts and notebooks only import from it.

| Subpackage | Module | Contents |
| --- | --- | --- |
| `data/` | 2-3 | dataset catalogs (FSD50K, speech, backgrounds), mixture generation with the PyClarity scene generator, strong labels (onset, offset, class), PyTorch datasets |
| `models/` | 2-3 | SED models (baselines, pretrained embeddings such as PANNs/AST/BEATs + heads) |
| `training/` | 2-3 | training loop, losses, callbacks |
| `evaluation/` | 2-4 | post-processing (thresholds, median filtering) and metrics (event-based F1, PSDS) |
| `enhancement/` | 4 | integration with speech enhancement: deciding what to let through, hearing-loss simulation (MSBG) and HASPI evaluation |
| `utils/` | all | audio I/O, seeding, logging helpers |
