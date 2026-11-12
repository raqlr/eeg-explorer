import pytest
from eeg_explorer.data import make_demo_raw


def test_demo_is_reproducible():
    a = make_demo_raw(seed=12)
    b = make_demo_raw(seed=12)
    assert a.ch_names == ["F3", "F4", "P3", "P4"]
    assert (a.get_data() == b.get_data()).all()


def test_invalid_duration():
    with pytest.raises(ValueError):
        make_demo_raw(duration=0)
