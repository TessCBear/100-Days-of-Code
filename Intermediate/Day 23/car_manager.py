from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid = 1, stretch_len= 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))

            self.all_cars.append(new_car)
        
    def move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def next_level(self):
        for car in self.all_cars:
            y_coor = car.ycor()
            car.goto(400, y_coor)

        self.all_cars.clear()
        self.move_distance += MOVE_INCREMENT

    
