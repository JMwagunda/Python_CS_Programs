import turtle

def draw_rectangular_body():
    car.color('#DC143C')
    car.fillcolor('#DC143C')
    car.penup()
    car.goto(0, 0)
    car.pendown()
    car.begin_fill()
    car.forward(170)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.end_fill()

def draw_window_and_roof():
    car.penup()
    car.goto(-80, 50)
    car.pendown()
    car.setheading(45)
    car.forward(70)
    car.setheading(0)
    car.forward(100)
    car.setheading(-45)
    car.forward(70)
    car.setheading(90)
    car.penup()
    car.goto(20, 50)
    car.pendown()
    car.forward(49.50)

def draw_tyres():
    def draw_single_tyre(x, y):
        car.penup()
        car.goto(x, y)
        car.pendown()
        car.color('#000000')
        car.fillcolor('#000000')
        car.begin_fill()
        car.circle(20)
        car.end_fill()

    draw_single_tyre(-100, -10)
    draw_single_tyre(100, -10)

def draw_rim_inside_circle():
    def draw_single_rim(x, y):
        car.penup()
        car.goto(x, y)
        car.pendown()
        car.color('#000000')
        car.fillcolor('#C0C0C0')
        car.begin_fill()
        car.circle(10)
        car.end_fill()

    draw_single_rim(-110, -10)
    draw_single_rim(90, -10)

# Below code for drawing rectangular upper body
def draw_rectangular_windows():
    car.color('#000000')
    car.fillcolor('#C0C0C0')
    car.penup()
    car.goto(-190, -2)
    car.pendown()
    car.begin_fill()
    car.forward(10)
    car.left(90)
    car.forward(17)
    car.left(90)
    car.forward(10)
    car.left(90)
    car.forward(17)
    car.end_fill()
    
# Safety_Lights
def draw_safety_lights():
    car.penup()
    car.goto(-202, 32)
    car.pendown()
    car.begin_fill()
    car.forward(3)
    car.left(90)
    car.forward(10)
    car.left(90)
    car.forward(3)
    car.left(90)
    car.forward(10)
    car.end_fill()

# front door glass
def draw_front_door_glass():
    car.color('#DC143C')
    car.fillcolor('#87CEFA')
    car.penup()
    car.goto(-42, 85)
    car.pendown()
    car.begin_fill()
    car.right(45)
    car.forward(45)
    car.left(135)
    car.forward(92)
    car.left(90)
    car.forward(43)
    car.left(90)
    car.forward(50)
    car.end_fill()

    car.penup()
    car.goto(68, 97)
    car.pendown()
    car.begin_fill()
    car.forward(45)
    car.left(90)
    car.forward(45)
    car.left(90)
    car.forward(90)
    car.left(135)
    car.forward(70)
    car.end_fill()

def draw_doors():
   # Door1
    car.color('#000000')
    car.penup()
    car.goto(-80, 50)
    car.pendown()  
    car.left(135)

    car.forward(45)
    car.left(90)
    car.forward(99)
    car.left(90)
    car.forward(45)

    # Door 2
    car.penup()
    car.goto(21, 50)
    car.pendown()  
    car.left(180)

    car.forward(45)
    car.left(90)
    car.forward(98)
    car.left(90)
    car.forward(45) 

# front Door handle
def draw_back_door_handle():
    car.penup()
    car.goto(100, 32)
    car.pendown()
    car.fillcolor('#C0C0C0')
    car.begin_fill()
    car.forward(3)
    car.left(90)
    car.forward(10)
    car.left(90)
    car.forward(3)
    car.left(90)
    car.forward(10)
    car.end_fill()
    
# front Door handle
def draw_front_door_handle():
    car.penup()
    car.left(90)
    car.goto(0, 32)
    car.pendown()
    car.fillcolor('#C0C0C0')
    car.begin_fill()
    car.forward(3)
    car.left(90)
    car.forward(10)
    car.left(90)
    car.forward(3)
    car.left(90)
    car.forward(10)
    car.end_fill()
    
# Back safety
def draw_back_safety():
    car.penup()
    car.left(90)
    car.goto(170, -2)
    car.pendown()
    car.fillcolor('#C0C0C0')
    car.begin_fill()
    car.forward(10)
    car.left(90)
    car.forward(20)
    car.left(90)
    car.forward(10)
    car.left(90)
    car.forward(20)
    car.end_fill()

# Main Function to Draw the Car
def draw_car():
    draw_rectangular_body()
    draw_window_and_roof()
    draw_tyres()
    draw_rim_inside_circle()
    draw_rectangular_windows()
    draw_safety_lights()
    draw_front_door_glass()
    draw_doors() #refactor draw doors functions
    draw_back_door_handle() #refactor the door handle code
    draw_front_door_handle()
    draw_back_safety()

# Set up the Turtle Screen
wn = turtle.Screen()
wn.setup(width=900, height=600)
wn.title("Car")
car = turtle.Turtle()
# Draw the Car
draw_car()
# Hide the Turtle
car.hideturtle()
# Keep the window open
turtle.done()