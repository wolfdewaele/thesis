# D002: Build own mixtures from FSD50K instead of using Clarity data directly (2026-10-23)

- Context: no Clarity/Cadenza round has event labels. FSD50K has the target classes (Siren, Vehicle horn,
  Alarm, Doorbell, Telephone, Ringtone) but clip-level labels only, rarely with speech.
- Options considered: A) Clarity data as is, B) own mixtures: FSD50K events + speech + background, placed
  with the PyClarity CEC2 scene generator, C) DCASE 2017 Task 4 only.
- Choice and reason: B (proposed). Gives exact onsets/offsets and SNRs, and hearing-aid realism
  (BTE mics, HRIRs). DCASE 2017 Task 4 and STARSS23 as real-data tests.
- Would change if: Stijn intended the Clarity data itself to be used.
- Status: proposed, question sent to Stijn on 2026-10-23
