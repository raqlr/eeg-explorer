import pytest
from eeg_explorer.data import make_demo_raw
from eeg_explorer.preprocessing import bandpass


def test_bandpass_does_not_modify_input():
    raw = make_demo_raw()
    before = raw.get_data().copy()
    result = bandpass(raw, 1, 40)
    assert result is not raw
    assert (raw.get_data() == before).all()
    assert result.get_data().shape == before.shape


def test_invalid_cutoffs():
    with pytest.raises(ValueError):
        bandpass(make_demo_raw(), 40, 1)
