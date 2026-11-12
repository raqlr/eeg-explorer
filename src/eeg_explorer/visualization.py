"""Reusable plotting functions."""

import matplotlib.pyplot as plt
import numpy as np


def plot_segment(raw, start: float = 0, duration: float = 5):
    """Plot EEG channel traces in microvolts with per-channel offsets."""
    if start < 0 or duration <= 0 or start >= raw.times[-1]:
        raise ValueError("Invalid start or duration")
    stop = min(start + duration, raw.times[-1])
    data, times = raw.get_data(picks="eeg", tmin=start, tmax=stop, return_times=True)
    data_uv = data * 1e6
    spacing = max(float(np.ptp(data_uv)) * 1.2, 1.0)
    fig, ax = plt.subplots(figsize=(10, 4))
    for i, (name, trace) in enumerate(zip(raw.copy().pick("eeg").ch_names, data_uv)):
        ax.plot(times, trace + i * spacing, linewidth=0.8, label=name)
    ax.set(xlabel="Time (s)", ylabel="EEG (µV; offset per channel)", title="EEG signals")
    ax.set_yticks([i * spacing for i in range(data_uv.shape[0])], raw.copy().pick("eeg").ch_names)
    fig.tight_layout()
    return fig


def plot_mean_psd(spectrum):
    """Plot mean channel PSD in dB relative to 1 V²/Hz."""
    powers = spectrum.get_data()
    mean_power = powers.mean(axis=0)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(spectrum.freqs, 10 * np.log10(np.maximum(mean_power, np.finfo(float).tiny)))
    ax.set(xlabel="Frequency (Hz)", ylabel="Power (dB re 1 V²/Hz)", title="Mean EEG power spectral density")
    fig.tight_layout()
    return fig
