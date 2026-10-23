# turpault_improving_2020: Improving SED using sound separation

N. Turpault, S. Wisdom, H. Erdogan, J. R. Hershey, R. Serizel, E. Fonseca, P. Seetharaman, J. Salamon, "Improving sound event detection in domestic environments using sound separation," DCASE Workshop 2020. https://arxiv.org/abs/2007.03932
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Does a separation front-end help SED?
- Method: Universal separation (FUSS) before the DCASE baseline; early, middle and late fusion.
- Data / metric: DESED. Event F1, PSDS.
- Main result: Late fusion best, but small gain (F1 +1.7, PSDS +0.018); mismatch between separation and SED data limits it.
- Limitation: 2020 baseline models.
- Relevance to my thesis (1 line): M3: evidence that a naive cascade gives little; motivates joint training or detector-driven gating.
- Tags: SED | separation | integration
