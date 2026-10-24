# nguyen_salsa_2022: SALSA features

T. N. T. Nguyen, K. N. Watcharasupat, N. K. Nguyen, D. L. Jones, W.-S. Gan, "SALSA: Spatial cue-augmented log-spectrogram features for polyphonic sound event localization and detection," IEEE/ACM TASLP, 2022. https://arxiv.org/abs/2110.00275
Status: draft by Claude from the paper (2026-10-24), for the question "how do people start with SED". Correct it when you read the paper.

- Problem: Spatial features like GCC-PHAT do not align with the spectrogram bins, which makes them hard for CNNs to combine.
- Method: Stack the multichannel log-spectrogram with spatial cues (eigenvector-based or normalised IPD) computed per time-frequency bin, so both are aligned. SALSA-Lite is a cheap IPD-based variant.
- Data / metric: DCASE SELD data (FOA and mic array). SELD metrics.
- Main result: Strong SELD results; SALSA-Lite became a common, cheap feature.
- Limitation: Designed for 4-channel arrays; needs adapting to 2-6 hearing-aid mics.
- Relevance to my thesis (1 line): M2-M3 multichannel experiment: SALSA-Lite/IPD is the cheapest way to add the second ear or mic.
- Tags: SELD | multichannel | features
