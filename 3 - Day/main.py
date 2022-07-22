print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# simple if else statement
if height >= 100:
    print('You can ride rollercoster')
else:
    print("Sorry, You can't ride rollercoster")

# nested if else statement
if height >= 100:
    bill = 0
    age = int(input("Enter age? \n"))
    if age < 12:
        bill = 5
        print("Please, Pay $5")
    elif age <= 18:
        bill = 7
        print("Please, Pay $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You don't need to pay any amount for ticket")
    else:
        bill = 12
        print("You have to pay $12")

    photo = input("Do you want take photo ? \n")
    if photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, You can't ride rollercoster")
