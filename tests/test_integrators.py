import numpy as np

from utils.integrators import integrate


def test_rk4_exp_growth():
    t = np.linspace(0.0, 1.0, 1001)

    def drift(t, y):
        return y

    y = integrate(drift, np.array([1.0]), t, method="rk4")
    assert np.isclose(y[-1, 0], np.e, atol=1e-3)


def test_euler_maruyama_shape():
    t = np.linspace(0.0, 1.0, 101)

    def drift(t, y):
        return -0.5 * y

    def diffusion(t, y):
        return np.ones_like(y) * 0.1

    y = integrate(drift, np.array([0.0, 1.0]), t, method="euler-maruyama", diffusion=diffusion, seed=1)
    assert y.shape == (101, 2)
