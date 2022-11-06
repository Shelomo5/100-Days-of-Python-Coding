from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# instantiating objects from imported classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

marker_on = True

while marker_on:
    # get_items() returns names of menu items
    menu_items = menu.get_items()
    choice = input(f'What would you like? {menu_items}: \n')
    if choice == "off":
        marker_on = False
    elif choice == "report":
        # methods to print report
        money_machine.report()
        coffee_maker.report()
    else:
        # find_drink() returns a MenuItem object "drink" which has attributes name, cost, ingredients
        drink = menu.find_drink(choice)
        # class method checks if there's enough resources to make a given MenuItem object
        if coffee_maker.is_resource_sufficient(drink):
            # class method returns True when payment is accepted, or False if insufficient
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
