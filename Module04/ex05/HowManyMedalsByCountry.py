import pandas as pd
from link import FileLoader


def how_many_medals_by_country(dataset: pd.DataFrame, name):
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
    dataset = dataset[dataset["Team"] == name]
    dataset = dataset.loc[:, ['Team', 'Games',
                              'Year', 'Sport', 'Event', 'Medal']]
    multiple = dataset[dataset['Sport'].isin(team_sports)].drop_duplicates()
    solo = dataset[dataset['Sport'].isin(team_sports)]
    dataset = pd.concat([multiple, solo]).loc[:, ['Year', 'Medal']]
    dt = dataset.groupby(['Year'])['Medal'].apply(list).to_dict()
    for year in dt.keys():
        dt[year] = {
            'G': dt[year].count('Gold'),
            'S': dt[year].count('Silver'),
            'B': dt[year].count('Bronze')
        }
    return (dt)


if (__name__ == "__main__"):
    data = FileLoader().load(
        "/Users/jeremyperras/Desktop/Pyhton_IA-42/Module04/athlete_events.csv")
    print(how_many_medals_by_country(data, "France"))
