from turtle import Turtle, Screen
from random import choice

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tom = Turtle()
screen = Screen()

x = 3
for _ in range(7):
    tom.color(choice(colours))
    for _ in range(x):
        tom.forward(100)
        tom.left(360 / x)
    x += 1


screen.exitonclick()
