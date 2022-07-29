from art import logo, vs
from game_data import data

import random


# GET RANDOM DATA
def get_data(items):
    return random.choice(items)


game_start = True
score = 0
a = get_data(data)
a_followers = a["follower_count"]

print(logo)

while game_start:
    b = get_data(data)

    if a == b:
        b = get_data(data)

    b_followers = b["follower_count"]

    if a_followers > b_followers:
        winner = 'a'
    else:
        winner = 'b'

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    if guess == winner:
        a = b
        b = get_data(data)
        score += 1
        print(f"You've right! Current score: {score}")
    else:
        print(f"Sorry, That's wrong. Final score: {score} ")
        game_start = False
