from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(x = -230, y = 250)
        self.write(f"Level {self.level}", align= "center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align= "center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font=FONT)

    