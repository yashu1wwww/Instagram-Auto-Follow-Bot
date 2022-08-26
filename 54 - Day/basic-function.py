def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


#   pass function as arguments
def calculate(cal_fun, n1, n2):
    return cal_fun(n1, n2)


result = calculate(add, 5, 10)
print(result)


#   nested function
def outer_fun():
    print("Outer Function")

    def inner_fun():
        print("Inner Function")

    inner_fun()


outer_fun()


#   return nested function
def outer_fun_1():
    print("Outer Function")

    def inner_fun_1():
        print("Inner Function")

    # return inner_fun_1()
    return inner_fun_1


print()
print()

x = outer_fun_1()
x()




























