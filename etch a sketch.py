from turtle import Turtle, Screen
# --------------------------------------Ecko Sketch---------------------------------------------
tom = Turtle()
screen = Screen()
def move_fowards():
    tom.forward(10)

def move_backwards():
    tom.backward(10)

def turn_right():
    new = tom.heading() - 10 # turn the heading of the arrow 90 degreee ould be north
    tom.setheading(new)  # able to turn head every direction every key being pressed (turn left 10 degrees)

def turn_left():
    new1 = tom.heading() + 10 # turn the heading of the arrow 90 degreee ould be north
    tom.setheading(new1)  # able to turn head every direction (turn left 10 degrees)screen.listen()

def clear():
    tom.clear() #Delete the turtle’s drawings from the screen
    tom.penup() # remove any writting
    tom.home() # Move turtle to the origin – coordinates (0,0)
    tom.pendown() # returns any writting after cleared

screen.listen()
screen.onkey(key='w', fun=move_fowards) # on pressing Key the function executes
screen.onkey(key='s', fun=move_backwards) # on pressing Key the function executes
screen.onkey(key='a', fun=turn_left) # on pressing Key the function executes
screen.onkey(key='d', fun=turn_right) # on pressing Key the function executes
screen.onkey(key='c', fun=clear) # on pressing Key the function executes


screen.exitonclick() # the terminal will close upon click
