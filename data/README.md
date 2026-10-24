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

## Making mixtures (FSD50K + Clarity CEC2)

Code: `src/hased/data/mixtures.py`. Recipe: `configs/data/pilot_v0.yaml`. Each scene is 10 s, 44.1 kHz, 6 BTE
channels (front, mid, rear; left/right). It holds one Clarity talker, 0-2 FSD50K target events and one FSD50K
background, each placed in a CEC2 room and rendered with the PyClarity HOA tools.

### 1. Python (one time)

```bash
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"     # pulls pyclarity, which brings torch (a few GB)
pytest                         # tests/test_mixtures.py runs the whole pipeline on fake data
```

### 2. Downloads (one time, about 200 GB downloaded, 30-75 GB kept)

Put `data/` on a big disk first if needed: `ln -s /media/<you>/<drive>/thesis-data data`.

FSD50K (Zenodo record 4060432, CC BY; only the dev set is needed for training mixtures):

```bash
mkdir -p data/raw/fsd50k && cd data/raw/fsd50k
for f in FSD50K.dev_audio.z0{1..5} FSD50K.dev_audio.zip FSD50K.ground_truth.zip; do
  wget -c "https://zenodo.org/records/4060432/files/$f?download=1" -O "$f"
done
zip -s 0 FSD50K.dev_audio.zip --out dev_audio.zip && unzip -q dev_audio.zip && unzip -q FSD50K.ground_truth.zip
rm FSD50K.dev_audio.z0* FSD50K.dev_audio.zip dev_audio.zip   # keeps FSD50K.dev_audio/ and FSD50K.ground_truth/
cd -
```

Clarity CEC2 (https://mab.to/zU7TS8jJelkoD, download in the browser): `clarity_CEC2_core.v1_1.tgz` (28 GB) and
`clarity_CEC2_hoairs.v1_0.tgz` (144 GB). Extract only what the mixtures use:

```bash
mkdir -p data/raw/clarity_CEC2 && cd data/raw/clarity_CEC2
tar -tzf ~/Downloads/clarity_CEC2_core.v1_1.tgz | head      # check the paths start with clarity_data/
tar -xzf ~/Downloads/clarity_CEC2_core.v1_1.tgz clarity_data/metadata clarity_data/hrir clarity_data/dev/targets
# pilot: 100 dev rooms (about 2 GB); drop the wildcard's 060 to extract all 2500 dev rooms (49 GB)
tar -xzf ~/Downloads/clarity_CEC2_hoairs.v1_0.tgz --wildcards 'clarity_data/dev/rooms/HOA_IRs/HOA_R060*'
cd -
```

Only rooms whose IRs are extracted get used, so a partial extract is fine. Once extracted, the .tgz files
can be deleted. Note each download in `data/SOURCES.md`.

### 3. Make samples

```bash
python scripts/make_mixtures.py configs/data/pilot_v0.yaml                  # 100 scenes, a few seconds each
python scripts/make_mixtures.py configs/data/pilot_v0.yaml n_scenes=5 out_dir=data/processed/try   # quick look
xdg-open data/processed/pilot_v0/index.html     # listen and look at every scene in the browser
```

`key=value` overrides any config entry (value read as YAML, e.g. `p_event_overlaps_speech=0.5`), and the
config actually used is saved as `config.yaml` in the output folder. The script refuses to overwrite an
existing folder. For a recipe you keep, copy the YAML to a new name instead of overriding.

Output folder:

| File | What |
| --- | --- |
| `audio/<id>.flac` | 6-channel mixture (BTE_fr L R, BTE_mid L R, BTE_rear L R), the model input |
| `preview/<id>.wav` | front BTE pair only, for listening |
| `plots/<id>.png` | spectrogram (front left) with speech and event labels drawn on it |
| `labels.tsv` | strong labels, DESED format: filename, onset, offset, event_label (seconds) |
| `scenes.json` | every random draw per scene: room, head, files and segments, positions, SNRs, overlap |
| `index.html` | all scenes on one page: audio player, spectrogram, labels |
