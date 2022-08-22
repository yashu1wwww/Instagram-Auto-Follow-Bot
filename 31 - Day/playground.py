import random
import pandas


data = pandas.read_csv("data/french_words.csv")

print(data)


a = data["French"].tolist()

print(random.choice(a))
