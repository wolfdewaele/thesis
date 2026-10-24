"""Print how often target events overlap speech in a strongly labelled dataset.

python scripts/speech_overlap.py audioset data/raw/audioset_strong/audioset_eval_strong.tsv \
    --mid-names data/raw/audioset_strong/mid_to_display_name.tsv
python scripts/speech_overlap.py desed data/raw/desed/metadata/validation/validation.tsv
python scripts/speech_overlap.py dcase2017 groundtruth_strong_label_evaluation_set.csv \
    --speech-from audioset_eval_strong.tsv audioset_train_strong.tsv --mid-names mid_to_display_name.tsv
"""

import argparse
from pathlib import Path

from hased.data.speech_overlap import (
    load_audioset_strong,
    load_dcase2017,
    load_desed,
    overlap_stats,
)

parser = argparse.ArgumentParser()
parser.add_argument("format", choices=["audioset", "desed", "dcase2017"])
parser.add_argument("labels", type=Path)
parser.add_argument("--mid-names", type=Path, help="AudioSet mid_to_display_name.tsv")
parser.add_argument("--speech-from", type=Path, nargs="+",
                    help="AudioSet-strong tsv(s) to take speech labels from (dcase2017)")
args = parser.parse_args()

if args.format == "audioset":
    events = load_audioset_strong(args.labels, args.mid_names)
elif args.format == "desed":
    events = load_desed(args.labels)
else:
    events = load_dcase2017(args.labels)

speech = None
if args.speech_from:
    speech = [e for tsv in args.speech_from for e in load_audioset_strong(tsv, args.mid_names)]
    labelled = {clip for clip, *_ in speech}
    clips = {clip for clip, *_ in events}
    print(f"clips with AudioSet-strong labels: {len(clips & labelled)} of {len(clips)}")
    events = [e for e in events if e[0] in labelled]

print(f"{'group':28} events clips ev+speech clips+speech time-under-speech")
for group, s in overlap_stats(events, speech).items():
    print(f"{group:28} {s['events']:6} {s['clips']:5} {s['events_with_speech']:9} "
          f"{s['clips_with_speech']:12} {s['time_share_under_speech']:17.0%}")
