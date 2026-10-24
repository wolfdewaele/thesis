import json
from pathlib import Path

import numpy as np
import soundfile as sf
import yaml
from scipy.io import savemat, wavfile

from hased.data.mixtures import SR, facing_talker, load_fsd50k, make_mixtures, place, render

N_HOA = 49  # order 6
DELAY = 30  # direct-path delay of the fake HOA IRs, in samples


def fake_data(root):
    """Tiny stand-ins for the Clarity CEC2 and FSD50K folders: W-only IRs, HRIRs that pass W through."""
    c = root / "clarity_data"
    for d in ("metadata", "dev/rooms/HOA_IRs", "dev/targets", "hrir/HRIRs_MAT"):
        (c / d).mkdir(parents=True)
    room = {"name": "R06001", "listener": {"position": [0, 0, 1], "view_vector": [1, 0, 0]},
            "target": {"position": [1, 1, 1]}, "interferers": [{"position": [2, 0, 1]}] * 3}
    (c / "metadata/rooms.dev.json").write_text(json.dumps([room]))
    (c / "metadata/hrir_data.json").write_text(
        json.dumps({"matrix": np.eye(N_HOA).tolist(), "selected_channels": list(range(N_HOA))}))
    ir = np.zeros((200, N_HOA), np.float32)
    ir[DELAY, 0] = 1.0
    for pos in ("t", "i1", "i2", "i3"):
        wavfile.write(c / f"dev/rooms/HOA_IRs/HOA_R06001_{pos}.wav", SR, ir)
    hrir = np.zeros((16, N_HOA, 2))
    hrir[0, 0] = 1.0
    for ch in ("BTE_fr", "BTE_mid", "BTE_rear"):
        savemat(c / f"hrir/HRIRs_MAT/KEMAR-{ch}.mat", {"M_data": hrir})
    rng = np.random.default_rng(0)
    burst = np.r_[np.zeros(SR // 4), 0.3 * rng.standard_normal(SR), np.zeros(SR // 4)]
    sf.write(c / "dev/targets/S0001.wav", burst, SR)

    f = root / "fsd50k"
    (f / "FSD50K.ground_truth").mkdir(parents=True)
    (f / "FSD50K.dev_audio").mkdir()
    vocab = ["Siren", "Alarm", "Telephone", "Ringtone", "Vehicle_horn_and_car_horn_and_honking",
             "Doorbell", "Rain"]
    (f / "FSD50K.ground_truth/vocabulary.csv").write_text(
        "".join(f"{i},{v},/m/{i}\n" for i, v in enumerate(vocab)))
    clips = {"1": "Siren,Alarm", "2": "Ringtone,Telephone,Alarm", "3": "Telephone,Alarm",
             "4": "Siren,Alarm,Vehicle_horn_and_car_horn_and_honking", "5": "Alarm",
             "6": "Vehicle_horn_and_car_horn_and_honking", "7": "Doorbell,Alarm",
             "8": "Rain", "9": "Rain,Siren,Alarm"}
    rows = "".join(f'{k},"{v}",x,train\n' for k, v in clips.items())
    (f / "FSD50K.ground_truth/dev.csv").write_text("fname,labels,mids,split\n" + rows)
    for k in clips:
        sf.write(f / f"FSD50K.dev_audio/{k}.wav", 0.3 * rng.standard_normal(SR // 2), SR)
    return c, f


CLASSES = {"siren": "Siren", "horn": "Vehicle_horn_and_car_horn_and_honking", "alarm": "Alarm",
           "doorbell": "Doorbell", "telephone": "Telephone", "ringtone": "Ringtone"}


def test_fsd50k_most_specific_class(tmp_path):
    _, f = fake_data(tmp_path)
    events, backgrounds = load_fsd50k(f, "train", CLASSES, ["Rain"])
    assert events == {"siren": ["1", "9"], "horn": ["6"], "alarm": ["5"], "doorbell": ["7"],
                      "telephone": ["3"], "ringtone": ["2"]}  # 4 (siren + horn) is skipped
    assert backgrounds == ["8"]  # 9 has a siren


def test_place_honours_overlap():
    rng = np.random.default_rng(0)
    n, speech, length = 10 * SR, (3 * SR, 5 * SR), SR
    for want in (True, False):
        for _ in range(50):
            on = place(rng, length, n, speech, want)
            assert 0 <= on <= n - length
            assert (on < speech[1] and on + length > speech[0]) == want


def test_render_label_alignment(tmp_path):
    c, _ = fake_data(tmp_path)
    room = json.loads((c / "metadata/rooms.dev.json").read_text())[0]
    _, ir = wavfile.read(c / "dev/rooms/HOA_IRs/HOA_R06001_i1.wav")
    hrir = {"M_data": np.pad(np.ones((1, N_HOA, 2)), ((0, 15), (0, 0), (0, 0)))}
    meta = {"matrix": np.eye(N_HOA).tolist(), "selected_channels": list(range(N_HOA))}
    x = np.ones(100)
    y, delay = render(x, 1000, ir.astype(float), facing_talker(room), [hrir] * 3, meta, 2000)
    active = np.flatnonzero(np.abs(y[:, 0]) > 1e-9)
    assert y.shape == (2000, 6) and delay == DELAY
    assert active[0] == 1000 + DELAY  # label onset = placement + direct-path delay


def test_make_mixtures_end_to_end(tmp_path):
    c, f = fake_data(tmp_path)
    cfg = yaml.safe_load(Path("configs/data/pilot_v0.yaml").read_text())
    cfg.update(n_scenes=4, duration_s=3.0, heads=["KEMAR"], background_labels=["Rain"],
               clarity_root=str(c), fsd50k_root=str(f), out_dir=str(tmp_path / "out"))
    scenes = make_mixtures(cfg)
    assert make_mixtures({**cfg, "out_dir": str(tmp_path / "out2")}) == scenes  # same config + seed, same scenes
    mix, sr = sf.read(tmp_path / "out/audio/pilot_v0_00000.flac")
    assert sr == SR and mix.shape == (3 * SR, 6)
    labels = (tmp_path / "out/labels.tsv").read_text().splitlines()
    assert len(labels) == 1 + sum(len(s["events"]) for s in scenes)
    for s in scenes:
        for e in s["events"]:
            assert 0 <= e["onset_s"] < e["offset_s"] <= 3.0
    assert (tmp_path / "out/index.html").exists()

