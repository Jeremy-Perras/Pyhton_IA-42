# TODO
from other_losses import check
import numpy as np
from matplotlib import pyplot as plt


def plot_with_loss(x, y, theta):
    if (not check(x, y)):
        return None
    if (theta.shape not in [(2,), (2, 1)] or not isinstance(theta, np.ndarray)):
        return None

    def h(x): return theta[0] + theta[1] * x
    plt.plot(x, y, "o")
    plt.plot(x, h(x))
    plt.show()
