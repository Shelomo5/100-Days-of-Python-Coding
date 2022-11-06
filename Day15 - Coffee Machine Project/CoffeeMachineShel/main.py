MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}



def insert_change():
    '''prompts user to input change and sums it up'''
    print('Please insert coins.')
    quarters = float(input('how many quarters?:'))
    dimes = float(input('how many dimes?:'))
    nickles = float(input('how many nickels?:'))
    pennies = float(input('how many pennies?:'))
    total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    return total


def price_compare(money_input, order_var):
    """function calculates difference between money given by user and bought item"""
    item_cost = MENU[order_var]['cost']
    if money_input >= item_cost:
        difference = money_input - item_cost
        change = round(difference, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def resource_check(avail_resources, order_name):
    """uses for loop to compare ingredients needed to make a specific drink and the amount
    of those ingredients available"""
    for ingredient in MENU[order_name]["ingredients"]:
        if avail_resources[ingredient] < MENU[order_name]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def resource_update(order_var, profit_var, resources_var):
    '''updates resources depending on which drink is made'''
    if order_var == "espresso":
        profit_var += 1.5
        resources_var['water'] -= 50
        resources_var['coffee'] -= 18
        resources_var['coffee'] -= 0
    elif order_var == "latte":
        profit_var += 2.5
        resources_var['water'] -= 200
        resources_var['coffee'] -= 24
        resources_var['milk'] -= 150
    elif order_var == "cappuccino":
        profit_var += 3.0
        resources_var['water'] -= 250
        resources_var['coffee'] -= 24
        resources_var['milk'] -= 100
    return profit_var, resources_var


def print_report(resources_var, profit_var):
    '''function prints report'''
    print(resources_var)
    print(f"$ {profit_var}")


# recursive function to restart program
def restart_machine():
    profit = 0
    resources = {
        "water": 300,
        "milk": 300,
        "coffee": 100,
    }

    machine_on = True
    while machine_on:
        # use input to store what user wants in a variable
        order = input('What would you like? (espresso/latte/cappuccino): \n').lower()
        # 'off' turns exits machine
        if order == 'off':
            print("bye")
            machine_on = False
            continue
        # typing report calls print_report function and machine restarted
        if order == 'report':
            print_report(resources, profit)
            restart_machine()
        # if user orders a drink, function checks if resources are sufficient to make it
        if resource_check(resources, order):
            pass
        else:
            machine_on = False
            continue
        # calls function to prompt user to put in money
        money_given = insert_change()
        # calls function to compare price of order and money given by user
        if price_compare(money_given, order):
            pass
        else:
            machine_on = False
            continue

        print_report(resources, profit)
        # call function to update the resources after the transaction
        profit, resources = resource_update(order, profit, resources)
        print_report(resources, profit)
        print(f'Here is your {order}.Enjoy!')


restart_machine()

