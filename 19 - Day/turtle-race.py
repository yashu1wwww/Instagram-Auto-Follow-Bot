from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

pos = -100
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
turtle_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
race_is_on = False

for i in range(6):
    tom = Turtle(shape="turtle")
    tom.color(colors[i])
    tom.penup()
    tom.goto(x=-230, y=turtle_position[i])
    all_turtle.append(tom)
    # pos += 50


if user_bet in colors:
    race_is_on = True


while race_is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_is_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lose! The {winner} turtle is the winner!")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
