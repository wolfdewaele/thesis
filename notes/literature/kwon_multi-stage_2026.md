# kwon_multi-stage_2026: Multi-stage separation-and-classification (KAIST, S5)

Y. Kwon, J. Park, H. Yin, J.-W. Choi, "A multi-stage separation-and-classification framework guided by complementary acoustic-to-semantic clues," DCASE 2026 Challenge Task 4 technical report, 2026. https://dcase.community/documents/challenge2026/technical_reports/DCASE2026_Choi_122_t4.pdf
Status: browsed by Wolf (2026-10-24); note drafted by Claude from the report. Correct it when you read it in full.

- Problem: Same S5 task: improve both separation and labels, including mixtures without targets.
- Method: Stage 1 universal separation (DeFT-Mamba-USS) + dual-path classifier (separator features + frozen M2D); stages 2-3 target extraction (DeFT-Mamba-TSE) guided by the previous waveform, the predicted class (FiLM) and AF-Whisper frame embeddings. Silence output with per-class thresholds.
- Data / metric: Online SpatialScaper mixtures, VCTK speech, extra AudioSet vacuum-cleaner clips, duration augmentation for short percussive sounds. CAPI-SDRi, label accuracy.
- Main result: CAPI-SDRi 15.5 dB, mixture accuracy 71.1% vs 8.5 dB / 60.7% baseline. Iterative refinement gives most of it (11.1 to 14.4 dB); AF-Whisper only ~0.2 dB.
- Limitation: Thresholds tuned on the same set they report on (optimistic); no size or latency; no code.
- Relevance to my thesis (1 line): M3: "detect, then extract with the label as a clue" in an iterative loop; the duration augmentation for short sounds (doorbell, horn beeps) is useful for M2 too. Lesson for me: tune thresholds on validation, never on test.
- Tags: separation | extraction | augmentation | DCASE-2026
