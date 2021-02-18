# Day 20 of 100 Days of Code
## Snake Game Part 1

We're finally building the famous Snake Game! This project will be done over 2 days since it's quite complex, and I am grateful for the step-by-step approach.

The first thing that we did was to create a 3-block snake body. This was done as a *for* loop:

```python
positions = [(0,0), (-20,0), (-40,0)]

for square_index in range(0,3):
    new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position[square_index])
            squares.append(new_square)
```

The next task was to make the "snake" move. I learnt about the *update()* and *time()* methods, which refresh the screen after a specific delay so that the motion of the "snake" is smoother.

I then converted the code into OOP so that it was easier to work with, and neater, before moving on to being able to control the snake's direction.

Tomorrow we will code the rest of the snake, and I'm really excited to finish such a classic game!