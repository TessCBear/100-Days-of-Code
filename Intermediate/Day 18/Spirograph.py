import turtle 
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("turquoise2")
timmy.speed("fastest")

def change_colour():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)

    turtle.colormode(255)
    timmy.pencolor((R,G,B))

def draw_circle(size_of_gap):
    for direction in range(int(360/size_of_gap)):
        change_colour()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
    
draw_circle(1)


screen = Screen()
screen.exitonclick()