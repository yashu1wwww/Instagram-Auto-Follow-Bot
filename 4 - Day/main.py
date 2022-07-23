# import my_module
# print(my_module.fullName)

import random

"""



rand_integer = random.randint(1, 5)
print(rand_integer)

rand_float = random.random() * 5
print(rand_float)

love_score = random.randint(1, 100)
print(f"You'r love score : {love_score}")

"""

states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina",
 "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
 "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
 "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
 "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
 "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states[0])
print(states[-1])

states[0] = "Delhi"
print(states[0])


print()
print()

# other example

list = ["Sohan", "Dohan", True, 42, 84.246]

print(list)

print(list[0])
print(list[1])
print(list[-1])

# add item at last of list
list.append("Hello")

# add new list to existing list
list.extend(['A', 'B'])

# insert item at a given position
list.insert(1, "Arunesh")

# remove item
list.remove("Hello")

print(list)

print(len(list))

a = "Hello Arunesh, How Are you?"
print(a.split(' '))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [a, b]
print(c)

aa = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(aa)


























