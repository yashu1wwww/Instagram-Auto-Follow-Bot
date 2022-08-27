def logging_decorator(function):
    def wrapper(*args):
        print(function.__name__)
        return function(args[0], args[1], args[2])
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a + b + c


# a_function(1, 2, 3)
print(a_function(1, 2, 3))
