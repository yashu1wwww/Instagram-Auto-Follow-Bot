from turtle import Turtle, Screen
from random import choice
import random


tom = Turtle()
screen = Screen()
tom.pensize(10)
tom.speed(0)
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


directions = [0, 90, 180, 270]


for _ in range(100):
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(choice(directions))


screen.exitonclick()
