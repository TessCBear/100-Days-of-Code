# Day 21 of 100 Days of Code
## Snake Game Part 2

Today we continued creating the famous Snake Game. First was a lesson on class inheritance: how to import the attributes and methods of a class (the *superclass*) to use and add to in a new class. For example:

```python
# Super class of Dog
class Dog:
    def __init__(self):
        self.temperament = "loyal"
    def bark(self):
        print("Woof")

# Another class which is also a dog, but with changes:
class Labrador(Dog):
    def __init__(self):
        super().__init__() # import all Dog attributes and methods
        self.temperament = "friendly" # Modified attribute

    def retrieve(self): #Additional method
        print("Fetch things")
```
We used this concept in a lot of the components today. The first of which, was to create a specialised *turtle* class, *food*, which creates the food for the snake. It should pop up in random positions and regenerate when the snake collides with (eats) it.

The next thing we made was the scoreboard. This keeps track of the score of the user and displays it at the top of the screen. This was done using the *write* method. The scoreboard also displays "GAME OVER" in case of the snake having a collision with the wall or itself.

The last thing implemented was the collisions with the wall and itself, and with this, the growing of the snake.

I really enjoyed this project and I'm so proud of how far I've come. I'm really enjoying coding for the first time in my life!