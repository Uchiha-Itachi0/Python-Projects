from turtle import Turtle

SCORE_COLOR = 'white'
ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCORE_COLOR)
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font= FONT)
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=FONT)

    def l_point(self):
        self.l_score += 1
        self.display_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.display_score()


