import numpy as np


def predict_(x, theta):
    if (not isinstance(theta, np.ndarray) or not isinstance(x, np.ndarray)) or np.any(x) is False or np.any(theta) is False:
        return None
    if theta.shape not in [(2,), (2, 1)] or x.shape not in [(x.size,), (x.size, 1)]:
        return None
    res = np.empty(shape=(1, x.size))
    return theta[0] + theta[1] * x


x = np.arange(1, 6)
print(np.shape(x))
theta1 = np.array([[5], [0]])
print(predict_(x, theta1))
theta2 = np.array([[0], [1]])
print(predict_(x, theta2))
