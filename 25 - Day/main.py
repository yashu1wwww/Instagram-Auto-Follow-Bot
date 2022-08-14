import pandas


"""

with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

"""


"""
            CSV

import csv


with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    
"""

#############################################################################
#
#                   PANDAS
#
#############################################################################

data = pandas.read_csv("weather_data.csv")

temp = data["temp"]

"""
print(data)
print()
print(temp)
print()

# datatype
print(type(data))
print(type(temp))
print()

# dict
data_dict = data.to_dict()
print(data_dict)

# list
temp_list = temp.to_list()
print(temp_list)
print()

# calculate average of temperature list

# 1 - method
total_temp = 0
for t in temp_list:
    total_temp += t

avg_temp = total_temp / len(temp_list)

print(avg_temp)


# 2 - method
a = sum(temp_list) / len(temp_list)
print(a)

# 3 - method ( using pandas )
print(temp.mean())
print()

# find max value using of pandas
print(temp.max())

# find min value using of pandas
print(temp.min())
print()


#    get data in column


print(data["condition"])
print(data.condition)



# get row data
a = data[data.day == "Monday"]
print(a)

# get row by max temp
max_temp = data["temp"].max()
b = data[data.temp == max_temp]
print(b)

# get row by min temp
min_temp = data["temp"].min()
c = data[data.temp == min_temp]
print(c)
print()

# get row ( only specifier value )
d = data[data.day == "Monday"]
e = d.condition
print(e)
print()

# convert monday's temperature to fahrenheit
# monday_temp = d.temp[0]
monday_temp = d.temp
f = (1.8 * monday_temp) + 32
print(f)





# create dataframe
data_dict = {
    "students": ["Arunesh", "Ankesh", "Sohan"],
    "scores": [43, 63, 54]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)


# save new csv file
new_data.to_csv("new_data.csv")


"""


print(data)

print()

sunny = data[data["condition"] == "Sunny"]

total_sunny = sunny.count()

a = total_sunny.condition

print(a)


















