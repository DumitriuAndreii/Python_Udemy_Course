from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffer_maker = CoffeeMaker()
is_on = True
menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink?? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffer_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffer_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffer_maker.make_coffee(drink)