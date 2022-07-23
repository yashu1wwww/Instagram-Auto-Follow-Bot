# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

import random

rand_num = random.randint(0, len(names) - 1)
print(f"{names[rand_num]} going to buy meal today")

rand_choice = random.choice(names)
print(f"{rand_choice} is going to buy meal today")

