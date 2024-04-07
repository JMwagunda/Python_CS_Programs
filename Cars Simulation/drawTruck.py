import turtle
import random
import vehicles
import flower

truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD') 

def generate_random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

car=turtle.Turtle()
car.speed("fastest")

turtle.title("truck")
turtle.tracer(0,0)#disable animation
def draw_lorry(i, j, rand_hex_color,scale):
    # Main body
    car.color("grey")
    car.fillcolor(rand_hex_color)
    car.penup()
    car.goto(i*scale, j*scale)
    car.pendown()
    car.begin_fill()
    car.forward(400*scale)
    car.left(90)
    car.forward(150*scale)
    car.left(90)
    car.forward(400*scale)
    car.left(90)
    car.forward(150*scale)
    car.end_fill()

    print(i,j)

    # Cabin
    car.penup()
    car.goto((i + 400)*scale,75*scale)
    car.pendown()
    car.fillcolor("Grey")
    car.begin_fill()
    car.setheading(0)
    car.forward(70*scale)
    car.setheading(-45)
    car.forward(40*scale)
    car.setheading(-90)
    car.forward(70*scale)
    car.left(-90)
    car.forward(100*scale)
    car.end_fill()

    # window
    car.penup()
    car.goto((i + 400)*scale,75*scale)
    car.pendown()
    car.fillcolor("white")
    car.begin_fill()
    car.setheading(0)
    car.forward(70*scale)
    car.setheading(-45)
    car.forward(40*scale)
    car.setheading(-180)
    car.forward(100*scale)
    car.penup()
    car.goto((i+440)*scale,75*scale)
    car.pendown()
    car.setheading(-90)
    car.forward(30*scale)
    car.end_fill()

    # Wheels
    car.penup()
    car.goto((i + 50)*scale,(j-30)*scale) 
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(40*scale)
    car.end_fill()

    car.penup()
    car.goto((i + 430)*scale, (j-30)*scale)
    car.pendown()
    car.color("black")
    car.fillcolor("black")
    car.begin_fill()
    car.circle(40*scale)
    car.end_fill()

    car.hideturtle()
    # turtle.done()
    turtle.update()

# Usage


# draw_lorry(-300, 0, rand_hex_color)

def main(): 
    turtle.title("truck")
    turtle.tracer(0,0)#disable animation

    rand_hex_color = generate_random_color()
    scale=random.uniform(0.1,1)

    flower.main()

    draw_lorry(-300,-20,rand_hex_color,scale)
    # truck INFO DISPLAY 
    boldfont=("Arial",15,"bold")
    reg_font=("Times",12,"normal")

    turtle.penup()
    turtle.goto(-635,325)
    turtle.right(90)
    turtle.write("USED CAR INVENTORY",font=boldfont)
    turtle.goto(-635,315)
    turtle.write("*******************",font=boldfont)
    turtle.goto(-635,305)
    turtle.write("The following truck is in inventory",font=boldfont)
    turtle.goto(-635,285)
    turtle.write('Make:',font=boldfont)
    turtle.goto(-550,285)
    turtle.write(f"{truck.get_make()}",font=reg_font)
    turtle.goto(-635,265)
    turtle.write('Model:',font=boldfont)
    turtle.goto(-550,265)
    turtle.write(f'{truck.get_model()}',font=reg_font)
    turtle.goto(-635,245)
    turtle.write('Mileage:',font=boldfont)
    turtle.goto(-550,245)
    turtle.write(f'{truck.get_mileage()}',font=reg_font)
    turtle.goto(-635,225)
    turtle.write('Price:',font=boldfont)
    turtle.goto(-550,225)
    turtle.write(f'{truck.get_price()}',font=reg_font)
    turtle.goto(-635,205)
    turtle.write('Drive type: ',font=boldfont)
    turtle.goto(-520,205)
    turtle.write(f'{truck.get_drive_type()}',font=reg_font)
    turtle.done()


if __name__=="__main__":
    main()
