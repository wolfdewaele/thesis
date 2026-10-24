# bando_end-to-end_2026: End-to-end iterative S5 system (TF-Locoformer + ATST-Frame)

Y. Bando, S. Sakurai, Y. Nozaki, K. Imoto, M. Onishi, "End-to-end iterative S5 system based on TF-Locoformer and ATST-Frame," DCASE 2026 Challenge Task 4 technical report, 2026. https://dcase.community/documents/challenge2026/technical_reports/DCASE2026_Bando_140_t4.pdf
Status: browsed by Wolf (2026-10-24); note drafted by Claude from the report. Correct it when you read it in full.

- Problem: Detect and separate target sound classes from a 4-channel mixture (S5), instead of the baseline's separate tagger and separator.
- Method: One jointly trained network: TF-Locoformer blocks in three groups, with class and signal heads after each group; separated signals go through ATST-Frame and the embeddings feed back into the next group. 5 output slots, PIT with SNR + BCE loss.
- Data / metric: DCASE 2026 Task 4 data only (18 classes). CAPI-SDRi, mixture and source label accuracy.
- Main result: CAPI-SDRi 16.5 dB on dev-test vs 8.5 dB baseline. Longer training was the biggest factor; ATST-Frame improves recall, not precision.
- Limitation: No parameter counts, no latency or causality; trained on 4 GPUs; some classes confused with silence; no code.
- Relevance to my thesis (1 line): M4 option A: shows that joint detection + separation trained end to end beats the cascade by a wide margin, at a compute cost far above a hearing aid.
- Tags: separation | extraction | joint-training | DCASE-2026
