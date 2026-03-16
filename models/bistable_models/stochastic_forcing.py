"""Noise-scan experiments for the double-well model."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from diagnostics.reversal_statistics import summary_statistics
from models.bistable_models.double_well import simulate_double_well


def run_noise_scan(
    sigmas: np.ndarray,
    n_realizations: int = 10,
    tmax: float = 150.0,
    dt: float = 0.01,
    method: str = "euler-maruyama",
    seed: int = 42,
) -> dict:
    mean_reversals, std_reversals = [], []
    mean_waiting = []

    for sigma in sigmas:
        counts, waits = [], []
        for i in range(n_realizations):
            _, x = simulate_double_well(
                tmax=tmax,
                dt=dt,
                sigma=float(sigma),
                method=method,
                seed=seed + i,
            )
            stats = summary_statistics(x, dt=dt, persistence=10)
            counts.append(stats["n_reversals"])
            if not np.isnan(stats["mean_waiting_time"]):
                waits.append(stats["mean_waiting_time"])

        mean_reversals.append(np.mean(counts))
        std_reversals.append(np.std(counts))
        mean_waiting.append(np.mean(waits) if waits else np.nan)

    return {
        "sigmas": np.asarray(sigmas),
        "mean_reversals": np.asarray(mean_reversals),
        "std_reversals": np.asarray(std_reversals),
        "mean_waiting_time": np.asarray(mean_waiting),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a noise-amplitude scan for the double-well model.")
    parser.add_argument("--sigma-min", type=float, default=0.1)
    parser.add_argument("--sigma-max", type=float, default=1.0)
    parser.add_argument("--n-sigmas", type=int, default=10)
    parser.add_argument("--n-realizations", type=int, default=10)
    parser.add_argument("--tmax", type=float, default=150.0)
    parser.add_argument("--dt", type=float, default=0.01)
    parser.add_argument(
        "--method",
        choices=["euler-maruyama", "stochastic-heun", "milstein"],
        default="euler-maruyama",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save", default=None)
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    sigmas = np.linspace(args.sigma_min, args.sigma_max, args.n_sigmas)
    results = run_noise_scan(
        sigmas=sigmas,
        n_realizations=args.n_realizations,
        tmax=args.tmax,
        dt=args.dt,
        method=args.method,
        seed=args.seed,
    )

    if args.save:
        np.savez(args.save, **results)

    if not args.no_plot:
        fig, axes = plt.subplots(2, 1, figsize=(9, 8))
        axes[0].errorbar(
            results["sigmas"],
            results["mean_reversals"],
            yerr=results["std_reversals"],
            marker="o",
            capsize=3,
        )
        axes[0].set_title("Reversal count versus noise amplitude")
        axes[0].set_xlabel("sigma")
        axes[0].set_ylabel("mean reversals")

        axes[1].plot(results["sigmas"], results["mean_waiting_time"], marker="o")
        axes[1].set_title("Mean waiting time versus noise amplitude")
        axes[1].set_xlabel("sigma")
        axes[1].set_ylabel("mean waiting time")
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
