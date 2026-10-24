# shimada_stereo_2025: DCASE 2025 Task 3: stereo SELD

K. Shimada et al., "Stereo sound event localization and detection with onscreen/offscreen classification," DCASE 2025 Challenge Task 3 description, 2025. https://arxiv.org/abs/2507.12042
Status: draft by Claude from the paper (2026-10-24), for the question "how do people start with SED". Correct it when you read the paper.

- Problem: SELD from only two channels (stereo, as in normal video), including distance and onscreen/offscreen.
- Method: Baseline: 64-band log-mel of the stereo signal at 24 kHz, CRNN (3 conv layers + BiGRU + self-attention), multi-ACCDOA with azimuth and distance.
- Data / metric: Stereo clips derived from STARSS23, 5 s. SELD metrics.
- Main result: Shows the DCASE setup for two-channel input, the closest to binaural hearing aids.
- Limitation: Stereo video mics, not head-worn; no hearing loss.
- Relevance to my thesis (1 line): M2-M3 multichannel option: closest benchmark setup to a 2-mic or binaural detector.
- Tags: SELD | stereo | multichannel | DCASE-2025
