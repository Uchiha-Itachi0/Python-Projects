from turtle import Screen

# All screen property
HEIGHT = 600
WEIGHT = 1000
SCREEN_COLOR = 'black'
GAME_TITLE = 'Pong'

screen = Screen()
screen.setup(height=HEIGHT, width=WEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(GAME_TITLE)