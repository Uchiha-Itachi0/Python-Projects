from turtle import Turtle

PADDLE_SHAPE = 'square'
PADDLE_COLOR = 'white'
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1


class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.shape(PADDLE_SHAPE)
        self.paddle.color(PADDLE_COLOR)
        self.paddle.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.paddle.penup()
        self.paddle.goto(position)

    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def w(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def s(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
