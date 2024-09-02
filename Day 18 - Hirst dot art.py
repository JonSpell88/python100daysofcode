# Day 18 - Hirst dot art
"""
import colorgram

colors = colorgram.extract('hirst_dots.jpg', 30)

rgb_list = []
for color in colors:
    my_color = color
    rgb = my_color.rgb # e.g. (255, 151, 210)
    rgb_tuple = (rgb.r, rgb.b, rgb.g)
    rgb_list.append(rgb_tuple)

print(rgb_list)
"""
import turtle
from turtle import Turtle, Screen
import random

# set up: color list comes from the colorgram code above, with values that are 220+ for all 3 codes removed
color_list = [(30, 34, 28), (33, 33, 27), (216, 5, 146), (51, 123, 81),  (247, 53, 122), (148, 211, 217), (42, 19, 30), (182, 36, 108), (110, 175, 154), (246, 125, 104), (54, 111, 133), (231, 94, 225), (193, 155, 6), (193, 2, 233), (221, 182, 177), (100, 7, 205), (103, 95, 80), (167, 224, 194), (184, 229, 207), (21, 27, 39), (61, 71, 62),  (155, 219, 217), (86, 13, 78), (134, 135, 188), (194, 109, 97), (43, 43, 83), (214, 93, 96)]

# set up: turtle class settings to initialize
shelly = Turtle()
screen = Screen()
turtle.colormode(255)
shelly.shape("turtle")
shelly.color("white")
# shelly.pencolor("white")
shelly.setpos(-300, -300)

# starts in lower left corner, draws 10 dots, then goes up a line to repeat
for i in range(0,10):
    y_coord = -300 + i*50
    for j in range(0, 10):
        x_coord = -300 + j*50
        rando_color = random.choice(color_list)
        shelly.dot(20, rando_color)
        shelly.teleport(x_coord,y_coord)

# for some reason, the very last dot is not drawn, this hack does it
# it's like it needed one more action after the dot-draw
rando_color = random.choice(color_list)
shelly.dot(20, rando_color)
shelly.teleport(x_coord+50,y_coord+50)
shelly.dot(20, "white")

# screen stays until you click it
screen.exitonclick()
