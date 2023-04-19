import numpy as np
from matplotlib import pyplot as plt


def plot(x, y, theta):
    if not all([isinstance(obj, np.ndarray) for obj in [x, y, theta]]):
        return None
    if theta.shape not in [(2,), (2, 1)] or x.shape not in [(x.size,), (x.size, 1)] or y.shape not in [(y.size,), (y.size, 1)] or y.size != x.size:
        return None

    def h(x): return theta[0] + theta[1] * x
    plt.plot(x, y, "o")
    plt.plot(x, h(x))
    plt.show()


x = np.arange(1, 6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
theta1 = np.array([[4.5], [-0.2]])
plot(x, y, theta1)
theta2 = np.array([[-1.5], [2]])
plot(x, y, theta2)
theta3 = np.array([[3], [0.3]])
plot(x, y, theta3)
