# ochiai_listen_2020: Listen to what you want

T. Ochiai, M. Delcroix, Y. Koizumi, H. Ito, K. Kinoshita, S. Araki, "Listen to what you want: Neural network-based universal sound selector," Interspeech 2020. https://arxiv.org/abs/2006.05712
Status: draft by Claude from the abstract and key numbers (2026-10-23). Correct it when you read the paper.

- Problem: Extract all sounds of user-selected classes from a mixture with one network.
- Method: Separation network conditioned on a multi-hot class vector.
- Data / metric: Mixtures from FSD-based sound events. SDR improvement.
- Main result: Shows class-query extraction works for multiple target classes at once.
- Limitation: Offline; not causal.
- Relevance to my thesis (1 line): M3 background: origin of user-configurable class selection, the idea behind "importance is configurable".
- Tags: extraction | user-configurable
