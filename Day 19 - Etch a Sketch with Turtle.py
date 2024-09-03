# Day 19 - Etch a Sketch
# W = forward, S = backward, A = counterclockwise, D = Clockwise, C = Clear Screen, go home
from turtle import Turtle, Screen

shelly = Turtle()
screen = Screen()

# function as input
def move_forward():
    shelly.forward(10)

def move_backward():
    shelly.right(180)
    shelly.forward(10)

def turn_clockwise():
    shelly.right(10)

def turn_counterclockwise():
    shelly.left(10)

def clear_the_screen():
    screen.resetscreen()


screen.listen()
# onkey is a "higher order function" - a function that triggers another function
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="c", fun=clear_the_screen)
screen.exitonclick()
