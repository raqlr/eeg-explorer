"""EEG filtering helpers."""

import mne


def bandpass(raw: mne.io.BaseRaw, low: float = 1.0, high: float = 40.0) -> mne.io.BaseRaw:
    """Return a filtered copy; never mutate the input recording."""
    nyquist = raw.info["sfreq"] / 2
    if not 0 < low < high < nyquist:
        raise ValueError(f"Require 0 < low < high < Nyquist ({nyquist:g} Hz)")
    result = raw.copy().load_data()
    result.filter(l_freq=low, h_freq=high, picks="eeg", verbose=False)
    return result
