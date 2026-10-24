# Datasets for sound event detection (modules 2-3, 2026-10-24)

Comparison of candidate datasets for M2-M3 (event class + onset/offset, first version by 14 Dec 2026).
Facts were checked on 2026-10-24 on the dataset pages (Zenodo, DCASE, Clarity docs) unless marked "(check)".
Target classes: siren, vehicle horn, alarm (car/smoke/fire/clock), doorbell, phone ringing.

## 1. Comparison

| Dataset | Target classes present | Labels | Size | Channels / format | Target events during speech (see §2) | Real or synthetic | License | Fit with Clarity + hearing loss |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **DESED** (DCASE Task 4, 2019-2024) | only `Alarm_bell_ringing` (lumps doorbell, phone, alarm clock); no siren, no horn | strong (synthetic + real validation), weak, unlabeled | 10k synthetic strong, 1,578 weak, 14,412 unlabeled, ~1.1k real strong validation; 10 s clips | mono, 16 kHz | few: 15% of alarm/bell events (63 of 420) overlap speech in validation, 19% (38 of 196) in public eval | both: real from AudioSet/YouTube, synthetic via Scaper | Freesound parts CC; YouTube parts must be downloaded yourself | mono, domestic; can be rendered through BTE HRIRs, but classes miss most targets |
| **MAESTRO Real** [martin-morato_training_2023] | none (17 classes like footsteps, people talking, car, metro, cutlery; no alarms or sirens) | soft labels (0-1) at 1 s resolution from crowdsourced weak tags | 75 recordings, ~287 min total; public dev part 49 files, ~190 min | from TUT Acoustic Scenes 2016 (binaural in-ear mics, check) | none: no target events at all | real (5 scenes: cafe, city centre, grocery, metro station, residential) | non-commercial ("Other (Non-Commercial)" on Zenodo) | real, outdoor-ish, but wrong classes and 1 s resolution is too coarse for onsets |
| **Own mix: FSD50K + PyClarity scene generator** (D002) | all (Siren, Vehicle horn, Alarm, Doorbell, Telephone, Ringtone, ...) | strong and exact, because you place them (onset/offset, SNR) | as large as you generate; FSD50K = 51,197 clips, 108 h, 200 classes (clip labels only, so FSD50K itself cannot show overlap) | 6-ch BTE (3 mics per ear) via Clarity HRIRs, plus listener audiograms | as many as you choose: set the share in the mixture config | synthetic mixture of real recordings | FSD50K per clip CC0 / CC BY / CC BY-NC: keep the per-clip license in the manifest | best fit: the only option that gives hearing-aid signals, hearing-loss conditions and exact labels |
| **CEC3 Task 3** (Clarity) | unknown and unlabeled; road scenes probably contain sirens/horns | no event labels; only scene type (road, station, party) and target speech times | 6,000 train + 2,500 dev scenes; eval 1,500 held back | 6-ch BTE hearing-aid signals at 48 kHz, made from 6th-order ambisonic recordings (Eigenmike em64) + measured IRs | unknown: speech in every scene, but events are not labelled | real backgrounds, simulated target | CC BY 4.0 (Zenodo); HRIRs "used with permission" | perfect acoustic fit, but only usable as **background** for your own mixtures |
| **AudioSet-strong** (Hershey et al., ICASSP 2021) | all (Siren and its subtypes, Vehicle horn, Car alarm, Smoke/Fire alarm, Doorbell, Telephone bell ringing, Ringtone, Alarm clock) | strong (start/end in s) | 103,463 train + 16,996 eval clips, 456 classes, ~935k events | mono-ish YouTube audio, 10 s | few: 15-30% of target events overlap speech, only 7-18% of target time is under speech | real (YouTube) | labels CC BY 4.0; audio not redistributed, part of the videos is gone | too big to handle yourself; use it through checkpoints pretrained on it (PretrainedSED, EfficientSED) |
| **DCASE 2017 Task 4** (smart cars) | Ambulance/Police/Fire engine/Civil defense siren, Car alarm, Train horn, Air horn, Reversing beeps, Screaming (+8 vehicle classes) | weak train; strong test and eval | 51,172 train, 488 test, 1,103 eval clips, 17 classes | mono, 10 s, YouTube | few, and no speech labels: on the 551 eval clips also in AudioSet-strong, 13% of siren events and 6% of horn events overlap speech | real (YouTube) | AudioSet audio, download yourself | the best real test set for warning sounds; mono, so render it or test it as single-mic |
| **SINGA:PURA** (Ooi et al., 2021) | Car horn, Car alarm, Siren, Reverse beeper (coarse class "Alert signal") | strong, hierarchical (SONYC-UST-compatible) | 6,547 clips of 10 s (~18 h) | 1 or 7 channels depending on unit | not counted yet (`Human voice` is labelled, so it can be) | real (Singapore street sensors) | CC BY-SA 4.0 | good second real test for alert signals; not hearing-aid geometry |
| **STARSS23** (DCASE SELD) | Telephone, Bell, Knock, Door (+ speech, music, footsteps...) | strong + direction (DOA, distance) | ~7.5 h dev, ~3.5 h eval, 13 classes, 16 rooms | 4-ch FOA and 4-ch tetrahedral mic, 24 kHz | not counted yet (speech classes are labelled, so it can be) | real indoor | MIT | real spatial indoor test for phone/bell; no sirens or horns |
| **DCASE 2025/2026 Task 4** (S5, SpAudSyn) | Doorbell, AlarmClock, Buzzer, BicycleBell (18 indoor classes); no siren, no horn | the task outputs labels + separated sources, no onset/offset; generator metadata may hold times (check) | synthetic on demand | 4-ch FOA | set by the generator (check) | synthetic | custom NTT license (read before reuse) | M4 reference (detect then separate), not an M2-M3 dataset |
| **UrbanSound8K / URBAN-SED** | Siren, Car horn (+8 urban classes) | UrbanSound8K weak (clips ≤4 s); URBAN-SED strong (Scaper) | 8,732 clips; URBAN-SED 10k soundscapes of 10 s | mono | unknown: one label per clip, speech not labelled | CC BY-NC (check URBAN-SED) | quick prototypes and debugging only; small, no speech |
| **ESC-50** | Siren, Car horn, Clock alarm, Church bells, Door knock | weak, 5 s clips | 2,000 clips, 50 classes | mono | unknown: one label per clip, speech not labelled | real clips | CC BY-NC | only for a quick sanity check |
| **SONYC-UST v2** | Car horn, Car alarm, Siren, Reverse beeper | weak (clip-level, multi-annotator) | 18,510 clips of 10 s (check) | mono | clip-level only: shows co-occurrence, not overlap in time | real (New York) | CC BY 4.0 (check) | extra real outdoor negatives/positives, weak only |

Other, lower priority: TUT Sound Events 2016/2017 (real street, strong, but no sirens); WildDESED (DESED with real noise, 2024); emergency-vehicle siren sets on Kaggle/Scientific Data (clip-level, quality varies); AHEAD-DS (hearing-aid scenes, not events, see [zhong_dataset_2025]).

## 2. Target events during speech (counted 2026-10-24)

"Overlap" means the event and a speech label are active at the same moment in the same clip, not only in the same clip.
Counted from the label files with `scripts/speech_overlap.py` (logic in `src/hased/data/speech_overlap.py`).
Speech = Speech, Male/Female/Child speech, Conversation, Narration, Babble, Whispering.
"Time under speech" = share of the summed event duration that has speech at the same time.

| Dataset (split) | Group | Events | Events overlapping speech | Time under speech |
| --- | --- | --- | --- | --- |
| AudioSet-strong (train, 103k clips) | siren | 2,129 | 437 (21%) | 8% |
| | horn | 4,027 | 588 (15%) | 7% |
| | alarm | 6,343 | 1,106 (17%) | 12% |
| | doorbell | 433 | 89 (21%) | 8% |
| | phone | 1,408 | 253 (18%) | 9% |
| AudioSet-strong (eval, 17k clips) | siren | 325 | 51 (16%) | 7% |
| | horn | 562 | 93 (17%) | 9% |
| | alarm | 1,027 | 175 (17%) | 10% |
| | doorbell | 111 | 33 (30%) | 18% |
| | phone | 412 | 75 (18%) | 10% |
| DESED real validation | Alarm_bell_ringing | 420 | 63 (15%) | 9% |
| DESED public eval | Alarm_bell_ringing | 196 | 38 (19%) | 9% |
| DCASE 2017 Task 4 eval (551 of 1,103 clips, speech taken from AudioSet-strong) | siren | 60 | 8 (13%) | 4% |
| | horn | 100 | 6 (6%) | 2% |
| | alarm (car alarm, reversing beeps) | 65 | 24 (37%) | 20% |
| DCASE 2017 Task 4 test (95 of 488 clips) | siren / horn / alarm | 19 / 22 / 43 | 6 / 2 / 7 | 14% / 8% / 5% |
| MAESTRO Real | - | 0 target events | - | - |

Groups: siren = Siren + ambulance/police/fire engine/civil defense; horn = vehicle, air/truck and train horn;
alarm = Alarm, car alarm, smoke/fire alarm, alarm clock, reversing beeps; phone = Telephone, telephone bell ringing, ringtone.

Not counted: SINGA:PURA and STARSS23 (strong labels with speech classes, but their label files are on Zenodo, which
this environment could not reach); FSD50K, UrbanSound8K, ESC-50, SONYC-UST (clip labels only, so overlap in time cannot
be measured); CEC3 Task 3 (no event labels).

What this means: in real data a target event rarely sounds **during** speech. Even in AudioSet-strong, the largest set,
only about 1 in 6 target events overlaps speech and at most a tenth of the event time is under speech, i.e. a few
hundred to about a thousand events per class in total. A detector trained on these sets mostly sees warning sounds without a talker on top,
which is the case a hearing aid cares about least. This is a strong argument for own mixtures (D002), where the share
of events under speech is a config parameter, and for reporting results separately for "event during speech" and
"event alone".

## 3. What the comparison shows

- No existing dataset has hearing-aid (BTE) signals **and** event labels for the target classes. Only your own mixtures can give both. This is also a thesis contribution: describe the generator and release its config.
- Real data with strong labels for warning sounds exists only in mono/array form (DCASE 2017 Task 4, SINGA:PURA) or indoor FOA (STARSS23). Use them as **real-world test sets**, never for tuning.
- DESED is still useful, but as a **pipeline check**: if your training and PSDS code reproduce the DCASE baseline score on DESED, your code is right, independent of your own data.
- MAESTRO is not a fit as data (wrong classes, 1 s labels, non-commercial), but the paper's idea is: soft labels for uncertain boundaries. Siren onsets fade in (Doppler, distance), so a soft onset ramp in your own labels is a cheap M3 (timing) extension.

## 4. Pitfalls to plan for now

- **Unlabeled targets in backgrounds**: CEC3 road/station recordings and FSD50K "background" clips can contain sirens or horns. In a mixture they become false "negatives". Screen backgrounds with a pretrained tagger (e.g. PANNs/EfficientSED on Siren, Vehicle horn) and drop or mark high-scoring segments.
- **Leakage**: split FSD50K by its official dev/eval split and by uploader, and keep CEC3 train/dev backgrounds apart, before mixing. A clip may appear in only one split.
- **Licenses**: FSD50K mixes CC0, CC BY and CC BY-NC per clip; MAESTRO and URBAN-SED are non-commercial. Fine for a thesis, but keep a per-clip license column in the mixture manifest so you can filter if you release data.
- **YouTube decay**: AudioSet and DCASE 2017 Task 4 audio may be partly missing. Record which clips you have in `data/SOURCES.md`.
- **Mono vs 6 channels**: start M2-M3 on one channel (front mic, one ear) for speed, but generate and store all 6 so M4 and spatial cues do not need new data.

## 5. Recommendation for M2-M3 (for Wolf to decide)

1. **Train/dev**: own mixtures v1 = FSD50K target events + speech (as in CEC2) + backgrounds (CEC3 Task 3 or CEC2 noise), rendered with the PyClarity scene generator to BTE signals. Exact labels from the generator; config + seed per version (`configs/data/mix_v1.yaml`).
2. **Model init**: a checkpoint pretrained on AudioSet-strong (EfficientSED or PretrainedSED), so AudioSet itself never has to be downloaded.
3. **Pipeline check**: DESED with the DCASE baseline recipe, once, to validate training and PSDS code.
4. **Real tests (frozen, never tuned on)**: DCASE 2017 Task 4 eval (sirens, horns, car alarm), SINGA:PURA (alert signals), STARSS23 (phone, bell). Report synthetic-to-real gap: that gap is a result in itself.
5. **Skip for M2-M3**: MAESTRO as data, DCASE 2026 Task 4 (keep for M4), UrbanSound8K/ESC-50 except for a first smoke test.

This supports D002 and adds a fixed set of real test sets (proposed as D003).
