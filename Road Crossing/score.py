from turtle import Turtle
from screenSetting import WIDTH, HEIGHT

ALIGNMENT = 'left'
FONT_SIZE = 20
FONT = ('Courier', FONT_SIZE, 'normal')
width = WIDTH // 2 - 20
height = HEIGHT // 2 - 40


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-width, height)
        self.write_score()

    def write_score(self):
        self.write(f'Level {self.score}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)
