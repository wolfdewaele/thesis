# How to find papers and code (repeatable)

Goal: a small, steady stream of relevant work, captured once in Zotero and once as a short note.
Budget: 30 min per week for the feed, plus deeper searches when a module starts.

## 1. One-time setup (about 1 hour)

1. **Zotero**: collection `Thesis` with sub-collections `SED`, `Hearing aids`, `Extraction-SE`, `Data-metrics`.
   Tags for status: `to-read`, `skimmed`, `read`, `cited`.
2. **Alerts** (all to email):
   - Google Scholar: "Create alert" on queries `"sound event detection" hearing aid`,
     `"target sound extraction"`, `siren detection`, and "Follow" for key authors
     (B. Veluri, F. Schmid, R. Serizel, A. Mesaros, J. Barker).
   - Semantic Scholar: create a research feed and save 5-10 core papers (start with the paper notes in this folder);
     it recommends new related papers.
   - arXiv: the daily `eess.AS` listing (https://arxiv.org/list/eess.AS/new); skim titles only.
3. **DCASE**: subscribe to the dcase-discussions Google group (task announcements, results).

## 2. Weekly loop (30 min)

1. Skim alert emails and arXiv titles. Only add to Zotero what touches your current module.
2. For each added paper: save with the Zotero Connector into the right sub-collection, tag `to-read`.
3. Pick at most 1-2 papers to read; write the 5-10 min note (`templates/paper.md`, file name = Zotero BibTeX key).
4. Add a dated line to `notes/log/next-meeting.md` if something changes your plan.

## 3. Deep search (when a module or sub-question starts)

Use these in order; stop when new results only repeat what you have.

1. **DCASE results pages** (https://dcase.community/challenge2026/): every task has a results table with
   technical reports (4 pages, honest about what worked) and often code links. The best entry point for M2.
   Also the DCASE workshop proceedings.
2. **Citation graph**: put a seed paper (e.g. Semantic Hearing) into Connected Papers, ResearchRabbit or Litmaps,
   and look at "derivative works" (newer papers citing it).
3. **Code**: Papers with Code shut down in July 2025. Use the "Code" links on Hugging Face Papers
   (https://huggingface.co/papers), the project page in the paper, or GitHub search, e.g.
   `sound event detection language:Python pushed:>2025-01-01`.
4. **Hearing-aid venues**: Clarity workshop papers (https://claritychallenge.org/), ICASSP/Interspeech/WASPAA,
   IEEE/ACM TASLP, and JASA for audiology-side papers.

## 4. Checking code before you depend on it

- License: MIT, BSD or Apache are fine to reuse with attribution. No license file means you may read it but
  not copy it; custom licenses (e.g. NTT's PDF) need reading first.
- Last commit and open issues: does it still run? Are checkpoints still downloadable?
- Record anything you reuse in `data/SOURCES.md` or the experiment card, with the commit hash.

## 5. Claude Code tips for this

- In the repo, run `claude` and ask e.g.:
  `draft a paper note in notes/literature/ for arXiv 2311.00320 using templates/paper.md`.
  Always read and correct the draft: the note must reflect your own reading.
- `claude -p "summarize the open questions in notes/literature/*.md"` gives a one-shot answer without
  starting a chat (`-p` = print mode).
- Commit notes weekly:
  ```bash
  git add notes/ && git commit -m "notes: papers week 43" && git push
  ```
