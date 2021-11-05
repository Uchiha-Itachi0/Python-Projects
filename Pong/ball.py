from turtle import Turtle

BALL_COLOR = 'white'
BALL_HEIGHT = 0.5
BALL_WEIGHT = 0.5
BALL_SHAPE = 'circle'
SPEED = 0.1



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.shapesize(stretch_wid=BALL_WEIGHT, stretch_len=BALL_HEIGHT)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = SPEED
        self.bounce_x()
