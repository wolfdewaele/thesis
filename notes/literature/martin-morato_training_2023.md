# martin-morato_training_2023: Training SED with soft labels from crowdsourced annotations

I. Martín-Morató, M. Harju, P. Ahokas, A. Mesaros, "Training sound event detection with soft labels from crowdsourced annotations," in Proc. IEEE ICASSP, 2023, pp. 1-5. https://arxiv.org/abs/2302.14572
Status: draft by Claude from the arXiv version (2026-10-24). Correct it when you read the paper.

- Problem: Strong labels are scarce, and hard 0/1 labels throw away how much annotators agreed.
- Method: MTurk workers tag overlapping 10 s segments; per 1 s segment a competence-weighted (MACE) average gives a soft label in [0, 1]. CRNN (3 conv + 2 BiGRU), 64 log-mel, 20 ms hop; hard BCE vs soft BCE vs soft MSE with linear output.
- Data / metric: MAESTRO Real: 75 recordings from TUT Acoustic Scenes 2016, ~287 min, 5 scenes, 17 classes. 1 s segment F1/ER, KL divergence. 5-fold CV.
- Main result: Soft MSE matches hard labels on F1 (70.8% vs 70.6%), ER 0.44, with much lower KLD; it still detects rare classes, which the hard-label model misses (needs per-class thresholds).
- Limitation: Small gains, one dataset, 1 s resolution (not strictly strong labels), no warning-sound classes, non-commercial license.
- Relevance to my thesis (1 line): Not a training set for my classes, but soft onset/offset labels could model fading sirens; MAESTRO was part of DCASE 2023/2024 Task 4.
- Tags: SED | datasets | labels | evaluation
