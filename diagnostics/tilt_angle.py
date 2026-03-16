"""Tilt-angle diagnostics from vector dipole components."""

from __future__ import annotations

import argparse
from typing import Iterable

import numpy as np


def tilt_angle(mx: Iterable[float], my: Iterable[float], mz: Iterable[float], degrees: bool = True) -> np.ndarray:
    mx = np.asarray(mx, dtype=float)
    my = np.asarray(my, dtype=float)
    mz = np.asarray(mz, dtype=float)
    horizontal = np.sqrt(mx**2 + my**2)
    angle = np.arctan2(horizontal, mz)
    return np.degrees(angle) if degrees else angle


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute tilt angle from dipole components.")
    parser.add_argument("path", help="CSV or TXT file with columns mx,my,mz")
    parser.add_argument("--delimiter", default=",")
    args = parser.parse_args()

    arr = np.loadtxt(args.path, delimiter=args.delimiter)
    if arr.ndim != 2 or arr.shape[1] < 3:
        raise SystemExit("Input must have at least three columns: mx,my,mz")
    ang = tilt_angle(arr[:, 0], arr[:, 1], arr[:, 2])
    print("Mean tilt angle:", float(np.mean(ang)))
    print("Std tilt angle:", float(np.std(ang)))


if __name__ == "__main__":
    main()
