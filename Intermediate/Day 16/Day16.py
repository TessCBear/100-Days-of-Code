from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# First create all required objects using the the classes
menu_object = Menu()
coffee_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()


# Prompt the user for their drink
machine_on = True
while machine_on:
    drink_options = menu_object.get_items()
    drink = input("What would you like to drink? {drink_options} ")
    if drink == "off":
        machine_on = False
    elif drink == "report":
        coffee_maker_object.report()
        money_machine_object.report()
    else:
        chosen_drink = menu_object.find_drink(drink)
        
        # Check resources sufficient to make drink
        if coffee_maker_object.is_resource_sufficient(chosen_drink):
            # Transact money
            if money_machine_object.make_payment(chosen_drink.cost):
                # Make Coffee
                coffee_maker_object.make_coffee(chosen_drink)
        
