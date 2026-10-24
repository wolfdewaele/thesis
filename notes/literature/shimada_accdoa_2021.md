# shimada_accdoa_2021: ACCDOA output format

K. Shimada, Y. Koyama, N. Takahashi, S. Takahashi, Y. Mitsufuji, "ACCDOA: Activity-coupled Cartesian direction of arrival representation for sound event localization and detection," ICASSP 2021. https://arxiv.org/abs/2010.15306
Status: draft by Claude from the paper (2026-10-24), for the question "how do people start with SED". Correct it when you read the paper.

- Problem: Two output branches (activity + direction) need loss balancing.
- Method: One output: a Cartesian vector per class; its length is the activity, its direction is the DOA. Single MSE loss. Multi-ACCDOA later adds tracks for same-class overlap.
- Data / metric: DCASE SELD data. SELD metrics.
- Main result: Simpler and better than two-branch SELD; used by every DCASE Task 3 baseline since.
- Limitation: Only relevant if I predict direction.
- Relevance to my thesis (1 line): Multichannel option only; read if direction becomes part of the scope.
- Tags: SELD | output-format
