from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()


def move():
    tom.forward(50)


screen.listen()
screen.onkey(fun=move, key="space")


screen.exitonclick()