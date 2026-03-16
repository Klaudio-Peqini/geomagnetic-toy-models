"""Reduced-observable utilities for toy-model/data comparison."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from diagnostics.power_spectra import power_spectrum_welch
from diagnostics.reversal_statistics import summary_statistics


def zscore(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    std = np.std(x)
    return (x - np.mean(x)) / std if std > 0 else x - np.mean(x)


def moving_average(x: np.ndarray, window: int = 10) -> np.ndarray:
    if window <= 1:
        return np.asarray(x, dtype=float)
    kernel = np.ones(window, dtype=float) / window
    return np.convolve(np.asarray(x, dtype=float), kernel, mode="same")


def compare_signals(x: np.ndarray, y: np.ndarray) -> dict:
    xz = zscore(x)
    yz = zscore(y)
    corr = float(np.corrcoef(xz, yz)[0, 1])
    return {
        "correlation": corr,
        "x_stats": summary_statistics(xz, dt=1.0, persistence=3),
        "y_stats": summary_statistics(yz, dt=1.0, persistence=3),
    }


def load_series(path: str | Path, column: str | None = None) -> np.ndarray:
    path = Path(path)
    if path.suffix in {".csv", ".txt"}:
        df = pd.read_csv(path)
        if column is None:
            column = df.columns[-1]
        return df[column].to_numpy(dtype=float)
    if path.suffix in {".npy"}:
        return np.load(path)
    if path.suffix in {".npz"}:
        data = np.load(path)
        if column is None:
            column = list(data.keys())[0]
        return data[column]
    raise ValueError(f"Unsupported format for {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute reduced observables and compare two series.")
    parser.add_argument("--input-a", default=None)
    parser.add_argument("--input-b", default=None)
    parser.add_argument("--column-a", default=None)
    parser.add_argument("--column-b", default=None)
    parser.add_argument("--smooth", type=int, default=1)
    parser.add_argument("--save", default=None)
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    if args.input_a and args.input_b:
        x = load_series(args.input_a, column=args.column_a)
        y = load_series(args.input_b, column=args.column_b)
    else:
        t = np.linspace(0, 200, 10000)
        rng = np.random.default_rng(42)
        x = np.sin(0.10 * t) + 0.35 * np.sin(0.03 * t + 0.4) + 0.20 * rng.standard_normal(len(t))
        y = 0.9 * np.sin(0.10 * t + 0.5) + 0.25 * np.sin(0.027 * t + 0.8) + 0.20 * rng.standard_normal(len(t))

    x = moving_average(x, window=args.smooth)
    y = moving_average(y, window=args.smooth)
    comp = compare_signals(x, y)

    for k, v in comp.items():
        print(k, ":", v)

    if args.save:
        np.savez(args.save, x=x, y=y, comparison=comp)

    if not args.no_plot:
        f1, p1 = power_spectrum_welch(zscore(x))
        f2, p2 = power_spectrum_welch(zscore(y))
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        axes[0].plot(zscore(x), label="signal A", alpha=0.8)
        axes[0].plot(zscore(y), label="signal B", alpha=0.8)
        axes[0].set_title("Normalized reduced observables")
        axes[0].legend()

        axes[1].loglog(f1, p1, label="signal A")
        axes[1].loglog(f2, p2, label="signal B")
        axes[1].set_title("Spectral comparison")
        axes[1].set_xlabel("frequency")
        axes[1].set_ylabel("power")
        axes[1].legend()
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
