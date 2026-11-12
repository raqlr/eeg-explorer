import numpy as np
import pytest
from eeg_explorer.data import make_demo_raw
from eeg_explorer.spectral import compute_psd


def test_psd_finds_10hz_peak():
    raw = make_demo_raw(duration=20)
    psd = compute_psd(raw, 1, 40)
    frequencies = psd.freqs
    peak = frequencies[np.argmax(psd.get_data()[0])]
    assert abs(peak - 10) < 1


def test_invalid_frequency_range():
    with pytest.raises(ValueError):
        compute_psd(make_demo_raw(), 1, 150)
