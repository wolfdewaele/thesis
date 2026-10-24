# Thesis repo: context for Claude Code

Master's thesis of Wolf De Waele, Ghent University (FEA), MSc Computer Science Engineering. Supervisor: Stijn.
Goal: detect important sound events (sirens, horns, alarms, doorbells, phones) in hearing-aid signals, so the
hearing aid lets them through instead of suppressing them as noise. Which sounds matter is user-configurable.
Submission: 20 May 2027 (Plato). About 800 hours, solo.

## Modules (defined by Wolf; do not redefine them)
1. Research approaches, set up architecture and workflows, consult papers.
2. Build event detection only: event type + onset/offset. First working version: 14 Dec 2026.
3. Integrate detection into speech enhancement; decide what to let through.
4. Write the thesis and fine-tune everything.
Throughout all modules: keep brief notes for the final writing, and improve other parts when new ideas appear.

## Conventions
- English, IEEE citations. AI use is described broadly in the thesis.
- Notes: `notes/` (see README). After meaningful work, suggest a dated line in `notes/log/next-meeting.md`,
  a paper note when a paper is consulted, a decision record for real choices, an experiment card per experiment.
- Code in `src/hased/`; scripts are thin; notebooks are exploration only.
- Never commit data, audio, checkpoints or outputs. Mixtures must be reproducible from a config + seed.
- Never tune on the test set.
- Always follow the ponytail skill (`.claude/skills/ponytail/`, level full) from the start of every session,
  unless Wolf says otherwise.
- Wolf works on Ubuntu and is learning Claude Code: give bash commands and briefly explain Claude Code features when useful.
