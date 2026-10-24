# cakir_convolutional_2017: CRNN for polyphonic SED

E. Çakır, G. Parascandolo, T. Heittola, H. Huttunen, T. Virtanen, "Convolutional recurrent neural networks for polyphonic sound event detection," IEEE/ACM TASLP, 2017. https://arxiv.org/abs/1702.06286
Status: draft by Claude from the paper (2026-10-24), for the question "how do people start with SED". Correct it when you read the paper.

- Problem: Detect overlapping (polyphonic) sound events with onset/offset.
- Method: CRNN: CNN with frequency-only pooling (keeps time resolution) + GRU + per-frame sigmoid per class; BCE; threshold 0.5.
- Data / metric: Log-mel, 40 bands, 40 ms window / 20 ms hop, per-band standardisation with training-set statistics. TUT-SED (binaural), CHiME-Home. Frame and 1 s segment F1, error rate.
- Main result: CRNN beats CNN-only and RNN-only; became the standard SED architecture.
- Limitation: Small datasets; no pretrained models; mono vs stereo not compared.
- Relevance to my thesis (1 line): M2-M3: the template for my first baseline (frame-wise CRNN on log-mel).
- Tags: SED | architecture | baseline | background
