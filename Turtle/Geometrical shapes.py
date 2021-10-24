"""
It's a simple turtle program that draws the geometrical shapes

By default it will draw triangle, square, pentagon, hexagon and heptagon on top of each other
but you can change that by changing the range of for loop on line 64
"""

# It's not good practice to use *.
# import turtle as t (this is known as alias name).
# Built in library are like family library.
import random
from turtle import Turtle, Screen
from random import choice

ghost = Turtle()

# To access property of screen.
screen = Screen()

# Setting colormode to 255 so that we can specify are rgb value up to 255
screen.colormode(255)

# To change the shape of pen.
ghost.shape('circle')

# To change the color of pen
ghost.color('SlateGray2')

# To move the turtle little bit toward the center for our drawing
ghost.penup()
ghost.backward(50)
ghost.pendown()


def color():
    """
    Generate random color in rgb format
    """
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color_combination = (r, g, b)
    return color_combination


def draw_shape(number_of_side: int):
    """
    Draw shapes according to the side provided in the argument
    For example :
                    If number_of_side = 5
                    Then it draw's pentagon

    ------------------------Argument----------------------------------
    number_of_side[int]
    """
    angle = 360 // number_of_side  # Calculate how many angle it should turn to form a specific shape
    for i in range(number_of_side):
        ghost.forward(100)
        ghost.left(angle)


# This loop will call the draw_shape function 5 times with arguments 3, 4, 5, 6, 7 and therefore
# draw respective shape with same base
for shape_side in range(3, 8):
    ghost.color(color())  # Color of each shape will be according to the value generated form color function
    draw_shape(shape_side)


screen.exitonclick()
