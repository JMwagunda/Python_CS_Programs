import turtle

# Create a turtle object
truck = turtle.Turtle()

# Set the speed of the turtle
truck.speed(1)

# Draw the body of the truck
truck.color("blue")
truck.begin_fill()
truck.forward(200)
truck.left(90)
truck.forward(50)
truck.left(90)
truck.forward(50)
truck.right(90)
truck.forward(100)
truck.left(90)
truck.forward(50)
truck.left(90)
truck.forward(100)
truck.right(90)
truck.forward(50)
truck.left(90)
truck.forward(50)
truck.left(90)
truck.forward(200)
truck.end_fill()

# Draw the wheels of the truck
truck.penup()
truck.goto(50, -50)
truck.pendown()
truck.color("black")
truck.begin_fill()
truck.circle(25)
truck.end_fill()

truck.penup()
truck.goto(150, -50)
truck.pendown()
truck.color("black")
truck.begin_fill()
truck.circle(25)
truck.end_fill()

# Draw the windows of the truck
truck.penup()
truck.goto(50, 0)
truck.pendown()
truck.color("black")
truck.begin_fill()
truck.forward(50)
truck.left(90)
truck.forward(30)
truck.left(90)
truck.forward(50)
truck.end_fill()

# Hide the turtle
truck.hideturtle()

# Exit on click
turtle.exitonclick()