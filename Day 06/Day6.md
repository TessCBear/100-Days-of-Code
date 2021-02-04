# Day 6 Of 100 Days of Code
## Escaping the Maze

Today's lesson focussed on functions *while* loops. It was an extremely interactive lesson with lots of coding challenges. The challenges were done using a site called [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json). Using Python and a few built-in functions, you have to make the robot perform various tasks. The tasks started very simple, like making him move in a square:

```python
#Make Reeborg move in a Square
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
```
and slowly built up to more complicated tasks such as making him jump over hurdles of varying heights and distances apart:

```python
#Make Reborg navigate varying hurdles
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
        turn_left() #so he begins facing up
        while wall_on_right():
            move() #go up until hurdle is finished
        turn_right() #turn forwards
        move() #move across hurdle
        turn_right() #turn down again
        move() #move down 1
        while wall_on_right() and front_is_clear():
            move() #continue moving down until reaches floor
        turn_left() #face forwards afain
        
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
```
The exercises gave me good practise on *while* loops as well as if statements. It sometimes took a lot of brain power and debugging to get it to work, but it was really a lot of fun.

The final project involved using the day's skills to help Reeborg escape a maze from a randomly generated position and starting direction. I was very thankful that the site gave some guidance into how the maze can be escaped since it was difficult to figure out how to implement this. I can't imagine having to figure that out too! It's not necessarily the most direct way to escape the maze, but he does eventually get there.