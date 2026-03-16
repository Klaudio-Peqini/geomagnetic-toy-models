"""Polarity diagnostics for scalar or vector dipole proxies."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import numpy as np


def polarity_from_signal(signal: Iterable[float], threshold: float = 0.0, fill_zeros: bool = True) -> np.ndarray:
    x = np.asarray(signal, dtype=float)
    pol = np.zeros_like(x, dtype=int)
    pol[x > threshold] = 1
    pol[x < -threshold] = -1
    if fill_zeros and len(pol) > 1:
        for i in range(1, len(pol)):
            if pol[i] == 0:
                pol[i] = pol[i - 1]
        if pol[0] == 0:
            nz = np.flatnonzero(pol != 0)
            if len(nz):
                pol[: nz[0]] = pol[nz[0]]
    return pol


def load_signal(path: str | Path, key: str | None = None) -> np.ndarray:
    path = Path(path)
    if path.suffix == ".npz":
        data = np.load(path)
        if key is None:
            key = list(data.keys())[0]
        return np.asarray(data[key], dtype=float)
    if path.suffix == ".npy":
        return np.asarray(np.load(path), dtype=float)
    arr = np.loadtxt(path, delimiter="," if path.suffix == ".csv" else None)
    if arr.ndim == 1:
        return arr
    return np.asarray(arr[:, -1], dtype=float)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute polarity from a signal.")
    parser.add_argument("path", help="Path to .npz, .npy, .csv, or text file.")
    parser.add_argument("--key", default=None, help="Key for .npz input.")
    parser.add_argument("--threshold", type=float, default=0.0)
    args = parser.parse_args()

    signal = load_signal(args.path, key=args.key)
    polarity = polarity_from_signal(signal, threshold=args.threshold)
    unique, counts = np.unique(polarity, return_counts=True)
    print("Counts by polarity:", dict(zip(unique.tolist(), counts.tolist())))


if __name__ == "__main__":
    main()
