print("Hello welcome to the simple calculator app in python!")
list = ['+', '-', '*', '/']


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


endcalc = False


while endcalc is False:
    n1 = int(input("What's the first number?: "))
    for ops in list:
        print(ops)
    operation = input("Pick an operation: ")
    n2 = int(input("What's the second number?: "))
    if operation == "+":
        result = add(n1, n2)
        print(result)
        cont = input("Do you wish to perform another operation? [y/n]: ")
        if cont == 'n':
            endcalc = True
    elif operation == "-":
        result = subtract(n1, n2)
        print(result)
        if cont == 'n':
            endcalc = True
    elif operation == "*":
        result = multiply(n1, n2)
        print(result)
        if cont == 'n':
            endcalc = True
    elif operation == "/":
        result = divide(n1, n2)
        print(result)
        if cont == 'n':
            endcalc = True
