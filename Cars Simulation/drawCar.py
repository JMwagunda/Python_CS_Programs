import turtle
import random
import flower
import vehicles

Car=vehicles.Car('BMW', 2001, 70000, 15000.0, 4)

def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

car=turtle.Turtle()
car.speed("fastest")

def draw_Car(i, j, rand_hex_color,scale):
    # Drawing the upper body
    car.fillcolor(rand_hex_color)
    car.penup()
    car.goto(i, j)
    car.pendown()
    car.begin_fill()
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(370)
    car.left(90)
    car.forward(50)
    car.end_fill()

    # Draw windows
    car.fillcolor("#D3D3D3")
    car.penup()
    car.goto(i + 100, 50)
    car.pendown()
    car.begin_fill()
    car.setheading(45)
    car.forward(70)
    car.setheading(0)
    car.forward(100)
    car.setheading(-45)
    car.forward(70)
    car.setheading(90)
    car.end_fill()
    car.penup()
    car.goto(i + 200, 50)
    car.pendown()
    car.forward(49.50)

    # Draw seats
    car.fillcolor("yellow")
    car.penup()
    car.goto(i + 150, 50)
    car.pendown()
    car.begin_fill()
    car.setheading(45)
    car.forward(40)
    car.setheading(0)
    car.forward(10)
    car.setheading(225)
    car.forward(40)

    car.penup()
    car.goto(i + 210, 50)
    car.pendown()
    car.setheading(45)
    car.forward(40)
    car.setheading(0)
    car.forward(10)
    car.setheading(225)
    car.forward(40)
    car.end_fill()

    # Draw the 2 wheels
    car.penup()
    car.goto(i + 100, 0)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(20)
    car.end_fill()
    car.penup()
    car.goto(i + 300, 0)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(20)
    car.end_fill()

    car.hideturtle()


def main(): 
    car = turtle.Turtle()
    car.speed("fastest")#set maximum speed
    turtle.tracer(0,0)# disable animation
    car.screen.bgcolor("#fff")


    rand_hex_color = generate_random_color()
    scale=random.uniform(0.1,1)

    flower.main()

    draw_Car(-200,0,rand_hex_color,scale)
    # Car INFO DISPLAY 
    boldfont=("Arial",15,"bold")
    reg_font=("Times",12,"normal")

    turtle.penup()
    turtle.goto(-635,325)
    turtle.right(90)
    turtle.write("USED CAR INVENTORY",font=boldfont)
    turtle.goto(-635,315)
    turtle.write("*******************",font=boldfont)
    turtle.goto(-635,305)
    turtle.write("The following Car is in inventory",font=boldfont)
    turtle.goto(-635,285)
    turtle.write('Make:',font=boldfont)
    turtle.goto(-550,285)
    turtle.write(f"{Car.get_make()}",font=reg_font)
    turtle.goto(-635,265)
    turtle.write('Model:',font=boldfont)
    turtle.goto(-550,265)
    turtle.write(f'{Car.get_model()}',font=reg_font)
    turtle.goto(-635,245)
    turtle.write('Mileage:',font=boldfont)
    turtle.goto(-550,245)
    turtle.write(f'{Car.get_mileage()}',font=reg_font)
    turtle.goto(-635,225)
    turtle.write('Price:',font=boldfont)
    turtle.goto(-550,225)
    turtle.write(f'{Car.get_price()}',font=reg_font)
    turtle.goto(-635,205)
    turtle.write('Drive type: ',font=boldfont)
    turtle.goto(-520,205)
    turtle.write(f'{Car.get_doors()}',font=reg_font)
    turtle.done()


if __name__=="__main__":
    main()
