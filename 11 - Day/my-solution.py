import random

from art import logo


print(logo)

####################################################
#       GAME LOGIC START FROM HERE 👇
####################################################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


####################################################
#       USER
####################################################
user_card_list = []
user_card_score = 0

# 2 random cards
for i in range(0, 2):
    user_card_list.append(random.choice(cards))

# total sum of user cards
for i in user_card_list:
    user_card_score += i

# UI
print(f"Your cards: {user_card_list}, current score: {user_card_score}")


####################################################
#       COMPUTER
####################################################
computer_card_list = []
computer_card_score = 0

for i in range(0, 2):
    computer_card_list.append((random.choice(cards)))

# UI
print(f"Computer's first card: {computer_card_list[0]}")


####################################################
#       COMPARE
####################################################
if user_card_score < 21:
    new_card = input("Type 'y' to get another card, type 'n' to pass:")

    if new_card == 'y':
        user_card_list.append(random.choice(cards))
    else:
        pass
