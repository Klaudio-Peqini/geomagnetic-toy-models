"""Default parameters for the domino geomagnetic toy model."""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np


@dataclass
class DominoParams:
    n_elements: int = 16
    alpha: float = 1.0
    gamma: float = 0.25
    coupling: float = 1.5
    sigma: float = 0.35
    dt: float = 0.01
    tmax: float = 200.0
    topology: str = "nearest"
    method: str = "euler-maruyama"
    seed: int = 42

    def time(self) -> np.ndarray:
        return np.arange(0.0, self.tmax + self.dt, self.dt)

    def to_dict(self) -> dict:
        return asdict(self)
