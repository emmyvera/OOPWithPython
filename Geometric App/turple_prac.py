import turtle

# Create a Turtle
myturtle = turtle.Turtle()

myturtle.penup()
myturtle.goto(50,90) # To to a particular coordinate
myturtle.pendown()

myturtle.forward(100) # move 100px forward
myturtle.left(90) # Turn 90 degrees
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

turtle.done()