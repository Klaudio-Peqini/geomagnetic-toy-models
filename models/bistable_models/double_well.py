"""Double-well bistable toy model for geomagnetic reversals."""

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


def potential(x: np.ndarray, a: float = 1.0, b: float = 1.0) -> np.ndarray:
    return -(a / 2.0) * x**2 + (b / 4.0) * x**4


def drift(_: float, x: np.ndarray, a: float = 1.0, b: float = 1.0) -> np.ndarray:
    return a * x - b * x**3


def diffusion(_: float, x: np.ndarray, sigma: float = 0.5) -> np.ndarray:
    return np.full_like(x, sigma, dtype=float)


def diffusion_derivative(_: float, x: np.ndarray) -> np.ndarray:
    return np.zeros_like(x, dtype=float)


def simulate_double_well(
    tmax: float = 200.0,
    dt: float = 0.01,
    x0: float = 0.2,
    a: float = 1.0,
    b: float = 1.0,
    sigma: float = 0.5,
    method: str = "euler-maruyama",
    seed: int | None = 42,
) -> tuple[np.ndarray, np.ndarray]:
    t = np.arange(0.0, tmax + dt, dt)

    def f(ti: float, yi: np.ndarray) -> np.ndarray:
        return drift(ti, yi, a=a, b=b)

    def g(ti: float, yi: np.ndarray) -> np.ndarray:
        return diffusion(ti, yi, sigma=sigma)

    y = integrate(
        f,
        np.array([x0], dtype=float),
        t,
        method=method,
        diffusion=g,
        seed=seed,
        diffusion_derivative=diffusion_derivative,
    )
    return t, y[:, 0]


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate a double-well bistable toy model.")
    parser.add_argument("--tmax", type=float, default=200.0)
    parser.add_argument("--dt", type=float, default=0.01)
    parser.add_argument("--x0", type=float, default=0.2)
    parser.add_argument("--a", type=float, default=1.0)
    parser.add_argument("--b", type=float, default=1.0)
    parser.add_argument("--sigma", type=float, default=0.5)
    parser.add_argument(
        "--method",
        choices=["euler", "rk2", "rk4", "euler-maruyama", "stochastic-heun", "milstein"],
        default="euler-maruyama",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save", default=None, help="Optional .npz output path.")
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    t, x = simulate_double_well(
        tmax=args.tmax,
        dt=args.dt,
        x0=args.x0,
        a=args.a,
        b=args.b,
        sigma=args.sigma,
        method=args.method,
        seed=args.seed,
    )

    stats = summary_statistics(x, dt=args.dt, persistence=10)
    for k, v in stats.items():
        print(f"{k}: {v}")

    if args.save:
        np.savez(args.save, t=t, x=x, params=vars(args))

    if not args.no_plot:
        xx = np.linspace(-2.0, 2.0, 400)
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        axes[0].plot(t, x, lw=0.8)
        axes[0].set_title(f"Double-well trajectory ({args.method})")
        axes[0].set_xlabel("time")
        axes[0].set_ylabel("x(t)")

        axes[1].plot(xx, potential(xx, a=args.a, b=args.b))
        axes[1].set_title("Effective potential")
        axes[1].set_xlabel("x")
        axes[1].set_ylabel("U(x)")
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
