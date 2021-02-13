# Day 16 of 100 Days of Code
## Coffee Machine: Object Oriented Programming

I have been quite bad and fallen behind a few days, but I will catch up! Life just got a bit crazy. As it says in the title, this lesson was an introduction to Object Oriented Programming. This was a concept that made sense theoretically, but I found it really challenging to apply. 

We started off by learning about classes, objects, attributes and methods. A class can be thought of as a blueprint for making an object which has attributes and methods. An attribute is a property of the object and a method is something the object can do. For example, a car has wheels and a steering wheel (attributes) as well as speed amount of fuel (methods).

The first thing we started playing with was the Turtle package. This is the most adorable thing ever! I learnt how to create objects from the built-in package classes and how to change attributes and use methods:

```python
from turtle import Turtle, Screen

# Create an object (timmy) of the Turtle class. 
timmy = Turtle()

# Change timmy using methods
timmy.shape("turtle")
timmy.color("cyan3")
timmy.forward(100)

# Create a screen object
my_screen = Screen()
# Use a method on the screen object
my_screen.exitonclick()
```

This new knowledge was then used to remake the project from Day 15, the Coffee Machine, using OOP. I struggled at first with practically applying the skills, and I had to watch the walkthrough of the solution to understand the last part. I'm proud for almost getting there, though, and I'm sure I'll improve the more I do it.