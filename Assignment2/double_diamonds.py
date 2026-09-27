"""this program is to generate two diamonds using turtle graphics"""

import turtle

# predefine the diamond side length
SIDE_LENGTH = 100
# predefine the fill color
FILL_COLOR = 'blue'

# setup the turtle window
turtle.setup(500,600)

#setup the turtle
turtle.hideturtle()
turtle.fillcolor(FILL_COLOR)

# draw the left-side diamond first using the predefined SIDE_LENGTH
turtle.penup()
turtle.goto(-120,0)
turtle.pendown()

turtle.begin_fill()
# fill the code to draw the left-side diamond
turtle.left(45)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.end_fill()

# draw the right-side diamond next
turtle.penup()
turtle.goto(20,0)
turtle.setheading(0)
turtle.pendown()
# fill the code to draw the right-side diamond
turtle.begin_fill()
turtle.left(45)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.right(90)
turtle.forward(SIDE_LENGTH)
turtle.end_fill()

turtle.done()