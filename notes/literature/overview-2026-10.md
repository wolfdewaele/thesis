# Literature and code overview (module 1, 2026-10-23)

A focused map of methods to compare, not an exhaustive survey. Links and licenses were checked on 2026-10-23.
Paper notes marked "draft" were written by Claude from the abstract and key numbers: correct them when you read the paper.
M2 = event detection (type + onset/offset), M3 = integration with speech enhancement.

## 1. SED models and training recipes (M2 core)

| Work | Approach | Data | Metric | Size / latency | Code (license) | Relevance |
| --- | --- | --- | --- | --- | --- | --- |
| DCASE Task 4 baseline (DESED) | CRNN, mean-teacher semi-supervised; recent versions add BEATs embeddings | DESED (10 domestic classes, no sirens), MAESTRO | PSDS1/2, event F1 | small CRNN, offline (clip) | [DESED_task](https://github.com/DCASE-REPO/DESED_task) (MIT) | M2: the reference training pipeline and data loader structure to copy |
| PANNs (Kong et al., TASLP 2020) | CNN14 pretrained on AudioSet, frame-wise output for SED | AudioSet (527 classes) | mAP | 80M params; also 16 kHz and MobileNet variants | [audioset_tagging_cnn](https://github.com/qiuqiangkong/audioset_tagging_cnn) (no LICENSE file: ask before reusing code; checkpoints on Zenodo) | M2: easy pretrained baseline, weak temporal resolution |
| AST / BEATs | transformer encoders on patches; BEATs uses self-supervised tokenizer | AudioSet | mAP | ~90M, offline | [ast](https://github.com/YuanGongND/ast) (BSD-3), [BEATs](https://github.com/microsoft/unilm/tree/master/beats) (MIT) | M2: strong frozen/fine-tuned feature extractors |
| ATST-SED [shao_fine-tune_2024] | fine-tune frame-level self-supervised ATST in a CRNN, two-stage | DESED | PSDS1 | ~transformer size, offline | [ATST-SED](https://github.com/Audio-WestlakeU/ATST-SED) (MIT; checkpoints CC BY 4.0) | M2: state-of-the-art recipe on DESED |
| PretrainedSED [schmid_improving_2024] | AST/BEATs/ATST etc. pretrained on AudioSet-strong in stages, then fine-tuned | AudioSet-strong, DESED | PSDS1 | large, offline | [PretrainedSED](https://github.com/fschmid56/PretrainedSED) (MIT) | M2: ready AudioSet-strong checkpoints that already include Siren, Vehicle horn, Alarm etc. |
| EfficientSED [morocutti_exploring_2025] | MobileNetV3 + sequence model, distilled from transformer ensembles | AudioSet-strong | PSDS1 45.3 with ~5M params | small; throughput reported, not latency | [EfficientSED](https://github.com/theMoro/EfficientSED) (MIT) | M2: best starting point for a hearing-aid-sized detector |

## 2. Hearing-aid and low-latency context (constraints for M2 and M3)

| Work | What it gives you | Code (license) |
| --- | --- | --- |
| CEC2 overview (Akeroyd et al., ICASSP 2023) | 5 ms latency constraint for enhancement systems; interferers are speech, noise, music | [PyClarity](https://github.com/claritychallenge/clarity) (MIT) |
| Low-latency deep filtering for hearing aids [schroter_low_2022] | how a DNN enhancer is made hearing-aid compatible (short windows, deep filtering), with a listening test | [DeepFilterNet](https://github.com/Rikorose/DeepFilterNet) (MIT or Apache-2.0) |
| AHEAD-DS / YAMNet+ [zhong_dataset_2025] | open hearing-aid scene classification dataset built on HEAR-DS, with mixing code; MobileNet on phone (~30 ms per s of audio). Scenes only, no alarm or siren classes | [prism-ml](https://github.com/Australian-Future-Hearing-Initiative), data on Hugging Face |
| Real-time SELD on edge (Yeow et al., arXiv 2024) | on a Raspberry Pi, feature extraction can take up to 43% of the block time; shorter windows cost accuracy | none checked |

Gap found: no paper was found that does event detection inside a hearing-aid pipeline under hearing loss. That gap is your contribution, so keep searching for it each month (see the workflow).

## 3. Target sound extraction and selective hearing (M3 option A: extract what matters)

| Work | Approach | Data | Metric | Latency | Code (license) | Relevance |
| --- | --- | --- | --- | --- | --- | --- |
| Listen to what you want [ochiai_listen_2020] | separate the classes given by a one-hot/multi-hot query | FSD-based mixtures | SDRi | offline | none checked | M3: origin of class-conditioned extraction |
| Waveformer [veluri_real-time_2023] | causal dilated-conv encoder + transformer decoder conditioned on class | Scaper mixtures, FSDKaggle2018 (41 classes) + TAU backgrounds | SI-SNRi ~9.4 dB | 9.4 ms chunks, RTF 0.66 on one CPU core | [Waveformer](https://github.com/vb000/Waveformer) (MIT) | M3: real-time baseline |
| Semantic Hearing [veluri_semantic_2023] | binaural Waveformer, user picks classes to hear | Scaper: FSD50K, ESC-50, MUSDB, HRTFs/BRIRs; 20 classes incl. siren, car horn, alarm clock, door knock | SI-SNRi 7.2 dB, ITD/ILD error, MOS | 6.6 ms per 10 ms chunk on iPhone 11, ~20 ms end-to-end | [SemanticHearing](https://github.com/vb000/SemanticHearing) (MIT) | M3: closest related work; its data recipe is close to D002 |

## 4. Detect and separate together, and SED + separation (M3 option B: detector gates enhancement)

| Work | Approach | Metric | Code (license) | Relevance |
| --- | --- | --- | --- | --- |
| SED with separation front-end [turpault_improving_2020] | universal separation (FUSS) before SED, early/middle/late fusion | PSDS +0.018, F1 +1.7: small gain, mismatch hurts | [sound-separation](https://github.com/google-research/sound-separation) (Apache-2.0) | M3: evidence that naive cascading helps little |
| DCASE 2025/2026 Task 4 "S5" [nguyen_description_2026] | audio tagging (M2D) then label-queried separation (ResUNet); 18 classes incl. AlarmClock, Doorbell, Buzzer, BicycleBell; 2026 adds zero-target and same-class mixtures | CAPI-SDRi (baseline 6.8 dB on eval), label F1 | [dcase2026_task4_baseline](https://github.com/nttcslab/dcase2026_task4_baseline) (custom NTT license in a PDF: read before reuse) | M3: the current benchmark that does exactly "detect, then let through"; tech reports are on the results page |

Two architectures to compare in M3: (A) one class-conditioned extraction network (Semantic Hearing) or (B) a detector that steers a separate speech enhancer (gain, mask or bypass). B keeps M2 and M3 cleanly separated and lets the detector run on longer windows than the 5-10 ms audio path, because it only controls the audio. The price is detection delay, so measure onset delay as a metric in M2.

## 5. Data generation and evaluation tools (M2 foundation)

| Tool | Use | License |
| --- | --- | --- |
| [Scaper](https://github.com/justinsalamon/scaper) (Salamon et al., WASPAA 2017) | soundscapes with exact onset/offset labels from a seed; used by Waveformer and Semantic Hearing | BSD-3 |
| [SpatialScaper](https://github.com/iranroman/SpatialScaper) | spatial version with room IRs | CC BY 4.0 |
| PyClarity scene generator | hearing-aid (BTE) signals, listener audiograms, MSBG hearing loss | MIT |
| [sed_eval](https://github.com/TUT-ARG/sed_eval) | event-based and segment-based F1/ER (explained in [mesaros_sound_2021]) | MIT |
| [sed_scores_eval](https://github.com/fgnt/sed_scores_eval) [ebbers_threshold_2022] | exact PSDS and threshold-independent metrics; used by DCASE now | MIT |
| PSDS [bilen_framework_2020] | the DCASE ranking metric for SED | (see sed_scores_eval) |

## What this suggests (for Wolf to decide)

- M2 baseline path: fine-tune a small AudioSet-strong model (EfficientSED or PretrainedSED) on your own Scaper/PyClarity mixtures; evaluate with sed_scores_eval. This reuses checkpoints that already know Siren, Vehicle horn, Alarm and Doorbell.
- Use one data pipeline (config + seed, see CLAUDE.md) for both M2 and M3, so the same mixtures give SED labels and clean target signals.
- Keep the class set and the "importance" setting separate from the model: the detector outputs all classes, the user setting acts in M3.
