import turtle
import pandas

IMAGE = ".\Intermediate\Day 25\\blank_states_img.gif"

data = pandas.read_csv(".\Intermediate\Day 25\\50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

states_guessed = []

while len(states_guessed) < 50:

    answer_state = screen.textinput(title = f"{len(states_guessed)}/50 guessed!", prompt = "Guess a State").title()
    for state in data.state:
        if state == answer_state and answer_state not in states_guessed:
            state_object = turtle.Turtle()
            state_object.hideturtle()
            state_object.penup()
            
            xcor = int(data[data.state == state].x)
            ycor = int(data[data.state == state].y)

            state_object.goto(xcor, ycor)
            state_object.write(f"{state}", align="center", font=("Arial", 9 , "normal"))

            states_guessed.append(state)

state_object.goto(0,0)
state_object.write("You guessed all 50 states! Well done!", align = "center", font = ("Arial", 24, "normal"))
screen.exitonclick()
