from turtle import Screen
import snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = snake.Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



























screen.exitonclick()
