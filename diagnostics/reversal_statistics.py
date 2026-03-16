"""Reversal statistics for dipole proxy time series."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import numpy as np

from diagnostics.polarity import load_signal, polarity_from_signal


def reversal_indices(
    signal: Iterable[float],
    threshold: float = 0.0,
    persistence: int = 1,
) -> np.ndarray:
    pol = polarity_from_signal(signal, threshold=threshold, fill_zeros=True)
    idx = []
    for i in range(1, len(pol) - persistence):
        if pol[i] != pol[i - 1] and np.all(pol[i : i + persistence] == pol[i]):
            idx.append(i)
    return np.asarray(idx, dtype=int)


def waiting_times(
    signal: Iterable[float],
    dt: float = 1.0,
    threshold: float = 0.0,
    persistence: int = 1,
) -> np.ndarray:
    idx = reversal_indices(signal, threshold=threshold, persistence=persistence)
    if len(idx) < 2:
        return np.array([], dtype=float)
    return np.diff(idx) * dt


def residence_times(
    signal: Iterable[float],
    dt: float = 1.0,
    threshold: float = 0.0,
) -> np.ndarray:
    pol = polarity_from_signal(signal, threshold=threshold, fill_zeros=True)
    if len(pol) == 0:
        return np.array([], dtype=float)
    durations = []
    current = pol[0]
    count = 1
    for val in pol[1:]:
        if val == current:
            count += 1
        else:
            durations.append(count * dt)
            current = val
            count = 1
    durations.append(count * dt)
    return np.asarray(durations, dtype=float)


def summary_statistics(
    signal: Iterable[float],
    dt: float = 1.0,
    threshold: float = 0.0,
    persistence: int = 1,
) -> dict:
    idx = reversal_indices(signal, threshold=threshold, persistence=persistence)
    waits = waiting_times(signal, dt=dt, threshold=threshold, persistence=persistence)
    resid = residence_times(signal, dt=dt, threshold=threshold)
    return {
        "n_reversals": int(len(idx)),
        "mean_waiting_time": float(np.mean(waits)) if len(waits) else np.nan,
        "std_waiting_time": float(np.std(waits)) if len(waits) else np.nan,
        "mean_residence_time": float(np.mean(resid)) if len(resid) else np.nan,
        "std_residence_time": float(np.std(resid)) if len(resid) else np.nan,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute reversal statistics.")
    parser.add_argument("path")
    parser.add_argument("--key", default=None)
    parser.add_argument("--dt", type=float, default=1.0)
    parser.add_argument("--threshold", type=float, default=0.0)
    parser.add_argument("--persistence", type=int, default=1)
    args = parser.parse_args()

    signal = load_signal(args.path, key=args.key)
    stats = summary_statistics(
        signal,
        dt=args.dt,
        threshold=args.threshold,
        persistence=args.persistence,
    )
    for k, v in stats.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
