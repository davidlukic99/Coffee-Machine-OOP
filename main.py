from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()  # object
coffee_maker = CoffeeMaker()

# TODO 1. Print Report
# coffee_maker.report()
# money_machine.report()

is_on = True
menu = Menu()
# TODO 2. Check if resource efficient
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # TODO 1. REPORT DONE
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):   # RESOURCES
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
