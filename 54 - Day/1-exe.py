import time

current_time = time.time()


def speed_calc_decorator(function):
    def wrapper_function():
        x = time.time()
        function()
        y = time.time() - x
        print(y)
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
