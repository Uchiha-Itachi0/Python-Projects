from turtle import Turtle
from screenSetting import HEIGHT, WIDTH
import random

SHAPE = 'square'
height = 2
width = 0.8
x_range = WIDTH // 2 + 20
y_range = HEIGHT // 2 - 60
TRAFFIC_SIZE = 20
SPEED = 1.1


class Traffic:
    def __init__(self):
        # super().__init__()

        self.traffic_size = []
        self.speed = .2

    def create(self):
        for i in range(TRAFFIC_SIZE):
            new_car = Turtle()
            new_car.penup()
            new_car.shape(SHAPE)
            new_car.shapesize(stretch_wid=width, stretch_len=height)
            new_car.goto(random.randint(-x_range, x_range), random.randint(-y_range, y_range))
            new_car.color(self.colors())
            self.traffic_size.append(new_car)

    def colors(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_color = (r, g, b)
        return new_color

    def move(self):
        for car in self.traffic_size:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def check_position(self):
        for car in self.traffic_size:
            if car.xcor() < -(WIDTH // 2):
                car.goto(WIDTH // 2, random.randint(-y_range, y_range))

    def increase_speed(self):
        self.speed *= SPEED
