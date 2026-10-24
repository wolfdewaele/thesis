"""Mixtures of FSD50K events + Clarity speech + FSD50K background, rendered to 6 BTE channels.

Scene i is drawn from np.random.default_rng([seed, i]), so a scene does not depend on the others,
and every draw is written to scenes.json. Rendering reuses the PyClarity CEC2 HOA tools: source
convolved with the room's HOA impulse response, rotated so the head faces the talker, decoded to
the BTE front/mid/rear HRIR pairs. Channel order: BTE_fr L R, BTE_mid L R, BTE_rear L R.
Labels are seconds at the microphones (placement + direct-path delay); reverb tails are not labelled.
"""

import csv
import json
import math
from functools import cache
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
import yaml
from clarity.data import HOA_tools_cec2 as hoa
from matplotlib.figure import Figure
from scipy.io import loadmat, wavfile
from scipy.signal import fftconvolve
from scipy.spatial.transform import Rotation

SR = 44100  # Clarity rate; FSD50K is 44.1 kHz too
ORDER = 6  # ambisonic order of the CEC2 HOA IRs
BTE = ["BTE_fr", "BTE_mid", "BTE_rear"]


def load_fsd50k(root, split: str, classes: dict[str, str], background_labels: list[str]):
    """Event clips per class {our label: [fname]} and background clips [fname] from FSD50K dev.csv.

    FSD50K labels are propagated up the AudioSet ontology (a Siren clip is also labelled Alarm), so
    each clip gets its most specific target class. Clips with two unrelated targets are skipped,
    and backgrounds never carry a target label.
    """
    gt = Path(root) / "FSD50K.ground_truth"
    with open(gt / "vocabulary.csv", newline="") as f:
        vocab = {row[1] for row in csv.reader(f)}
    unknown = (set(classes.values()) | set(background_labels)) - vocab
    if unknown:
        raise ValueError(f"not in the FSD50K vocabulary: {sorted(unknown)}")
    with open(gt / "dev.csv", newline="") as f:
        rows = [(r["fname"], set(r["labels"].split(",")))
                for r in csv.DictReader(f) if r["split"] == split]

    targets = set(classes.values())
    clips = {t: {f for f, labels in rows if t in labels} for t in targets}
    # A is an ancestor of B when every B clip also has A
    ancestors = {b: {a for a in targets if a != b and clips[b] <= clips[a]} for b in targets}
    ours = {fsd: name for name, fsd in classes.items()}
    events: dict[str, list[str]] = {name: [] for name in classes}
    backgrounds = []
    for fname, labels in sorted(rows):
        hits = labels & targets
        leaves = hits - set().union(*(ancestors[h] for h in hits))
        if len(leaves) == 1:
            events[ours[leaves.pop()]].append(fname)
        elif not hits and labels & set(background_labels):
            backgrounds.append(fname)
    return events, backgrounds


def place(rng, length: int, n: int, speech: tuple[int, int], overlap: bool, tries: int = 100) -> int:
    """Onset so that [onset, onset + length) overlaps the speech interval, or not, as asked."""
    for _ in range(tries):
        onset = int(rng.integers(0, n - length + 1))
        if (onset < speech[1] and onset + length > speech[0]) == overlap:
            return onset
    # shortcut: gives up when there is no room beside the speech; scenes.json records the real overlap
    return onset


def segment(rng, path, max_len: int):
    """Random part of at most max_len samples of the clip, leading/trailing silence trimmed.

    shortcut: silences inside the part stay labelled as event; fine for the pilot, revisit if
    labels look too long when listening.
    """
    x, _ = librosa.load(path, sr=SR)
    _, (a, b) = librosa.effects.trim(x, top_db=40)
    if b - a > max_len:
        a = int(rng.integers(a, b - max_len + 1))
        _, (a2, b2) = librosa.effects.trim(x[a:a + max_len], top_db=40)
        a, b = a + a2, a + b2
    return x[a:b], a, b


def facing_talker(room: dict) -> np.ndarray:
    """HOA rotation matrix that turns the listener's head towards the talker (CEC2 convention)."""
    lis, tal = room["listener"]["position"], room["target"]["position"]
    view = room["listener"]["view_vector"]
    theta = math.atan2(tal[1] - lis[1], tal[0] - lis[0]) - math.atan2(view[1], view[0])
    foa = np.linalg.inv(Rotation.from_euler("y", math.degrees(theta), degrees=True).as_matrix())
    return hoa.compute_rotation_matrix(ORDER, foa)


def render(x, onset: int, ir, rot, hrirs, hrir_meta, n: int):
    """Mono x placed at onset in an (n, 6) BTE signal; also returns the direct-path delay (samples)."""
    # every step is linear and time-invariant, so the chain is applied to the IR once (a 6-channel
    # BRIR) instead of to the signal: same result as CEC2's order, about 10x faster
    brir = np.hstack([hoa.binaural_mixdown(ir[:, :(ORDER + 1) ** 2] @ rot, hrir, hrir_meta)
                      for hrir in hrirs])
    y = fftconvolve(x[:, None], brir, axes=0)
    out = np.zeros((n, y.shape[1]))
    m = min(len(y), n - onset)
    out[onset:onset + m] = y[:m]
    w = np.abs(ir[:, 0])
    return out, int(np.argmax(w >= 0.5 * w.max()))


def rms(x, a: int, b: int) -> float:
    """RMS of the front BTE pair between samples a and b (where SNRs are defined)."""
    return float(np.sqrt(np.mean(x[a:b, :2] ** 2))) + 1e-12


@cache
def _hrir(path: str):
    return loadmat(path)


@cache
def _hoa_ir(path: str):
    return wavfile.read(path)[1].astype(np.float64)


def make_scene(cfg, i, rooms, speech_files, events, backgrounds, hrir_meta):
    """Draw and render scene i; returns its description and the (n, 6) mixture."""
    rng = np.random.default_rng([cfg["seed"], i])
    n = int(cfg["duration_s"] * SR)
    clarity = Path(cfg["clarity_root"])
    fsd_audio = Path(cfg["fsd50k_root"]) / "FSD50K.dev_audio"
    room = rooms[rng.integers(len(rooms))]
    head = str(rng.choice(cfg["heads"]))
    rot = facing_talker(room)
    hrirs = [_hrir(str(clarity / f"hrir/HRIRs_MAT/{head}-{ch}.mat")) for ch in BTE]

    def ir(pos):
        return _hoa_ir(str(clarity / f"{cfg['clarity_split']}/rooms/HOA_IRs/HOA_{room['name']}_{pos}.wav"))

    slots = list(rng.permutation([f"i{k + 1}" for k in range(len(room["interferers"]))]))
    lo, hi = cfg["n_events"]
    assert hi < len(slots), "one interferer position is kept for the background"

    # background: looped to the scene length from a random start
    bg_file = str(rng.choice(backgrounds))
    x, _, _ = segment(rng, fsd_audio / f"{bg_file}.wav", 10**9)
    start = int(rng.integers(len(x)))
    x = np.tile(x, n // len(x) + 2)[start:start + n]  # shortcut: hard loop seams, fine for noise beds
    bg_pos = slots.pop()
    bg, _ = render(x, 0, ir(bg_pos), rot, hrirs, hrir_meta, n)
    bg *= 10 ** (cfg["background_dbfs"] / 20) / rms(bg, 0, n)

    # speech: one Clarity target utterance at the talker position
    sp_file = speech_files[rng.integers(len(speech_files))]
    x, a, b = segment(rng, sp_file, n)
    sp_on = int(rng.integers(0, n - len(x) + 1))
    sp, delay = render(x, sp_on, ir("t"), rot, hrirs, hrir_meta, n)
    s0, s1 = sp_on + delay, min(sp_on + len(x) + delay, n)
    snr = float(rng.uniform(*cfg["snr_speech_db"]))
    sp *= 10 ** (snr / 20) * rms(bg, s0, s1) / rms(sp, s0, s1)
    mix = bg + sp
    scene = {
        "id": f"{cfg['name']}_{i:05d}", "room": room["name"], "head": head,
        "speech": {"file": sp_file.name, "segment_s": [a / SR, b / SR], "position": "t",
                   "onset_s": s0 / SR, "offset_s": s1 / SR, "snr_db": snr},
        "background": {"file": bg_file, "start_s": start / SR, "position": bg_pos},
        "events": [],
    }

    for _ in range(int(rng.integers(lo, hi + 1))):
        label = str(rng.choice(list(events)))
        fname = str(rng.choice(events[label]))
        x, a, b = segment(rng, fsd_audio / f"{fname}.wav", int(min(cfg["max_event_s"], cfg["duration_s"]) * SR))
        want = bool(rng.random() < cfg["p_event_overlaps_speech"])
        onset = place(rng, len(x), n, (sp_on, sp_on + s1 - s0), want)
        pos = slots.pop()
        ev, delay = render(x, onset, ir(pos), rot, hrirs, hrir_meta, n)
        e0, e1 = onset + delay, min(onset + len(x) + delay, n)
        snr = float(rng.uniform(*cfg["snr_event_db"]))
        ev *= 10 ** (snr / 20) * rms(bg, e0, e1) / rms(ev, e0, e1)
        mix += ev
        scene["events"].append({
            "label": label, "file": fname, "segment_s": [a / SR, b / SR], "position": pos,
            "onset_s": e0 / SR, "offset_s": e1 / SR, "snr_db": snr,
            "overlaps_speech": bool(e0 < s1 and e1 > s0),
        })

    peak = np.abs(mix).max()
    scene["mix_gain"] = float(min(1.0, 0.99 / peak))  # only ever scales down; SNRs are unchanged
    return scene, mix * scene["mix_gain"]


def plot(path, mix, scene, classes):
    """Spectrogram of the front-left BTE mic with the labels drawn on top."""
    fig = Figure(figsize=(12, 3.5))
    ax = fig.subplots()
    ax.specgram(mix[:, 0], NFFT=1024, noverlap=768, Fs=SR, cmap="magma", vmin=-140)
    ax.set_ylim(0, 12000)
    s = scene["speech"]
    ax.hlines(11000, s["onset_s"], s["offset_s"], color="white", lw=6)
    ax.text(s["onset_s"], 11400, "speech", color="white", fontsize=8)
    for k, e in enumerate(scene["events"]):
        y = 9500 - 1500 * k
        ax.hlines(y, e["onset_s"], e["offset_s"], color=f"C{classes.index(e['label'])}", lw=6)
        ax.text(e["onset_s"], y + 400, f"{e['label']} {e['snr_db']:+.0f} dB", color="white", fontsize=8)
    ax.set(title=scene["id"], xlabel="time (s)", ylabel="Hz")
    fig.tight_layout()
    fig.savefig(path, dpi=80)


def make_mixtures(cfg: dict):
    """Build the mixture set described by a configs/data/*.yaml config (loaded as a dict)."""
    out = Path(cfg["out_dir"])
    if out.exists():
        raise FileExistsError(f"{out} exists; delete it to rebuild, or use a new name and out_dir")
    clarity, split = Path(cfg["clarity_root"]), cfg["clarity_split"]
    with open(clarity / f"metadata/rooms.{split}.json") as f:
        rooms = json.load(f)
    # rooms whose HOA IRs were extracted; lets a small set use only part of the 144 GB IR package
    rooms = [r for r in rooms if (clarity / f"{split}/rooms/HOA_IRs/HOA_{r['name']}_t.wav").exists()]
    with open(clarity / "metadata/hrir_data.json") as f:
        hrir_meta = json.load(f)
    speech_files = sorted((clarity / split / "targets").glob("*.wav"))
    events, backgrounds = load_fsd50k(cfg["fsd50k_root"], cfg["fsd50k_split"],
                                      cfg["event_classes"], cfg["background_labels"])
    empty = [c for c, fs in events.items() if not fs] + ([] if backgrounds else ["background"])
    if empty or not speech_files or not rooms:
        raise ValueError(f"no clips found for {empty or 'speech/rooms'}; check the paths in the config")
    print(f"{len(rooms)} rooms, {len(speech_files)} utterances, {len(backgrounds)} backgrounds, "
          + ", ".join(f"{c} {len(fs)}" for c, fs in events.items()))

    for d in ("audio", "preview", "plots"):
        (out / d).mkdir(parents=True)
    (out / "config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))  # incl. overrides
    classes = list(cfg["event_classes"])
    scenes = []
    for i in range(cfg["n_scenes"]):
        scene, mix = make_scene(cfg, i, rooms, speech_files, events, backgrounds, hrir_meta)
        sf.write(out / f"audio/{scene['id']}.flac", mix, SR, subtype="PCM_16")
        sf.write(out / f"preview/{scene['id']}.wav", mix[:, :2], SR, subtype="PCM_16")
        plot(out / f"plots/{scene['id']}.png", mix, scene, classes)
        scenes.append(scene)
        print(f"{scene['id']}: {', '.join(e['label'] for e in scene['events']) or 'no events'}")

    # DESED-style strong labels, readable by sed_scores_eval
    rows = [f"{s['id']}.flac\t{e['onset_s']:.3f}\t{e['offset_s']:.3f}\t{e['label']}"
            for s in scenes for e in s["events"]]
    (out / "labels.tsv").write_text("\n".join(["filename\tonset\toffset\tevent_label", *rows]) + "\n")
    with open(out / "scenes.json", "w") as f:
        json.dump(scenes, f, indent=1)
    write_index(out / "index.html", scenes)
    return scenes


def write_index(path, scenes):
    """One page to listen to every scene (front BTE pair) next to its spectrogram and labels."""
    parts = [("<!doctype html><meta charset=utf-8><title>mixtures</title>"
              "<body style='font-family:sans-serif;max-width:1000px;margin:auto'>")]
    for s in scenes:
        sp = s["speech"]
        rows = "".join(
            f"<li>{e['label']} {e['onset_s']:.2f}-{e['offset_s']:.2f} s, {e['snr_db']:+.1f} dB, "
            f"{'overlaps speech' if e['overlaps_speech'] else 'no speech overlap'}, FSD50K {e['file']}</li>"
            for e in s["events"]) or "<li>no events</li>"
        parts.append(
            f"<h3 id={s['id']}>{s['id']}</h3><p>room {s['room']}, head {s['head']}, speech "
            f"{sp['onset_s']:.2f}-{sp['offset_s']:.2f} s at {sp['snr_db']:+.1f} dB, background FSD50K "
            f"{s['background']['file']}</p><ul>{rows}</ul>"
            f"<audio controls preload=none src='preview/{s['id']}.wav'></audio><br>"
            f"<img src='plots/{s['id']}.png' width=960 loading=lazy>")
    Path(path).write_text("\n".join(parts))
