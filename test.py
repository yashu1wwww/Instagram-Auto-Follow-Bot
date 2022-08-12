from turtle import Turtle

COORDINATES = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 12
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.parts = []
        self.make_snake()
        self.head = self.parts[0]
        self.head_mod()

    def make_snake(self):
        for pos in COORDINATES:
            self.add_part(pos)

    def add_part(self, pos):
        part = Turtle("square")
        part.penup()
        part.color("orange")
        part.shapesize(0.5, 0.5)
        part.goto(pos)
        self.parts.append(part)

    def extend(self):
        self.add_part(self.parts[-1].position())

    def head_mod(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.6, 0.8)

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            po_x = self.parts[i - 1].xcor()
            po_y = self.parts[i - 1].ycor()
            self.parts[i].goto(po_x, po_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)