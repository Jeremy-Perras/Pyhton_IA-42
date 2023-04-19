from mse import loss_
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt


def check(y, y_hat):
    if (not all([isinstance(obj, np.ndarray) for obj in [y, y_hat]
                 or y.size == 0 or y.shape != y_hat.shape])):
        return False
    return (True)


def mse_(y, y_hat):
    return (2 * loss_(y, y_hat))


def rmse_(y, y_hat):
    return (sqrt((2 * loss_(y, y_hat))))


def mae_(y, y_hat):
    if (check(y, y_hat)):
        return (np.sum(abs(y - y_hat)) / y.size)
    return None


def r2score_(y, y_hat):
    if (check(y, y_hat)):
        return (1-(np.sum([i * j for i, j in zip(y_hat - y, y_hat - y)]) /
                np.sum([i * j for i, j in zip(y - (np.sum(y) / y.size), y - (np.sum(y) / y.size))])))
    return None


# Example 1:
x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])

print(mse_(x, y))
# Output:
4.285714285714286

print(mean_squared_error(x, y))
# Output:
4.285714285714286

print(rmse_(x, y))
# Output:
2.0701966780270626

print(sqrt(mean_squared_error(x, y)))
# Output:
2.0701966780270626

print(mae_(x, y))
# Output:
1.7142857142857142

print(mean_absolute_error(x, y))
# Output:
1.7142857142857142

print(r2score_(x, y))
# Output:
0.9681721733858745

print(r2_score(x, y))
# Output:
0.968172173385874
