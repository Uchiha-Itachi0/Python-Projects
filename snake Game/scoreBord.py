from turtle import Turtle
from screenSetting import HEIGHT

ALIGNMENT = 'center'
FONT_SIZE = 20
FONT = ('Courier', FONT_SIZE, 'normal')
height = HEIGHT // 2 - 30
SCOREBOARD_COLOR = 'white'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open('Data.txt') as data:
            self.high_score = int(data.read())
        self.score_number = 0
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(-35, height)
        self.color(SCOREBOARD_COLOR)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'  Score = {self.score_number}  High Score {self.high_score}', align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        if self.score_number >= self.high_score:
            self.high_score = self.score_number
            with open('Data.txt', 'w') as data:
                data.write(str(self.high_score))
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score_number += 1
        self.write_score()

    def reset_score(self):
        self.score_number = 0
        self.write_score()
