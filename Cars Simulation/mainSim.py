import turtle
from turtle import Screen
from tkinter import *
import math 
import vehicles
import random 
# import project modules
import flower
import drawSUV
import drawTruck
import drawCar

def openSUVWindow():
    turtle.clearscreen()
    drawSUV.main()

def openTruckWindow():
    turtle.clearscreen()
    drawTruck.main()

def openCARWindow():
    turtle.clearscreen()
    drawCar.main()

def main():
    screen=Screen()

    canvas=screen.getcanvas()

    car_button=Button(canvas.master,text="CAR",width=5,height=1,bg="blue",fg="white",font=("Arial",12),command=openCARWindow)
    suv_button=Button(canvas.master,text="SUV",width=5,height=1,bg="green",fg="white",font=("Arial",12),command=openSUVWindow)
    truck_button=Button(canvas.master,text="Truck",width=5,height=1,bg="red",fg="white",font=("Arial",12),command=openTruckWindow)

    car_button.pack()
    car_button.place(x=500,y=50)

    suv_button.pack()
    suv_button.place(x=600,y=50)

    truck_button.pack()
    truck_button.place(x=700,y=50)


    turtle.done()

if __name__=="__main__":
    main()