# EEG Explorer

An educational, reproducible EEG exploration starter built with **Python**, **MNE-Python** and **Streamlit**.
Designed as a neuroscience/neurotechnology portfolio project. **Not for clinical diagnosis.**

## What works in v0.1

- Synthetic four-channel EEG-like signals, generated locally with a fixed seed (no download).
- Optional official MNE Sample audiovisual dataset, with EEG channels selected.
- EEG channel/time-series visualization.
- Optional 1–40 Hz band-pass filtering.
- Welch power spectral density (PSD) visualization.
- Unit tests for synthetic data, filtering and spectral analysis.

**Not yet implemented:** ERP, topographic power maps, artifact rejection, file upload, export and scientific validation. These are planned milestones, not existing features.

## Setup

Requires **Python 3.11+**. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
streamlit run app/streamlit_app.py
```

Choose **Synthetic demo (offline)** to run without downloading data. To use the MNE Sample dataset, select it in the sidebar and click **Load MNE Sample dataset**. This dataset can be large.

## Run tests

```bash
pytest -q
```

## Repository layout

- `app/streamlit_app.py` — minimal interactive dashboard.
- `src/eeg_explorer/data.py` — synthetic demo and MNE Sample loading.
- `src/eeg_explorer/preprocessing.py` — filtering.
- `src/eeg_explorer/spectral.py` — PSD calculation.
- `src/eeg_explorer/visualization.py` — Matplotlib plots.
- `tests/` — reproducible unit tests.
- `docs/` — methods, data provenance and limitations.

## Scientific scope

The synthetic data contain known oscillations; the PSD test checks recovery of a 10 Hz peak.
The MNE Sample recording is prefiltered and is used only as an exploratory public dataset.
For details, see [`docs/methodology.md`](docs/methodology.md), [`docs/dataset.md`](docs/dataset.md)
and [`docs/limitations.md`](docs/limitations.md).

## Roadmap

1. Inspect metadata and compare pre/post filtering.
2. Add band-power summaries and sensor topomaps.
3. Add event detection, epoching and ERP plots.
4. Add exports, richer tests, methodological report and reproducibility checks.

## Data and privacy

Downloaded recordings and exports are excluded from git. Do not commit participant data.
Use the source dataset's citation and licensing requirements when publishing derived results.

## License

MIT (see `LICENSE`). Dataset licenses are separate.
