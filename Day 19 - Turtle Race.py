from turtle import Turtle, Screen
import random

# create instances of turtle, set the color, turn off the trailing pen

screen = Screen()

screen.setup(width=500,height=400) # x bet -250 to 250, y bet 200 to -200

# turns out there's a way to assign 6 turtles to the same variable name (i.e. new_turtle = Turtle() ) where
# each one gets a different memory reference, but I don't like that way. It is faster, in that you can create them in
# a loop instead of spelling out each one like I'm doing here.
shelly = Turtle(shape="turtle")
shelly.color("orange")
shelly.penup()

absalom = Turtle(shape="turtle")
absalom.color("red")
absalom.penup()

bronwyn = Turtle(shape="turtle")
bronwyn.color("green")
bronwyn.penup()

cattress = Turtle(shape="turtle")
cattress.color("blue")
cattress.penup()

dug = Turtle(shape="turtle")
dug.color("black")
dug.penup()

egghead = Turtle(shape="turtle")
egghead.color("purple")
egghead.penup()



shelly.goto(x=-230, y=-150)
absalom.goto(x=-230, y=-90)
bronwyn.goto(x=-230, y=-30)
cattress.goto(x=-230, y=30)
dug.goto(x=-230, y=90)
egghead.goto(x=-230, y=150)

def go_turtles():
    shelly.forward(random.randint(0,10))
    absalom.forward(random.randint(0,10))
    bronwyn.forward(random.randint(0,10))
    cattress.forward(random.randint(0,10))
    dug.forward(random.randint(0,10))
    egghead.forward(random.randint(0,10))




user_choice = screen.textinput(title="It's a turtle race!", prompt="Choose a color to win: ")
is_race_over = False
winner = ""
turtle_list = ["shelly", "absalom", "bronwyn", "cattress", "dug", "egghead"]

# on_your_marks()
# get_set()
while is_race_over == False:
    go_turtles() # moves each turtle ahead a random value between 0 and 10

    # tests to see if any turtle has crossed the finish line at x value 230
    if shelly.xcor() >= 230:
        winner = "orange"
    elif absalom.xcor() >= 230:
        winner = "red"
    elif bronwyn.xcor() >= 230:
        winner = "green"
    elif cattress.xcor() >= 230:
        winner = "blue"
    elif dug.xcor() >= 230:
        winner = "black"
    elif egghead.xcor() >= 230:
        winner = "purple"
    else:
        pass
    # if winner has been assigned, exit the loop
    if winner != "":
        is_race_over = True

if user_choice == winner:
    print(f"You picked the winning turtle! Go {winner}!")
else:
    print(f"You chose the wrong turtle. {winner} won.")



# keep screen active until clicked
screen.exitonclick()