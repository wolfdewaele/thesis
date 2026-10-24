# Log until next meeting (date to fill in)

## Work
- 2026-10-23: surveyed all Clarity/Cadenza rounds (none is an event detection task); found DCASE 2017 Task 4
  and candidate datasets (FSD50K, AudioSet-strong, STARSS23); asked Stijn about own mixtures vs Clarity data.
- 2026-10-23: read the UGent masterproef rules and the ir rubric; set up this notes repo (D001).
- 2026-10-23: defined the four modules with Stijn's input; literature study is built up throughout the year.
- 2026-10-23: set up the project layout for all four modules (code package `hased`, configs, data, thesis LaTeX), see README.
- 2026-10-24: compared SED datasets (DESED, MAESTRO, own FSD50K+Clarity mixtures, CEC3 Task 3, AudioSet-strong,
  DCASE 2017 Task 4, SINGA:PURA, STARSS23, ...): none has hearing-aid signals with event labels, so own mixtures
  for training and real sets for testing (notes/literature/datasets-sed-2026-10.md, D003).
- 2026-10-24: counted how often target events overlap speech in time: 15-30% of events in AudioSet-strong,
  15-19% in DESED, 6-37% in DCASE 2017 Task 4; so real data rarely has warning sounds during speech.
- 2026-10-23: first literature and code survey (SED models, hearing-aid latency, target sound extraction,
  detect-and-separate); 13 draft paper notes in notes/literature/. No paper found on event detection in hearing
  aids under hearing loss: likely the thesis contribution.
- 2026-10-24: browsed the DCASE 2024 Task 4 baseline and three DCASE 2026 Task 4 reports. Joint detect + separate
  systems (Bando, Kwon) roughly double the baseline score; in the cascade (Deng) the tagger is the bottleneck.
- 2026-10-24: looked up how SED pipelines start (preprocessing, log-mel input, multichannel features, architecture
  families); plan for the first SED baseline: mono, 16 kHz log-mel, frame-wise CRNN on own mixtures.

## Decisions made
- D001 notes as Markdown in this repo (decided)
- D002 own FSD50K mixtures (proposed, waiting for Stijn)
- D003 real test sets: DCASE 2017 Task 4, SINGA:PURA, STARSS23 (proposed)

## Problems and open questions for Stijn
- Own FSD50K mixtures, or the Clarity data itself? (D002)

## AI use (broad)
- Claude: overview of Clarity rounds and datasets, looking up UGent rules, setting up the notes structure,
  first literature/code overview and draft paper notes (to verify while reading).

## After the meeting: Stijn's feedback -> what I will do with it
