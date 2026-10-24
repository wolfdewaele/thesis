# adavanne_sound_2019: SELDnet

S. Adavanne, A. Politis, J. Nikunen, T. Virtanen, "Sound event localization and detection of overlapping sources using convolutional recurrent neural networks," IEEE JSTSP, 2019. https://arxiv.org/abs/1807.00129
Status: draft by Claude from the paper (2026-10-24), for the question "how do people start with SED". Correct it when you read the paper.

- Problem: Detect sound events and estimate their direction jointly from a microphone array.
- Method: CRNN on multichannel magnitude + phase spectrograms, two output branches: frame-wise SED (sigmoid) and DOA regression.
- Data / metric: Synthetic and real Ambisonics/array datasets. SED F1/ER and DOA error.
- Main result: Founded the SELD task (DCASE Task 3).
- Limitation: Superseded by ACCDOA outputs and better features (SALSA).
- Relevance to my thesis (1 line): Background for the multichannel option; direction could matter later (is the siren approaching?).
- Tags: SELD | multichannel | architecture
