from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()


for _ in range(20):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()


screen.exitonclick()
