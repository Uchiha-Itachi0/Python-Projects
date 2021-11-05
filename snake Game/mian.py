from screenSetting import *
from snake import Snake
from food import Food
from scoreBord import Score
import time

# For delaying drawing.
screen.tracer(0)

# Making Snake
snake = Snake()

# Making Food
food = Food()

# Making Score
score = Score()

# Listening key strokes
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True
while is_game_on:
    # When to display the drawing.
    screen.update()

    time.sleep(0.1)

    # Moving Snake
    snake.move()

    # Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend_body()

    # Collision with wall.
    width = WIDTH // 2 - 20
    height = HEIGHT // 2 - 20
    if snake.head.xcor() > width or snake.head.xcor() < -width or snake.head.ycor() > height or snake.head.ycor() < \
            -height:
        score.update_high_score()
        snake.repeat()
        score.reset_score()
        # is_game_on = False
        # score.game_over()

    # Collision with tail.
    for i in snake.body[1:]:
        if snake.head.distance(i) < 10:
            score.update_high_score()
            snake.repeat()
            score.reset_score()
            # score.game_over()
            # is_game_on = False

screen.exitonclick()
