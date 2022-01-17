from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
menu_item = MenuItem

turned_on = True
while True:
    options = menu.get_items()
    coffee_choice = input(f"What would you like to order? ({options}):\n").lower()
    if coffee_choice == "off":
        print("Coffee machine shutting down...")
        turned_on = False
    elif coffee_choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)