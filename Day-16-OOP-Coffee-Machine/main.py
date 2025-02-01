from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    print(f"What drink would you like? {menu.get_items()}")
    action = input()
    if action == "off":
        exit()
    elif action == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(action)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)

