from turtle import Turtle
from screenSetting import HEIGHT, WIDTH
import random

FOOD_SHAPE = 'turtle'
FOOD_COLOR = 'green'
STRETCH_HEIGHT = 0.8
STRETCH_WIDTH = 0.8
height = HEIGHT // 2
width = WIDTH // 2


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=STRETCH_HEIGHT, stretch_wid=STRETCH_WIDTH)
        self.color(FOOD_COLOR)
        self.speed('fastest')
        random_x = random.randint(-width + 20, width - 20)
        random_y = random.randint(-height + 20, height - 20)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-width + 20, width - 20)
        random_y = random.randint(-height + 20, height - 20)
        self.goto(random_x, random_y)
