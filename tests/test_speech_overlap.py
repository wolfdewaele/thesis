from hased.data.speech_overlap import overlap_stats


def test_overlap_counts_and_time_share():
    events = [
        ("a", 0.0, 4.0, "Siren"),
        ("a", 2.0, 3.0, "Speech"),
        ("a", 2.5, 5.0, "Male speech, man speaking"),  # merged with the line above: 2.0-5.0
        ("b", 0.0, 2.0, "Siren"),
        ("b", 5.0, 6.0, "Speech"),  # same clip, no overlap in time
    ]
    s = overlap_stats(events)["siren"]
    assert (s["events"], s["clips"], s["events_with_speech"], s["clips_with_speech"]) == (2, 2, 1, 1)
    assert abs(s["time_share_under_speech"] - 2.0 / 6.0) < 1e-9


def test_speech_from_other_annotation():
    events = [("a", 0.0, 2.0, "Doorbell")]
    speech = [("a", 1.0, 3.0, "Speech")]
    assert overlap_stats(events, speech)["doorbell"]["time_share_under_speech"] == 0.5
