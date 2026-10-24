# deng_label-guided_2026: Label-guided ensemble for same-class sources (Wuhan, S5)

Y. Deng, T. Zou, Y. Tian, Y. Yan, J. Luo, G. Huang, H. Shi, "A label-guided ensemble system for spatial semantic segmentation of same-class sound sources," DCASE 2026 Challenge Task 4 technical report, 2026. https://dcase.community/documents/challenge2026/technical_reports/DCASE2026_Deng_114_t4.pdf
Status: browsed by Wolf (2026-10-24); note drafted by Claude from the report. Correct it when you read it in full.

- Problem: Same S5 task, keeping the baseline's cascade (tagger, then label-queried separator).
- Method: Ensemble of three taggers (two M2D-AT variants, one CLAP/HTS-AT) by weighted voting; fine-tuned ResUNetK separator with a small class-dependent TF-GridNet fusion; silence as a label marks inactive slots.
- Data / metric: DCASE 2026 Task 4 data. CAPI-SDRi, label accuracy.
- Main result: CAPI-SDRi 8.6 dB vs 8.3 dB baseline; most of the gain from better tagging and fine-tuning the separator.
- Limitation: Small gains; all choices made on the dev set; no size, latency or code.
- Relevance to my thesis (1 line): M3: evidence that in a cascade the tagger (my M2 detector) is the bottleneck, and that improving the separator around it gives little.
- Tags: separation | audio-tagging | ensemble | DCASE-2026
