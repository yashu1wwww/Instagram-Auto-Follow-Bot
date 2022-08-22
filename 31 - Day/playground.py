import random
import pandas


data = pandas.read_csv("data.csv")

a = data.to_dict(orient="records")

print(a)

b = a[0]

print(b)

a.remove(b)
a.remove(a[1])


print()

print(a)

new_data = pandas.DataFrame(a)

new_data.to_csv("new_csv.csv")
