"""

This script creates a Turtle object that walks in random direction
on the screen.

This script requires that 'turtle' be installed within the Python
environment you are running this script in.

"""

from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
tim.shape('turtle')
angles = [90, 0, 270]
tim.speed(10)
tim.pensize(width = 8)
turtle.colormode(255)

while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple = (r, g, b)
    tim.forward(100)
    tim.color(color_tuple)
    tim.right(random.choice(angles))


screen = Screen()
screen.exitonclick()