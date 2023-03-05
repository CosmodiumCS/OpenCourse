# for this module's practice:
# we will be building a aimple calclulator

# created by : C0SM0

# addition function
def addition(n1, n2):
    return n1 + n2

# subtraction function
def subtraction(n1, n2):
    return n1 - n2

# multiplication function
def multiplication(n1, n2):
    return n1 * n2

# division funciton
def division(n1, n2):
    return n1 / n2

# loop code, in case of exception
while True:
    # banner
    print("Simple Calculator")

    # option menu
    print("Choose an Operation:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n")
    # user input, operation
    operation = input("Option : ")

    # try to get numeric values
    try: 
        # user input, first number
        first_number = float(input("Enter first number : "))
        second_number = float(input("Enter second number : "))

        # addition
        if operation == "1":
            print(f"{first_number} + {second_number} = {addition(first_number, second_number)}")
            break
        # subtraction
        elif operation == "2":
            print(f"{first_number} - {second_number} = {subtraction(first_number, second_number)}")
            break
        # multiplication
        elif operation == "3":
            print(f"{first_number} × {second_number} = {multiplication(first_number, second_number)}")
            break
        # division
        elif operation == "4":
            print(f"{first_number} ÷ {second_number} = {division(first_number, second_number)}")
            break
        # exception
        else:
            print("Input was invalid, try again\n")
            continue

    # exception
    except ValueError:
        print("Enter a numeric value [1, 2.5, 7, etc.]\n")

# feel free to keep practicing, here are some more ideas
"""
- simplify this calculator using lambdas
- remove ".0" in float values for a cleaner look
    - hint: you can convert float data to string, use ".endswith"
"""