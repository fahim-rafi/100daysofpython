print("Hello welcome to the simple calculator app in python!")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

endcalc = False


while endcalc is False:
    n1 = int(input("What's the first number?: "))
    for ops in operations_dict:
        print(ops)
    operation = input("Pick an operation: ")
    n2 = int(input("What's the second number?: "))
    answer = operations_dict[operation](n1, n2)
    print(answer)
    cont = input("Do you wish to perform another operation? [y/n]: ")
    if cont == 'n':
        endcalc = True
    elif cont == "y":
        endcalc = False
    else:
        print("Please write y for yes and n for no! Breaking!")
        break
