# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         print("1")
#         #   do something before
#         function()
#         #   do something after
#         print("2")
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
#
# @delay_decorator
# def say_bye():
#     print("Bye")
#
#
# def greet():
#     print("Good Morning")
#
#
# # say_hello()
# say_bye()
# # greet()











import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        print("2")
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


def greet():
    print("Good Morning")


say_hello()
# greet()
