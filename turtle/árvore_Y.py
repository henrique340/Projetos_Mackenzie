# Python Program to draw a Y Fractal Tree in Turtle - Python
from turtle import *

speed('fast')
# Making the turtle facing upwards
right(-90)

# Using an acute angle btw
# the base and the Y's branch
angle = 30

# method for plotting a Y
def y(length, lvl):
    if lvl > 0:
        # altering the colour
        # according to the current level
        # by dividing the rgb range for green
        # into equal intervals for each level.
        pencolor(0, 254 // lvl, 0)

        # drawing the base
        forward(length)

        right(angle)

        # calling recursion for
        # the right subtree
        y(0.8 * length, lvl - 1)

        pencolor(0, 254 // lvl, 0)

        left(2 * angle)

        # calling recursion for
        # the left subtree
        y(0.8 * length, lvl - 1)

        pencolor(0, 254 // lvl, 0)

        right(angle)
        forward(-length)

    # Drawing the tree of length 40 and level 8

y(40, 8)

hideturtle()