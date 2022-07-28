from art import logo


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for ope in operations:
        print(ope)

    flag = True

    while flag:
        operation_symbol = input("Pick an operation?: ")
        num2 = float(input("What's the second number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating with {answer}, or type 'n' to exit.:") == "y":
            num1 = answer
        else:
            flag = False
            calculator()

calculator()


















# calculator_start = True
#
# result = 0
#
# while calculator_start:
#
#     def calculator():
#         global result
#         n1 = float(input("What's the first number?: "))
#         operator = input("+\n-\n*\n/\nPick an operation?:")
#         n2 = float(input("What's the next number?: "))
#
#         if operator == '+':
#             result = add(n1, n2)
#         elif operator == '-':
#             result = sub(n1, n2)
#         elif operator == '*':
#             result = mul(n1, n2)
#         elif operator == '/':
#             result = div(n1, n2)
#
#     calculator()
#
#     print(result)
#
#     con = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
#
#     if con == 'y':
#         calculator()
