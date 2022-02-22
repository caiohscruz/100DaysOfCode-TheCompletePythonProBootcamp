from data import MENU, resources, coins_value

profit = 0


def is_menu_option(entry):
    if entry in MENU:
        return True
    else:
        return False


def has_resources_available(drink_ingredients):
    result = True
    for key, value in drink_ingredients.items():
        if value > resources[key]:
            print(f'Sorry there is not enough {key}.')
            result = False
    return result


def process_coins():
    total = 0
    for key, value in coins_value.items():
        coins = int(input(f'Put the {key}: '))
        total += coins * value
    return total


def payment_enough(cash, cost):
    if cash < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif cash >= cost:
        global profit
        profit += cost
        if cash > cost:
            change = cash - cost
            print(f"Here is ${change:.2f} dollars in change.")
    return True


def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${profit:.2f}')


def serve(drink_ingredients):
    for key, value in drink_ingredients.items():
        resources[key] -= value


def process_order(entry):
    drink_ingredients = MENU[entry]['ingredients']
    drink_cost = MENU[entry]['cost']
    if has_resources_available(drink_ingredients):
        print(f'The {entry} costs ${drink_cost}')
        cash = process_coins()
        if payment_enough(cash, drink_cost):
            serve(drink_ingredients)
            print(f'Here is you {entry}. Enjoy')
