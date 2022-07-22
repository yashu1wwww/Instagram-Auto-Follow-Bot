# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true = t+r+u+e

l = name.count('l')
o = name.count('o')
v = name.count('v')
ee = name.count('e')
love = l+o+v+ee

love_score = int(f"{true}{love}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
