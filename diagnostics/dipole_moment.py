"""Dipole-moment-like observables from vector or scalar data."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import numpy as np


def dipole_moment_from_components(mx: Iterable[float], my: Iterable[float], mz: Iterable[float]) -> np.ndarray:
    mx = np.asarray(mx, dtype=float)
    my = np.asarray(my, dtype=float)
    mz = np.asarray(mz, dtype=float)
    return np.sqrt(mx**2 + my**2 + mz**2)


def axial_dipole_from_angles(theta: Iterable[float]) -> np.ndarray:
    theta = np.asarray(theta, dtype=float)
    return np.cos(theta)


def global_axial_dipole(theta_matrix: np.ndarray) -> np.ndarray:
    arr = np.asarray(theta_matrix, dtype=float)
    return np.mean(np.cos(arr), axis=1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a dipole-moment-like observable.")
    parser.add_argument("path", nargs="?")
    parser.add_argument("--mode", choices=["angles"], default="angles")
    parser.add_argument("--key", default="theta")
    args = parser.parse_args()

    if args.path is None:
        raise SystemExit("Please provide a .npz file containing angles.")
    data = np.load(Path(args.path))
    theta = data[args.key]
    dipole = global_axial_dipole(theta)
    print("Dipole mean:", float(np.mean(dipole)))
    print("Dipole std:", float(np.std(dipole)))


if __name__ == "__main__":
    main()
