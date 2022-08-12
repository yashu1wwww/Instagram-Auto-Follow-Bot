from turtle import Turtle, Screen
from peddle import Peddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


peddle = Turtle()
peddle.shape("square")
peddle.shapesize(stretch_wid=5, stretch_len=1)
peddle.goto(x=350, y=0)
peddle.penup()
peddle.color("white")


def go_up():
    new_y = peddle.ycor() + 20
    peddle.goto(x=peddle.xcor(), y=new_y)


def go_down():
    new_y = peddle.ycor() - 20
    peddle.goto(x=peddle.xcor(), y=new_y)


#  scree listen
screen.listen()
screen.onkey(fun=go_up, key="Up")
screen.onkey(fun=go_down, key="Down")


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
