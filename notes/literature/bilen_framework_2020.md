# bilen_framework_2020: PSDS

C. Bilen, G. Ferroni, F. Tuveri, J. Azcarreta, S. Krstulović, "A framework for the robust evaluation of sound event detection," ICASSP 2020. https://arxiv.org/abs/1910.08440
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Event F1 depends on one threshold and on arbitrary collar choices.
- Method: Polyphonic Sound Detection Score: area under a ROC-like curve over thresholds, with cross-trigger handling.
- Data / metric: DCASE data. PSDS.
- Main result: Became the DCASE Task 4 ranking metric (PSDS1 for onset precision, PSDS2 for class confusion).
- Limitation: Harder to explain than F1; for user-facing claims also report F1 at a chosen threshold.
- Relevance to my thesis (1 line): M3 (timing): main metric, comparable with DCASE papers.
- Tags: evaluation
