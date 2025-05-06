from OOP_Coffee_Machine import menu
from OOP_Coffee_Machine import coffee_maker
from OOP_Coffee_Machine import money_machine

menu = menu.Menu()
maker = coffee_maker.CoffeeMaker()
money = money_machine.MoneyMachine()

def valid_order(order):
    if order == 'latte' or order == 'espresso' or order == 'cappuccino'\
        or order == 'report' or order == 'off':
        return True
    return False

off = False
while not off:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if valid_order(order) and order != 'off' and order != 'report':
        is_order = menu.find_drink(order)
    else:
        print("Invalid input")
        continue
    if order == 'report':
        maker.report()
        money.report()
    elif order == 'off':
        off = True
        print("GoodBye")
    else:
        if (maker.is_resource_sufficient(is_order)) and money.make_payment(is_order.cost):
            maker.make_coffee(is_order)