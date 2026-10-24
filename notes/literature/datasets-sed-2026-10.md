# Datasets for sound event detection (module 2, 2026-10-24)

Comparison of candidate datasets for M2 (event class + onset/offset, first version by 14 Dec 2026).
Facts were checked on 2026-10-24 on the dataset pages (Zenodo, DCASE, Clarity docs) unless marked "(check)".
Target classes: siren, vehicle horn, alarm (car/smoke/fire/clock), doorbell, phone ringing.

## 1. Comparison

| Dataset | Target classes present | Labels | Size | Channels / format | Speech in it | Real or synthetic | License | Fit with Clarity + hearing loss |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **DESED** (DCASE Task 4, 2019-2024) | only `Alarm_bell_ringing` (lumps doorbell, phone, alarm clock); no siren, no horn | strong (synthetic + real validation), weak, unlabeled | 10k synthetic strong, 1,578 weak, 14,412 unlabeled, ~1.1k real strong validation; 10 s clips | mono, 16 kHz | yes (`Speech` is a class) | both: real from AudioSet/YouTube, synthetic via Scaper | Freesound parts CC; YouTube parts must be downloaded yourself | mono, domestic; can be rendered through BTE HRIRs, but classes miss most targets |
| **MAESTRO Real** [martin-morato_training_2023] | none (17 classes like footsteps, people talking, car, metro, cutlery; no alarms or sirens) | soft labels (0-1) at 1 s resolution from crowdsourced weak tags | 75 recordings, ~287 min total; public dev part 49 files, ~190 min | from TUT Acoustic Scenes 2016 (binaural in-ear mics, check) | yes (people talking, children) | real (5 scenes: cafe, city centre, grocery, metro station, residential) | non-commercial ("Other (Non-Commercial)" on Zenodo) | real, outdoor-ish, but wrong classes and 1 s resolution is too coarse for onsets |
| **Own mix: FSD50K + PyClarity scene generator** (D002) | all (Siren, Vehicle horn, Alarm, Doorbell, Telephone, Ringtone, ...) | strong and exact, because you place them (onset/offset, SNR) | as large as you generate; FSD50K = 51,197 clips, 108 h, 200 classes | 6-ch BTE (3 mics per ear) via Clarity HRIRs, plus listener audiograms | yes, you add it (target speech as in CEC2/CEC3) | synthetic mixture of real recordings | FSD50K per clip CC0 / CC BY / CC BY-NC: keep the per-clip license in the manifest | best fit: the only option that gives hearing-aid signals, hearing-loss conditions and exact labels |
| **CEC3 Task 3** (Clarity) | unknown and unlabeled; road scenes probably contain sirens/horns | no event labels; only scene type (road, station, party) and target speech times | 6,000 train + 2,500 dev scenes; eval 1,500 held back | 6-ch BTE hearing-aid signals at 48 kHz, made from 6th-order ambisonic recordings (Eigenmike em64) + measured IRs | yes (target sentences, party babble) | real backgrounds, simulated target | CC BY 4.0 (Zenodo); HRIRs "used with permission" | perfect acoustic fit, but only usable as **background** for your own mixtures |
| **AudioSet-strong** (Hershey et al., ICASSP 2021) | all (Siren and its subtypes, Vehicle horn, Car alarm, Smoke/Fire alarm, Doorbell, Telephone bell ringing, Ringtone, Alarm clock) | strong (start/end in s) | 103,463 train + 16,996 eval clips, 456 classes, ~935k events | mono-ish YouTube audio, 10 s | yes, a lot | real (YouTube) | labels CC BY 4.0; audio not redistributed, part of the videos is gone | too big to handle yourself; use it through checkpoints pretrained on it (PretrainedSED, EfficientSED) |
| **DCASE 2017 Task 4** (smart cars) | Ambulance/Police/Fire engine/Civil defense siren, Car alarm, Train horn, Air horn, Reversing beeps, Screaming (+8 vehicle classes) | weak train; strong test and eval | 51,172 train, 488 test, 1,103 eval clips, 17 classes | mono, 10 s, YouTube | some | real (YouTube) | AudioSet audio, download yourself | the best real test set for warning sounds; mono, so render it or test it as single-mic |
| **SINGA:PURA** (Ooi et al., 2021) | Car horn, Car alarm, Siren, Reverse beeper (coarse class "Alert signal") | strong, hierarchical (SONYC-UST-compatible) | 6,547 clips of 10 s (~18 h) | 1 or 7 channels depending on unit | yes (`Human voice`) | real (Singapore street sensors) | CC BY-SA 4.0 | good second real test for alert signals; not hearing-aid geometry |
| **STARSS23** (DCASE SELD) | Telephone, Bell, Knock, Door (+ speech, music, footsteps...) | strong + direction (DOA, distance) | ~7.5 h dev, ~3.5 h eval, 13 classes, 16 rooms | 4-ch FOA and 4-ch tetrahedral mic, 24 kHz | yes | real indoor | MIT | real spatial indoor test for phone/bell; no sirens or horns |
| **DCASE 2025/2026 Task 4** (S5, SpAudSyn) | Doorbell, AlarmClock, Buzzer, BicycleBell (18 indoor classes); no siren, no horn | the task outputs labels + separated sources, no onset/offset; generator metadata may hold times (check) | synthetic on demand | 4-ch FOA | yes | synthetic | custom NTT license (read before reuse) | M3 reference (detect then separate), not an M2 dataset |
| **UrbanSound8K / URBAN-SED** | Siren, Car horn (+8 urban classes) | UrbanSound8K weak (clips ≤4 s); URBAN-SED strong (Scaper) | 8,732 clips; URBAN-SED 10k soundscapes of 10 s | mono | no | real clips / synthetic soundscapes | CC BY-NC (check URBAN-SED) | quick prototypes and debugging only; small, no speech |
| **ESC-50** | Siren, Car horn, Clock alarm, Church bells, Door knock | weak, 5 s clips | 2,000 clips, 50 classes | mono | no | real clips | CC BY-NC | only for a quick sanity check |
| **SONYC-UST v2** | Car horn, Car alarm, Siren, Reverse beeper | weak (clip-level, multi-annotator) | 18,510 clips of 10 s (check) | mono | yes | real (New York) | CC BY 4.0 (check) | extra real outdoor negatives/positives, weak only |

Other, lower priority: TUT Sound Events 2016/2017 (real street, strong, but no sirens); WildDESED (DESED with real noise, 2024); emergency-vehicle siren sets on Kaggle/Scientific Data (clip-level, quality varies); AHEAD-DS (hearing-aid scenes, not events, see [zhong_dataset_2025]).

## 2. What the comparison shows

- No existing dataset has hearing-aid (BTE) signals **and** event labels for the target classes. Only your own mixtures can give both. This is also a thesis contribution: describe the generator and release its config.
- Real data with strong labels for warning sounds exists only in mono/array form (DCASE 2017 Task 4, SINGA:PURA) or indoor FOA (STARSS23). Use them as **real-world test sets**, never for tuning.
- DESED is still useful, but as a **pipeline check**: if your training and PSDS code reproduce the DCASE baseline score on DESED, your code is right, independent of your own data.
- MAESTRO is not a fit as data (wrong classes, 1 s labels, non-commercial), but the paper's idea is: soft labels for uncertain boundaries. Siren onsets fade in (Doppler, distance), so a soft onset ramp in your own labels is a cheap M2 extension.

## 3. Pitfalls to plan for now

- **Unlabeled targets in backgrounds**: CEC3 road/station recordings and FSD50K "background" clips can contain sirens or horns. In a mixture they become false "negatives". Screen backgrounds with a pretrained tagger (e.g. PANNs/EfficientSED on Siren, Vehicle horn) and drop or mark high-scoring segments.
- **Leakage**: split FSD50K by its official dev/eval split and by uploader, and keep CEC3 train/dev backgrounds apart, before mixing. A clip may appear in only one split.
- **Licenses**: FSD50K mixes CC0, CC BY and CC BY-NC per clip; MAESTRO and URBAN-SED are non-commercial. Fine for a thesis, but keep a per-clip license column in the mixture manifest so you can filter if you release data.
- **YouTube decay**: AudioSet and DCASE 2017 Task 4 audio may be partly missing. Record which clips you have in `data/SOURCES.md`.
- **Mono vs 6 channels**: start M2 on one channel (front mic, one ear) for speed, but generate and store all 6 so M3 and spatial cues do not need new data.

## 4. Recommendation for M2 (for Wolf to decide)

1. **Train/dev**: own mixtures v1 = FSD50K target events + speech (as in CEC2) + backgrounds (CEC3 Task 3 or CEC2 noise), rendered with the PyClarity scene generator to BTE signals. Exact labels from the generator; config + seed per version (`configs/data/mix_v1.yaml`).
2. **Model init**: a checkpoint pretrained on AudioSet-strong (EfficientSED or PretrainedSED), so AudioSet itself never has to be downloaded.
3. **Pipeline check**: DESED with the DCASE baseline recipe, once, to validate training and PSDS code.
4. **Real tests (frozen, never tuned on)**: DCASE 2017 Task 4 eval (sirens, horns, car alarm), SINGA:PURA (alert signals), STARSS23 (phone, bell). Report synthetic-to-real gap: that gap is a result in itself.
5. **Skip for M2**: MAESTRO as data, DCASE 2026 Task 4 (keep for M3), UrbanSound8K/ESC-50 except for a first smoke test.

This supports D002 and adds a fixed set of real test sets (proposed as D003).
