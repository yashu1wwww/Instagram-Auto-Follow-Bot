from turtle import Turtle

RIGHT_STARTING = [(350, 40), (350, 20), (350, 0), (350, -20)]


class Peddle(Turtle):
    def __init__(self):
        super().__init__()
        self.right_peddles = []
        # self.create_peddle()

        self.shape("square")
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.goto(x=350, y=0)
        self.penup()
        self.color("white")
