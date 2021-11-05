from screenSetting import *
from body import Body
from score import Score
from traffic import Traffic
import time

screen.tracer(0)
screen.colormode(255)

body = Body()
score = Score()
traffic = Traffic()
traffic.create()
# Listening events
screen.listen()

screen.onkeypress(body.up, 'Up')
# screen.onkeypress(body.down, 'Down')

is_game_on = True
while is_game_on:
    screen.update()
    traffic.move()
    traffic.check_position()

    # Checking for stopping point
    if body.ycor() >= HEIGHT // 2 - 20:
        score.update_score()
        time.sleep(0.5)
        body.start()
        traffic.increase_speed()
    # if body.ycor() < -(HEIGHT // 2 - 20):
    #     body.start()

    # checking for collision
    for car in traffic.traffic_size:
        if body.distance(car) <= 30:
            score.game_over()
            is_game_on = False

screen.exitonclick()
