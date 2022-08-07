from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander"])

table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)

"""

from turtle import Turtle, Screen


timmy = Turtle()

print(timmy)

timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

myscreen = Screen()

print(myscreen.canvheight)

myscreen.exitonclick()


import prettytable

"""