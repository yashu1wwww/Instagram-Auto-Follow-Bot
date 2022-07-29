import random
from art import logo


computer_num = random.randint(1, 100)
easy = 10
hard = 5
game_start = True

# testing
print(computer_num)

# WELCOME message
print(logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ")


def masala(level):
    global game_start
    while game_start:
        print(f"You have {level} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == computer_num:
            print(f"You got it! The answer was {computer_num}")
            game_start = False
        elif guess < computer_num:
            print("Too low")
        elif guess > computer_num:
            print("Too high")

        if level == 1:
            game_start = False
            print("You've run out of guesses, you lose.")

        level -= 1


# EASY LEVEL
if choose_level == "easy":
    masala(easy)
#   HARD LEVEL
elif choose_level == "hard":
    masala(hard)
