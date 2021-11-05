from screenSetting import *
from paddle import Paddle
from ball import Ball
from scoreBoard import Score
import time

screen.tracer(0)

# Creating paddles
paddle_pos_x = WEIGHT // 2 - 20
r_paddle = Paddle((paddle_pos_x, 0))
l_paddle = Paddle((-paddle_pos_x - 10, 0))

# Listening and performing events
screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.w, 'w')
screen.onkeypress(l_paddle.s, 's')

# Creating Ball.
ball = Ball()

# Making score
score = Score()

is_game_on = True
while is_game_on:
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()

    # Detecting Collision with wall
    if ball.ycor() >= HEIGHT // 2 - 10 or ball.ycor() <= -(HEIGHT // 2 - 10):
        ball.bounce_y()

    # Detecting collision with the paddle
    if ball.distance(r_paddle.paddle) < 50 and ball.xcor() >= WEIGHT // 2 - 30 or ball.distance(l_paddle.paddle) < 50 and ball.xcor() <= -(WEIGHT // 2 - 20):
        ball.bounce_x()

    # Collision with the wall (restart)
    if ball.xcor() >= WEIGHT // 2 - 10:
        score.l_point()
        ball.reset_position()

    if ball.xcor() <= - (WEIGHT // 2 - 10):
        score.r_point()
        ball.reset_position()


screen.exitonclick()
