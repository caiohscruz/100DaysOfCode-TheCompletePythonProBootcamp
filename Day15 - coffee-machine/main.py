from functions import is_menu_option, print_report, process_order

is_on = True

while is_on:
    entry = input("What would you like? (espresso/latte/cappuccino): ")
    if entry == "off":
        is_on = False
    elif entry == 'report':
        print_report()
    elif is_menu_option(entry):
        process_order(entry)
    else:
        print('Invalid option')
