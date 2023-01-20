import pandas

contents = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_primary = contents["Primary Fur Color"]
grey_squirrel_count = len(contents[data_primary == "Gray"])
red_squirrel_count = len(contents[data_primary == "Cinnamon"])
black_squirrel_count = len(contents[data_primary == "Black"])

dic = {
    "Fur color": ["grey", "red", "black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count],
}

df = pandas.DataFrame(dic)
df.to_csv("squirrel_count.csv")

