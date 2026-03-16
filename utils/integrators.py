"""Shared deterministic and stochastic integrators for toy geomagnetic models."""

from __future__ import annotations

from typing import Callable, Optional

import numpy as np

Array = np.ndarray
DriftFunc = Callable[[float, Array], Array]
DiffusionFunc = Callable[[float, Array], Array]
DiffusionDerivativeFunc = Callable[[float, Array], Array]


DETERMINISTIC_METHODS = {"euler", "rk2", "rk4"}
STOCHASTIC_METHODS = {"euler-maruyama", "stochastic-heun", "milstein"}
ALL_METHODS = DETERMINISTIC_METHODS | STOCHASTIC_METHODS


def _asarray_state(y: Array | float) -> Array:
    arr = np.asarray(y, dtype=float)
    return arr.copy()


def _rng(seed: Optional[int]) -> np.random.Generator:
    return np.random.default_rng(seed)


def euler_step(f: DriftFunc, t: float, y: Array, dt: float) -> Array:
    return y + dt * f(t, y)


def rk2_step(f: DriftFunc, t: float, y: Array, dt: float) -> Array:
    k1 = f(t, y)
    k2 = f(t + 0.5 * dt, y + 0.5 * dt * k1)
    return y + dt * k2


def rk4_step(f: DriftFunc, t: float, y: Array, dt: float) -> Array:
    k1 = f(t, y)
    k2 = f(t + 0.5 * dt, y + 0.5 * dt * k1)
    k3 = f(t + 0.5 * dt, y + 0.5 * dt * k2)
    k4 = f(t + dt, y + dt * k3)
    return y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def euler_maruyama_step(
    drift: DriftFunc,
    diffusion: DiffusionFunc,
    t: float,
    y: Array,
    dt: float,
    dW: Array,
) -> Array:
    return y + drift(t, y) * dt + diffusion(t, y) * dW


def stochastic_heun_step(
    drift: DriftFunc,
    diffusion: DiffusionFunc,
    t: float,
    y: Array,
    dt: float,
    dW: Array,
) -> Array:
    g = diffusion(t, y)
    predictor = y + drift(t, y) * dt + g * dW
    return y + 0.5 * (drift(t, y) + drift(t + dt, predictor)) * dt + g * dW


def milstein_step(
    drift: DriftFunc,
    diffusion: DiffusionFunc,
    diffusion_derivative: DiffusionDerivativeFunc,
    t: float,
    y: Array,
    dt: float,
    dW: Array,
) -> Array:
    g = diffusion(t, y)
    gp = diffusion_derivative(t, y)
    return y + drift(t, y) * dt + g * dW + 0.5 * g * gp * (dW**2 - dt)


def integrate_ode(
    f: DriftFunc,
    y0: Array | float,
    t: Array,
    method: str = "rk4",
) -> Array:
    method = method.lower()
    if method not in DETERMINISTIC_METHODS:
        raise ValueError(f"Unsupported ODE method '{method}'. Choose from {sorted(DETERMINISTIC_METHODS)}.")

    y0 = _asarray_state(y0)
    y = np.zeros((len(t),) + y0.shape, dtype=float)
    y[0] = y0

    stepper = {"euler": euler_step, "rk2": rk2_step, "rk4": rk4_step}[method]
    for i in range(len(t) - 1):
        dt = float(t[i + 1] - t[i])
        y[i + 1] = stepper(f, float(t[i]), y[i], dt)

    return y


def integrate_sde(
    drift: DriftFunc,
    diffusion: DiffusionFunc,
    y0: Array | float,
    t: Array,
    method: str = "euler-maruyama",
    seed: Optional[int] = None,
    diffusion_derivative: Optional[DiffusionDerivativeFunc] = None,
) -> Array:
    method = method.lower()
    if method not in STOCHASTIC_METHODS:
        raise ValueError(f"Unsupported SDE method '{method}'. Choose from {sorted(STOCHASTIC_METHODS)}.")

    y0 = _asarray_state(y0)
    y = np.zeros((len(t),) + y0.shape, dtype=float)
    y[0] = y0
    rng = _rng(seed)

    for i in range(len(t) - 1):
        dt = float(t[i + 1] - t[i])
        dW = np.sqrt(dt) * rng.standard_normal(size=y0.shape)
        if method == "euler-maruyama":
            y[i + 1] = euler_maruyama_step(drift, diffusion, float(t[i]), y[i], dt, dW)
        elif method == "stochastic-heun":
            y[i + 1] = stochastic_heun_step(drift, diffusion, float(t[i]), y[i], dt, dW)
        elif method == "milstein":
            if diffusion_derivative is None:
                raise ValueError("Milstein requires diffusion_derivative.")
            y[i + 1] = milstein_step(
                drift, diffusion, diffusion_derivative, float(t[i]), y[i], dt, dW
            )

    return y


def integrate(
    drift: DriftFunc,
    y0: Array | float,
    t: Array,
    method: str = "rk4",
    diffusion: Optional[DiffusionFunc] = None,
    seed: Optional[int] = None,
    diffusion_derivative: Optional[DiffusionDerivativeFunc] = None,
) -> Array:
    """Unified wrapper for deterministic and stochastic integration."""
    method = method.lower()
    if method in DETERMINISTIC_METHODS:
        return integrate_ode(drift, y0, t, method=method)
    if method in STOCHASTIC_METHODS:
        if diffusion is None:
            raise ValueError(f"Method '{method}' requires a diffusion function.")
        return integrate_sde(
            drift,
            diffusion,
            y0,
            t,
            method=method,
            seed=seed,
            diffusion_derivative=diffusion_derivative,
        )
    raise ValueError(f"Unknown integration method '{method}'. Choose from {sorted(ALL_METHODS)}.")
