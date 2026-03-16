"""Analysis script for saved domino-model simulations."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from diagnostics.power_spectra import power_spectrum_welch
from diagnostics.reversal_statistics import summary_statistics


def load_domino_npz(path: str | Path) -> dict:
    data = np.load(path, allow_pickle=True)
    return {k: data[k] for k in data.files}


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a saved domino-model .npz file.")
    parser.add_argument("path")
    parser.add_argument("--dt", type=float, default=None)
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    data = load_domino_npz(args.path)
    t = data["t"]
    dipole = data["dipole"]
    order = data["order"]
    dt = float(np.mean(np.diff(t))) if args.dt is None else args.dt

    stats = summary_statistics(dipole, dt=dt, persistence=10)
    for k, v in stats.items():
        print(f"{k}: {v}")

    freqs, power = power_spectrum_welch(dipole, dt=dt)

    if not args.no_plot:
        fig, axes = plt.subplots(3, 1, figsize=(10, 10))
        axes[0].plot(t, dipole, lw=0.8)
        axes[0].set_title("Dipole proxy")
        axes[0].set_xlabel("time")
        axes[0].set_ylabel("M(t)")

        axes[1].plot(t, order, lw=0.8)
        axes[1].set_title("Order parameter")
        axes[1].set_xlabel("time")
        axes[1].set_ylabel("R(t)")

        axes[2].loglog(freqs, power)
        axes[2].set_title("Power spectrum of dipole proxy")
        axes[2].set_xlabel("frequency")
        axes[2].set_ylabel("power")

        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
