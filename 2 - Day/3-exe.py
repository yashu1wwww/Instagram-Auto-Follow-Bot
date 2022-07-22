# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

year = 90 - age

days = year * 365
months = year * 12
weeks = year * 52

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
