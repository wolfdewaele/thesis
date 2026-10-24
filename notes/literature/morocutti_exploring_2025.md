# morocutti_exploring_2025: Performance-complexity trade-offs in SED models

T. Morocutti, F. Schmid, J. Greif, F. Foscarin, G. Widmer, "Exploring performance-complexity trade-offs in sound event detection models," arXiv:2503.11373, 2025.
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Get transformer-level SED with a small model.
- Method: MobileNetV3 adapted for frame-wise output + sequence model (transformer, GRU, TCN, Mamba-2 ...), knowledge distillation from transformer ensembles.
- Data / metric: AudioSet-strong (407 classes). PSDS1, params, MACs, throughput.
- Main result: PSDS1 45.3 with ~5M params, comparable to ~90M-param transformers. Code: EfficientSED (MIT).
- Limitation: Offline evaluation; no latency or causality analysis.
- Relevance to my thesis (1 line): M2-M3: strongest candidate backbone for a hearing-aid-sized detector; causal variant would be your own step.
- Tags: SED | efficiency | latency
