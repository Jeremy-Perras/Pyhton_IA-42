from link import FileLoader
import pandas as pd


def youngest_fellah(dataset: pd.DataFrame, year):
    dic = {"F": None, "M": None}
    dt = dataset[dataset["Year"] == year].sort_values(by=["Age"])
    if (len(dt)):
        first = dt.iloc[0]
        second = dt.loc[lambda x: x["Sex"] != first["Sex"]].iloc[0]
        if (first["Sex"] == "F"):
            dic["F"] = first["Age"]
        if (first["Sex"] == "M"):
            dic["M"] = first["Age"]
        if (second["Sex"] == "F"):
            dic["F"] = second["Age"]
        if (second["Sex"] == "M"):
            dic["M"] = second["Age"]
        dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        return (dic)
    return


if (__name__ == "__main__"):
    data = FileLoader().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module04/athlete_events.csv")
    youngest_fellah(data, 1998)
