"""Generate synthetic EEG for a fast, fully offline demo."""

import numpy as np
import mne


def make_demo_raw(duration: float = 20.0, sfreq: float = 200.0, seed: int = 42) -> mne.io.RawArray:
    """Return reproducible synthetic EEG (not human recordings)."""
    if duration <= 0 or sfreq <= 0:
        raise ValueError("duration and sfreq must be positive")
    rng = np.random.default_rng(seed)
    n_samples = int(round(duration * sfreq))
    times = np.arange(n_samples) / sfreq
    frequencies = (10.0, 6.0, 18.0, 12.0)
    signals = np.array([
        15e-6 * np.sin(2 * np.pi * freq * times) + rng.normal(0, 3e-6, n_samples)
        for freq in frequencies
    ])
    info = mne.create_info(["F3", "F4", "P3", "P4"], sfreq=sfreq, ch_types="eeg")
    raw = mne.io.RawArray(signals, info, verbose=False)
    raw.set_montage("standard_1020")
    return raw


def load_sample_eeg() -> mne.io.BaseRaw:
    """Download the official MNE sample dataset on demand and return its EEG channels."""
    from pathlib import Path

    root = Path(mne.datasets.sample.data_path())
    path = root / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif"
    if not path.exists():
        raise FileNotFoundError(f"Expected MNE sample recording at {path}")
    return mne.io.read_raw_fif(path, preload=False, verbose=False).pick("eeg")
