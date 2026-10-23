# configs

One YAML file per reusable choice, combined per experiment. Every run logs the exact config it used.

- `data/`        mixture recipes and dataset versions (e.g. `mix_v1.yaml`: sources, SNR ranges, seed)
- `model/`       model architectures and hyperparameters
- `experiment/`  one file per experiment, referencing a data and a model config (matches `notes/experiments/E00x-*.md`)

Never edit a config that a finished experiment used; copy it to a new name instead.
