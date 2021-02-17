# import colorgram

# colours = colorgram.extract("image.jpg", 30)

# colour_list = []
# for colour in colours:
#     r = colour.rgb.r
#     b = colour.rgb.b
#     g = colour.rgb.g
#     new_colour = (r, g, b)
#     colour_list.append(new_colour)

# print(colour_list)

# List generated from code above, with very light colours manually removed
colours = [(43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 
147), (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37), (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 
108), (154, 222, 193), (181, 170, 221), (30, 163, 170), (84, 35, 39), (40, 46, 80), (233, 167, 180), (237, 172, 162), (76, 40, 39), (154, 208, 221), (115, 46, 
43)]

import turtle as t
import random

timmy = t.Turtle()
timmy.hideturtle()

def draw_dot():
    t.colormode(255)
    random_colour = random.choice(colours)
    timmy.dot(20, random_colour )

timmy.penup()
timmy.setposition(-250,-250)

def draw_row():
    for dot in range(10):
        draw_dot()
        timmy.forward(50)

def new_row():
    timmy.setposition(-250, timmy.ycor() + 50)


for i in range(10):
    draw_row()
    new_row()

screen = t.Screen()
screen.exitonclick()