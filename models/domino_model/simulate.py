"""Simulation script for a domino-style interacting-angle geomagnetic toy model."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from models.domino_model.parameters import DominoParams
from utils.integrators import integrate


def build_adjacency(n: int, topology: str = "nearest") -> np.ndarray:
    A = np.zeros((n, n), dtype=float)
    if topology == "nearest":
        for i in range(n):
            A[i, (i - 1) % n] = 1.0
            A[i, (i + 1) % n] = 1.0
    elif topology == "all-to-all":
        A[:] = 1.0
        np.fill_diagonal(A, 0.0)
        A /= max(n - 1, 1)
    else:
        raise ValueError("topology must be 'nearest' or 'all-to-all'")
    return A


def domino_drift_factory(params: DominoParams):
    A = build_adjacency(params.n_elements, params.topology)

    def drift(_: float, y: np.ndarray) -> np.ndarray:
        n = params.n_elements
        theta = y[:n]
        omega = y[n:]
        coupling_term = np.array([
            np.sum(A[i] * np.sin(theta - theta[i])) for i in range(n)
        ])
        dtheta = omega
        domega = (
            -params.gamma * omega
            - params.alpha * np.sin(2.0 * theta)
            + params.coupling * coupling_term
        )
        return np.concatenate([dtheta, domega])

    return drift


def domino_diffusion_factory(params: DominoParams):
    def diffusion(_: float, y: np.ndarray) -> np.ndarray:
        n = params.n_elements
        out = np.zeros_like(y)
        out[n:] = params.sigma
        return out

    return diffusion


def domino_diffusion_derivative(_: float, y: np.ndarray) -> np.ndarray:
    return np.zeros_like(y)


def observables(solution: np.ndarray, n_elements: int) -> dict:
    theta = solution[:, :n_elements]
    omega = solution[:, n_elements:]
    dipole = np.mean(np.cos(theta), axis=1)
    order = np.abs(np.mean(np.exp(1j * theta), axis=1))
    mean_omega = np.mean(omega, axis=1)
    return {"theta": theta, "omega": omega, "dipole": dipole, "order": order, "mean_omega": mean_omega}


def simulate_domino(params: DominoParams, theta0: np.ndarray | None = None, omega0: np.ndarray | None = None):
    t = params.time()
    n = params.n_elements
    rng = np.random.default_rng(params.seed)
    if theta0 is None:
        theta0 = rng.uniform(-0.2, 0.2, size=n)
    if omega0 is None:
        omega0 = np.zeros(n, dtype=float)

    y0 = np.concatenate([theta0, omega0])
    sol = integrate(
        domino_drift_factory(params),
        y0,
        t,
        method=params.method,
        diffusion=domino_diffusion_factory(params),
        seed=params.seed,
        diffusion_derivative=domino_diffusion_derivative,
    )
    obs = observables(sol, n)
    obs["t"] = t
    return obs


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate the domino geomagnetic toy model.")
    parser.add_argument("--n-elements", type=int, default=16)
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--gamma", type=float, default=0.25)
    parser.add_argument("--coupling", type=float, default=1.5)
    parser.add_argument("--sigma", type=float, default=0.35)
    parser.add_argument("--dt", type=float, default=0.01)
    parser.add_argument("--tmax", type=float, default=200.0)
    parser.add_argument("--topology", choices=["nearest", "all-to-all"], default="nearest")
    parser.add_argument(
        "--method",
        choices=["euler", "rk2", "rk4", "euler-maruyama", "stochastic-heun", "milstein"],
        default="euler-maruyama",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save", default=None)
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    params = DominoParams(
        n_elements=args.n_elements,
        alpha=args.alpha,
        gamma=args.gamma,
        coupling=args.coupling,
        sigma=args.sigma,
        dt=args.dt,
        tmax=args.tmax,
        topology=args.topology,
        method=args.method,
        seed=args.seed,
    )
    obs = simulate_domino(params)

    if args.save:
        np.savez(args.save, **obs, params=params.to_dict())

    print("Dipole mean:", float(np.mean(obs["dipole"])))
    print("Order mean:", float(np.mean(obs["order"])))

    if not args.no_plot:
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        axes[0].plot(obs["t"], obs["dipole"], lw=0.8)
        axes[0].set_title(f"Domino-model dipole proxy ({args.method})")
        axes[0].set_xlabel("time")
        axes[0].set_ylabel("M(t)")

        axes[1].plot(obs["t"], obs["order"], lw=0.8)
        axes[1].set_title("Kuramoto-style order parameter")
        axes[1].set_xlabel("time")
        axes[1].set_ylabel("R(t)")
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
