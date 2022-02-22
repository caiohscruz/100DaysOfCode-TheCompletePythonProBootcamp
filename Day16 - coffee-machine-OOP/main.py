from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from moneymachine import MoneyMachine

is_on = True

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

while is_on:
    entry = input(f"What would you like? ({menu.get_items()}): ")
    if entry == 'off':
        is_on = False
    elif entry == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    elif menu.find_drink(entry) is not None:
        drink = menu.find_drink(entry)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)

