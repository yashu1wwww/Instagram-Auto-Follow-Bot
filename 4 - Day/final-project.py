rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

game = [rock, paper, scissors]

rand_num = random.randint(0, 2)

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# UI
print(game[user])
print("Computer Choose")
print(game[rand_num])

if user == 0 and rand_num == 2:
    # rock win against scissors
    print('You Win')
elif user == 1 and rand_num == 0:
    # paper win against rock
    print('You Win')
elif user == 2 and rand_num == 1:
    # scissors win against paper
    print('You Win')
elif user == 2 and rand_num == 1:
    # scissors win against paper
    print('You Win')
elif user == rand_num:
    print("DRAW")
else:
    print("You Lose")
