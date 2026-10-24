# zhong_dataset_2025: AHEAD-DS and YAMNet+

H. Zhong, J. M. Buchholz, J. Maclaren, S. Carlile, R. Lyon, "A dataset and model for recognition of audiologically relevant environments for hearing aids: AHEAD-DS and YAMNet+," arXiv:2508.10360, 2025.
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: No ready-to-use open dataset for hearing-aid scene recognition (HEAR-DS lacks mixing code).
- Method: Re-mix HEAR-DS-based recordings with released code; MobileNet (YAMNet+) classifier.
- Data / metric: 14 scene labels (traffic, in vehicle, speech in X ...). mAP 0.83, accuracy 0.93.
- Main result: ~30 ms processing per second of audio on a 2018 phone; data and model on Hugging Face.
- Limitation: Scenes, not events; no alarms or sirens; 960 ms windows.
- Relevance to my thesis (1 line): Hearing-aid context and a possible background source; shows the scene-vs-event gap your thesis fills.
- Tags: hearing-aid | datasets | efficiency
