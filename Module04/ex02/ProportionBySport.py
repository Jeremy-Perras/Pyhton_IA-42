from link import FileLoader
import pandas as pd


def proportion_by_sport(dataset: pd.DataFrame, year, sport, gender):
    sl_y = dataset[dataset["Year"] == year]
    sl_g = sl_y[sl_y["Sex"] == gender]
    sl_s = sl_g[sl_g["Sport"] == sport]
    return (sl_s.shape[0]/sl_g.shape[0])


if (__name__ == "__main__"):
    data = FileLoader().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module04/athlete_events.csv")
    print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
