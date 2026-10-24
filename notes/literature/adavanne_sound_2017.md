# adavanne_sound_2017: SED with spatial features and CRNN

S. Adavanne, P. Pertilä, T. Virtanen, "Sound event detection using spatial features and convolutional recurrent neural network," ICASSP 2017. https://arxiv.org/abs/1706.02291
Status: draft by Claude from the paper (2026-10-24), for the question "how do people start with SED". Correct it when you read the paper.

- Problem: Does a second (binaural) channel help sound event detection?
- Method: CRNN on stacked per-channel features: binaural log-mel (40 bands) + GCC-PHAT at three resolutions; channels as separate input layers.
- Data / metric: TUT-SED 2009 and 2016 (in-ear binaural recordings). F1, error rate.
- Main result: Binaural features improve F1 by 2.7 and 6.1 points over mono with the same network.
- Limitation: Old, small datasets; no pretrained models.
- Relevance to my thesis (1 line): M2-M3: evidence for a later mono-vs-binaural experiment with hearing-aid mics.
- Tags: SED | multichannel | binaural | features
