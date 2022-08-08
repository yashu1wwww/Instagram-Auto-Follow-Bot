from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

timmy.color("red")
timmy.shape("turtle")

x = 50

for _ in range(100):
    timmy.forward(x)
    timmy.right(90)
    x += 10


screen.exitonclick()