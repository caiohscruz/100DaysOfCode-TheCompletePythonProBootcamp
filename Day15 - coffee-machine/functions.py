from data import MENU, resources


def is_order_valid(order):
    if order in MENU:
        return True
    else:
        return False


def has_resources_available(order):
    result = True
    if MENU[order]["ingredients"]["water"] > resources["water"]:
        print('Sorry there is not enough water.')
        result = False
    if MENU[order]["ingredients"]["milk"] > resources["milk"]:
        print('Sorry there is not enough milk.')
        result = False
    if MENU[order]["ingredients"]["coffee"] > resources["coffee"]:
        print('Sorry there is not enough coffee.')
        result = False
    return result

