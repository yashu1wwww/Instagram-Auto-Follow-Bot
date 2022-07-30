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

money_in_machine = 0
penny = 0.01
nickle = 0.05
dime = 0.1
quarter = 0.25
machine_status = True


def management(menu, total):
    global money_in_machine
    # user money change return and add money in machine
    change = round(total - menu[user]["cost"], 2)
    money_in_machine += menu[user]["cost"]

    resources["water"] -= menu[user]["ingredients"]["water"]
    resources["coffee"] -= menu[user]["ingredients"]["coffee"]
    if "milk" in menu[user]["ingredients"]:
        resources["milk"] -= menu[user]["ingredients"]["milk"]

    print(f"Here is ${change} in change")
    print(f"Here is your {user} ☕. Enjoy")


def coffee_management(menu):
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))
    total = (q * quarter) + (d * dime) + (n * nickle) + (p * penny)

    #   compare price
    if total >= menu[user]["cost"]:
        #   check resource
        if resources["water"] >= menu[user]["ingredients"]["water"]:
            if resources["coffee"] >= menu[user]["ingredients"]["coffee"]:
                #   check milk in ingredients
                if "milk" in menu[user]["ingredients"]:
                    if resources["milk"] >= menu[user]["ingredients"]["milk"]:
                        management(menu, total)
                    else:
                        print("Sorry there is not enough coffee.")
                else:
                    management(menu, total)
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    else:
        print("Sorry that's not enough money. Money refunded.")

    return total


while machine_status:
    user = input("What would you like? (espresso/latte/cappuccino): ")

    if user == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_in_machine}")
    elif user == "off":
        machine_status = False
    elif user == "espresso":
        coffee_management(MENU)
    elif user == "latte":
        coffee_management(MENU)
    elif user == "cappuccino":
        coffee_management(MENU)

    #   THIS IS ALSO WORKING FINE
    # else:
    #     coffee_management(MENU)
