# ebbers_threshold_2022: Threshold-independent SED evaluation

J. Ebbers, R. Haeb-Umbach, R. Serizel, "Threshold independent evaluation of sound event detection scores," ICASSP 2022. https://arxiv.org/abs/2201.13148
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Approximating PSDS with a few thresholds is inaccurate and slow.
- Method: Compute metrics exactly over all thresholds from score outputs; sed_scores_eval package.
- Data / metric: DCASE data. PSDS, collar-based and intersection-based F1.
- Main result: Exact and fast PSDS; now used by the DCASE baseline.
- Limitation: Python package to learn, nothing more.
- Relevance to my thesis (1 line): M3 (timing): use sed_scores_eval (MIT) in src/hased/evaluation from the start.
- Tags: evaluation | tools
