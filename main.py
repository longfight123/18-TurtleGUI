"""

This script creates a Turtle object that draws shapes with
increasing number of sides.

This script requires that 'turtle' be installed within the Python
environment you are running this script in.

"""

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('deep sky blue')
colors = ['red2', 'gold', 'salmon1', 'SteelBlue1', 'cyan3', 'green2', 'orange2', 'aquamarine', 'bisque', 'linen']

for sides in range(3, 11):
    tim.color(random.choice(colors))
    angle = 360 / sides
    for turns in range(sides):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()
