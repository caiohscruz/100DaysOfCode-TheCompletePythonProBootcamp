from functions import is_order_valid, has_resources_available

should_continue_operating = True

while should_continue_operating:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if not is_order_valid(order):
        print("Sorry. We don't have that.")
        continue
    else:
        if not has_resources_available(order):
            print("err")
