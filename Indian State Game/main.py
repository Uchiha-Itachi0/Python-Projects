import pandas
import turtle
from turtle import Turtle, Screen

# Declaring some variable for use
IMAGE_LOCATION = './India_map.gif'
TITLE = 'Indian State Game'
WIDTH, HEIGHT = 450, 500
FILE_NAME = 'Indian_State_Data.csv'

rock = Turtle()
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

screen.title(TITLE)

# Adding our default image
screen.addshape(IMAGE_LOCATION)
rock.shape(IMAGE_LOCATION)

turtle.hideturtle()

# Reading csv data from csv file
data = pandas.read_csv(FILE_NAME)

# Extracting state column from data and converting it to list
state_list = data.state.to_list()


# for getting coordinate of screen by mouse click
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)


# Rendering state name on screen
def render_state_name(x_cor_of_state, y_cor_of_state):
    turtle.penup()
    turtle.goto(x_cor_of_state, y_cor_of_state)
    turtle.pendown()
    turtle.write(user_answer, align='center')


is_game_on = True
right_guess = 0
user_guess_state = []

while is_game_on:

    user_answer = turtle.textinput(title='Guess the state', prompt=f'❌Type exit to quit the game \n'
                                                                   f'\n'
                                                                   f'⭐If you fail to guess all the state a file is '
                                                                   f'create for you to learn all state that you fail to'
                                                                   f'guess\n'
                                                                   f'\n'
                                                                   f'🚩Type the state name [{right_guess}/29]')

    # Converting user answer to match the value store in the sate_list
    user_answer = user_answer.title()

    # Checking if user want to exit the game
    if user_answer == 'Exit':
        is_game_on = False

    if user_answer in state_list and user_answer not in user_guess_state:
        right_guess += 1
        user_guess_state.append(user_answer)

        # Finding x and y coordinate of state location from stored data
        x_cor_of_state = float(data[data.state == user_answer].x)
        y_cor_of_state = float(data[data.state == user_answer].y)

        # Calling function to render state name
        render_state_name(x_cor_of_state, y_cor_of_state)

    # Checking if user guess all the answer
    if right_guess == 29:
        break

# Finding remaining state
learning_state = [state for state in state_list if state not in user_guess_state]

# Creating file for all remaining state
learn_state_file = pandas.DataFrame(learning_state)
learn_state_file.to_csv('Learn State.csv')
