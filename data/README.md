# data (not in Git)

Everything in this folder except this README is git-ignored. Datasets are large and get downloaded, not committed.

```
data/
  raw/         downloaded datasets, never modified (FSD50K, speech corpus, CEC3 backgrounds, DCASE 2017 Task 4, STARSS23)
  interim/     cleaned or resampled versions
  processed/   generated mixtures, one folder per version (mix_v1/, mix_v2/) with its labels and the config that made it
```

Generated mixtures must be reproducible from `configs/data/<version>.yaml` + seed, so they can always be deleted and rebuilt.
If disk space is short, make `data/` a symlink to an external drive: `ln -s /path/to/drive/thesis-data data`.
Record where each dataset came from (URL, version, download date) in `data/SOURCES.md`.
