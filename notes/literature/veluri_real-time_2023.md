# veluri_real-time_2023: Real-time target sound extraction (Waveformer)

B. Veluri, J. Chan, M. Itani, T. Chen, T. Yoshioka, S. Gollakota, "Real-time target sound extraction," ICASSP 2023. https://arxiv.org/abs/2211.02250
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Class-conditioned target sound extraction that runs in real time on a CPU.
- Method: Waveformer: dilated causal conv encoder + transformer decoder, chunk-based streaming.
- Data / metric: Scaper mixtures, FSDKaggle2018 (41 classes) + TAU backgrounds. SI-SNRi.
- Main result: 9.0-9.4 dB SI-SNRi (2.2-3.3 dB above Conv-TasNet/ReSepformer); 9.4 ms chunks, RTF 0.66 on one i5 core; 1.1-3.9M params.
- Limitation: Single channel, monaural; synthetic data only.
- Relevance to my thesis (1 line): Real-time M3 baseline; the architecture behind Semantic Hearing.
- Tags: extraction | latency
