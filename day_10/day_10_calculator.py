from os import system, name
import art 

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }
def clear():
    if name == "nt":
        _ = system("cls") #For windows users
    else:
        _ = system("clear")#For mac users
def calculator():
    num1 = float(input("Please input a number: \n"))
    for symbol in operations:
        print(symbol, "", end = '')
    go_again = True
    while go_again:
        operation = input("\nPlease select an operation to apply to your numbers. \n")
        function = operations[operation]
        num2 = float(input("Please select another number: \n"))
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        check = input(f"Type 'yes' to continue calculating with {answer}, or type 'no' to start again: \n").lower()
        if check == "yes":
            num1 = answer
        else:
            go_again = False
            clear()
            calculator()

calculator()