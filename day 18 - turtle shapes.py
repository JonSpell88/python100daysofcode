from turtle import Turtle, Screen
# also possible from turtle import *   --- but this is bad code
# also possible to alias the import : from turtle import Turtle as t, then you could have tom = t(), like pandas as pd # or numpy as np
import random


shelly = Turtle()

shelly.shape("turtle")
shelly.color("red")
shelly.pencolor("orange") # starting color
shelly.speed(3) # about half speed
# just a selection of colors I pulled from 
# https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
color_list = ["peach puff", "navy", "aquamarine", "orange",
"violet red", "purple", "LemonChiffon2", "RoyalBlue1",
"DeepSkyBlue2", "turquoise1", "SeaGreen1",
"chartreuse3", "OliveDrab1", "yellow2", "gold3",
"sienna1", "burlywood1", "firebrick1", "salmon1",
"tomato2", "red3", "HotPink1", "maroon1",
"orchid1", "purple4", "thistle4", "gray20"]

for i in range(3, 11): # cycles through shapes from triangle to uh, 10-sided polygon
    shape_color = random.choice(color_list)
    shelly.pencolor(shape_color)
    shelly.width(5)
    for j in range(1, i+1): # draws each line of the object, turning on an equal angle for that object
        angle = 360 / i
        shelly.forward(100)
        shelly.right(angle)
