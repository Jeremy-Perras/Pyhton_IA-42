from matplotlib import pyplot as plt
from link import FileLoader
import pandas as pd
# TODO


class Komparator():
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        data = self.data[[categorical_var, numerical_var]].dropna()
        features = data[categorical_var].unique()

        fig, axes = plt.subplots(ncols=len(features))
        for i, feat in enumerate(features):
            axes[i].set_title(feat)
            axes[i].boxplot(data[data[categorical_var] == feat]
                            [numerical_var])
        plt.show()


if (__name__ == "__main__"):

    data = FileLoader().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module04/athlete_events.csv")
    kompar = Komparator(data)
    kompar.compare_box_plots("Sex", "Height")
