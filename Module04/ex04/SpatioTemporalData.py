import pandas as pd
from link import FileLoader


class SpatioTemporalData():
    data: pd.DataFrame

    def __init__(self, dataset: pd.DataFrame) -> None:
        self.data = dataset

    def when(self, location):
        dt = self.data[self.data["City"] == location]
        lst = dt["Year"].drop_duplicates().to_list()
        return (lst)

    def where(self, year):
        dt = self.data[self.data["Year"] == year]
        lst = dt["City"].drop_duplicates().to_list()
        return (lst)


if (__name__ == "__main__"):

    data = FileLoader().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module04/athlete_events.csv")
    sp = SpatioTemporalData(data)
    print(sp.when("Paris"))
    print(sp.where(1924))
