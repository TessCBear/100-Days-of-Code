# Day 4 of 100 Days of Code
## Rock, Paper, Scissors

Today's lesson focussed on randomisation and lists. The first thing that was required was to learn how to import modules such as the one we needed, *random*. I did know this before, but I didn't know that you could save a new file and import that in as a module.

I then played around with the *random* module and created a virtual coin toss:

```python
import random

print('Welcome to virtual coin toss')

coin = random.randint(0,1)

if coin == 0:
    print('Heads')
else:
    print('Tails')
```

The next topic was lists. I learnt a lot about list manipulation and referencing and worked with a nested list for the first time. 

The exercise that I found most challenging in terms of brain power was the "treasure map". This required manipulation of nested lists to mark an "X" on a grid:

```python
import random
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter as double digit number <column><row> ")

column = int(position[0])
row = int(position[1])

map[row-1][column-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")
```
The final project for the day was to create a game of "Rock, Paper, Scissors" using the skills of lists, random number generators and skills from previous days. I decided to make it more challenging for myself and instead created a game of "Rock, Paper, Scissors, Lizard, Spock". The hardest part was working out all of the scenarios and then coding them, but it gave me a good chance to practise a ton of coding. 