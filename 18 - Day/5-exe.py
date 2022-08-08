from turtle import Turtle, Screen
from random import randint


tom = Turtle()
screen = Screen()
screen.colormode(255)
tom.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


# # MY SOLUTION
# for _ in range(40):
#     tom.circle(100)
#     tom.left(5)
#     tom.color(random_color())


# ANGELA SOLUTION
def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tom.circle(100)
        tom.color(random_color())
        tom.setheading(tom.heading() + size)


draw_spirograph(5)


screen.exitonclick()
