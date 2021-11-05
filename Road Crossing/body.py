from screenSetting import HEIGHT
from turtle import Turtle

STARTING_POSITION = (0, -(HEIGHT // 2 - 20))
width = 1.5
height = 1.5
SHAPE = 'turtle'
# COLOR = 'black'
SPEED = 5


class Body(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(stretch_len=height, stretch_wid=width)

    def up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    # def down(self):
    #     new_y = self.ycor() - SPEED
    #     self.goto(self.xcor(), new_y)

    def start(self):
        self.goto(STARTING_POSITION)
