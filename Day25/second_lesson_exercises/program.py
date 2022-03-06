import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

COLORS = ["Gray", "Cinnamon", "Black"]

counts = []

for color in COLORS:
    counts.append(len(data[data["Primary Fur Color"] == color]))

data_dict = {
    "Fur Color": COLORS,
    "Count": counts
}

df = pd.DataFrame(data_dict)

df.to_csv("Squirrel_count.csv")
