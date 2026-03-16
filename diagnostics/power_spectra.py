"""Power spectral diagnostics for scalar time series."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.signal import welch

from diagnostics.polarity import load_signal


def power_spectrum_fft(signal: Iterable[float], dt: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(signal, dtype=float)
    x = x - np.mean(x)
    freqs = np.fft.rfftfreq(len(x), d=dt)
    power = np.abs(np.fft.rfft(x)) ** 2 / max(len(x), 1)
    return freqs[1:], power[1:]


def power_spectrum_welch(
    signal: Iterable[float],
    dt: float = 1.0,
    nperseg: int | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(signal, dtype=float)
    fs = 1.0 / dt
    freqs, power = welch(x, fs=fs, nperseg=nperseg)
    return freqs[1:], power[1:]


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a power spectrum.")
    parser.add_argument("path")
    parser.add_argument("--key", default=None)
    parser.add_argument("--dt", type=float, default=1.0)
    parser.add_argument("--method", choices=["fft", "welch"], default="welch")
    parser.add_argument("--nperseg", type=int, default=None)
    args = parser.parse_args()

    signal = load_signal(args.path, key=args.key)
    if args.method == "fft":
        freqs, power = power_spectrum_fft(signal, dt=args.dt)
    else:
        freqs, power = power_spectrum_welch(signal, dt=args.dt, nperseg=args.nperseg)

    print("Computed spectrum with", len(freqs), "frequency bins.")
    print("Peak frequency:", float(freqs[np.argmax(power)]))


if __name__ == "__main__":
    main()
