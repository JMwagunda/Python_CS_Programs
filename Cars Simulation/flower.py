import turtle
import random
def generate_random_color():
    color="#{:06x}".format(random.randint(0,0xFFFFFF))
    return color

def draw_flower(x, y, scale,color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Rose base
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(5 * scale, 180)
    turtle.circle(12.5 * scale, 110)
    turtle.left(50)
    turtle.circle(30 * scale, 45)
    turtle.circle(10 * scale, 170)
    turtle.right(24)
    turtle.fd(15 * scale)
    turtle.left(10)
    turtle.circle(15 * scale, 110)
    turtle.fd(10 * scale)
    turtle.left(40)
    turtle.circle(45 * scale, 70)
    turtle.circle(15 * scale, 150)
    turtle.right(30)
    turtle.fd(7.5 * scale)
    turtle.circle(40 * scale, 90)
    turtle.left(15)
    turtle.fd(22.5 * scale)
    turtle.right(165)
    turtle.fd(10 * scale)
    turtle.left(155)
    turtle.circle(75 * scale, 80)
    turtle.left(50)
    turtle.circle(75 * scale, 90)
    turtle.end_fill()

    # Petal 1
    turtle.left(150)
    turtle.circle(-45 * scale, 70)
    turtle.left(20)
    turtle.circle(37.5 * scale, 105)
    turtle.setheading(60)
    turtle.circle(40 * scale, 98)
    turtle.circle(-45 * scale, 40)

    # Petal 2
    turtle.left(180)
    turtle.circle(45 * scale, 40)
    turtle.circle(-40 * scale, 98)
    turtle.setheading(-83)

    # Leaves 1
    turtle.fd(15 * scale)
    turtle.left(90)
    turtle.fd(12.5 * scale)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-40 * scale, 90)
    turtle.right(90)
    turtle.circle(-40 * scale, 90)
    turtle.end_fill()
    turtle.right(135)
    turtle.fd(30 * scale)
    turtle.left(180)
    turtle.fd(42.5 * scale)
    turtle.left(90)
    turtle.fd(40 * scale)

    # Leaves 2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(40 * scale, 90)
    turtle.left(90)
    turtle.circle(40 * scale, 90)
    turtle.end_fill()
    turtle.left(135)
    turtle.fd(30 * scale)
    turtle.left(180)
    turtle.fd(30 * scale)
    turtle.right(90)
    turtle.circle(100 * scale, 60)

    turtle.penup()

# Set up the turtle
def main():
    # set up turtle
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0,0)

    # Draw 7 flowers with reduced size
    for i in range(10):
        x = -200 + (i % 10) *50
        y = -90
        scale =0.2
        print(scale)
        draw_flower(x, y, scale,generate_random_color())
    # update screen
        turtle.update()
    # Keep the window open
    # turtle.done()

if __name__=="__main__":
    main()