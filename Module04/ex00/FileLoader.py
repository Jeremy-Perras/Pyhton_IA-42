import pandas as pd
from sys import stderr


class FileLoader():
    @staticmethod
    def load(path):
        data = None
        try:
            data = pd.read_csv(path)
            print(data.shape[0], data.shape[1])
            return (data)
        except Exception as error:
            print(
                f"Exception : {error.__class__.__name__} -- strerror: {error}")

    @staticmethod
    def display(df, n):
        res = df[:n]
        if (n >= 0):
            res = df[n:]
        return (res)


if (__name__ == "__main__"):
    data = FileLoader().load("/Users/jeremyperras/Desktop/Pyhton_IA-42/Module04/test.csv")
    # print(FileLoader().display(data, 1))
    print(FileLoader().display(data, -1))
