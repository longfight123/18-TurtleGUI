"""

This script creates a Turtle object that creates a spirograph.

This script requires that 'turtle' be installed within the Python
environment you are running this script in.

"""

from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
tim.shape('turtle')
tim.speed(15)
tim.pensize(width=2)
turtle.colormode(255)
to_angle = 5

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    tim.circle(radius=100)
    tim.setheading(to_angle)
    to_angle += 5
    tim.color(color_tuple)


screen = Screen()
screen.exitonclick()
