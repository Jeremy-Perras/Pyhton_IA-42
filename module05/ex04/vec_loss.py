import numpy as np


def loss_(y, y_hat):
    if (not all([isinstance(obj, np.ndarray) for obj in [y, y_hat] or y.size == 0 or y.shape != y_hat.shape])):
        return None
    return ((np.sum([i * j for (i, j) in zip(y_hat - y, y_hat - y)]) / (2 * y.size)))
