
"""
        DEFAULT ARGUMENTS

"""

def fun(a=11, b=12, c=13):
    print(a, b, c)


fun(1, 2, 3)

fun(1, 2)

fun()


"""
        *args ARGUMENTS ( Many positional arguments )

"""

# 1 - EXAMPLE
def first(*numbers):
    print(numbers)
    print(numbers[2])
    print(type(numbers))
    for number in numbers:
        print(number)


first(1, 2, 3, 4, 5)


print()
print()


# 2 - EXAMPLE
def add(*args):
    total = 0
    for i in args:
        total += i

    print(total)


add(1, 2, 3, 4, 5)


# 3 - EXAMPLE
def second(*args):
    for i in args:
        print(i * 2)


second(1, 2, 3, 4, 5)


"""
        **kwargs : ( KeyWord Arguments )
"""


def first(x, **kwargs):
    print(kwargs)
    print(type(kwargs))
    print()

    for key, value in kwargs.items():
        print(key, " = ", value)

    print()
    print(kwargs["a"])
    print(kwargs["c"])

    print()
    x += kwargs["a"]
    x *= kwargs["b"]
    print(x)


first(5, a=1, b=2, c=3)

print()
print()


#   BEST EXAMPLE
class Car:
    def __init__(self, **kwargs):
        # # if user will not provide argument then it will generate error
        # self.make = kwargs["make"]
        # self.speed = kwargs["speed"]

        # skip error
        self.make = kwargs.get("make")
        self.speed = kwargs.get("speed")
        self.color = kwargs.get("color")
        self.model = kwargs.get("model")


car = Car(make="BMW", speed=90)

print(car.make)
print(car.speed)


car_1 = Car(make="Audi")
print(car_1.make)
