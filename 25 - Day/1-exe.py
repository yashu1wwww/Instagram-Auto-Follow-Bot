import pandas as pd


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = data[data["Primary Fur Color"] == "Gray"].count()
gray_total = gray["Primary Fur Color"]

black = data[data["Primary Fur Color"] == "Black"].count()
black_total = black["Primary Fur Color"]

red_total = len(data[data["Primary Fur Color"] == "Cinnamon"].count())


# create new dataframe
color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_total, red_total, black_total]
}

new_data = pd.DataFrame(color_dict)

# save new dataframe
new_data.to_csv("squirrel_count.csv")
