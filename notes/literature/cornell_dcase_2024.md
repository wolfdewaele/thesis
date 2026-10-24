# cornell_dcase_2024: DCASE 2024 Task 4 baseline: SED with heterogeneous data and missing labels

S. Cornell, J. Ebbers, C. Douwes, I. Martín-Morató, M. Harju, A. Mesaros, R. Serizel, "DCASE 2024 Task 4: Sound event detection with heterogeneous data and missing labels," DCASE Workshop 2024. https://dcase.community/documents/challenge2024/technical_reports/DCASE2024_Cornell_baseline_t4.pdf
Status: browsed by Wolf (2026-10-24); note drafted by Claude from the report. Correct it when you read it in full.

- Problem: Train one SED system on datasets with different classes and annotation styles, where a sound present in one dataset is unlabelled in the other.
- Method: CRNN (7-layer CNN + biGRU) with frozen BEATs features concatenated before the GRU; mean teacher; mixup within each dataset; missing labels handled by loss masking, attention masking and a class cross-mapping; per-class median filters tuned with Optuna.
- Data / metric: DESED (10 domestic classes, strong + weak labels) and MAESTRO Real (soft labels, 11 classes evaluated). PSDS1 on DESED, segment-based mean partial AUC on MAESTRO; energy via CodeCarbon.
- Main result: PSDS1 0.491 and segMPAUC 0.731 on dev-test. Without DESED, MAESTRO collapses (0.115); cross-mapping and time masking each give small gains.
- Limitation: Domestic classes only (no sirens or horns); hand-designed mapping rules; offline, bidirectional GRU (not causal).
- Relevance to my thesis (1 line): M2: the reference SED pipeline to start from (code in DESED_task), and its missing-label tricks matter if I combine FSD50K, AudioSet-strong and my own mixtures.
- Tags: SED | baseline | heterogeneous-data | evaluation
