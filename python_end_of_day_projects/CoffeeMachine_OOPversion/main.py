from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

switch = True
menu = Menu()
making_coffee = CoffeeMaker()
money = MoneyMachine()

while switch:

    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    menu_items = 0

    if prompt == "off":
        switch = False
    elif prompt == "report":
        print(f"These are the available drinks {menu.get_items()}")
        making_coffee.report()
        money.report()
    else:
        if prompt == "espresso":
            menu_items = menu.menu[1]
            if not making_coffee.is_resource_sufficient(menu_items):
                continue
        if prompt == "latte":
            menu_items = menu.menu[0]
            if not making_coffee.is_resource_sufficient(menu_items):
                continue
        if prompt == "cappuccino":
            menu_items = menu.menu[2]
            if not making_coffee.is_resource_sufficient(menu_items):
                continue

        if not money.make_payment(menu_items.cost):
            continue

        making_coffee.make_coffee(menu_items)




