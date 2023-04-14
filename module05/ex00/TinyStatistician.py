import numpy as np


class TinyStatistician():

    def guard(funct):
        def inner(*args) -> None:
            if not isinstance(args[0], list or np.array):
                return None
            if len(args[0]) == 0:
                return None
            return funct(*args)
        return (inner)

    @staticmethod
    @guard
    def mean(x: list) -> float:
        return sum(x) / len(x)

    @staticmethod
    @guard
    def median(x):
        x = sorted(x)
        return (x[int((len(x) - 1) / 2)])

    @staticmethod
    @guard
    def percentile(x, percentile):
        m = len(x)
        i = int((percentile / 100) * m)
        x = sorted(x)
        res = x[i]
        if m % 2 == 0:
            res += x[i - 1]
            res /= 2
        return float(res)

    @staticmethod
    @guard
    def quartile(x):
        return ([TinyStatistician().percentile(x, 25), TinyStatistician().percentile(x, 75)])

    @staticmethod
    @guard
    def var(x):
        m = len(x)
        v = 0
        me = TinyStatistician().mean(x)
        for i in x:
            v += ((i-me) ** 2)
        return (v / (m-1))

    @staticmethod
    @guard
    def std(x):
        return (TinyStatistician().var(x) ** 1/2)


if (__name__ == "__main__"):
    a = [1, 42, 300, 10, 59]
    print(TinyStatistician().mean(a))
    print(TinyStatistician().median(a))
    print(TinyStatistician().quartile(a))
    print(TinyStatistician().percentile(a, 10))
    print(TinyStatistician().percentile(a, 15))
    print(TinyStatistician().percentile(a, 20))
    print(TinyStatistician().var(a))
    print(TinyStatistician().std(a))
