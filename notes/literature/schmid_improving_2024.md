# schmid_improving_2024: Improving AST for SED through multi-stage training

F. Schmid, P. Primus, T. Morocutti, J. Greif, G. Widmer, "Improving audio spectrogram transformers for sound event detection through multi-stage training," DCASE Workshop 2024. https://arxiv.org/abs/2408.00791
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Transformers pretrained on clip labels are not ideal for frame-level SED.
- Method: Pretrain several transformers (e.g. ATST, BEATs, PaSST) on AudioSet-strong in stages, then fine-tune and distill.
- Data / metric: AudioSet-strong, DESED. PSDS1.
- Main result: Strong DCASE 2024 Task 4 results; released checkpoints (PretrainedSED, MIT).
- Limitation: Large models, offline; not suited to a hearing aid as-is.
- Relevance to my thesis (1 line): M2-M3: AudioSet-strong checkpoints already cover Siren, Vehicle horn, Alarm, Doorbell: a quick strong baseline and a teacher for distillation.
- Tags: SED | pretrained | AudioSet-strong
