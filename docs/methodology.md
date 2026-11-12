# Methodology (starter)

- **Synthetic demonstration:** four sinusoidal signals (6, 10, 12, 18 Hz) with seeded Gaussian noise. These are not biological EEG recordings.
- **MNE Sample:** optional public audiovisual EEG/MEG example; only EEG channels are selected.
- **Band-pass:** optional 1–40 Hz MNE FIR filter, with a copy of the input.
- **Spectrum:** Welch PSD, mean across EEG channels, reported in dB relative to 1 V²/Hz.
- **Limits:** No artifact rejection, referencing comparison, ERP, source localization, statistical inference, or clinical validation in this starter release.

Future iterations will document reference choices, bad-channel handling, events, epochs, ERP, and topomaps.
