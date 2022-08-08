from turtle import Turtle, Screen
from random import choice

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tom = Turtle()
screen = Screen()
y = -300
screen.colormode(255)
tom.speed(0)
tom.penup()
tom.hideturtle()

for _ in range(10):
    tom.goto(-370, y)
    for _ in range(10):
        tom.penup()
        tom.dot(20, choice(color_list))
        tom.forward(50)
    y += 50








screen.exitonclick()


"""

        GENERATE COLOR FROM IMAGE
        



import colorgram

colors = colorgram.extract('image.jpg', 30)

color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    color_list.append(rgb)


print(color_list)

"""