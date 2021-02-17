from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)

def turtle_race():
    is_race_on = False
    user_bet = screen.textinput(title = "Make your bet", prompt = "Which colour turtle do you think will win the race? ")
    if user_bet:
        is_race_on = True
    colours = ["red", "orange", "yellow", "green", "blue", "purple", "hotpink"]
    y_positions = [150, 100, 50, 0, -50, -100, -150]
    turtles = []

    for turtle_index in range(0,7):
        new_turtle = Turtle(shape = "turtle")
        new_turtle.penup()
        new_turtle.color(colours[turtle_index])
        new_turtle.goto(-230, y_positions[turtle_index])
        turtles.append(new_turtle)

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_colour = turtle.pencolor()
                if user_bet == winning_colour:
                    play_again = screen.textinput(title = "You win!", prompt = f"The {winning_colour} turtle won. Play again? Y/N ")
                    if play_again == "Y":
                        screen.clearscreen()
                        turtle_race()
                    else:
                        return
                else:
                    play_again = screen.textinput(title = "You lose!", prompt = f"The {winning_colour} turtle won. Play again? Y/N ")
                    if play_again == "Y":
                        screen.clearscreen()
                        turtle_race()
                    else:
                        return
            distance = random.randint(0,10)
            turtle.forward(distance)

turtle_race()

screen.exitonclick()