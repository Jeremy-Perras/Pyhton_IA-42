import pandas as pd
from link import FileLoader


def how_many_medals(dataset: pd.DataFrame, name):
    dt = dataset[dataset["Name"] == name]
    dic = dict()
    print(dt)
    for index, row in dt.iterrows():
        year = row["Year"]
        medal = row["Medal"]
        if (year not in dic.keys()):
            dic.update({year: {"G": 0, "S": 0, "B": 0}})
        if medal == "Gold":
            dic[year]["G"] += 1
        elif medal == "Silver":
            dic[year]["S"] += 1
        elif medal == "Bronze":
            dic[year]["B"] += 1
    return (dic)


if (__name__ == "__main__"):
    data = FileLoader().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module04/athlete_events.csv")
    print(how_many_medals(data, "Kjetil Andr Aamodt"))
