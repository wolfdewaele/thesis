# nguyen_description_2026: DCASE 2026 Task 4: Spatial semantic segmentation of sound scenes

B. T. Nguyen et al., "Description and discussion on DCASE 2026 Challenge Task 4: Spatial semantic segmentation of sound scenes," arXiv:2604.00776, 2026. See also the 2025 edition, arXiv:2506.10676.
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Jointly detect which target classes are present and separate each one from a multichannel mixture.
- Method: Baseline: audio tagging (M2D) followed by label-queried separation (ResUNet).
- Data / metric: 4-channel FOA mixtures, 18 classes (incl. AlarmClock, Doorbell, Buzzer, BicycleBell); zero-target and same-class mixtures in 2026. CAPI-SDRi, label F1.
- Main result: Baseline CAPI-SDRi 6.77 dB on eval; results and technical reports are online.
- Limitation: Clip-level labels (no onset/offset); no sirens; offline.
- Relevance to my thesis (1 line): M4 option B benchmark: detect, then let through. The tech reports show which tagger+separator combinations work.
- Tags: extraction | separation | benchmark
