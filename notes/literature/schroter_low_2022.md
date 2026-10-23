# schroter_low_2022: Low-latency SE for hearing aids using deep filtering

H. Schröter, T. Rosenkranz, A.-N. Escalante-B., A. Maier, "Low latency speech enhancement for hearing aids using deep filtering," IEEE/ACM TASLP, vol. 30, pp. 2716-2728, 2022. doi:10.1109/TASLP.2022.3198548
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Hearing aids need very short processing windows, which hurts frequency resolution for DNN enhancement.
- Method: Deep filtering (predicted complex filter over time-frequency), compared with complex ratio masks; per-band loss.
- Data / metric: Objective metrics + subjective listening study.
- Main result: Outperforms complex ratio mask; preferred over existing hearing-aid noise reduction.
- Limitation: Speech only: it suppresses everything else, including alarms.
- Relevance to my thesis (1 line): M3: candidate speech enhancer to steer with the detector; code DeepFilterNet (MIT/Apache-2.0).
- Tags: hearing-aid | speech-enhancement | latency
