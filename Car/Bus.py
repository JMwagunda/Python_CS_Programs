import turtle

# Draw bus body function
def draw_bus_body(bus):
    bus.fillcolor("yellow")
    bus.begin_fill()
    bus.forward(200)
    bus.left(90)
    bus.forward(100)
    bus.left(90)
    bus.forward(200)
    bus.left(90)
    bus.forward(100)
    bus.left(90)

    bus.penup()
    bus.goto(200, 0)
    bus.pendown()
    bus.forward(50)
    bus.left(90)
    bus.forward(50)
    bus.left(90)
    bus.forward(50)
    bus.left(90)
    bus.end_fill()

# Draw wheel function
def draw_wheel(bus):
    # Back wheel code
    bus.penup()
    bus.goto(10, 0)
    bus.pendown()
    bus.fillcolor("black")
    bus.begin_fill()
    bus.circle(20)
    bus.end_fill()

    # Back wheel hub code
    bus.penup()
    bus.goto(20, 0)
    bus.pendown()
    bus.fillcolor("grey")
    bus.begin_fill()
    bus.circle(10)
    bus.end_fill()

    # Front wheel code
    bus.penup()
    bus.goto(185, 0)
    bus.pendown()
    bus.fillcolor("black")
    bus.begin_fill()
    bus.circle(20)
    bus.end_fill()

    # Front wheel hub code
    bus.penup()
    bus.goto(195, 0)
    bus.pendown()
    bus.fillcolor("grey")
    bus.begin_fill()
    bus.circle(10)
    bus.end_fill()

# Draw door function
def draw_door(bus):
    bus.penup()
    bus.goto(180, 5)
    bus.pendown()
    bus.fillcolor("cyan")
    bus.begin_fill()
    bus.backward(85)
    bus.left(90)
    bus.backward(25)
    bus.left(90)
    bus.backward(85)
    bus.left(90)
    bus.backward(25)
    bus.left(90)
    bus.end_fill()

    # Draw door handle
    bus.penup()
    bus.goto(170, 45)
    bus.pendown()
    bus.fillcolor("grey")
    bus.begin_fill()
    bus.circle(4)
    bus.end_fill()

# Draw windows function
def draw_windows(bus):
    bus.penup()
    bus.goto(10, 90)
    bus.pendown()
    bus.fillcolor("cyan")
    bus.begin_fill()
    bus.forward(35)
    bus.left(90)
    bus.forward(120)
    bus.left(90)
    bus.forward(35)
    bus.left(90)
    bus.forward(120)
    bus.left(90)

    bus.forward(35)
    bus.left(90)
    bus.forward(30)
    bus.left(90)
    bus.forward(35)
    bus.right(90)
    bus.forward(30)
    bus.right(90)
    bus.forward(35)
    bus.left(90)
    bus.forward(30)
    bus.left(90)
    bus.forward(35)
    bus.end_fill()

# Driver window function
def draw_driver_window(bus):
    bus.penup()
    bus.goto(200, 90)
    bus.pendown()
    bus.fillcolor("cyan")
    bus.begin_fill()
    bus.left(90)
    bus.forward(5)
    bus.left(90)
    bus.forward(35)
    bus.left(90)
    bus.forward(5)
    bus.left(90)
    bus.end_fill()

# Draw bus function
def draw_bus():
    draw_bus_body(bus)
    draw_wheel(bus)
    draw_door(bus)
    draw_windows(bus)
    draw_driver_window(bus)
     
# Set up the Turtle Screen
wn = turtle.Screen()
wn.setup(width=900, height=600)
wn.title("Bus")
bus = turtle.Turtle()

# Draw the Car
draw_bus()
# Hide the Turtle
bus.hideturtle()
# Keep the window open
turtle.done()


