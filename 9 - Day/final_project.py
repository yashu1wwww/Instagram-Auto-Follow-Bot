from art import logo

print(logo)

bidders = {}
start = True

while start:
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    there = input("Are there any other bidders? Type 'yes' or 'no'.")
    bidders[name] = amount
    if there == "no":
        start = False

winner_name = ''
winner_amount = 0

for key in bidders:
    if winner_amount < bidders[key]:
        winner_amount = bidders[key]
        winner_name = key

print(f"The winner is {winner_name} with a bid of {winner_amount}")
