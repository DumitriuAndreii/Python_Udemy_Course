from game_data import resources
from game_data import menu


def report_resources(resources_in):
    water = resources_in['water']
    milk = resources_in['milk']
    coffee = resources_in['coffee']
    money = resources_in['money']
    return f"{water}ml of water \n{milk}ml of milk \n{coffee}g of coffee \n{money} dollars"


def machine_off():
    print("The coffee machine will turn off now")


def money_sum():
    print("Please insert your coins!")
    quarters = int(input("How many quarters do u have?")) *0.25
    dimes = int(input("How many dimes do u have?")) *0.10
    nickles = int(input("How many nickles do u have?"))*0.05
    pennies = int(input("How many pennies do u have?"))*0.01
    money = quarters + dimes+ nickles + pennies
    return money


def money_check(money_in_machine, order):
    price = menu[order]['cost']
    if money_in_machine >= price:
        money_out = round(money_in_machine - price,2)
        print(f"your rest is {money_out}")
        return 1
    else:
        return 0


def check_resources(order):
    if resources['water'] >= menu[order]['ingredients']['water'] and resources['coffee'] >= menu[order]['ingredients']['coffee'] and resources['milk'] >= menu[order]['ingredients']['milk']:
        return 1
    else:
        return 0


def update_resources(order):
    resources['water'] -= menu[order]['ingredients']['water']
    resources['coffee'] -= menu[order]['ingredients']['coffee']
    resources['milk'] -= menu[order]['ingredients']['milk']
    resources['money'] += menu[order]['cost']


machine_on = 1
while machine_on:
    order = input("what would you like? (espresso/latte/cappuccino)  ")
    if order == 'report':
        print(report_resources(resources))
    elif order == 'off':
        machine_off()
        machine_on = 0
        break
    elif order not in menu:
        print("take care to your typo")
        continue
    else:
        availability = check_resources(order)
        if availability == 1:
            money_in = money_sum()
            check_money = money_check(money_in, order)
            if check_money == 1:
                update_resources(order)
                print("your coffee will be ready in a minute")
            else:
                print("Sorry, you do not have enough money")
        else:
            print("There are not enough resources to prepare your drink")