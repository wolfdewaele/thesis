"""How often target events overlap speech in strongly labelled datasets.

Events are (clip, onset, offset, label) tuples in seconds. Used for the dataset comparison
(notes/literature/datasets-sed-2026-10.md) and later to report the same statistic for own mixtures.
"""

import csv
from collections import defaultdict
from pathlib import Path

Event = tuple[str, float, float, str]

# Target groups by label name; covers AudioSet display names, DESED and DCASE 2017 Task 4 names.
TARGET_GROUPS = {
    "siren": {"Siren", "Ambulance (siren)", "Police car (siren)", "Fire engine, fire truck (siren)",
              "Civil defense siren", "Ambulance siren", "Police car siren",
              "Fire engine, fire truck siren"},
    "horn": {"Vehicle horn, car horn, honking, toot", "Vehicle horn, car horn, honking",
             "Air horn, truck horn", "Train horn"},
    "alarm": {"Alarm", "Car alarm", "Smoke detector, smoke alarm", "Fire alarm", "Alarm clock",
              "Reversing beeps"},
    "doorbell": {"Doorbell", "Ding-dong"},
    "phone": {"Telephone", "Telephone bell ringing", "Ringtone"},
    "alarm_bell_ringing (DESED)": {"Alarm_bell_ringing"},
}

SPEECH_LABELS = {"Speech", "Male speech, man speaking", "Female speech, woman speaking",
                 "Child speech, kid speaking", "Conversation", "Narration, monologue",
                 "Hubbub, speech noise, speech babble", "Whispering"}


def _merge(intervals: list[tuple[float, float]]) -> list[tuple[float, float]]:
    merged: list[tuple[float, float]] = []
    for on, off in sorted(intervals):
        if merged and on <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], off))
        else:
            merged.append((on, off))
    return merged


def _covered(on: float, off: float, speech: list[tuple[float, float]]) -> float:
    return sum(max(0.0, min(off, s_off) - max(on, s_on)) for s_on, s_off in speech)


def overlap_stats(events: list[Event], speech_events: list[Event] | None = None) -> dict[str, dict]:
    """Per target group: events, clips, events overlapping speech, share of event time under speech.

    speech_events defaults to the speech labels inside `events`; pass it to take speech from another
    annotation of the same clips (e.g. AudioSet-strong for DCASE 2017 Task 4).
    """
    speech_src = events if speech_events is None else speech_events
    speech = defaultdict(list)
    for clip, on, off, label in speech_src:
        if label in SPEECH_LABELS:
            speech[clip].append((on, off))
    speech = {clip: _merge(iv) for clip, iv in speech.items()}

    stats = {}
    for group, names in TARGET_GROUPS.items():
        n = n_overlap = 0
        dur = dur_overlap = 0.0
        clips, clips_overlap = set(), set()
        for clip, on, off, label in events:
            if label not in names or off <= on:
                continue
            covered = _covered(on, off, speech.get(clip, []))
            n += 1
            dur += off - on
            clips.add(clip)
            if covered > 0:
                n_overlap += 1
                dur_overlap += covered
                clips_overlap.add(clip)
        if n:
            stats[group] = {"events": n, "clips": len(clips), "events_with_speech": n_overlap,
                            "clips_with_speech": len(clips_overlap),
                            "time_share_under_speech": dur_overlap / dur}
    return stats


def load_audioset_strong(tsv: Path, mid_names: Path) -> list[Event]:
    """AudioSet-strong tsv (segment_id, start, end, mid) with labels mapped to display names."""
    with open(mid_names) as f:
        names = dict(row for row in csv.reader(f, delimiter="\t"))
    with open(tsv) as f:
        rows = csv.reader(f, delimiter="\t")
        next(rows)
        return [(seg, float(on), float(off), names.get(mid, mid)) for seg, on, off, mid in rows]


def load_desed(tsv: Path) -> list[Event]:
    """DESED strong tsv (filename, onset, offset, event_label); rows without a label are skipped."""
    with open(tsv) as f:
        rows = csv.DictReader(f, delimiter="\t")
        return [(r["filename"], float(r["onset"]), float(r["offset"]), r["event_label"])
                for r in rows if r["event_label"]]


def load_dcase2017(csv_path: Path) -> list[Event]:
    """DCASE 2017 Task 4 strong csv (ytid_start_end.wav, onset, offset, label), clip renamed to the
    AudioSet segment id (ytid_startms) so it can be joined with AudioSet-strong."""
    events = []
    with open(csv_path) as f:
        for name, on, off, label in csv.reader(f, delimiter="\t"):
            ytid, start, _ = name.removesuffix(".wav").rsplit("_", 2)
            events.append((f"{ytid}_{round(float(start) * 1000)}", float(on), float(off), label))
    return events
