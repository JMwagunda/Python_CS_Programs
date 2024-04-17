import turtle
import tkinter as tk     # GUI
import random        # generating random colours and lengths for vehicles

# turtle screen, dimensions and background color
turtle.setup(width=1450, height=800)
screen = turtle.Screen()
screen.bgcolor('light blue')
screen.title('JMWagunda Car Inventory')


# maximum animation speed
turtle.tracer(1, 0)

car_details = """JMwagunda's Car inventory:
    Make: BMW
    Model: 2001
    Mileage: 70000
    Price: $15000.0
    Number of doors: 4"""

suv_details = """JMwagunda's SUV inventory:
    Make: Volvo
    Model: 2000
    Mileage: 30000
    Price: $18500.0
    Passenger Capacity: 5"""

truck_details = """JMwagunda's Truck inventory:
    Make: Toyota
    Model: 2002
    Mileage: 40000
    Price: $12000.0
    Drive type: 4WD"""


# load screen
def draw_initial_details():
    global car_details, suv_details, truck_details
    turtle.penup()    # lift the pen so no drawing occurs as turtle moves
    turtle.goto(-630, 300) # moves turtle to these coordinates and prints the below
    turtle.write("JMwagunda'S CAR INVENTORY", font=("Times New Roman", 14, "bold"))

    turtle.goto(-630, 190)
    turtle.write(car_details, align="left", font=("Helvetica", 11, "normal"))

    turtle.goto(-630, 50)
    turtle.write(suv_details, align="left", font=("Helvetica", 11, "normal"))

    turtle.goto(-630, -90)
    turtle.write(truck_details, align="left", font=("Helvetica", 11, "normal"))
    turtle.hideturtle() # hides the turtle cursor after printing


draw_initial_details()  # calling this function


# clear_screen function to clear screen ie if want to draw new object
def clear_screen():
    for turtle_object in turtle.Screen().turtles():
        turtle_object.clear()


# functions to draw cars
def draw_car():
    global car_details # Get car details
    clear_screen()     # clear screen in preparation of drawing new car
    turtle.penup()
    turtle.goto(-630, 300)
    turtle.write(" JMwagunda'S  CAR INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 290)
    turtle.write("------------------------------------------", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 190)
    turtle.write(car_details, align="left", font=("Arial", 11, "normal"))  # write car details on the left

    # Car dimensions
    a = 20 # lower bound of the car
    b = 80  # upper bound of the car
    u = random.random()   # generates a random value between 0 and 1 that is used to calculate actual length
    car_length = a + u * (b - a)

    # turtle object
    car = turtle.Turtle()   # creates a new turtle object called car
    # hiding initial turtle
    turtle.ht()

    # lifts the pen of the turtle (car) and moves to starting point, so no drawing occurs
    car.penup()
    car.goto(-100, 0)

    # random colors for vehicle
    blue_amount = random.random() # random generates a number between 0 and 1 representing amount of colour
    green_amount = random.random()
    red_amount = random.random()

    # drawing flowers
    draw_flowers()

    # Initialise drawing SUV
    car.speed(0)
    car.pendown()
    car.fillcolor(red_amount, green_amount, blue_amount)  # Set fill color of the car to the specified RGB values
    car.begin_fill()
    car.forward(car_length * 4)  # "length" Move the turtle forward by the car's length multiplied by 4
    car.left(90)  # turn turtle by 90 degrees to begin drawing width
    car.forward(car_length / 1.175)  # width
    car.left(90)
    car.forward(car_length * 5)  # to draw back side of car
    car.left(90)
    car.forward(car_length / 1.175)
    car.end_fill()

    # wheel1
    car.left(90)  # turn turtle by 90 degrees
    car.forward(car_length / 1.25)   # distance of wheel from front of the car
    car.right(90)
    car.forward(car_length / 8) # width of the wheel
    car.fillcolor('black')
    car.begin_fill()
    car.circle(car_length / 3.45)  # draw circle to represent wheel
    car.end_fill()
    # wheel2
    car.back(car_length / 8)
    car.left(90)
    car.forward(car_length * 2.75)
    car.right(90)
    car.forward(car_length / 8)
    car.fillcolor('black')
    car.begin_fill()
    car.circle(car_length / 3.45)
    car.end_fill()
    
    # upper body(trapezium and middle-line)
    car.back(car_length / 8)
    car.left(90)
    car.forward(car_length * 1.45)
    car.left(90)
    car.forward(car_length / 1.175)
    car.left(90)
    car.forward(car_length * 0.75)
    # trapezium
    car.right(60)
    car.forward(car_length * 1.35)
    car.left(60)
    car.forward(car_length * 2.15)
    car.left(60)
    car.forward(car_length * 1.35)
    # middle line
    car.left(120)
    car.forward(car_length * 1.7)
    car.left(90)
    car.forward(car_length * 1.185)
    car.right(90)

    car.hideturtle()
    turtle.update()



def draw_suv():
    global suv_details
    clear_screen()
    turtle.penup()
    turtle.goto(-630, 300)
    turtle.write("JMwagunda'S SUV INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 290)
    turtle.write("------------------------------", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 190)
    turtle.write(suv_details, align="left", font=("Arial", 11, "normal"))

    # parameters
    a = 25
    b = 90
    u = random.random()
    suv_length = a + u * (b - a)

    # turtle object
    suv = turtle.Turtle()

    # hiding initial turtle
    turtle.ht()

    # random colors for vehicle
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()

    # drawing flowers
    draw_flowers()

    # Initialise drawing SUV
    suv.penup()
    suv.goto(-100, 0)
    suv.speed(0)
    suv.pendown()
    suv.fillcolor(red_amount, green_amount, blue_amount)
    suv.begin_fill()
    suv.forward(suv_length * 5)  # length
    suv.left(90)
    suv.forward(suv_length / 1.175)  # width
    suv.left(90)
    suv.forward(suv_length * 5)
    suv.left(90)
    suv.forward(suv_length / 1.175)
    suv.end_fill()
    # wheel1
    suv.left(90)
    suv.forward(suv_length / 1.25)
    suv.right(90)
    suv.forward(suv_length / 8)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle(suv_length / 3.45)
    suv.end_fill()
    # wheel2
    suv.back(suv_length / 8)
    suv.left(90)
    suv.forward(suv_length * 2.75)
    suv.right(90)
    suv.forward(suv_length / 8)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle(suv_length / 3.45)
    suv.end_fill()
    
    # upper body(trapezium, backwheel, middle-line)
    suv.back(suv_length / 8)
    suv.left(90)
    suv.forward(suv_length * 1.45)
    suv.left(90)
    suv.forward(suv_length / 1.175)
    suv.left(90)
    suv.forward(suv_length * 1.6)
    # trapezium
    suv.right(60)
    suv.forward(suv_length * 1.2)
    suv.left(60)
    suv.forward(suv_length * 2.25)
    suv.left(63)
    suv.forward(suv_length * 1.2)
    # back-wheel
    suv.left(27)
    suv.forward(suv_length * 0.085)
    suv.right(90)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle((suv_length / 2.95), extent=180)
    suv.end_fill()
    # middle line
    suv.left(90)
    suv.forward(suv_length * 0.785)
    suv.right(90)
    suv.forward(suv_length * 2.49)
    suv.left(90)
    suv.forward(suv_length * 1.075)

    turtle.update()
    suv.hideturtle()


def draw_truck():
    global truck_details
    clear_screen()
    turtle.penup()
    turtle.goto(-630, 300)
    turtle.write("JMwagunda'S TRUCK INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 290)
    turtle.write("------------------------------", font=("Calibri", 14, "bold"))
    turtle.goto(-630, 190)
    turtle.write(truck_details, align="left", font=("Arial", 11, "normal"))
    
    # parameters
    a = 30
    b = 95
    u = random.random()
    truck_length = a + u * (b - a)

    # random colors for vehicle
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()

    # turtle object
    truck = turtle.Turtle()

    # hiding initial turtle
    turtle.ht()

    # drawing flowers
    draw_flowers()

    # initialising drawing of truck
    truck.penup()
    truck.goto(-200, 0)
    truck.speed(0)
    truck.pendown()
    truck.fillcolor(red_amount, green_amount, blue_amount)
    truck.begin_fill()
    truck.forward(truck_length * 4.5)  # length
    truck.left(90)
    truck.forward(truck_length * 2.875)  # width
    truck.left(90)
    truck.forward(truck_length * 4.5)
    truck.left(90)
    truck.forward(truck_length * 2.875)
    truck.end_fill()
    # wheel1
    truck.left(90)
    truck.forward(truck_length / 1.975)
    truck.right(90)
    truck.forward(truck_length / 10.025)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.15)
    truck.end_fill()
    # wheel2
    truck.back(truck_length / 10.45)
    truck.left(90)
    truck.forward(truck_length * 1.285)
    truck.right(90)
    truck.forward(truck_length / 7)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.095)
    truck.end_fill()
    # trapezium
    truck.back(truck_length / 7.015)
    truck.left(90)
    truck.forward(truck_length * 2.7)
    truck.left(90)
    truck.forward(truck_length * 0.145)
    truck.right(90)
    truck.forward(truck_length * 1.15)
    truck.right(90)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.095)
    truck.end_fill()
    truck.left(90)
    truck.forward(truck_length * 1.75)
    truck.left(90)
    truck.forward(truck_length * 1.35)
    truck.left(60)
    truck.forward(truck_length * 1.75)
    truck.left(120)
    truck.forward(truck_length * 0.875)
    truck.left(90)
    truck.forward(truck_length * 1.5)
    truck.left(150)
    truck.forward(truck_length * 1.75)
    truck.left(30)
    truck.forward(truck_length * 1.425)

    truck.hideturtle()
    turtle.update()


def gencolors():  # generate random colors
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()
    # normalized RGB values (0 rep. absence of color and 1 represents the maximum intensity of that component)
    return red_amount,green_amount,blue_amount


def draw_flowers():
    turtle.speed(0)  # set drawing speed to maximum
    turtle.ht()   # hide the turtle cursor
    turtle.penup() # lifts the pen till it moves to the given coordinates then begins drawing
    turtle.goto(500, -150)
    turtle.pendown()

    for i in range(8):  # loop iterates 8 times drawing 8 flowers
        turtle.penup()  # lifts pen
        turtle.left(180)   # rotate left 180 degrees
        turtle.fd(110)   # move foward by 110 units the pendown
        turtle.pendown()
        turtle.right(180)

        # flower base where petals will be positioned
        # Set the fill color of the flower base to a randomly generated color
        turtle.fillcolor(gencolors())

        # Begin the filling process for the flower base
        turtle.begin_fill()

        # Draw the first semicircle of the flower base
        turtle.circle(1, 180)

        # Draw the second, larger semicircle of the flower base
        turtle.circle(2.5, 110)

        # Rotate the turtle 50 degrees to the left
        turtle.left(50)

        # Draw a smaller circle to form part of the flower base
        turtle.circle(6, 45)

        # Draw another smaller circle to complete the flower base
        turtle.circle(2, 170)

        # Rotate the turtle 24 degrees to the right
        turtle.right(24)

        # Move the turtle forward by 3 units
        turtle.fd(3)

        # Rotate the turtle 10 degrees to the left
        turtle.left(10)

        # Draw a small circle to add detail to the flower base
        turtle.circle(3, 110)

        # Move the turtle forward by 2 units
        turtle.fd(2)

        # Rotate the turtle 40 degrees to the left
        turtle.left(40)

        # Draw a larger circle to add more detail to the flower base
        turtle.circle(9, 70)

        # Draw another smaller circle to add detail to the flower base
        turtle.circle(3, 150)

        # Rotate the turtle 30 degrees to the right
        turtle.right(30)

        # Move the turtle forward by 1.5 units
        turtle.fd(1.5)

        # Draw a circle to add further detail to the flower base
        turtle.circle(8, 90)

        # Rotate the turtle 15 degrees to the left
        turtle.left(15)

        # Move the turtle forward by 4.5 units
        turtle.fd(4.5)

        # Rotate the turtle 165 degrees to the right
        turtle.right(165)

        # Move the turtle forward by 2 units
        turtle.fd(2)

        # Rotate the turtle 155 degrees to the left
        turtle.left(155)

        # Draw a circle to add more detail to the flower base
        turtle.circle(15, 80)

        # Rotate the turtle 50 degrees to the left
        turtle.left(50)

        # Draw a circle to complete the flower base
        turtle.circle(15, 90)

        # End the filling process for the flower base
        turtle.end_fill()

        # Petal 1
        turtle.left(150)
        turtle.circle(-9, 70)
        turtle.left(20)
        turtle.circle(7.5, 105)
        turtle.setheading(60)
        turtle.circle(8, 98)
        turtle.circle(-9, 40)

        # Petal 2
        turtle.left(180)
        turtle.circle(9, 40)
        turtle.circle(-8, 98)
        turtle.setheading(-83)

        # Leaf 1
        turtle.fd(3)
        turtle.left(90)
        turtle.fd(2.5)
        turtle.left(45)
        turtle.fillcolor(gencolors())
        turtle.begin_fill()
        turtle.circle(-8, 90)
        turtle.right(90)
        turtle.circle(-8, 90)
        turtle.end_fill()
        turtle.right(135)
        turtle.fd(6)
        turtle.left(180)
        turtle.fd(8.5)
        turtle.left(90)
        turtle.fd(8)

        # Leaf 2
        turtle.right(90)
        turtle.right(45)
        turtle.fillcolor(gencolors())
        turtle.begin_fill()
        turtle.circle(8, 90)
        turtle.left(90)
        turtle.circle(8, 90)
        turtle.end_fill()
        turtle.left(135)
        turtle.fd(6)
        turtle.left(180)
        turtle.fd(6)
        turtle.right(90)
        turtle.circle(20, 60)

    # Hide turtle
    turtle.hideturtle()


# Create buttons using tkinter
root = tk.Tk()


root.geometry("400x100+1000+50")  # Set window size and position (top right corner)


root.title("Display Cars")

# Button colors
car_button_color = "#FF5733"  # Orange
suv_button_color = "#33FF57"  # Green
truck_button_color = "#3366FF"  # Blue

car_button = tk.Button(root, text="Display Car", command=draw_car, width=10, height=2, bg=car_button_color)  # Adjusting button size
car_button.pack(side=tk.LEFT,padx=6.5, pady=10)

suv_button = tk.Button(root, text="Display SUV", command=draw_suv, width=10, height=2, bg=suv_button_color)  # Adjusting button size
suv_button.pack(side=tk.LEFT,padx=6.5, pady=10)

truck_button = tk.Button(root, text="Display Truck", command=draw_truck, width=10, height=2, bg=truck_button_color)  # Adjusting button size
truck_button.pack(side=tk.LEFT,padx=6.5, pady=10)

root.mainloop()