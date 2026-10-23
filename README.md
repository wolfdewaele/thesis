# Thesis: important sound event detection for hearing aids

Master's thesis, Ghent University (Faculty of Engineering and Architecture), 2026-2027.
Author: Wolf De Waele. Supervisor: Stijn. Submission: 20 May 2027 (Plato).

This repo holds the thesis notes now, and the code and the thesis text later.
Everything is plain Markdown so it stays versioned with the code and converts easily to LaTeX.

## Layout

```
notes/
  literature/   one note per paper, named <citekey>.md (citekey from Zotero / Better BibTeX)
  decisions/    one record per real choice: D001-<topic>.md
  log/          one file per supervision meeting: work done since the previous meeting
                (append to next-meeting.md, rename it to YYYY-MM-DD.md after the meeting)
  outline.md    parking lot: one-line ideas under the future thesis chapters
templates/      copy these when creating a new note
references.bib  auto-exported by Zotero + Better BibTeX (do not edit by hand)
```

Added when code starts: `notes/experiments/`, `src/`, `configs/`, and W&B tracking.

## Habits (throughout all modules)

| What | When | Time |
| --- | --- | --- |
| Paper note (`templates/paper.md`) | whenever you consult a paper, all year (this builds the literature study) | 5-10 min |
| Decision record (`templates/decision.md`) | when you make a real choice | 5 min |
| Meeting log (`notes/log/next-meeting.md`) | a dated line when you finish something; tidy before each meeting with Stijn | 1-2 min per entry |
| Outline line (`notes/outline.md`) | whenever an idea for the text comes up | 1 min |

Rule of thumb: if a note takes more than 10 minutes, it is too long.
Commit at least once a week (`git commit -m "notes: ..."`). The dated history is part of the
process evidence the supervision committee grades (30% of the thesis grade).

Conventions agreed with Stijn: IEEE citations, thesis in English, AI use described broadly.

## Zotero setup (one time)

1. Install Zotero and the Better BibTeX plugin.
2. Create a collection `Thesis`.
3. Right-click the collection > Export Collection > format "Better BibTeX",
   tick "Keep updated", and save it as `references.bib` in this repo.
4. Use the Better BibTeX citekey as the filename of the paper note (e.g. `veluri2023semantic.md`).

## Obsidian (optional)

Open this folder as a vault for backlinks and a nicer editor. `.obsidian/workspace*` is git-ignored.
