import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
carmanager = CarManager()


# LISTEN
screen.listen()
screen.onkeypress(fun=player.go_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_car()

    # detect when turtle collision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # detect reached goal
    # if player.ycor() > 300:
    #     player.got_to_start()
    if player.is_at_finish_line():
        player.got_to_start()
        carmanager.level_up()



screen.exitonclick()