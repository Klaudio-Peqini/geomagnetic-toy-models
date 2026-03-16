"""Kuramoto-like phase oscillator model for geomagnetic toy dynamics."""

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
from utils.integrators import integrate


def kuramoto_drift_factory(
    omega0: np.ndarray,
    coupling: float,
) :
    n = len(omega0)

    def drift(_: float, theta: np.ndarray) -> np.ndarray:
        phase_diff = theta[None, :] - theta[:, None]
        coupling_term = np.sum(np.sin(phase_diff), axis=1) / n
        return omega0 + coupling * coupling_term

    return drift


def kuramoto_diffusion_factory(sigma: float):
    def diffusion(_: float, theta: np.ndarray) -> np.ndarray:
        return np.full_like(theta, sigma, dtype=float)

    return diffusion


def diffusion_derivative(_: float, theta: np.ndarray) -> np.ndarray:
    return np.zeros_like(theta)


def simulate_kuramoto(
    n_osc: int = 32,
    tmax: float = 200.0,
    dt: float = 0.02,
    coupling: float = 1.0,
    sigma: float = 0.15,
    freq_std: float = 0.5,
    method: str = "euler-maruyama",
    seed: int = 42,
):
    rng = np.random.default_rng(seed)
    t = np.arange(0.0, tmax + dt, dt)
    omega0 = rng.normal(loc=0.0, scale=freq_std, size=n_osc)
    theta_init = rng.uniform(-np.pi, np.pi, size=n_osc)

    sol = integrate(
        kuramoto_drift_factory(omega0, coupling),
        theta_init,
        t,
        method=method,
        diffusion=kuramoto_diffusion_factory(sigma),
        seed=seed,
        diffusion_derivative=diffusion_derivative,
    )

    order_complex = np.mean(np.exp(1j * sol), axis=1)
    order = np.abs(order_complex)
    dipole_proxy = np.mean(np.cos(sol), axis=1)
    return {
        "t": t,
        "theta": sol,
        "order": order,
        "phase": np.angle(order_complex),
        "dipole_proxy": dipole_proxy,
        "omega0": omega0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate a Kuramoto-like phase oscillator model.")
    parser.add_argument("--n-osc", type=int, default=32)
    parser.add_argument("--tmax", type=float, default=200.0)
    parser.add_argument("--dt", type=float, default=0.02)
    parser.add_argument("--coupling", type=float, default=1.0)
    parser.add_argument("--sigma", type=float, default=0.15)
    parser.add_argument("--freq-std", type=float, default=0.5)
    parser.add_argument(
        "--method",
        choices=["euler", "rk2", "rk4", "euler-maruyama", "stochastic-heun", "milstein"],
        default="euler-maruyama",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save", default=None)
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    out = simulate_kuramoto(
        n_osc=args.n_osc,
        tmax=args.tmax,
        dt=args.dt,
        coupling=args.coupling,
        sigma=args.sigma,
        freq_std=args.freq_std,
        method=args.method,
        seed=args.seed,
    )

    stats = summary_statistics(out["dipole_proxy"], dt=args.dt, persistence=10)
    for k, v in stats.items():
        print(f"{k}: {v}")

    if args.save:
        np.savez(args.save, **out, params=vars(args))

    if not args.no_plot:
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        axes[0].plot(out["t"], out["order"], lw=0.8)
        axes[0].set_title("Synchronization order parameter")
        axes[0].set_xlabel("time")
        axes[0].set_ylabel("R(t)")

        axes[1].plot(out["t"], out["dipole_proxy"], lw=0.8)
        axes[1].set_title("Dipole-like proxy")
        axes[1].set_xlabel("time")
        axes[1].set_ylabel("M(t)")
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
