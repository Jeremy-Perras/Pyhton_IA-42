import numpy as np


def add_intercept(x):
    if (not isinstance(x, np.ndarray)):
        return None
    if (np.any(x) is False):
        return (None)
    res = np.c_[x, np.ones(np.shape(x)[0])]
    return (res)


if (__name__ == "__main__"):
    x = np.arange(1, 6)
    x = add_intercept(x)
    print(x)

    # y = np.arange(1, 10).reshape((3, 3))
    y = "s"
    print(y)
    y = add_intercept(y)
    print(y)
