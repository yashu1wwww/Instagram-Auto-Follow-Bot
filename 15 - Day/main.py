MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#######################################################################
#
#######################################################################

#   Variables => money, money types
money_in_machine = 0

penny = 0.01
nickle = 0.05
dime = 0.1
quarter = 0.25


def user_money(menu):
    global money_in_machine
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))

    total = (q * quarter) + (d * dime) + (n * nickle) + (p * penny)

    if total >= menu[user]["cost"]:
        # check resource
        if resources["water"] >= menu[user]["ingredients"]["water"]:
            if resources["coffee"] >= menu[user]["ingredients"]["coffee"]:
                if "milk" in menu[user]["ingredients"]:
                    if resources["milk"] >= menu[user]["ingredients"]["milk"]:

                    else:
                        print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")

        # user money change return and add money in machine
        change = round(total - menu[user]["cost"], 2)
        money_in_machine += menu[user]["cost"]

        # resource management
        resources["water"] -= menu[user]["ingredients"]["water"]
        resources["coffee"] -= menu[user]["ingredients"]["coffee"]
        if "milk" in menu[user]["ingredients"]:
            resources["milk"] -= menu[user]["ingredients"]["milk"]

        print(f"Here is ${change} in change")
        print(f"Here is your {user} ☕. Enjoy")
    else:
        print("Sorry that's not enough money. Money refunded.")

    return total


while True:
    user = input("What would you like? (espresso/latte/cappuccino): ")

    #   Display machine resources and money
    if user == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_in_machine}")

    #   Espresso Coffee
    elif user == "espresso":
        user_money(MENU)
    #   latte
    elif user == "latte":
        user_money(MENU)
    #   cappuccino
    elif user == "cappuccino":
        user_money(MENU)



























































