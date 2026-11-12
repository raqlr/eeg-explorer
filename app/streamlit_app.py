"""Minimal interactive EEG Explorer."""

import matplotlib.pyplot as plt
import streamlit as st

from eeg_explorer.data import load_sample_eeg, make_demo_raw
from eeg_explorer.preprocessing import bandpass
from eeg_explorer.spectral import compute_psd
from eeg_explorer.visualization import plot_mean_psd, plot_segment

st.set_page_config(page_title="EEG Explorer", page_icon="🧠", layout="wide")
st.title("EEG Explorer")
st.caption("Educational EEG analysis · MNE-Python · Not a diagnostic tool")

source = st.sidebar.selectbox("Data source", ["Synthetic demo (offline)", "MNE Sample (download)"])
try:
    if source.startswith("Synthetic"):
        raw = make_demo_raw()
        st.info("Synthetic EEG: generated signals, not human recordings.")
    else:
        st.warning("The MNE Sample dataset is large and may require a substantial download.")
        if not st.sidebar.button("Load MNE Sample dataset"):
            st.stop()
        with st.spinner("Downloading / loading MNE Sample dataset…"):
            raw = load_sample_eeg()

    st.write(f"**Channels:** {len(raw.ch_names)} | **Sampling:** {raw.info['sfreq']:.1f} Hz | **Duration:** {raw.times[-1]:.1f} s")
    max_seconds = min(10.0, float(raw.times[-1]))
    duration = st.sidebar.slider("Visible segment (s)", 1.0, max_seconds, min(5.0, max_seconds))
    start = st.sidebar.slider("Start time (s)", 0.0, max(0.0, float(raw.times[-1]) - duration), 0.0)
    enable_filter = st.sidebar.checkbox("Apply 1–40 Hz bandpass", value=False)
    if enable_filter:
        with st.spinner("Filtering…"):
            raw = bandpass(raw)

    tab1, tab2 = st.tabs(["Signals", "Spectrum"])
    with tab1:
        # Loading only the selected interval avoids pulling the entire sample into memory.
        segment = raw.copy().crop(tmin=start, tmax=start + duration).load_data()
        fig = plot_segment(segment, start=0, duration=duration)
        st.pyplot(fig)
        plt.close(fig)
    with tab2:
        # PSD uses a short segment by default, to keep the demo responsive.
        spectral_segment = raw.copy().crop(tmin=0, tmax=min(20.0, raw.times[-1])).load_data()
        spectrum = compute_psd(spectral_segment, fmin=1, fmax=min(40, raw.info["sfreq"] / 2))
        fig = plot_mean_psd(spectrum)
        st.pyplot(fig)
        plt.close(fig)
        st.caption("PSD is descriptive; no clinical or cognitive-state inference is made.")
except Exception as exc:
    st.error(f"Could not load or process the data: {exc}")
    st.info("Try the synthetic demo, or consult the README for dataset requirements.")
