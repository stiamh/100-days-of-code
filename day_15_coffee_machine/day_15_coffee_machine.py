from coffee_data import MENU, resources

def is_resource_sufficient(order_ingredients):
    """Compares the amount of ingredients required to make the drink vs how many ingredients the machine has
    and returns true if there is sufficient ingredients."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not {item} to create your drink.")
            return False
    return True 

def process_coins():
    """Returns the total amount of money inputted into the machine."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost ):
    """Compares the amount money received to the price of the drink and returns true if it is accepted"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Insufficient funds. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Your {drink_name} is ready, enjoy!")
profit = 0
turned_on = True
while True:
    coffee_choice = input("What would you like to order? (Espresso/Latte/Cappuccino):\n").lower()
    if coffee_choice not in MENU:
        print("Your entry is invalid. Please try again.")
    elif coffee_choice == "off":
        print("Coffee machine shutting down...")
        turned_on = False
    elif coffee_choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else: 
        drink = MENU[coffee_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_choice, drink["ingredients"])