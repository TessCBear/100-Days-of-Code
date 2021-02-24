# Day 23 of 100 Days of Code
## Turtle Crossing

Today's lesson was another project-based day with no specific topic covered. We created a version of "Crossy Road" using Turtle graphics. 

First, we had to make the player which can only move up. This was not hard to acheive. Next we made the car manager. This was arguably the hardest to get at the right speed. I did have to look at Dr Yu's solution because I had the cars working fine, but just too many cars were spawning. Her solution was so clever: cars are spawned in a 1/6 chance.

```python
def create_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid = 1, stretch_len= 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))

            self.all_cars.append(new_car)
```
The next task was to detect collisions with cars, a familiar concept after the Pong and Snake games, and to check when the turtle has made it to the top of the screen and to increase the speed of the cars. Finally, we made a scoreboard - copying much of the code from the Snake game with small modifications.

This project was good practise again for OOP and Turtle graphics, and I enjoyed making it.