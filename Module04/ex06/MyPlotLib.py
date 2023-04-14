from matplotlib import pyplot as plt
from link import FileLoader
import pandas as pd


class MyPlotLib():
    @staticmethod
    def histogram(data, features):
        nfeatures = len(features)
        fig, ax = plt.subplots(ncols=nfeatures)
        for i in range(nfeatures):
            ax[i].set_title(features[i])
            ax[i].hist(data[features[i]].dropna())
            ax[i].grid()
        plt.show()

    @staticmethod
    def density(data, features):
        pd.DataFrame(data[features]).plot(kind='density')
        plt.show()

    @staticmethod
    def pair_plot(data: pd.DataFrame, features: list):
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    @staticmethod
    def box_plot(data: pd.DataFrame, features: list):
        fig, ax = plt.subplots()
        ax.boxplot(data[features].dropna(), labels=features)
        plt.show()


if (__name__ == "__main__"):
    data = FileLoader().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module04/athlete_events.csv")

    MyPlotLib().pair_plot(data, ["Height", "Weight"])
