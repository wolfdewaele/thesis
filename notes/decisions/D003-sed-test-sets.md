# D003: Fixed real-world test sets for event detection (2026-10-24)

- Context: own mixtures (D002) give hearing-aid signals with exact labels, but they are synthetic. A real test is
  needed to show the detector works outside the generator. See notes/literature/datasets-sed-2026-10.md.
- Options considered: A) only a held-out split of own mixtures, B) A + real strong-labelled sets: DCASE 2017 Task 4
  eval (sirens, horns, car alarm), SINGA:PURA (alert signals), STARSS23 (phone, bell), C) MAESTRO Real (no target classes).
- Choice and reason: B (proposed). Covers outdoor warning sounds and indoor phone/bell with real recordings; DESED is
  used once as a pipeline check (reproduce the DCASE baseline PSDS), not as a test of the thesis question.
- Would change if: Stijn has annotated hearing-aid recordings, or a test set with BTE recordings of target events appears.
- Status: proposed
