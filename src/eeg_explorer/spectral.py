"""Power spectral density helpers."""

import mne


def compute_psd(raw: mne.io.BaseRaw, fmin: float = 1.0, fmax: float = 40.0):
    """Compute Welch PSD, excluding channels marked bad."""
    nyquist = raw.info["sfreq"] / 2
    if not 0 <= fmin < fmax <= nyquist:
        raise ValueError(f"Require 0 <= fmin < fmax <= Nyquist ({nyquist:g} Hz)")
    return raw.compute_psd(method="welch", fmin=fmin, fmax=fmax,
                           picks="eeg", exclude="bads", verbose=False)
