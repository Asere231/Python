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

switch = True
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
money = 0


def update_resources(rep):
    if rep == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18

    if rep == "latte":
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150

    if rep == "cappuccino":
        resources["water"] -= 250
        resources["coffee"] -= 24
        resources["milk"] -= 100


while switch:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    cost = 0

    if prompt == "off":
        switch = False
    elif prompt == "report":
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f"Money: {money}")
    else:
        if prompt == "espresso":
            if resources["water"] < 50:
                print("Sorry, there is not enough water.")
                continue
            elif resources["coffee"] < 18:
                print("Sorry, there is not enough coffee.")
                continue

        if prompt == "latte":
            if resources["water"] < 200:
                print("Sorry, there is not enough water.")
                continue
            elif resources["coffee"] < 24:
                print("Sorry, there is not enough coffee.")
                continue
            elif resources["milk"] < 150:
                print("Sorry, there is not enough milk.")
                continue

        if prompt == "cappuccino":
            if resources["water"] < 250:
                print("Sorry, there is not enough water.")
                continue
            elif resources["coffee"] < 24:
                print("Sorry, there is not enough coffee.")
                continue
            elif resources["milk"] < 100:
                print("Sorry, there is not enough milk.")
                continue

        print("Please insert coins.")
        count_quarters = int(input("How many quarters? "))
        count_dimes = int(input("How many dimes? "))
        count_nickles = int(input("How many nickles? "))
        count_pennies = int(input("How many pennies? "))
        coins = (
                quarters * count_quarters
                + dimes * count_dimes
                + nickles * count_nickles
                + pennies * count_pennies
        )

        if prompt in MENU:
            cost = MENU[prompt]["cost"]
            money = round(money + cost, 2)

        if coins < cost:
            print("Sorry, that's not enough money. Money refunded!")
            money = 0
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is your ${change} in change.")
            print(f"Here is your {prompt}. Enjoy!")
        else:
            money = round(money + cost, 2)
            print(f"Here is your {prompt}. Enjoy!")

        update_resources(prompt)
