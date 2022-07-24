import random

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

rps = [rock, paper, scissors]

# user choose
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# computer generating random
computer_generate = random.randint(0, 2)

print(rps[choose])
print("Computer choose")
print(rps[computer_generate])


if choose > 2:
    print("Invalid Input")
elif choose == computer_generate:
    print("It's DRAW")
# 0 => Rock and 2 => scissors
elif choose == 0 and computer_generate == 2:
    print("You Win! 🥳")
# 1 => paper and 2 => rock
elif choose == 1 and computer_generate == 0:
    print("You Win! 🥳")
# 2 => scissors and 1 => paper
elif choose == 2 and computer_generate == 1:
    print("You Win!")
else:
    print("You Lose")


#       Using of Function

def data(status):
    print(rps[choose])
    print("Computer choose")
    print(rps[computer_generate])
    print(status)


if choose > 2:
    print("Invalid Input")
elif choose == computer_generate:
    data("It's DRAW")
elif choose == 0 and computer_generate == 2:
    data("You Win! 🥳")
elif choose == 1 and computer_generate == 0:
    data("You Win! 🥳")
elif choose == 2 and computer_generate == 1:
    data("You Win!")
else:
    data("You Lose")
