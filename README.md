# Thesis: important sound event detection for hearing aids

Master's thesis, Ghent University (Faculty of Engineering and Architecture), 2026-2027.
Author: Wolf De Waele. Supervisor: Stijn. Submission: 20 May 2027 (Plato).

This repo holds the thesis notes now, and the code and the thesis text later.
Everything is plain Markdown so it stays versioned with the code and converts easily to LaTeX.

## Layout

```
notes/        thesis notes, kept all year (literature/, decisions/, experiments/, log/, outline.md)
templates/    copy these when creating a new note
src/hased/    Python package: data, models, training, evaluation, enhancement, utils
configs/      YAML configs for data, models and experiments
scripts/      thin command-line entry points (make mixtures, train, evaluate, make figures)
tests/        pytest tests (label alignment, metrics)
notebooks/    exploration only, never imported
data/         datasets and generated mixtures (git-ignored, see data/README.md)
outputs/      checkpoints and run outputs (git-ignored)
thesis/       LaTeX thesis, extended abstract, figures, references.bib
CLAUDE.md     context that Claude Code reads automatically
```

How the folders map to the modules:

| Module | Main folders |
| --- | --- |
| 1 Research, architecture, workflows | `notes/` |
| 2 Event classification (which events) | `src/hased/{data,models,training,evaluation}`, `configs/`, `scripts/`, `tests/` |
| 3 Event timing (onset/offset) | same folders as module 2 (strong labels, frame-level outputs, post-processing) |
| 4 Integration with speech enhancement | `src/hased/enhancement/`, `src/hased/evaluation/` |
| 5 Writing and fine-tuning | `thesis/` |
| Throughout | `notes/` (log, papers, decisions, experiments) |

## Python setup (when code starts)

```
curl -LsSf https://astral.sh/uv/install.sh | sh   # one time: install uv
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
```

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

1. Install Zotero and the Zotero Connector browser extension. Create a collection `Thesis`.
2. Name paper notes after Zotero's default BibTeX key, e.g. `veluri_semantic_2023.md`.
3. Better BibTeX (auto-updating `references.bib`): postponed. Version 9.0.71 does not support Zotero 10 yet
   (export fails). When a version for Zotero 10 is released: install it, right-click `Thesis` > Export... >
   format "Better BibTeX", tick "Keep updated", save as `thesis/references.bib`.
   Until then, export manually with the normal "BibTeX" format when the file is needed.

## Obsidian (optional)

Open this folder as a vault for backlinks and a nicer editor. `.obsidian/workspace*` is git-ignored.
