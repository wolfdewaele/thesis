# shao_fine-tune_2024: Fine-tune the pretrained ATST model for SED

N. Shao, X. Li, X. Li, "Fine-tune the pretrained ATST model for sound event detection," ICASSP 2024. https://arxiv.org/abs/2309.08153
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: How to fine-tune a large self-supervised frame-level model with little strong-labelled data.
- Method: ATST-Frame features + CRNN, two-stage fine-tuning, mean teacher.
- Data / metric: DESED. PSDS1/PSDS2.
- Main result: State of the art on DESED at publication; code ATST-SED (MIT).
- Limitation: Domestic classes only; offline.
- Relevance to my thesis (1 line): M2-M3: a well-documented fine-tuning recipe to compare against.
- Tags: SED | pretrained | semi-supervised
