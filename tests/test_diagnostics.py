import numpy as np

from diagnostics.polarity import polarity_from_signal
from diagnostics.reversal_statistics import reversal_indices


def test_polarity_basic():
    x = np.array([-2.0, -1.0, 0.2, 1.0])
    p = polarity_from_signal(x, threshold=0.0)
    assert np.array_equal(p, np.array([-1, -1, 1, 1]))


def test_reversal_indices():
    x = np.array([-1, -0.5, 0.1, 0.5, -0.2, -1.0, 1.0, 1.1])
    idx = reversal_indices(x, persistence=1)
    assert len(idx) >= 2
