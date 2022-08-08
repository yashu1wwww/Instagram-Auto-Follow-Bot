from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()


for _ in range(4):
    tom.right(90)
    tom.forward(100)


screen.exitonclick()
