from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_SHAPE = 'square'
SNAKE_COLOR = 'white'


class Snake:
    def __init__(self):
        self.body = []
        self.create_ghost_body()
        self.head = self.body[0]

    def create_ghost_body(self):

        # Making ghost initial body.
        for position in POSITIONS:
            self.add_new_body(position)

    def add_new_body(self, position):
        ghost = Turtle(SNAKE_SHAPE)
        ghost.color(SNAKE_COLOR)
        ghost.penup()
        ghost.goto(position)
        self.body.append(ghost)

    # Extending snake body
    def extend_body(self):
        self.add_new_body(self.body[-1].position())

    def repeat(self):
        # Hiding all the snake body expect the base body so that it can response
        for i in self.body[3:]:
            i.hideturtle()
        self.body = self.body[:3]
        self.head.goto(0, 0)

    def move(self):

        # For moving and turning.
        for body_number in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_number - 1].xcor()
            new_y = self.body[body_number - 1].ycor()
            self.body[body_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Making turtle move with keys.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
