# veluri_semantic_2023: Semantic Hearing

B. Veluri, M. Itani, J. Chan, T. Yoshioka, S. Gollakota, "Semantic hearing: Programming acoustic scenes with binaural hearables," UIST 2023. https://arxiv.org/abs/2311.00320
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Let a hearable user choose which sound classes to hear, in real time, while keeping binaural cues.
- Method: Causal time-domain network (dilated causal conv encoder, transformer decoder conditioned on a label embedding), both ears processed jointly.
- Data / metric: Scaper mixtures from FSD50K, ESC-50, MUSDB18, DISCO noise, HRTFs/BRIRs, TAU urban backgrounds; 20 target classes (incl. siren, car horn, alarm clock, door knock). SI-SNRi, ITD/ILD error, MOS.
- Main result: SI-SNRi 7.2 dB (0.52M params); 6.56 ms per 10 ms chunk on iPhone 11, ~20 ms end-to-end.
- Limitation: Normal-hearing listeners; extraction only, no explicit onset/offset output; no hearing loss.
- Relevance to my thesis (1 line): Closest related work for M3 option A, and its data recipe matches the planned own mixtures (D002).
- Tags: hearing-aid | extraction | latency | binaural
