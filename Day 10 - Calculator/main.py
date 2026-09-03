from os import WCONTINUED

from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

# my_favourite_operation = add

# print(my_favourite_operation(2, 3))
# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as values. Keys = '+', '-', '*', '/'

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }

# TODO: use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
number_1 = None
while True:
    if number_1 is None:
        number_1 = float(input("What's the first number?:  "))
    for symbol in operations:
        print(symbol)
    op = input("Pick an operation:  ")
    number_2 = float(input("What's the next number?:  "))
    result = operations[op](number_1, number_2)
    print(f"{number_1} {op} {number_2} = {operations[op](number_1, number_2)}")

    choice = input(f"Type 'y' to continue calculating with {result}, "
                      f"or type 'n' to start a new calculation:  ").lower()

    if choice == "y":
        number_1 = result
    else:
        print("\n"*100)
        number_1 = None
        #note: you can also use recursion here
