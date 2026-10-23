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
  log/          one entry per week: YYYY-Www.md (ISO week, e.g. 2026-W43)
  outline.md    parking lot: one-line ideas under the future thesis chapters
templates/      copy these when creating a new note
references.bib  auto-exported by Zotero + Better BibTeX (do not edit by hand)
```

Added later (module 2, when code starts): `notes/experiments/`, `src/`, `configs/`, and W&B tracking.

## Habits (module 1)

| What | When | Time |
| --- | --- | --- |
| Paper note (`templates/paper.md`) | after reading a paper seriously | 5-10 min |
| Decision record (`templates/decision.md`) | when you make a real choice | 5 min |
| Weekly log (`templates/weekly-log.md`) | every Friday | 15 min |
| Outline line (`notes/outline.md`) | whenever an idea for the text comes up | 1 min |

Rule of thumb: if a note takes more than 10 minutes, it is too long.
Commit at least once a week (`git commit -m "notes: week 2026-W44"`). The dated history is part of the
process evidence the supervision committee grades (30% of the thesis grade).

## Zotero setup (one time)

1. Install Zotero and the Better BibTeX plugin.
2. Create a collection `Thesis`.
3. Right-click the collection > Export Collection > format "Better BibLaTeX" (or "Better BibTeX"),
   tick "Keep updated", and save it as `references.bib` in this repo.
4. Use the Better BibTeX citekey as the filename of the paper note (e.g. `veluri2023semantic.md`).

## Obsidian (optional)

Open this folder as a vault for backlinks and a nicer editor. `.obsidian/workspace*` is git-ignored.
